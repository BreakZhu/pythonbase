from datetime import  datetime
"""
        输入年月日 判断是第几天

"""


def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        is_leap = True
    return is_leap



def main():
    input_date_str = input('请输入年月日 ( yyyy/mm/dd): ')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    print(input_date)
    year = input_date.year
    month = input_date.month
    day = input_date.day


    #包含30 天的月份的集合
    _30_day = {4, 6, 9, 11}
    _31_day = {1, 3, 5, 7, 8, 10, 12}

    # 初始化 days
    days = day;
    for i in range(1,month):
        if i in _30_day:
            days += 30
        elif i in _31_day:
            days += 31
        else:
            days += 28
    if is_leap_year(year) and month > 2:
        days += 1

    print(" 这是{}年的第{}天".format(year, days))

if __name__ == '__main__':
    main()