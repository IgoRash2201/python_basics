"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

""" Решение задания №6 """ 
start = float(input('Ввести расстояние первой пробежки в км: '))
the_end = float(input('Ввести целевой результат за тренировку в км: '))
training = 0
while start < the_end:
    start += 0.1
    training += 1
print(f"На {training}-й день спортсмен достиг результата — не менее {the_end} км")
