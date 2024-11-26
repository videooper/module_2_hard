# Дополнительное практическое задание по модулю: "Основные операторы"
# Задание "Слишком древний шифр":

# Вывод паролей для одного, вводимого числа
def pairs(number):
    result = []
    for i in range(1, 20):
        for j in range(i + 1, 20):
            suma = i + j
            if number % suma == 0:
                result.append(i)
                result.append(j)
    print(number, ' - ', *result)

attempts = 3  # Количество попыток

for attempt in range(attempts):
    number = int(input('Введите число (от 3 до 20): '))
    if 2 < number < 21:
        pairs(number)
        print('Введен правильный шифр')
        print('Ворота открываются')
        break  # Выход из цикла, если число введено правильно
    else:
        if attempt < attempts - 1:
            print('Введен неверный код, попробуйте еще раз.')
            print('Шипы все ближе')
        else:
            print('Все попытки исчерпаны.')

# Вывод сообщения, если все попытки исчерпаны
if attempt == attempts - 1 and not (2 < number < 21):
    print('Вас раздавило шипами')

# Вывод всех паролей для чисел от 3 до 20:
"""
for i in range(3,21):
    result = []
    for j in range(1, 20):
        for k in range (j + 1, 20):
            if i % (j + k) == 0:
                result.append(j)
                result.append(k)
                break
    print(i, ' - ', *result)
"""