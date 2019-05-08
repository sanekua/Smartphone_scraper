# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class PhonesPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Jove248/fail',
            database='store_phone'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS quot_tb""")
        self.curr.execute("""create table quot_tb(
                        product_name text,
                        product_corp text,
                        product_price text,
                        product_image text             
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into quot_tb values (%s,%s,%s,%s)""", (
            item['product_name'][0],
            item['product_corp'][0],
            item['product_price'][0],
            item['product_image'][0]
            ))
        self.conn.commit()
