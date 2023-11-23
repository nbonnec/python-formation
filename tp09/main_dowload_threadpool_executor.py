#!/usr/bin/env python

import time
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL: str = 'https://logs.eolem.com/'


def download(log: str) -> None:
    rsp = requests.get(log)
    filename = log.split('/')[-1]
    with open(filename, 'w') as f:
        f.write(rsp.text)


def main():
    start = time.perf_counter()

    rsp = requests.get(URL)
    soup = BeautifulSoup(rsp.text, 'html.parser')
    all_a = soup.find_all('a')

    all_logs = [f'{URL}/{a["href"]}' for a in all_a if a['href'].endswith('.log')]
    pprint(all_logs)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download, all_logs)

    print(time.perf_counter() - start)


if __name__ == '__main__':
    main()
