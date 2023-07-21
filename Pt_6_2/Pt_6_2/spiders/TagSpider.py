import scrapy


class TagSpider(scrapy.Spider):
    name = "TagSpider"
    url = 'https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s'
    page = 1
    start_urls = [url % page]
    games_count = 0

    def parse(self, response):
        for link in response.css('#search_resultsRows a::attr(href)'):
            yield response.follow(link, callback=self.parse_tags)

        if self.games_count < 1000:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)

    def parse_tags(self, response):
        if 'sub/' in response.url:
            return

        if self.games_count == 1000:
            return

        self.games_count += 1

        yield {
            'appName': response.css('#appHubAppName::text').get(),
            'link': response.url.split('/?')[0],
            'tags': list(map(str.strip, response.css('a.app_tag::text').getall()))
        }
