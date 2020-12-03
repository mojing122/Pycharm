def plus(i):
    if i == 1: return 1/3
    else:return  plus(i-1)+i/(2*i+1)

i = eval(input())
print(plus(i))


