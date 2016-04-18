#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bbscraper - MIT license

# Current package semantic version
__version__ = version = "0.1.0"

import os
import sys
import argparse
import csv
from scraper import Scraper

# Declare supported command-line flags
parser = argparse.ArgumentParser(description='Scrape all thread posts of a phpBB based forum', epilog='Report any issues to https://github.com/h2non/bbscraper/issues')
parser.add_argument('-u','--url', required=True, nargs=1, help='Full URL to the forum thread to scrape', type=str, default='http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591')
parser.add_argument('-f','--format', required=False, nargs=1, help='Output format', default='csv')
parser.add_argument('-v', '--version', action='version', version='bbscraper %s' % version)

# Parse command-line arguments
args = parser.parse_args()

# main is automatically executed when calling
# the script directly via Python interpreter
def main():
    # Collect target URL to scrape from CLI flag
    url = args.url[0]

    # Create the CSV serializer and writer (by default writes into stdout)
    writer = csv.writer(sys.stdout)

    try:
        Scraper(writer).scrape(url)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

# run main function if we're running as main module
if __name__ == "__main__":
    main()
