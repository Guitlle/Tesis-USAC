# Scrape de las tesis de la USAC hasta Septiembre de 2016

He decidido aprender a utilizar scrapy haciendo un dataset de las tesis de la USAC listadas en el catálogo de la biblioteca central: http://biblos.usac.edu.gt . 

El script para scrapear utiliza variables de entorno para funcionar. Basta con ver el código en tesis/spiders/tesis.py para comprender el funcionamiento. El script almacena los datos en líneas en formato JSON, por eso es necesario el script jsonLines_to_csv.py, que también utiliza variables de entorno para definir el archivo de entrada y el de salida.

He bajado el catálogo de tesis en 4 lotes (tesis_A.csv-tesis_D.csv) y lo he unido en tesis_todo.csv. Pronto estaré publicando análisis sobre estos datos. 
