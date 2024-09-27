#PRZ-2 вариант-4
import math
x=int (0.4*10**4)
y=-0.875
z=-0.475*10**(-3)
d=math.cos(x)
e=math.cos(y)
f=math.sin(y)**2
result= abs(d-e)**(1+2*f)*(1+z+((z**2)/2)+((z**3)/3)+((z**4)/4))
print("X равен:", x)
print('Косинус X(',x,')=',d)
print('Косинус Y(',y,')=',e)
print('Синус Y^2(',y,')=',f)
print("Ответ:", result)