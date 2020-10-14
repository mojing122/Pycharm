balance = eval(input("本金为："))
year = eval(input("存入年数："))
i = 1

while i <= year:
    balance *= 1.05
    i = i+1
#同步

print("本息总和为:",balance)