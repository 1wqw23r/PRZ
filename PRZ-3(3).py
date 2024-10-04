#PRZ-3(3)
#1
import math
from math import sqrt
print ("Задание 1")
a= int (input("Введите первое число:"))
print (a)
b= int (input("Введите второе число:"))
print (b)
if a>b:
    print("a больше b")
elif a==b:
    print("числа равны")
else:
    print("a меньше b")
#2
print ("Задание 2")
a= int (input("Введите любое число:"))
print (a)
print ("Задание 2")
if a%2 == 0:
    print ("Число a четное")
else:
    print ("Число a нечетное")
#3
print ("Задание 3")
n = int(input())

for i in range(1, n + 1, 2):
    print(i, end=' ')
#4
print ("Задание 4")
n = int (input("Введите число:"))
print (n)
simple= True
i=2
while i <= sqrt(n):
    if n % i == 0:
        simple = False
        break
    i += 1

if simple:
    print ("Простое число")
else:
    print("Сложное число")
#5
print ("Задание 5")
a=int (input("Введите первое число:"))
print (a)
b=int (input("Введите второе число:"))
print (b)
c=int (input("Введите третье число:"))
print (c)
avg=(a+b+c)/3
print ("Среднее значение:", avg)
#6
print ("Задание 6")
a=int (input("Введите число:"))
print (a)
if a % 7 == 0:
    print ("Число кратно 7")
else:
    print ("Число не кратно 7")
#7
print ("Задание 7")
year = int(input("Введите год: "))

if year % 4 != 0:
    print ("Год не високосный")
else:
    print ("Год високосный")
#8
print ("Задание 8")
i = int(input("Введите номер месяца:"))
if i == 1 or i == 3:
    print(31)
elif i == 4 or i == 6:
    print(30)
elif i == 2:
    print(28)
else: 
    print ("такого месяца нет!")
#9
print ("Задание 9")
a=int (input ("Введите значение стороны a треугольника: "))
b=int (input ("Введите значение стороны b треугольника: "))
c=int (input ("Введите значение стороны c треугольника: "))
p= (a+b+c)/2
s=math.sqrt (p*(p-a)*(p-b)*(p-c))
print ("p - полупериметр треугольника:", p)
print ("s - площадь треугольника:", s) 
#10
print ("Задание 10")
a=int (input("Введите первое число:"))
print (a)
b=int (input("Введите второе число:"))
print (b)
c=int (input("Введите третье число:"))
print (c)
if a==b==c:
    print ("Все числа равны")
else:
    print ("Равенство отсутствует")
#11
print ("Задание 11")
age=int(input("Введите свой возраст:"))
print (age)
if age>=18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
#12
print ("Задание 12")
num = int (input("Введите любое число:"))
print (num)
if num >= 0:
    print ("Число положительное")
elif num == 0:
    print ("Число равно 0")
else:
    print ("Число отрицательное")
#13
print ("Задание 13")
year = int(input('Введите год: '))
 
if year % 100 == 0 and year % 400 == 0:
    print('В', year, 'году в феврале 29 дней')
elif year % 100 != 0 and year % 4 == 0:
    print('В', year, 'году в феврале 29 дней')
else:
    print('В', year, 'году в феврале 28 дней')
#15
print ("Задание 15")
a = int (input("Введите первое число:"))
print (a)
b = int (input("Введите второе число:"))
print (b)
sum = a+b
dif = a-b
print ("Сумма равна:", sum)
print ("Разность равна:", dif)
#16
print ("Задание 16")
a = int (input("Введите любое число:"))
print (a)
if a % 3 == 0 and a  % 5 == 0:
    print ("Число кратно 3 и 5")
else:
    print ("Число не кратно 3 и 5")
#17
print ("Задание 17")
year = int (input("Введите год:"))
print (year)
if year % 100 == 0:
    print ("Вековой год")
else:
    print ("Невековой год")
#18
print ("Задание 18")
a= input ("Число:")
print (a)
if (a%10==0):   print("Целое")
else: print("Дробное")