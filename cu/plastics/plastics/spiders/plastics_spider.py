import scrapy
from plastics import items

class ApprovedPlastics(scrapy.Spider):
    name = "plastics"
    
    def start_requests(self):
        
        urls = [
            "https://www.acplasticsinc.com/informationcenter/r/fda-approved-plastics-for-food-contact"
            ]
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


            
    def parse(self,response):

        filename = 'ApprovedPlastics'
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
         
        

    print('Saved file')
