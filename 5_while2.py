"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
  "Как дела?": "Хорошо!",
  "Что делаешь?": "Программирую",
  "На чём программируешь?": "На питоне",
  "Что программируешь?": "Цикл while",
  "Получается?" : ":("
  }


my_keys = questions_and_answers.keys()
my_values = questions_and_answers.values()


def ask_user(answers_dict):
    user_que = input("Введите вопрос: ").capitalize()
    while True:
        if user_que in my_keys:
            print(questions_and_answers[user_que])
            break
        else:
            user_que = input("Введите вопрос: ").capitalize()
      
       
if __name__ == "__main__":
        ask_user(questions_and_answers)
