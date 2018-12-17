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

    day_in_month_tup = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        day_in_month_tup[1] = 29
    print(day_in_month_tup[:month - 1])
    days = sum(day_in_month_tup[:month - 1]) + day
    print(days)

if __name__ == '__main__':
    main()