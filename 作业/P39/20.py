import random
lst_suit=["黑桃","红桃","梅花","方块"]
lst_face=["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
lst=[x+y for x in lst_face for y in lst_suit]
random.shuffle(lst)
idx_user = int(input("请您抽一张牌(0~51):"))
card_user=lst[idx_user]
print("您抽到的牌是：{}".format(card_user))
idx_computer=random.randint(0,51)
card_computer=lst[idx_computer]
print("电脑抽到的牌是：{}".format(card_computer))
val_user=lst_face.index(card_user[0])
val_computer=lst_face.index(card_computer[0])
if val_user>val_computer:
    print("恭喜，您赢了！")
elif val_user<val_computer:
    print("很遗憾，您输了！")
else:
     print("咱们平手了！")
