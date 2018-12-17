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


def get_all_city():
    url = "http://pm25.in"
    city_list = []
    r = requests.get(url, timeout=30)
    b = BeautifulSoup(r.text, 'lxml')
    city_div = b.find_all('div', {'class': 'bottom'})[1]
    city_list_link = city_div.find_all('a')
    for city_link in city_list_link:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    city_list = get_all_city()
    for city in city_list:
        city_name = city[0]
        city_py = city[1]
        aqi_val = get_city_aqi(city_py)
        print(city_name, aqi_val)
    

if __name__ == '__main__':
    main()
