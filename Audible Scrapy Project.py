#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy


# In[2]:


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    start_urls = ['https://www.audible.com/search/']

    def parse(self, response):
        # Getting the box that contains all the info we want (title, author, length)
        product_container = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')

        # Looping through each product listed in the product_container box
        for product in product_container:
            book_title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            # Return data extracted
            yield {
                'title': book_title,
                'author': book_author,
                'length': book_length,
            }


# In[3]:


from scrapy.crawler import CrawlerProcess
process = CrawlerProcess(settings = {'FEEDS': {'output5.csv':{'format':'csv'}}})
process.crawl(AudibleSpider)
process.start()

