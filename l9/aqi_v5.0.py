import csv
import json
import os

import requests

"""
    简单爬虫

"""


def get_html_text(url):
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    cityPy = input(" 请输入城市拼音 ")
    url = "http://pm25.in/" + cityPy
    url_text = get_html_text(url)
    aqi_div = """<div class="span12 data">
        <div class="span1">
          <div class="value">
            """
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 3
    aqi_val = url_text[begin_index: end_index]
    print(aqi_val)
    

if __name__ == '__main__':
    main()
