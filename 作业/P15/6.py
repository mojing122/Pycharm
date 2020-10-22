m = eval(input("请输入一个三位数："))

a = m//100
b = m//10-a*10
c = m%10
n = a+b*10+c*100

print("倒序数为：",n)