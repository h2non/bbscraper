# -*- coding: utf-8 -*-

import sys

class UserExtractor(object):
    """
    UserExtractor is used to extract the specific post author
    username from the parsed post HTML tree.
    """

    SELECTOR = "span.name > b"

    def __init__(self, tree):
        self.tree = tree

    def extract(self):
        nodes = self.tree.select(UserExtractor.SELECTOR)
        return None if len(nodes) == 0 else nodes.pop().get_text()

class PostIDExtractor(object):
    """
    PostIDExtractor is used to extract the specific post ID
    from the parsed post HTML tree.
    """

    SELECTOR = "table > tr > td > a"

    def __init__(self, tree):
        self.tree = tree

    def extract(self):
        nodes = self.tree.select(PostIDExtractor.SELECTOR)
        return None if len(nodes) == 0 else nodes[0].get("href").split('#').pop()

class CreationDateExtractor(object):
    """
    CreateDateExtractor is used to extract the specific post creation
    date from the parsed post HTML tree.
    """

    SELECTOR = "span.postdetails"

    SEPARATOR = 'Post subject:' # \xa0\xa0'

    def __init__(self, tree):
        self.tree = tree

    def extract(self):
        nodes = self.tree.select(CreationDateExtractor.SELECTOR)
        if len(nodes) == 0:
            return None

        node = nodes.pop().get_text() # remove HTML tags
        date = node.split(CreationDateExtractor.SEPARATOR) # get date slice

        if len(date) == 0:
            return None
        else:
            return date[0].split(': ').pop().strip()

class PostDataExtractor(object):
    """
    PostDataExtractor is used to extract the specific post data
    from the parsed post HTML tree.
    """

    SELECTOR = "span.postbody"

    SEPARATOR = "_________________"

    def __init__(self, tree):
        self.tree = tree

    def extract(self):
        nodes = self.tree.select(PostDataExtractor.SELECTOR)
        if len(nodes) == 0:
            return None

        node = nodes.pop().get_text() # remove HTML tags
        if node != "":
            return self.sanitize(node.split(PostDataExtractor.SEPARATOR)[0])

    def sanitize(self, value):
        # Escape carriage return and linefeed sequences to avoid CSV parsing issues
        return value.replace('\r\n', '').replace('\n', '\\n')

