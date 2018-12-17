import csv
import json
import os


def process_json_file(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = csv.reader(f)
        for s in city_list:
            print(s)


def main():
    filepath = input(" 请输入数据文件 ")
    filename, file_ext = os.path.splitext(filepath)
    if file_ext == '.json':
        process_json_file(filepath)
    elif file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print('文件格式异常')


if __name__ == '__main__':
    main()
