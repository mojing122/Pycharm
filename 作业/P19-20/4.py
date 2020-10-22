months="JanFebMarAprMayJunJulAugSepOctNovDec"
i=eval(input("请输入一个数："))
pos = 3*(i-1)

print("{}月对应的英文缩写是：{}".format(i,months[pos:pos+3]))

