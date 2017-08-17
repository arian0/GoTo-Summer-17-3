import random

while True:
    secret_number = random.randint(1,10)
    answer = input('Введи число от 1 до 10: ')

    if answer.lower() == "хватит!":
        break
    else:
        answer = int(answer)

    while answer != secret_number:
        print("Неправильно! Азаза!")
        answer = int(input('Попробуй еще раз: '))

    print("Да! Ответ - {0}".format(answer))
    
print("Ок, все...")
        
