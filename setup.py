#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Dead simple phpBB thread web scraper',
    'author': 'Tomas Aparicio',
    'url': 'https://github.com/h2non/bbscraper',
    'download_url': 'https://github.com/h2non/bbscraper/archive/v0.1.0.tar.gz',
    'author_email': 'tomas@aparicio.me',
    'version': '0.1.0',
    'install_requires': ['nose'],
    'packages': ['bbscraper'],
    'scripts': [],
    'name': 'bbscraper',
    'install_requires': [
        'beautifulsoup4>=4.4.0',
    ],
    'entry_points': {
        'console_scripts': [
            'bbscraper = bbscraper.__main__:main',
        ],
        'virtualenvwrapper.project.template': [
            'base = bbscraper.virtualenvwrapper:template',
        ],
    }
}

setup(**config)