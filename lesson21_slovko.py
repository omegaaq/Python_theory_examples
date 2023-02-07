# гра 'Словко'

from random import choice


lst_guess_words = ['okean', 'viter', 'train', 'kumys', 'fayno', 'brody']

def check_word_decorator(func):
    used_words = []

    def wrapper(*args, **kwargs):
        nonlocal used_words
        if kwargs['answer'] in used_words:
            return True

        used_words += [kwargs['answer']]
        if func(*args,**kwargs):
            return kwargs['answer']
        return False

    return wrapper


@check_word_decorator
def check_word(guess, answer,*args, **kwargs):
    if guess == answer:
        return True
    return False


def translate_decorator(func):
    tries = dict()
    def wrapper(*args, **kwargs):
        print('decorator work')
        func(*args, **kwargs)

    return wrapper

# !!!!!!!!!    -----Home task here
@translate_decorator
def translate(answer, guess):
    print('translete def work')
    print(' '.join(answer))
    text = ''
    for tup in zip(answer, guess):
        if tup[0] == tup[1]:
            text += '+'
        else:
            text += ' '

    print(' '.join(text))
    return True


lives = 6
rand_word = choice(lst_guess_words)
while lives > 0:
    print(rand_word)
    user_answer = input('enter word:')
    if len(user_answer) == 5:
        res = check_word(guess=rand_word, answer=user_answer, lst_guess_words=lst_guess_words)
        print(res)
    else:
        print('word is more than 5 symbols')
        continue

    if type(res) is not bool:
        lst_guess_words.remove(res)
        print('you are win')
        print(lst_guess_words)
        break
    elif res:
        print(f'ви вже вводили слово {user_answer}')
        continue
    translate(answer=user_answer, guess=rand_word)
    lives -= 1
    print(f'u have {lives} lives')


# guess = 'okean'
# while True:
#     answer = input('enter:')
#     text = ''
#     print(' '.join(answer))
#     for tup in zip(answer, guess):
#         if tup[0] == tup[1]:
#             text += '*'
#         else:
#             text += ' '
#     print(' '.join(text))


# guess = 'okean'
# while True:
#     answer = input('enter:')
#     text = ''
#     print(' '.join(answer))
#     for tup in zip(answer, guess):
#         if tup[0] == tup[1]:
#             text += '+'
#         else:
#             if tup[0] in guess:
#                 text += '*'
#             else:
#                 text += ' '
#     print(' '.join(text))