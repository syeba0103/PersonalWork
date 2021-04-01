import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'Sukegawa AI'
    if answer_number == 2:
        return 'Yamagishi Haruka'
    if answer_number == 3:
        return 'Ikemiya Mutuki'
    if answer_number == 4:
        return 'Sano Hitomi'
    if answer_number == 5:
        return 'Kubota Sayo'
    if answer_number == 6:
        return 'Osuji Yurika'
    if answer_number == 7:
        return 'Kadono Yui'

r = random.randint(1, 7)
fortune = get_answer(r)
print(fortune)
print(fortune)