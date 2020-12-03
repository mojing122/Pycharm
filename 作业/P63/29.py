def y(n):
    if n==0:return 0
    elif n==1:return 1
    elif n==2:return  2
    else:return y(n-1)+y(n-2)+y(n-3)
n = eval(input())
print(y(n))