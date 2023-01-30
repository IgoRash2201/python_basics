"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

""" Задание №5 """

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        my_str = input('Введите строку чисел через пробел (для суммирования). Либо нажмите Z для выхода:  ').split()

        res = 0
        for el in range(len(my_str)):
            if my_str[el] == 'z' or my_str[el] == 'Z':
                ex = True
                break
            else:
                res = res + int(my_str[el])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Ваша окончательная сумма: {sum_res}')
    exit('Программа завершена')
my_sum()
