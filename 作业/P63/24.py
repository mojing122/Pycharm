trunk={'红色':'活泼而充满斗志的人','黄色':'智慧型的理想家','蓝色':'浪漫的人','绿色':'谨慎而知性的人','紫色':'注重美感和个性化的人'}
print('有红色，黄色，蓝色，绿色，紫色可选')
def test(color):
    s = trunk[color]
    return s

color=input('请输入一个颜色：')
print(test(color))
n = input('是否继续：yes or no')
while True:
    if n == 'yes':
        color = input('请输入一个颜色：')
        print(test(color))
    else:
        break




