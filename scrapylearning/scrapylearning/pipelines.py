# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ScrapylearningPipeline:
    def process_item(self, item, spider):
        return item


class DangDangPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='dangdang',
        )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into waiyu values(%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, [
            item['title'],
            item['score_num'],
            item['score'],
            item['author'],
            item['time'],
            item['pub'],
            item['price']
        ]
                            )
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
        pass
