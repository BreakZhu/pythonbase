"""
   功能  52周存钱
   版本   1.0

"""


def main():
    money_pre_week = 10    # 每周存入的金额
    i = 1                  # 周数
    increase_money = 10    # 递增金额
    total_week = 52        # 总的周数
    saving = 0             # 总体金额
    while i <= total_week:
        # 存钱
        saving += money_pre_week
        # 输出
        print("第{} 周，存入{} 元, 账户累计{} 元".format(i, money_pre_week, saving))
        # 更新一下下一周的存钱的金额
        money_pre_week += increase_money
        i += 1

if __name__ == '__main__':
    var1 = 'hello world'
    print(var1[0])
    main()
