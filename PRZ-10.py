print ("PRZ-8")
import random 
from random import randint
import math

print ("#1")
matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print('Исходная матрица:',matrix)
s=[]
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print("Строка с наибольшей суммой:",matrix[s.index(max(s))],"Сумма элементов:",max(s),"Строка с наименьшей суммой:",matrix[s.index(min(s))],"Сумма элементов:",min(s))

print ("#2")
a = [[1,2,-3],
     [-1,2,3],
     [1,-2,3]]
a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')
with open('ФИО_группа_vvod.txt', 'r') as fin:
    with open('ФИО_группа_vivod.txt', 'w') as fout:
        fout.writelines(fin.readlines())