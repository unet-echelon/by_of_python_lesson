import random
#Вивод приветствия
greetings = [
   "Привет, дорогой друг. Отвечаю на твой вопрос... ",
   "Кто вопрошает, тот получит ответ: ",
   "Здравствуй, смертный. Сегодня для тебя такой ответ: "
]
##sample - выводит рандомно 1 елемент масива
print(random.choice(greetings))
print()
#Вивод ответов
answers = [
  #Положительные ответи
  "Бусспорно",
  "Предрешео",
  "Никаких сомнений",
  "Определённо да",
  "Может быть уверен в этом",

  #Нерешительно положительные
  "Мне кажеться - да",
  "Вероятнее всего",
  "Хорошие перспективы",
  "Знаки говорят - да",
  "Да",
  
  #Нейтральные
  "Пока не ясно, попробуй снова",
  "Спроси позже",
  "Лучше не рассказивать",
  "Сейчас нельзя предсказать",
  "Сконцентрируйся и спроси опять",

  #Отрицание
  "Даже не думай",
  "Мой ответ - нет",
  "По моим данным - нет",
  "Перспективы не очень хорошие",
  "Весьма сомнительно"
]
print(random.choice(answers))