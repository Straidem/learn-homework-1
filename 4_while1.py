"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    user_ask = input("Как дела? ")
    while user_ask != "Хорошо":
        user_ask = input("Как дела? ")
        if user_ask == "Хорошо":
            break

    #Или можно так:
    #while True:
        #ask = input("Как дела? ")
        #if ask == "Хорошо":
            #break

    
if __name__ == "__main__":
    hello_user()
