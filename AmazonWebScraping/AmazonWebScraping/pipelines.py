# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazonwebscrapingPipeline:
    def process_item(self, item, spider):
        if item['Product_Category'] == 'Laptop':
            if item['Average_Rating'] is not None:
                item['Average_Rating'] = (item['Average_Rating'].split(' '))[0]
            if item['Number_of_Rating'] is not None:
                item['Number_of_Rating'] = (item['Number_of_Rating'].split(' '))[0]
            for key in item.keys():
                if item[key] is not None:
                    if '\u200e' in item[key]:
                        item[key] = item[key].lstrip('\u200e')
        return item