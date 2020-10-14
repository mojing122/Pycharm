m = eval(input("请输入一个三位数："))

a = m//100
b = (m-a*100)//10
c = (m-a*100-b*10)
n = a+b*10+c*100

print("倒序数为：",n)