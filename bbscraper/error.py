# -*- coding: utf-8 -*-

class ScraperError(Exception):
    """
    ScraperError is used to raise library specific errors.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
