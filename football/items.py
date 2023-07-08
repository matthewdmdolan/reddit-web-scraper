# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PostItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  title = scrapy.Field()
  user = scrapy.Field()
  upvotes = scrapy.Field()
  comments = scrapy.Field()
  subreddit = scrapy.Field()
  content_link = scrapy.Field()
  awards = scrapy.Field()
  time = scrapy.Field()







