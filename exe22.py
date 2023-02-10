'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств'''
n=int(input('Введите количество элементов первого множиства: '))
m=int(input('Введите количество элементов первого множиства: '))
first=[]
for i in range(n):
    new_element=int(input(f'Введите {n} числа для множества 1: '))
    first.append(new_element)
second=[]
for i in range(m):
    new_element=int(input(f'Введите {m} числа для множества 2: '))
    second.append(new_element)
print(first)
print(second)
first_mn=set(first)
second_mn=set(second)
temp=first_mn.intersection(second_mn)
a=sorted(temp)
print(a)


