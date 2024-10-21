#Вариант 4
S1 = "армада"
print ("S1: ", S1)
print ("Замена", S1.replace("а","о"))
j = 0
for i in S1:
    if i == 'а':
        S1 = S1.replace(i, 'о')
        j+=1
print(S1)
print(f'Замен: {j}')
print(f'Символов: {len(S1)}')
