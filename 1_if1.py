"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
user_age = int(input("Введите Ваш возраст: "))

def age():  
    if user_age < 7:
        return("Тебе нужно учиться в детском саду")
    elif user_age >= 7 and user_age < 18:
        return("Тебе нужно учиться в школе")
    elif user_age >= 18 and user_age < 23:
        return("Тебе нужно учиться в ВУЗе")
    elif user_age >= 23 and user_age < 65:
        return("Уважаемый, Вам нужно работать!")
    else:
        return("Вам пора отдыхать и на пенcию)")
your = age()

print(your)

      


if __name__ == "__main__":
    main()
