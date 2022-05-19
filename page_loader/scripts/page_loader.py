#!/usr/bin/env python3
import os

from page_loader.cli import parse_cli
from page_loader.path import format_page_path
from requests import request


def download(webpage, save_path):
    page_name = format_page_path(webpage)
    page_path = os.path.join(save_path, page_name)
    with open(page_path, 'w', encoding='utf-8') as f:
        page = request('GET', webpage).text
        f.write(page)
    return page_path


def main():
    save_path, webpage = parse_cli()
    download(webpage, save_path)


if __name__ == '__main__':
    main()
