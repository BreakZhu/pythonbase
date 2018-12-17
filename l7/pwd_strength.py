"""
    判断密码强度

"""


def check_number_exist(password):
    """
     判断是否包含数子
    :param password:
    :return:
    """
    for c in  password:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password):
    """
     判断是否包含字母
    :param password:
    :return:
    """
    for c in  password:
        if c.isalpha():
            return True
    return False

def main():
    password = input("请输入密码 :")
    # 密码强度
    strength_level = 0

    # 密码长度大于8
    if len(password) >= 8:
        strength_level += 1
    else:
        print(" 长度不够 至少8位")
    # 判断是否有数字存在
    if check_number_exist(password):
        strength_level += 1
    else:
        print(" 至少包含以为数字 ")
    # 判断是否有字母存在
    if check_letter_exist(password):
        strength_level += 1
    else:
        print(" 至少包含字母 ")
    if strength_level == 3:
        print("合格")
    else:
        print(" 强度 不够 ")

if __name__ == '__main__':
    main()