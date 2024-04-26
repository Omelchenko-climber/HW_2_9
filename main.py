from scrapy.crawler import CrawlerProcess
from hw_scrapy_spider.hw_scrapy_spider.spiders import authors, quotes


def main():
    process = CrawlerProcess()
    process.crawl(quotes.QuotesSpider)
    process.crawl(authors.AuthorsSpider)
    process.start()


if __name__ == '__main__':
    main()
