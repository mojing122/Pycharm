import math

a = eval(input("请输入第一条边长的长度："))
b = eval(input("请输入第二条边长的长度："))
c = eval(input("请输入第三条边长的长度："))

if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    h = (a+b+c)/2
    area = math.sqrt(h*(h-a)*(h-b)*(h-c))
    print("三角形周长为：",h*2)
    print("三角形面积为：",area)
else:
    print("输入的三边无法构成三角形")

