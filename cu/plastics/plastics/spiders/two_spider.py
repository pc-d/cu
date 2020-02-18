import scrapy
from plastics import items2

class ApprovedPlastics(scrapy.Spider):
    name = "ps"
    
    def start_requests(self):
        
        urls = [
            "https://www.professionalplastics.com/FDAApprovedPlasticMaterials?gclid=Cj0KCQiAs67yBRC7ARIsAF49CdWGrswhrwhbMTlcMJPVyHCm2DA2yAvxmrQtrIqV75JV_W0OmKTnd7UaAssIEALw_wcB"
            ]
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


            
    def parse(self,response):

        filename = 'ApprovedPs'
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
                
        item = items()
        iemt['main_headline']=response.xpath('//span/text()').extract()
        item['headline']=response.xpath('//title/text()').extract()
        item['url']=response.url
        item['project']=self.settings.get('BOT_NAME')
        item['spider']=self.name

        return item
         
        

 
