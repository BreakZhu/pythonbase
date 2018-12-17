import json


def process_json_file(filepath):
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    filepath = input(" 请输入 json 数据文件 ")
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    topic5_list = city_list[:5]
    f = open('./top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(topic5_list, f, ensure_ascii=False)
    f.closed()


if __name__ == '__main__':
    main()
