#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GoogleScraper import scrape_with_config, GoogleSearchError

keywords = [
    '一汽 试验台 ',
    '上汽 试验台',
    '吉利 试验台'
]

# See in the config.cfg file for possible values
config = {
    'use_own_ip': 'False',
    'keywords': keywords,
    'search_engines': ['google','baidu'],
    'num_pages_for_keyword': 2,
    'scrape_method': 'http',
    'do_caching': 'True',
    'output_filename': '555-out.csv'
}

try:
    search = scrape_with_config(config)
except GoogleSearchError as e:
    print(e)

for serp in search.serps:
    print(serp)
    for link in serp.links:
        print(link)