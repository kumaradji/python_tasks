# def get_rect_value(a, b, type=0):
#     return a * b if type else (a + b) * 2


# P = 'ihdbciwhbcihw!'
#
# def check_password(P, chars="$%!?@#"):
#     return True if len(P) >= 8 and any(i in P for i in chars) else False
#
#
# print(check_password(P))

# M = input()
#
#
# def mail(M):
#     if '@' and '.' in M:
#         print('ДА')
#     else:
#         print('НЕТ')
#
# s = 'ZpglnRxqenU'
#
#
# def accum(s):
#     str = [char for char in s]
#     res = []
#     a = 0
#     for x in str:
#         a += 1
#         b = x * a
#         b = b.title()
#         res.append(b)
#     res = '-'.join(res)
#
#     return res
#
#
# print(accum(s))

# def accum(s):
#     return '-'.join((a * i).title() for i, a in enumerate(s, 1))

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
# number = 86543.43
#
#
# def opposite(number):
#     # return number + abs(number) * 2 if number < 0 else number - number * 2
#     return number - number * 2
#
# print(opposite(number))
# a = "45385593107843568"
#
#
# def fake_bin(x):
#     sss = x
#     res = ""
#     for i in sss:
#         if int(i) >= 5:
#             res += "1"
#         if int(i) < 5:
#             res += "0"
#     return res
#
#
# print(fake_bin(a))
#
#
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)

# '''
# Реализуйте функцию unique_in_order, которая принимает в качестве аргумента
# последовательность и возвращает список элементов без каких-либо элементов
# с одинаковым значением рядом друг с другом и сохраняет исходный порядок элементов.
#
# '''
#
# sequence = "AAAABBBCCDAABBB"
#
#
# def unique_in_order(sequence):
#     chars = []
#     for i in range(len(sequence)):
#         if i == 0 or sequence[i] != sequence[i - 1]:
#             chars.append(sequence[i])
#     return chars
#
#
# def unique_in_order(iterable):
#     res = []
#     for item in iterable:
#         if len(res) == 0 or item != res[-1]:
#             res.append(item)
#     return res
#
#
# print(unique_in_order(sequence))


# '''Завершите функцию так, чтобы она нашла среднее значение
# из трех переданных ей баллов и вернула
# буквенное значение, связанное с этой оценкой.'''
# def get_grade(s1, s2, s3):
#     score = (s1 + s2 + s3) / 3
#     if 90 <= score <= 100:
#         return "A"
#     elif 80 <= score < 90:
#         return "B"
#     elif 70 <= score < 80:
#         return "C"
#     elif 60 <= score < 70:
#         return "D"
#     elif 0 <= score < 60:
#         return "F"
#
#
# print(get_grade(100, 85, 96))
#
# '''Вы, вероятно, знаете систему "лайков" на Facebook и
# других страницах. Люди могут "лайкать" записи в блоге,
# фотографии или другие элементы. Мы хотим создать текст,
# который должен отображаться рядом с таким элементом.
#
# Реализуйте функцию, которая принимает массив, содержащий
# имена людей, которым нравится элемент. Он должен
# возвращать отображаемый текст, как показано в примерах:
#
# [] --> "это никому не нравится"
# ["Питер"]                         --> "Питеру это нравится"
# ["Джейкоб", "Алекс"] --> "Джейкоб и Алекс вот так"
# ["Макс", "Джон", "Марк"] --> "Макс, Джон и Марк вот так"
# ["Алекс", "Джейкоб", "Марк", "Макс"] --> "Алекс, Джейкоб и еще 2 таких же"
# Примечание: Для 4 или более имен число в "и 2 других" просто увеличивается.
# '''
#
# names = ['Alex', 'Jacob', 'Mark', 'Max', 'Alex', 'Jacob', 'Mark', 'Max']


# def likes(names):
#     n = len(names)
#
#     if names == []:
#         return 'no one likes this'
#     elif n == 1:
#         return f'{names[0]} likes this'
#     elif n == 2:
#         return f'{names[0]} and {names[1]} like this'
#     elif n == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     elif n == 4:
#         return f'{names[0]}, {names[1]} and 2 others like this'
#     elif n > 4:
#         return f'{names[0]}, {names[1]} and {n - 2} others like this'
#
#
# print(likes(names))


# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n - 2)
#
#
# print(likes(names))