import random
lst_suit=["黑桃","红桃","梅花","方块"]
lst_face=["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
lst=[x+y for x in lst_face for y in lst_suit]
random.shuffle(lst)
player = int(input("请您抽一张牌(0~51):"))
card1=lst[player]
print("您抽到的牌是：{}".format(card1))
com=random.randint(0,51)
card2=lst[com]
print("电脑抽到的牌是：{}".format(card2))
players=lst_face.index(card1[0])
coms=lst_face.index(card2[0])
if players>coms:
    print("恭喜，您赢了！")
elif players<coms:
    print("很遗憾，您输了！")
else:
     print("咱们平手了！")
