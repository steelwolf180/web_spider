import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'tenders2'


    start_urls = [
        'https://www.gebiz.gov.sg/ptn/opportunity/BOListing.xhtml?origin=menu',
    ]

    def parse(self, response):
            yield {
                'quotation_number': response.xpath('//div[re:test(@class,"formSectionHeader6_TEXT")]/text()').extract(),
                'tender_title' :    response.xpath('//a[re:test(@class,"commandLink_TITLE-BLUE")]/text()').extract(),
                'tender_description' : response.xpath('//div[re:test(@class,"formOutputText_VALUE-DIV")]/text()').extract(),
                'closing_date' : response.xpath('//div[re:test(@class,"formOutputText_HIDDEN-LABEL outputText_DATE-GREEN")]/text()').extract()

            }