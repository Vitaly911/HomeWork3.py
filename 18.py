from random import randint
long = int(input('Введите количество элементов в массиве: '))
mass = []
for i in range(long):
    mass.append(randint(-10, 10))
print(mass)    
number = int(input('Введите число: '))
i = 0
max = 0
while(i < len(mass)):
    if(max < mass[i]):
        max = mass[i]
    i +=1
if(number > max):
    print(max)
i = 0
j = 0
while(i < max):
    while(j < len(mass)):
        if(number == mass[j]):
            print(mass[j])
            i = max
        else:
            if(number == mass[j] - i):
                print(mass[j])
                i = max
            else:
                if(number == mass[j] + i):
                    print(mass[j])
                    i = max
        j += 1            
    i += 1
    j = 0