"""
 添加画图 直方图

"""
import random
import matplotlib.pyplot as plt


# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    totaltimes = 200
    roll_list = []

    for i in range(totaltimes):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1 + roll2)

    # 画出直方图 bins 边界   normed 归一化  edgecolor 边界线   linewidth = 线宽度
    plt.hist(roll_list, bins=range(2, 14), normed=True, edgecolor='black', linewidth = 1)
    plt.title('色子点数统计 ')
    plt.xlabel(' 点数 ')
    plt.ylabel(' 频率 ')
    plt.show()

if __name__ == '__main__':
    main()
