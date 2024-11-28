x=1
while x<5:
    for i in range(3):
        if i == 2:
            x+=1
            break
        x+=1
        print(x)