lst_who = ['小马','小羊','小鹿']
lst_where= ['草地上','电影院','家里']
lst_what = ['看电影','听故事','吃晚饭']
from random import  *
n1 = randint(0,2)
n2 = randint(0,2)
n3 = randint(0,2)
str = lst_who[n1]+'在'+lst_where[n2]+lst_what[n3]
print(str)