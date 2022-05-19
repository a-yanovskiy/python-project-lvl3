import os
import re


def format_page_path(web_page):
    page_name = os.path.splitext(web_page)[0]
    page_name = page_name.split('//')[1]
    page_name = re.sub(r'\W', '-', page_name)
    page_name = page_name + '.html'
    return page_name
