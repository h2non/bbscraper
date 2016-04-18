# bbscraper [![Build Status](https://travis-ci.org/h2non/bbscraper.svg?branch=master)](https://travis-ci.org/h2non/bbscraper)

Simple phpBB forum thread web scraper written in Python. 
Designed for command-line usage. Outputs data as CSV format into `stdout`.

This is an experiment-driven project. The code tends to be, but it's not fully idiomatic according to [PEP8](https://www.python.org/dev/peps/pep-0008). 
The current implementation is very ad-hoc for a concrete particular scenario, 
however extending it to cover additional behavior and features should be trivial.

The scraped data fields per thread post are (in order): `Post ID`, `Post name`, `Date of the post` and `Post body`

Uses [urllib3](https://github.com/shazow/urllib3) for HTTP networking and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML parsing.

This package is not available via `pip`.
You must [download](https://github.com/h2non/bbscrape/releases) or [clone](#installation) this repository in order to use it.

## Requirements

- **python** `+3` (developed using python@3.4.2)
- **pip** (optional)

## Installation

Clone this repository:
```bash
git clone https://github.com/h2non/bbscraper.git && cd bbscraper
```

Install dependencies via `pip`:
```bash
sudo pip install -r requirements.txt
```

Or alternatively using `setup.py`:
```bash
python setup.py install
```

## Command-line interface

```bash
usage: __main__.py [-h] -u URL [-f FORMAT] [-l LIMIT]

Scrape all thread posts of a phpBB based forum

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Full URL to forum thread
  -f FORMAT, --format FORMAT
                        Output format (default to CSV)

Report any issues to https://github.com/h2non/bbscraper/issues
```

Scrap the website and save data in `forum.csv`:

```bash
python bbscraper -u http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591 > forum.csv
```

## Development

Run tests:
```bash
make test
```

## License

MIT - Tomas Aparicio