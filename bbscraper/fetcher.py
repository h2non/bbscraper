# -*- coding: utf-8 -*-

from urllib import request as req

class Fetcher(object):
  """
  Fetcher fetches and returns the response
  body of the given URL.
  """

  def __init__(self, url):
    self.url = url

  def fetch(self):
    return req.urlopen(self.url).read()
