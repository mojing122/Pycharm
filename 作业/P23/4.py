km = float(input("请输入千米数："))
if km <= 0:
    print("千米数输入有误，请重新输入：")
elif 0 < km <= 3:
    print("您需支付10元车费！")
elif km <= 10:
    cost = 10+1.2*(km-3)
    print("您需要支付{:.1f}元车费".format(cost))
else:
    cost = 18.4+1.5*(km-10)
    print("您需要支付{:.1f}元车费".format(cost))