"""
 添加画图

"""
import numpy as np
import matplotlib.pyplot as plt


# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice(totaltimes):
    roll = np.random.randint(1, 7, totaltimes)
    return roll


def main():
    totaltimes = 200
    roll_list = []
    roll1 = roll_dice(totaltimes)
    roll2 = roll_dice(totaltimes)
    roll_list = roll1 + roll2

    hist, bins = np.histogram(roll_list, bins=range(2, 14))
    print(hist,bins)
    # 画出直方图 bins 边界   normed 归一化  edgecolor 边界线   linewidth = 线宽度
    tick_label = ["2点", "3点", "4点", "5点", "6点", "7点", "8点", "9点", "10点", "11点", "12点"]
    tick_point = np.arange(2, 13) + 0.5
    plt.xticks(tick_point, tick_label)
    plt.hist(roll_list, bins=range(2, 14), normed=True, edgecolor='black', linewidth = 1)
    plt.title('色子点数统计 ')
    plt.xlabel(' 点数 ')
    plt.ylabel(' 频率 ')
    plt.show()

if __name__ == '__main__':
    main()
