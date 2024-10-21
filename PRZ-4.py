#1
a = int(input("Введите число A: ")) 
b = int(input("Введите число B: ")) 
while a<=b:
    print ('Числа от a до b:', a)
    a+=1
#2
a = int(input("Введите число A: ")) 
b = int(input("Введите число B: ")) 
while a<b:
    print ('Числа от a до b:', a)
    a+=1
while a>b:
    a-=1
    print ('Числа от a до b:', a)
    break
#3    
a = int(input('1 число'))
b = int(input('2 число'))
for i in range(a|1, b+1, 2): 
        print(i, end=' ; ')
#4

sum=0
for i in range(int(input("Колличество чисел"))):
    sum+=int(input('Введите несколько чисел'))
print(sum)
#5
n = int(input('Число:'))
sum_of_factorials = 1
curr_factorial = 1
for i in range(2, n + 1):
    curr_factorial *= i
    sum_of_factorials += curr_factorial
print(sum_of_factorials)
#6
res = 1
n = int(input('число: '))
for i in range(1, n + 1):
    res *= i
print(res)
#7
n = int(input())
N = 1
sum = 0
for a in range(1, n+1):
    for b in range(1, a+1):
        N = N * b
    sum += N
print(sum) 
#8
n = int(input())
 
for i in range(n):
    for j in range(1, i+2):
        print(j, end='')
    print()
#9
def task(n):
   s,c,p=0,0,1
   for _ in range(n):
      c,p=c+p,c
      s+=c
   return s 
 
n=int(input("n="))
print(task(n))
#10
a, b = 1, 1
n = int(input())
num = 2
while b<n:
    a, b = b, a + b
    num += 1
OK = n == b
print(int(OK))
if OK:
    print(num)