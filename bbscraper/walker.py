# -*- coding: utf-8 -*-

# from error import ScraperError

class ScraperError(Exception):
    """
    ScraperError is used to raise library specific errors.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class ThreadWalker(object):
    """
    ThreadWalker is used to walk the parsed HTML tree.
    """

    # Initial CSS selector used to find valid post nodes
    SELECTOR = "table.forumline > tr > td > table"

    # number of ancestors nodes in the tree to reach the post tr node
    PARENT_NODES = 5

    def __init__(self, tree):
        self.tree = tree
        self.total = 0
        self.current = 0
        self.posts = None

    def __iter__(self):
        return self

    # Python 3 specific iterator interface
    def __next__(self):
        if self.posts == None:
            self.walk()

        if self.current > self.total - 1:
            raise StopIteration

        self.current += 1
        return self.posts[self.current - 1]

    def walk(self):
        self.current = 0
        nodes = self.tree.select(ThreadWalker.SELECTOR)
        if len(nodes) == 0:
            raise ScraperError("Cannot find post nodes in the HTML tree")

        self.posts = self.map_valid_posts(nodes)
        self.total = len(self.posts)

        return self.posts

    def map_valid_posts(self, entries):
        return list(filter(lambda x: x != None, map(self.map, entries)))

    # map is used to lookup and map table elements
    # of valid post nodes in the parsed HTML tree
    def map(self, post):
        nodes = post.select("span.postbody")
        if len(nodes) == 0:
            return None

        node = nodes[0] # fetch first child node
        for _ in range(ThreadWalker.PARENT_NODES):
            if node == None:
                raise ScraperError("Cannot find post parent node in HTML tree")
            node = node.parent

        return node