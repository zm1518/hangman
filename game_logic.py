import random
from word_list import random_word
hangman_parts = [
    ' o',
    ' |',
    '/|\\',
    ' |',
    '/ \\'
]
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def game():
    letter_error = 1
    letters = []

    while True:
        letter = input().lower()
        if letter not in ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                          'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']:
            print('Вы ввели неправильный символ')

        elif letter in set(random_word):
            print('Правильно! Такая буква есть!')
            letters.append(letter)
            if len(letters) == len(set(random_word)):
                print('Поздравляю! Вы выиграли!')
                print(f'Загаданное слово - {random_word}')
                break
        else:
            for i in range(1, letter_error + 1):
                print(hangman_parts[i - 1])
            letter_error += 1
            if letter_error == 6:
                print('Игра закончена!')
                print(f'Угаданные буквы - {",".join(letters)}')
                print(f'Загаданное слово - {random_word}')
                break

def trait():
    num_trait = len(random_word)
    print(f'В слове {num_trait} букв. Напишите букву')
    print('_' * num_trait)
    game()