# Задача 2: Найдите сумму цифр трехзначного числа.
print('Введите трёхзначное число')
number = input()
sumn = 0
num = 0
for n in number:
    num = int(n) 
    sumn += num
print("Сумма цифр: ", sumn)


