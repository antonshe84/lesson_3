"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
"один"
# >>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
 начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
"Один"
# >>> num_translate_adv("two")
"два"
"""

numb_dict = {   'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}

def num_translate_adv(numb_str):
    if numb_str.istitle():
        numb_ru = numb_dict.get(numb_str.lower())
        if numb_ru is None:
            return None
        else:
            return numb_ru.title()
    else:
        return numb_dict.get(numb_str)


print(num_translate_adv('three'))
print(num_translate_adv('eleven'))
print(num_translate_adv('Eight'))
print(num_translate_adv('Twelve'))
print(num_translate_adv('Ten'))
print(num_translate_adv('five'))



