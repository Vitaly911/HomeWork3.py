from random import randint
number = int(input('Введите количество элементов в массиве: '))
count = 0
mass = []
for i in range(number):
    mass.append(randint(-10, 10))
a = int(input('Введите число: '))
while (i < number):
    if (a == mass[i]):
        count += 1
    i += 1
print(count)
print(mass)