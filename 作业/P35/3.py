lst = [1,1]
for i in range(1,29):
    lst.append(lst[-1]+lst[-2])
print(lst)