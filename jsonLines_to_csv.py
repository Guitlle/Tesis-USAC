# -*- coding: utf-8 -*-
import pandas as pd
import json
import re
import os
archivo = os.environ.get("PROCFILE")
if True:
    f = open(archivo, "r")
    i=0
    df = pd.DataFrame()
    for linea in f:
        tesis = json.loads(linea)
        i= i+1
        print i
        for attr in tesis["attributes"]:
            if attr["key"] is not None and attr["key"] != "":
                df.set_value(i, attr["key"], value=attr["value"] if type(attr["value"]) != list else ", ".join(attr["value"]) )
            del attr
        copiaN = 0
        for copia in tesis["copies"]:
            copiaN = copiaN + 1
            barcode = re.findall("\<[^>]*\>[\s-]*([^><]*)\<\/[^>]*\>", copia["barcode"])
            ubicacion = re.findall("\<[^>]*\>([^><]*)\<\/[^>]*\>", copia["ubicacion"])
            copia_txt =  u"(Status: " + copia["status"] + u"), (Ubicación: " + (ubicacion[0] if len(ubicacion)==1 else "") + u"), (Barcode: " + (barcode[0] if len(barcode)==1 else u"") + u") "
            df.set_value(i, "copia"+str(copiaN), value=copia_txt)
        del tesis
        del linea

    f.close()

    df.to_csv(os.environ.get("OUTFILE"), encoding="utf-8")
