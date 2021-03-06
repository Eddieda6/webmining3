import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li");
        for item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_name'] = item.xpath(".//div[@class='item']//div[@class='pic']/em/text()").extract_first()
            douban_item['book_name'] = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']/a/span[1]/text()").extract_first()
            content = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describe'] = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[@class='quote']//span[@class='inq']/text()").extract_first()

            yield douban_item

        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://book.douban.com/top250" + next_link,callback=self.parse)