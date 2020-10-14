for year in range(2000,3000):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print(year,"是闰年")
            else:
                print(year,"不是闰年")
                #同步
        else:
            print(year,"是闰年")
    else:
        print(year,"不是闰年")

