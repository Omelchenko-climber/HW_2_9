# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HwScrapySpiderPipeline:
    def process_item(self, item, spider):
        if spider.name == "authors":
            normal_description: str = item.get("description")
            if normal_description:
                item["description"] = normal_description.strip("\n").strip()
        return item
