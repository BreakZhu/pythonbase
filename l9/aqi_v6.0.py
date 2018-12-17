import csv
import json
import os
from bs4 import BeautifulSoup
import requests

"""
    简单爬虫

"""


def get_city_aqi(cityPy):
    url = "http://pm25.in/" + cityPy
    r = requests.get(url, timeout=30)
    b = BeautifulSoup(r.text, 'lxml')
    div_list = b.find_all('div', {'class': 'span1'})
    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))
    return city_aqi


def main():
    cityPy = input(" 请输入城市拼音 ")
    aqi_val = get_city_aqi(cityPy)
    print(aqi_val)
    

if __name__ == '__main__':
    main()
