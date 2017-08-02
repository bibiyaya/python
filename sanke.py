#turtle是Python很流行的图像库
import turtle
#库的引用有两种方式，除了上述的一种，也可以这样  from turtle import *,使用该方法引入库时，可以直接使用函数，而不需要加上库名

#def用于定义函数，def函数未经调用是不会被执行的,def后连续缩进的语句都是这个函数的一部分，

#Python魅力所在是因为可以大量调用外部函数库，开始执行语句也是main函数。

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnake(40, 80, 5, pythonsize/2)

main()
