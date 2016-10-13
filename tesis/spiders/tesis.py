import scrapy
import os

class TesisUsacBiblos(scrapy.Spider):
    name = "tesis"
    pagInicial = int(os.environ.get("PAGINICIAL", 0))
    pagFinal = int(os.environ.get("PAGFINAL", 0))
    start_urls =  [ 'http://biblos.usac.edu.gt/library/index.php?title=Special%3AGSMSearchPage&process=&lang=es&titulo=&autor=&subheadings=&keywords=&material=tesis&sortby=sorttitle&page='+str(x) \
    for x in range(pagInicial, pagFinal + 1)]
    
    def parse(self, response):
        for row in response.css('div.row'):
            row_href = row.xpath(".//a/@href").extract_first()
            row_link = response.urljoin(row_href)
            yield scrapy.Request(row_link, callback=self.parse_detail)
    
    def parse_detail(self, response):
        kvs = []
        for row in response.css("div.marc div.row"):
            value = row.css("div.td").xpath(".//text()").extract()
            kvs.append({
                "key": row.css("div.th").xpath(".//text()").extract_first(),
                "value": value[0] if len(value)==1 else None if len(value) == 0 else value
            })
        copias = []
        for row in response.css("div.copia"):
            copias.append({
                "ubicacion": row.css("span.ubicacion").extract_first(),
                "barcode": row.css("span.barcode").extract_first(),
                "digital":  row.css("a.copia-digital::attr(href)").extract_first(),
                "status": row.css("span.status").xpath(".//text()").extract_first().replace("  ", "").replace("\n",""),
            })
        return {
            "attributes": kvs,
            "copies": copias
        }
