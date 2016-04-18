# -*- coding: utf-8 -*-

import os
import unittest
from bs4 import BeautifulSoup
from bbscraper.walker import ThreadWalker
from bbscraper.extractors import UserExtractor, PostIDExtractor, CreationDateExtractor, PostDataExtractor

def parse_tree(html):
    return BeautifulSoup('<html><body>' + str(html) + ' </body></html>', 'html.parser')

def read_fixture(file):
    path = os.path.dirname(os.path.abspath(__file__)) + '/fixtures/' + file
    return open(path, 'r').read().encode('utf8', errors='ignore')

class TestUserExtractor(unittest.TestCase):

    def test_valid_tree(self):
        tree = parse_tree('<span class="name"><b>foo<b></span>')
        self.assertEqual(UserExtractor(tree).extract(), 'foo')

    def test_invalid_tree(self):
        tree = parse_tree('<span>foo</span>')
        self.assertEqual(UserExtractor(tree).extract(), None)

class TestPostIDExtractor(unittest.TestCase):

    def test_valid_tree(self):
        tree = parse_tree('<table><tr><td><a href="?viewpost=123#123"></a></td></tr></table>')
        self.assertEqual(PostIDExtractor(tree).extract(), '123')

    def test_invalid_tree(self):
        tree = parse_tree('<table><tr><td></td></tr></table>')
        self.assertEqual(PostIDExtractor(tree).extract(), None)

class TestCreationDateExtractor(unittest.TestCase):

    def test_valid_tree(self):
        tree = parse_tree("<table><span class=\"postdetails\">Posted: 18 Apr 2016 \xa0\xa0 </span></table>")
        self.assertEqual(CreationDateExtractor(tree).extract(), '18 Apr 2016')

    def test_invalid_tree(self):
        tree = parse_tree('<table><span class="details">Posted: 18 Apr 2016</span></table>')
        self.assertEqual(CreationDateExtractor(tree).extract(), None)

class TestPostDataExtractor(unittest.TestCase):

    def test_valid_tree(self):
        tree = parse_tree('<table><tr><td><span class="postbody">blablabla\n\r\n' + PostDataExtractor.SEPARATOR + '\n Foo</span></td></tr></table>')
        self.assertEqual(PostDataExtractor(tree).extract(), 'blablabla\\n')

    def test_invalid_tree(self):
        tree = parse_tree('<table><tr><td></td></tr></table>')
        self.assertEqual(PostDataExtractor(tree).extract(), None)

class TestThreadWalker(unittest.TestCase):

    def test_single_page_walker(self):
        html = read_fixture('thread_single_page.html')
        tree = BeautifulSoup(html, 'html.parser')
        posts = ThreadWalker(tree).walk()

        self.assertEqual(len(posts), 15)

        # Assert last post values via extraction
        post_tree = parse_tree(posts.pop())
        self.assertEqual(UserExtractor(post_tree).extract(), "Rick")
        self.assertEqual(PostIDExtractor(post_tree).extract(), "87157")
        self.assertEqual(CreationDateExtractor(post_tree).extract(), "Tue Sep 25, 2012 7:41 am")
        self.assertEqual(PostDataExtractor(post_tree).extract(), "Times like this I wish I had shares in Isopon \\n\\n\\nRJ")

if __name__ == '__main__':
    unittest.main()