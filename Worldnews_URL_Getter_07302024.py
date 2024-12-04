import scrapy

class BooksSpider(scrapy.Spider):
    name = "getter"


    def start_requests(self):
        for i in range(1,12):
            url = f'https://worldnews.net.ph/category/ben-dao?page={i}'
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        item = {}
        blocks = response.xpath('//h2[@class="post-title"]/a/@href').getall()
        for block in blocks:
            item['url'] = response.urljoin(block)
            yield item

