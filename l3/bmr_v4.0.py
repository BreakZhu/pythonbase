def main():
    y_or_n = input("是否退出程序:y/n")
    while y_or_n != 'y':
        print(" 请输入以下信息，用空格分隔 ：")
        input_str = input("性别 体重 身高 年龄")
        try:
            str_list = input_str.split(' ')
            gender = str_list[0]
            wight = float(str_list[1])

            height = float(str_list[2])

            age = int(str_list[3])

            if gender == '男':
                bmr = (13.7 * wight) + 5.0 * height - 6.8 * age + 66
            elif gender == '女':
                bmr = (9.6 * wight) + 1.8 * height - 4.7 * age + 655
            else:
                bmr = -1

            if bmr != -1:
                print("您的性别：{}， 体重：{}公斤， 身高：{}厘米，  年龄：{}岁".format(gender, wight, height, age))
                print('基础代谢率 {} 大卡'.format(bmr))
            else:
                print('暂时不支持该性别')
        except ValueError:
            print("请您输入正确信息")
        except IndexError:
            print("您输入的信息过少")
        except:
            print("请检查您的输入")
        y_or_n = input("是否退出程序:y/n")


if __name__ == '__main__':
    main()
