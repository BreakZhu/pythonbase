"""
   作者:朱洪明
   功能:绘制五角星

"""
import turtle


def main():
    turtle.penup()
    turtle.backward(30)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor('red')


    # 五角星的边长
    length = 50
    while length <= 100:
        exitonclick(length)
        # length = length + 20
        length += 20
    turtle.exitonclick()


def exitonclick(length):
    # 计数器
    count = 1
    while count <= 5:
        # 前进50 第count条边
        turtle.forward(length)
        # 右转 144度
        turtle.right(144)
        count += 1


if __name__ == '__main__':
    main()


"""
  turtle 库的补充
  turtle.penup() 抬起笔 之后移动画笔不绘制图形
  pendown() 落笔
  pensize() 笔的宽度
  pencolor() 笔的颜色
  white black grey dark green   




"""