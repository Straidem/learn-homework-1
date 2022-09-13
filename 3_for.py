"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

from cgi import FieldStorage
from re import S
from tabnanny import verbose
from traceback import format_tb


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]



len_sum = 0
all_sum = 0
for sale in sales:
    item_sum = 0
    for product in sale['items_sold']:
        item_sum = item_sum + product      
    all_sum = all_sum + item_sum
    print(f'Cуммарное количество продаж для {sale["product"]}: {item_sum}') 
    print(f"среднее количество продаж для {sale['product']}: {round(item_sum / len(sale['items_sold']),2)}")
    all_len = len(sale['items_sold'])
    len_sum = len_sum + all_len
print(f'Длина всех ключей items-sold: {len_sum}')
print(f'Среднее количество продаж всех товаров: {all_sum / len(sale["items_sold"])}')
print(f'Общее количество продаж для всех товаров: {all_sum}')
        















if __name__ == "__main__":
    main()
