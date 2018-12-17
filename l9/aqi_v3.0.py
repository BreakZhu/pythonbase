import csv
import json


def process_json_file(filepath):
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    filepath = input(" 请输入 json 数据文件 ")
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    lines = []
    # 获取列名
    lines.append(city_list[0].keys())
    for city in city_list:
        lines.append(city.values())
    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.closed()

if __name__ == '__main__':
    main()
