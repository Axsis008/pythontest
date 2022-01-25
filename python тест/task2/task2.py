numbers1 = []
for line in open("файл1.txt").readlines():
    numbers1.extend([int(n) for n in line.split()])
x = numbers1[0]
y = numbers1[1]
r = numbers1[2]
numbers2 = []
for line in open("файл2.txt").readlines():
    numbers2.extend([int(n) for n in line.split()])
x1 = numbers2[0]
y1 = numbers2[1]
x2 = numbers2[2]
y2 = numbers2[3]
x3 = numbers2[4]
y3 = numbers2[5]
import math
tochka1 = math.sqrt(x1**2 + y1**2)
if tochka1 <= r:
    print(x1, y1,'= Точка принадлежит окружности')
else:
    print(x1, y1, '= Точка не принадлежит окружности')
tochka2 = math.sqrt(x2**2 + y2**2)
if tochka2 <= r:
    print(x2, y2, '= Точка принадлежит окружности')
else:
    print(x2, y2, '= Точка не принадлежит окружности')
tochka3 = math.sqrt(x3**2 + y3**2)
if tochka3 <= r:
    print(x3, y3,'= Точка принадлежит окружности')
else:
    print(x3, y3, '= Точка не принадлежит окружности')
