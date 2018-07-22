# 获取规定的图形面积
# ZD


def yuan(number):

    r = float(input("请输入圆的半径:"))
    s = 3.14*r*r
    return round(s, number)


# 长方形
def chang(number):
    w = input('请输入长方形的宽：')
    h = input('请输入长方形的高：')
    s = float(w)*float(h)
    return round(s, number)


# 三角形
def san(number):
    d = input('请输入三角形的底：')
    h = input('请输入三角形的高：')
    s = float(d)*float(h)/2
    return round(s, number)


# 正方形
def fang(number):
    d = input('请输入正方形的边长：')
    s = float(d)**2
    return round(s, number)


# 菱形
def ling(number):
    d1 = input('请输入菱形的第一条对角线：')
    d2 = input('请输入菱形的第二条对角线：')
    s = float(d1)*float(d2)/2
    return round(s, number)


# 椭圆
def tuo(number):
    d1 = input('椭圆长：')
    d2 = input('椭圆宽：')
    s = 3.14*float(d1)*float(d2)/4
    return round(s, number)


# 梯形
def ti(number):

    d1 = input('梯形上边长：')
    d2 = input('梯形下边长：')
    h = input('梯形下的高：')
    s = (float(d1)+float(d2))*float(h)/2
    return round(s, number)


# flag是true 的时候循环，是false的时候结束循环
flag = True
while flag:
    tag = input('请输入你要计算面积的图形：（yuan，chang，san，fang, ling, tuo, ti, tui）')
    if tag == 'yuan':
        print('开始计算圆形的面积！')
        print('圆形的面积是:', yuan(2))

    elif tag == 'san':
        print('开始计算三角形的面积！')
        print('三角形的面积是:', san(2))

    elif tag == 'chang':
        print('开始计算长方形的面积！')
        print('长方形的面积是:', chang(2))

    elif tag == 'fang':
        print('开始计算正方形的面积！')
        print('正方的面积是:', fang(2))

    elif tag == 'ling':
        print('开始计算菱形的面积！')
        print('菱形的面积是:', ling(2))

    elif tag == 'tuo':
        print('开始计算椭圆的面积！')
        print('椭圆的面积是:', tuo(2))

    elif tag == 'ti':
        print('开始计算梯形的面积！')
        print('梯形的面积是:', ti(2))

    elif tag == 'tui':
        flag = False
        print('\n已经退出')
