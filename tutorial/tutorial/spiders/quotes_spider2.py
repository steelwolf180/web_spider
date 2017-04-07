import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'tenders2'
    start_urls = [
        'https://www.gebiz.gov.sg/ptn/opportunity/BOListing.xhtml?origin=menu',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'quotation_number' : quote.xpath('//div[re:test(@class,"formSectionHeader6_TEXT")]/text()').extract(),
                'tender-title' : quote.xpath('//a[re:test(@class,"commandLink_TITLE-BLUE")]/text()').extract(),
                'tender-description' : quote.xpath('//div[re:test(@class,"formOutputText_VALUE-DIV")]/text()').extract(),
                'closing_date' : quote.xpath('//div[re:test(@class,"formOutputText_HIDDEN-LABEL outputText_DATE-GREEN")]/text()').extract()
            }