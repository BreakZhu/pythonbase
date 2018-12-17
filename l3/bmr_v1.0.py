def main():
    gender = '男'

    wight = 70

    height = 175

    age = 25

    if gender == '男':
        bmr = (13.7 * wight) + 5.0 * height - 6.8 * age + 66
    elif gender == '女':
        bmr = (9.6 * wight) + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1

    if bmr != -1:
        print('基础代谢率（大卡）：', bmr)
    else:
        print('暂时不支持该性别')


if __name__ == '__main__':
    main()
