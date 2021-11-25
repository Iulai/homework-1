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
sold_products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    def items_counter(sold_phones):
        items_sum = 0
        for items in sold_phones:
            items_sum += items
        return items_sum

    def product_avg(sold_phones):
        for phones in sold_phones:
            return len(sold_phones)

    sum_counter = 0
    for prod in sold_products:
        product_sum = items_counter(prod['items_sold'])
        print(f'Суммарное количество продаж телефона {prod["product"]}: {product_sum}')
        sum_counter += product_sum

    len_counter = 0
    for el in sold_products:
        items_avg = items_counter(el['items_sold'])
        phones_avg = product_avg(el['items_sold'])
        print(f'Среднее количество продаж телефона {el["product"]}: {int(items_avg / phones_avg)}')
        len_counter += phones_avg

    print(f'Суммарное количество продаж всех товаров: {sum_counter}')
    print(f'Среднее количество продаж всех товаров: {int(sum_counter / len_counter)}')


if __name__ == "__main__":
    main()
