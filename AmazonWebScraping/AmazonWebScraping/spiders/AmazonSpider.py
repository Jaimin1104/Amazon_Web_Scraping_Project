import scrapy


class AmazonSpider(scrapy.Spider):
    name = "AmazonSpider"
    allowed_domains = ["amazon.in"]
    search_query = ["laptop"]
    start_urls = ["https://amazon.in/s?k="+query for query in search_query]
    visited_urls = set()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print("-" * 150)
        print("Visited URL = ", response.url)
        print("-" * 150)

        if 'laptop' in response.url:
            urls = response.css('.s-line-clamp-2 .a-link-normal::attr(href)').extract()
            print("Length of URLs : ", len(urls))
            for url in urls:
                url = response.urljoin(url)
                yield scrapy.Request(url, callback=self.parse_laptop)
            next_url = response.css('.s-pagination-separator::attr(href)').extract()
            if next_url:
                next_url = response.urljoin(next_url[0])
                yield scrapy.Request(next_url, callback=self.parse)

    def parse_laptop(self, response):
        print("-" * 150)
        print("Visited LAPTOP URL = ", response.url)
        print("-" * 150)
        item = {'Product_Category': "Laptop", 'URL': response.url}
        title = response.css('#productTitle::text').extract_first()
        item['Title'] = title
        price = response.css('.a-price-whole::text').extract_first()
        item['Price'] = price
        avg_rating = response.css('#acrPopover .a-icon-alt::text').extract_first()
        item['Average_Rating'] = avg_rating
        num_of_rating = response.css('#acrCustomerReviewText::text').extract_first()
        item['Number_of_Rating'] = num_of_rating
        table_rows = response.css('#productDetails_techSpec_section_1 tr')
        for i in range(len(table_rows)):
            th_data = table_rows[i].css('th::text').extract_first().strip()
            td_data = table_rows[i].css('td::text').extract_first().strip()
            item[th_data] = td_data
        yield item