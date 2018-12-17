"""


"""
import random


def main():
    totaltimes = 200
    result = [0] * 6
    for i in range(totaltimes):
        roll = random.randint(1, 6)
        for j in range(1, 7):
            if roll == j:
                result[j-1] += 1
    for index, res in enumerate(result):
        print("点数是{}出现了{}次 频率是{} ".format(index,res,res / totaltimes))

if __name__ == '__main__':
    main()
