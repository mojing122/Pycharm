dicsell={"方糖":99,"X1":499,"魔盒":399,"曲奇":299}
sum = 0
max = 0
count = 0
for k,v in dicsell.items():
    print("{:3}………………{:3}元".format(k,v))
    sum = sum+v
    count+=1
    if v>max:
        max=v
avg = sum/count
print("平均价格为{}元，最高价格为{}元".format(avg,max))