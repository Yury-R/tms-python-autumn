# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]
import random
from itertools import groupby
N = 100
l = [random.randint(-10, 10) for i in range(N)]
s = ''
for i in range(1,len(l)):
    if l[i-1] < l[i]:
        s += '+'
    else:
        s += '-'
g = groupby(s)
out = [k for k,v in g if k=='+']
print('result:',len(out))