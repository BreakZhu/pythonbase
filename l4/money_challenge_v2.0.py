"""
   功能  52周存钱
   版本   2.0

"""
import math

def main():
    money_pre_week = 10    # 每周存入的金额
    i = 1                  # 周数
    increase_money = 10    # 递增金额
    total_week = 52        # 总的周数
    money_list = []
    while i <= total_week:
        # 存钱
        money_list.append(money_pre_week)
        saving = math.fsum(money_list)
        # 输出
        print("第{} 周，存入{} 元, 账户累计{} 元".format(i, money_pre_week, saving))
        # 更新一下下一周的存钱的金额
        money_pre_week += increase_money
        i += 1

if __name__ == '__main__':
    x = [1,2,3,4]
    del x[1]
    print(x)
    main()
