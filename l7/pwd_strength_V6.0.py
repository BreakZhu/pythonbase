"""
    判断密码强度
    r 读
    w 写
    a 在文件末尾追加
    r+ 读写

"""


class PasswordTool:
    """
         密码工具类

    """

    def __init__(self, password):
        self.password = password
        self.strength_level = 0
        self.level_dict = {0: "弱", 1: "较弱", 2: "一般", 3: "强"}

    # 处理字符串
    def process_password(self):
        # 密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print(" 长度不够 至少8位")
        # 判断是否有数字存在
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print(" 至少包含以为数字 ")
        # 判断是否有字母存在
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print(" 至少包含字母 ")

    def check_number_exist(self):
        """
         判断是否包含数子
        :param password:
        :return:
        """
        hasNumber = False
        for c in self.password:
            if c.isnumeric():
                hasNumber = True
                break

        return hasNumber

    def check_letter_exist(self):
        """
         判断是否包含字母
        :param password:
        :return:
        """
        hasLetter = False
        for c in self.password:
            if c.isalpha():
                hasLetter = True
                break
        return hasLetter

    def save_pwd(self):
        w = open("./password", 'a')
        w.write("密码是{} 强度是{} ".format(self.password, self.level_dict[self.strength_level]) + '\n')
        w.closed


class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line, 'a')
        f.closed

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.closed
        return lines


def main():
    try_times = 5

    while try_times > 0:
        password = input("请输入密码 :")
        # 密码强度
        password_tool = PasswordTool(password)
        password_tool.process_password()
        password_tool.save_pwd()
        if password_tool.strength_level == 3:
            print("合格")
            break
        else:
            print(" 强度 不够 ")
            try_times -= 1
        if try_times == 0:
            print("尝试次数过多")


if __name__ == '__main__':
    main()
