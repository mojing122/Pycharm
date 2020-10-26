n = eval(input("请输入一个年份（四位整数）："))
if n%400==0:
    print("是闰年")
elif n%4==0 and n%100!=0:
    print("是闰年")
else:
    print("不是闰年")