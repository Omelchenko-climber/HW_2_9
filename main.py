from scrapy.crawler import CrawlerProcess
from hw_scrapy_spider.hw_scrapy_spider.spiders import authors, quotes
from seeds import send_data, get_quote

import logging


logger = logging.getLogger('pymongo')
logger.setLevel(logging.INFO)


def main():
    process = CrawlerProcess()
    process.crawl(quotes.QuotesSpider)
    process.crawl(authors.AuthorsSpider)
    process.start()

    # send_data()

    # get_quote()


if __name__ == '__main__':
    main()
