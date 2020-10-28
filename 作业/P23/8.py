x = eval(input("请输入该点的横坐标："))
y = eval(input("请输入该点的纵坐标："))

if x>0 and y>0:
    print("该点在第一象限")
elif x>0 and y<0:
    print("该点在第二象限")
elif x<0 and y<0:
    print("该点在第三象限")
elif x<0 and y>0:
    print("该点在第四象限")
else:
    print("该点在坐标轴上")
