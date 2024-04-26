import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            about = quote.xpath("span/a/@href").get()
            if about:
                yield response.follow(about, callback=self.parse_author)

    def parse_author(self, response):
        yield {
            "fullname": response.css("h3.author-title::text").get(),
            "born_date": response.css("span.author-born-date::text").get(),
            "born_location": response.css("span.author-born-location::text").get(),
            "description": response.css("div.author-description::text").get()
        }
