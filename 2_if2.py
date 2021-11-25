"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    def str_compare(arg_one, arg_two):
        result = ''

        if (type(arg_one) == str and type(arg_two) == str) is False:
            result = 0

        elif arg_one == arg_two:
            result = 1

        elif len(arg_one) > len(arg_two):
            result = 2

        elif arg_one != arg_two and arg_two == 'learn':
            result = 3

        else:
            print('Bug')

        return result

    print(str_compare((input('Введите первую строку: ')), (input('Введите вторую строку: '))))


if __name__ == "__main__":
    main()