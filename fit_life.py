WATER_PER_KG = 30
ML_IN_L = 1000


def bmi():
    print("Здравствуйте!")
    user_name = input("Пожалуйста, введите ваше имя: ")
    user_age = int(input("Пожалуйста, введите ваш возраст: "))
    user_weight = float(input("Пожалуйста, введите ваш вес в килограммах: "))
    user_height = float(input("Пожалуйста, введите ваш рост в метрах, используя точку: "))
    #расчет ИМТ и нормы воды
    bmi = round(user_weight / (user_height ** 2), 1)
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / ML_IN_L

    print(f'Отчет для пользователя {user_name} ({user_age}).\n'
          f'Твой Индекс Массы Тела: {bmi}\n'
          f'Рекомендуемая норма воды: {water_l} л')


bmi()
print('Расчет окончен\nБудьте здоровы!')
