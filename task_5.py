"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        	Например:
# >>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
from random import randint
from random import choice


def get_jokes(n, repeat=False):
    """
    Функция возвращает случайные шутки, сформированные из трех спиской слов

    :param n: колличество шуток
    :param repeat: посторять слова или нет
    :return: список случайных шуток
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_ha_ha = []
    for i in range(0, n):
        if repeat and len(nouns) == 0:
            break
        nouns_select = randint(0, len(nouns) - 1)
        adverbs_select = randint(0, len(adverbs) - 1)
        adjectives_select = randint(0, len(adjectives) - 1)
        list_ha_ha.append(' '.join([nouns[nouns_select], adverbs[adverbs_select], adjectives[adjectives_select]]))
        if repeat:
            nouns.pop(nouns_select)
            adverbs.pop(adverbs_select)
            adjectives.pop(adjectives_select)

    return list_ha_ha


print(help(get_jokes))
print(get_jokes(repeat=True, n=8))