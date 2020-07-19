# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #序号
    serial_name = scrapy.Field()
    #书名
    book_name = scrapy.Field()
    #书介绍
    introduce = scrapy.Field()
    #书星级
    star = scrapy.Field()
    #书评论数
    evaluate = scrapy.Field()
    #书描述
    describe = scrapy.Field()
