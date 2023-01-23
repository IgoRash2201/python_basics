"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

""" Решение задания №6 """
list_1 = []
while True:
    list_1.append((input("Номер товара: "),
                   {"Названия": input("Название: "),
                    "Цены": input("Цена: "),
                    "Количества": input("Количество: "),
                    "ед.": input("Ед. учёта: ")}))
    e = input("Закончить ввод данных? Y / N: ")
    if e == "Y":
        break
list_1 = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
          (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
          (3,{"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."})]
name_list = []
price_list = []
count_list = []
unit_list = []
result_dict = {}
for i in range(len(list_1)):
    name_list.append(list_1[i][1]['названия'])
    price_list.append(list_1[i][1]['цены'])
    count_list.append(list_1[i][1]['количества'])
    unit_list.append(list_1[i][1]['ед.'])
result_dict.update({'названия': name_list, 'цены': price_list, 'количества': count_list, 'ед.': unit_list})
print(result_dict)
