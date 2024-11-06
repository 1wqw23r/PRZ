#1
print('#1')
import random
from random import randint
from re import I
from tkinter import N
a=[randint(1,100) for i in range(5)]
max_num=max(a)
index=a.index(max_num)
print ("Массив:", a)
print ("Максимальное число:", max_num)
print ("Порядковый номер:", index)
#2
print ("#2")
mass = [random.randint(0, 10) for i in range(10)]
print(mass)
res = []
for i in mass:
    if i % 2 == 0:
        res.append(i)
if len(res) == 0:
    print('Нет чисел')
 
print(sorted(res, reverse=True))

    




