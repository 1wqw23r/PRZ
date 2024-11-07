print ("PRZ-4")
print ("#1")

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mul(a,b,c,d):
    num = a * c
    den = b * d
    val = gcd (num,den)
    return num // val, den // val

a = int (input("Числитель первой дроби: "))
b = int (input("Знаменатель первой дроби: "))
c = int (input("Числитель второй дроби: "))
d = int (input("Знаменатель второй дроби: "))

result = mul (a,b,c,d)
print ("Умножение дробей: {}/{}".format(result[0],result[1]))

print ("#2")

a = 0 
b = 0 
R = 10 

def Func(x,y): 
    if (x-a)**2+(y-b)**2<R**2: 
        return True 
    else: 
        return False 

p1 = 1 
p2 = 3 
if Func(p1,p2): 
    print("Точка P лежит внутри окружности") 
else: 
    print("Точка P лежит не внутри окружности") 

f1 = 10 
f2 = 7 
if Func(f1,f2): 
    print("Точка F лежит внутри окружности") 
else: 
    print("Точка F лежит не внутри окружности") 

l1 = 1 
l2 = 1 
if Func(l1,l2): 
    print("Точка L лежит внутри окружности") 
else: 
    print("Точка L лежит не внутри окружности")
