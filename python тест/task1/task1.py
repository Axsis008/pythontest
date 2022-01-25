n = int(input())
m = int(input())
mas = [1,2,3,1,2,3,1]
def circular():
    while True:
        for connection in mas:
            yield connection
from itertools import chain, repeat
i = 0
while i <= n:
    print(mas[i])
    i += m

