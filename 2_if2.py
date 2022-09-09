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

def lines(line_1, line_2):
    if type(line_1) is not str or type(line_2) is not str:
        return(0)
    elif line_1 == line_2:
        return(1) 
    elif len(line_1) > len(line_2):
        return(2)
    elif line_2 == 'learn':
        return(3)


answer_1 = lines(1, 'python')
answer_2 = lines('python', 'python')
answer_3 = lines('learn_python', 'python')
answer_4 = lines('py', 'learn')

print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)





if __name__ == "__main__":
    main()
