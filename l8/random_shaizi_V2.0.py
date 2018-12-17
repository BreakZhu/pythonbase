"""
 添加画图

"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    totaltimes = 200
    result = [0] * 11
    roll_list = list(range(2, 13))
    z = zip(roll_list, result)
    result_dict = dict(z)

    roll1_list = []
    roll2_list = []
    for i in range(totaltimes):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll1_list.append(roll1)
        roll2_list.append(roll2)
        for j in range(2, 13):
            if (roll1 + roll2) == j:
                result_dict[j] += 1
    for index, res in result_dict.items():
        print("点数是{}出现了{}次 频率是{} ".format(index, res, res / totaltimes))

    x = range(1, totaltimes + 1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
