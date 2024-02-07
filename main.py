from game_logic import game, trait
from word_list import random_word

print('Привет! Давай сыграем в игру? да/нет')
answer = input().lower()
if answer == 'да':
    print('Круто!')
    trait()
else:
    print('Жалко! До встречи!')