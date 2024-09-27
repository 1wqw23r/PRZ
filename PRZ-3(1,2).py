#PRZ-3(1.2)
a= int (input("Введите двузначное число:"))
print (a)
if len(str(a))==2:
    print ("Введено двузначное число")
else:
    print ("Неправильное число")
if a%10 == a//10:
    print("Да")
else:
    print("Нет")