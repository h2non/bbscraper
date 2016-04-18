# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from fetcher import Fetcher
from walker import ThreadWalker
from extractors import UserExtractor, PostIDExtractor, CreationDateExtractor, PostDataExtractor

# extract_post_data is used to extract post specific data.
# Currently its an static, field specific implementation.
#
# Without too much effort extractor functions could be dynamically registered
# as sort of plugins to extend functionality for the data extraction process.
def extract_post_data(post_tree):
    # Post author name
    username = UserExtractor(post_tree).extract()

    # Post ID
    post_id = PostIDExtractor(post_tree).extract()

    # Post creation date
    date = CreationDateExtractor(post_tree).extract()

    # Post user content
    content = PostDataExtractor(post_tree).extract()

    # Return fields list in specific order (could be dictionary for semantic convenience)
    return [ post_id, username, date, content ]

class Scraper(object):
    """
    Scraper is used to scrape a phpBB forum thread, performing
    an HTTP request to the given URL, parsing the response HTML
    and walking the parsed tree structure finding the thread
    published posts by the users.
    """

    # Number of posts per thread page.
    # This could be automatically inferred based on the first
    # page number of posts, but is something that is not
    # prone to change too much.
    PAGE_SIZE = 15

    # Only HTML parsing for now
    PARSER = "html.parser"

    def __init__(self, writer):
        self.writer = writer # current only supports CSV as writer

    def scrape(self, url, page=0, recur=True):
        # Fetch and parse the forum thread page
        tree = self.parse(self.fetch(url, page))
        # Walk the thread HTML parsed tree and extract posts data
        posts = self.extract(tree)
        # Serialize posts data as CSV entries
        self.writer.writerows(posts)
        # Recursively process subsequent thread pages, if necessary
        if recur:
            self.scrape_subpages(tree, url)

    def scrape_subpages(self, tree, url):
        pages = self.num_pages(tree) - 1
        [self.scrape(url, num + 1, False) for num in range(pages) if pages > 0]

    def fetch(self, url, page):
        url = url + '&start=' + str(Scraper.PAGE_SIZE * page)
        return Fetcher(url).fetch()

    def parse(self, html):
        return BeautifulSoup(html, Scraper.PARSER) # only HTML syntax supported for now

    def extract(self, tree):
        return [extract_post_data(post_tree) for post_tree in ThreadWalker(tree)]

    # num_pages is used to obtain the number
    # of pages of the current scraped forum thread
    def num_pages(self, tree):
        pages = tree.select("span.nav > b")
        return 0 if len(pages) == 0 else int(pages.pop().get_text())
