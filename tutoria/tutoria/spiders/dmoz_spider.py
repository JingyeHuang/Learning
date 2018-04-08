import scrapy

class Dmozspider(scrapy.Spider):
    name = 'Dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = ['https://dmoztools.net/Games/Board_Games/' , 'https://dmoztools.net/Games/Card_Games/']
    
    
    def parse(self,response):
        filename = response.url.split('/')[-2]
        with open(filename,'wb') as f:
            f.write(response.body)