import scrapy

class ApprovedPlastics(scrapy.Spider):
    name = "plastics"
    
    def start_request(self):
        start_irls = [
            "https://newsforkids.net/fastfacts/microplastics/",
        
        ]

            
    def parse(self,response):
        filename = 'ApprovedPlastics'
        with open(filename,'wb') as f:
            f.write(response.body)
    print('Saved file')
