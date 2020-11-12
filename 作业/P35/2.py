lst = [31,28,31,30,31,30,31,31,30,31,30,31]
while True:
    n = eval(input("请输入一个月份数字，若输入0则结束循环："))
    if n!=0:
        print(lst[n-1])
    else:
        break
