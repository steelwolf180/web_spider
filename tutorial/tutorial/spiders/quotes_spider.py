import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tenders"

    def start_requests(self):
        urls = [
            'https://www.gebiz.gov.sg/ptn/opportunity/BOListing.xhtml?origin=menu'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'tenders-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    '''

    def parse(self, response):

        yield{

        'quotation_number' : response.xpath('//div[re:test(@class,"formSectionHeader6_TEXT")]/text()').extract(),
        'tender-title' : response.xpath('//a[re:test(@class,"commandLink_TITLE-BLUE")]/text()').extract(),
        'tender-description' : response.xpath('//div[re:test(@class,"formOutputText_VALUE-DIV")]/text()').extract(),
        'closing_date' : response.xpath('//div[re:test(@class,"formOutputText_HIDDEN-LABEL outputText_DATE-GREEN")]/text()').extract()
        }
    '''