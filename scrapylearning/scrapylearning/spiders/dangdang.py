# -*- coding:utf-8 -*-
import scrapy
from ..items import DangDangItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['www.dangdang.com']
    start_urls = [

    ]
    url = 'http://bang.dangdang.com/books/bestsellers/01.45.00.00.00.00-24hours-0-0-1-'
    for r in range(1, 11):
        url_new = url + str(r)
        start_urls.append(url_new)

    # print(start_urls)

    def parse(self, response):
        res = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')
        item_dangdang = DangDangItem()
        title_res = res.xpath(
            './/div[@class="name"]/a/text()').getall()
        score_num_res = res.xpath(
            '//div[@class="star"]/a/text()').getall()
        score_res = res.xpath(
            '//div[@class="star"]/span/text()').getall()
        author_res = res.xpath(
            '//div[@class="publisher_info"][1]/a[1]/text()').getall()
        time_res = res.xpath(
            '//div[@class="publisher_info"][2]/span/text()').getall()
        pub_res = res.xpath(
            '//div[@class="publisher_info"][2]/a/text()').getall()
        price_res = res.xpath(
            '//div[@class="price"]/p/span[@class="price_r"]/text()').getall()

        for title, score_num, score, author, time, pub, price in zip(title_res, score_num_res, score_res, author_res,
                                                                     time_res, pub_res, price_res):
            item_dangdang['title'] = title
            item_dangdang['score_num'] = score_num
            item_dangdang['score'] = score
            item_dangdang['author'] = author
            item_dangdang['time'] = time
            item_dangdang['pub'] = pub
            item_dangdang['price'] = price
            yield item_dangdang

        pass
