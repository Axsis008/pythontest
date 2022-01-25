mas = []
for line in open("файл.txt").readlines():
    mas.extend([int(n) for n in line.split()])
import math
x = sorted(mas)[len(mas) // 2]
print(sum(abs(v - x) for v in mas))
