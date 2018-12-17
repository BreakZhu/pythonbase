"""
   作者:朱洪明
   功能:利用递归绘制分形树

"""
import turtle


def draw_branch(branchLength):
    # 绘制分形树树枝的函数
    if branchLength > 2:
        # 画右侧
        turtle.forward(branchLength)
        print("向前", branchLength)
        turtle.right(20)
        print("向右 20 度")
        draw_branch(branchLength-15)

        # 绘制左侧
        turtle.left(40)
        print("向左 40 度")
        draw_branch(branchLength-15)

        # 返回之前的树枝
        turtle.right(20)
        print("向右 20 度")
        turtle.backward(branchLength)
        print("向后 ", branchLength)


def main():
    """
     主函数
   """
    turtle.left(90)
    draw_branch(40)
    turtle.exitonclick()
    pass


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
