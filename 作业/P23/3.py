ch = input("请输入一个字符：")
if 48<=ord(ch)<=57:
    print("输入的是数字")
elif 65<=ord(ch)<=90 or 97<=ord(ch)<=122:
    print("输入的是英文字母")
else:
    print("输入的是其他字符")