"""
   作者:朱洪明
   功能:绘制五角星

"""
import turtle


def main():

    # # 前进50  第一条边
    # turtle.forward(50)
    # # 右转 144度
    # turtle.right(144)
    # # 前进50  第二条边
    # turtle.forward(50)
    # # 右转 144度
    # turtle.right(144)
    # # 前进50 第三条边
    # turtle.forward(50)
    # # 右转 144度
    # turtle.right(144)
    # # 前进50  第四条边
    # turtle.forward(50)
    # # 右转 144度
    # turtle.right(144)
    # # 前进50  第5条边
    # turtle.forward(50)
    # turtle.exitonclick()


    # 计数器
    count = 1
    while count <= 5:
        # 前进50 第count条边
        turtle.forward(50)
        # 右转 144度
        turtle.right(144)
        count  = count + 1
    turtle.exitonclick()

if __name__ == '__main__':
    main()
