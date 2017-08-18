word = input('Введите слово:').lower()

old_words = [word]

while True:
    new_word = input('Введите слово:').lower()
    
    if word[-1] == new_word[0] and new_word not in old_words:
        print('Подходит')
        old_words.append(new_word)
        word = new_word
        print('Теперь другой игрок!')
    else:
        print('Не подходит')
