# text = input().lower().split()
# words = []
#
# for i in text:
#     a = i.isalnum()
#     if a:
#         words.append(i)
# print(*words)


# THISL = ['THIS', 'IS', 'LOVE']
# print(list(map(str.lower, L)))

#
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
# если хотите продолжать работу как анонимный пользователь:""")
#
# auth = yesno == "Y"
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             global username
#             username = input("Введите ваш username:")
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь не авторизован. Функция выполнена не будет")
#     return wrapper
#
#
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещён")
#     return wrapper
#
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()
#
#
# def testing(arg):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return outer
#
#
# def
#
#
#


# # импортируем tkinter
# import tkinter
# # создаем окно
# window = tkinter.Tk()
# # создаем холст
# canvas = tkinter.Canvas(window)
# # размещаем в окне
# canvas.pack()
# # запускаем графический интерфейс
# window.mainloop()

# import tkinter
# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()
# canvas.create_rectangle(35, 45, 100, 150)
# canvas.create_rectangle(110, 135, 130, 170)
# window.mainloop()


# import time
# print(time.asctime())

# string = input()
# i = 0
# while i < len(string):
#     a = string.find('##')
#     if i == a:
#         break
#     else:
#         print(string[i])
#         i += 1

# text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# # разделение по пробелам
# splitted_text = text.split()
# print(splitted_text)
# print(splitted_text[6])     # дуб,

# number = input()
#
# if len(number) >= 8 and number.isdigit():
#     num_ = number[-4:]
#     num__ = len(number[:-4])
#     s = '*' * num__
#     print(s + num_)
#
# else:
#     print('Ошибка')

# Напишите рекурсивную функцию, находящую минимальный
# элемент списка без использование циклов и встроенной функции min().
#
# L = [12, 34, 75, 97, -34, -289, -56, 23, 45]
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
#
#
# a = min_list(L)
# print(a)


#
# a, b = input().split()
#
# print('Коды:', str(a), '=', str(ord(a)), ',', str(b), '=', str(ord(b)))
#
#

# def kort(tp):
#     def inner(s):
#         nonlocal tp
#         if tp(tuple(type)):
#         return tp
#
#     return inner
#
#
# tp = input()
# s = input()
# cnt = header(tp)
# print(cnt(s))


# def header(teg):
#     def inner(s):
#         nonlocal teg
#         return f'<teg>{s}</teg>'
#
#     return inner
#
#
# teg = input()
# s = input()
# cnt = header(teg)
# print(cnt(s))


'''
Реализуйте программу, которая сжимает последовательность символов.
На вход подается последовательность вида:

aaabbccccdaa

Необходимо вывести строку, где каждая последовательность
из одинаковых символов, идущих подряд, заменяется на один символ,
и длину этой последовательности (включая последовательности единичной длины).
Вывод должен выглядеть так:

a3b2c4d1a2
'''

# text = input()  # получаем строку
#
# last = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
#
# for c in text:
#     if c == last:  # если символ совпадает с сохраненным,
#         count += 1  # то увеличиваем счетчик
#     else:
#         result += last + str(count)  # иначе - записываем в результат
#         last = c  # и обновляем сохраненный символ с его счетчиком
#         count = 1
#
# result += last + str(count)  # и добавляем в результат последний символ
# print(result)


'''
Используя функцию zip() внутри генераторов списков,
вычислите поэлементные произведения списков L и M.
'''
#
# L = [i for i in range(10)]
# M = [i for i in range(10, 0, -1)]
#
# # for a, b in zip(L, M):
# #     c = a * b
# #     print('a =', a, 'b =', b)
# #     print(c)
#
# N = [a*b for a, b in zip(L, M)]
# print(N)


# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(T)


# L = [int(input()) % 2 == 0 for i in range(5)]
#
# print(L)
#
'''
Подумайте, как нужно записать логическое выражение, используя
all([ ]) и any([ ]) над списком четности, если его результат будет
истинным тогда и только тогда, когда в списке есть хотя бы один четный
и хотя бы один нечетный элемент
'''
# any(L) and not all(L)
#
# L = [for i % 2 == 0 in range()]
# print(any(i % 2 == 0) for (L) and any(i % 2 == 1) for (L))


'''
Используя замыкания функций, определите вложенную функцию, которая бы
увеличивала значение переданного параметра на 5 и возвращала бы вычисленный
результат. При этом внешняя функция должна иметь следующую сигнатуру:
def counter_add(): ...
Вызовите функцию counter_add и результат ее работы присвойте переменной с
именем cnt. Вызовите внутреннюю функцию через переменную cnt со значением
k, введенным с клавиатуры:
'''

# k = int(input())
# def counter_add():
#     global k
#     def add_5():
#         k + 5
#     return add_5
#
#
# cnt = counter_add()
# print(cnt)


# k = int(input())
#
# def counter_add(n):
#
#     def add_5(k):
#         return k + 5
#
#     return add_5
#
# k = counter_add(7)
#
# k()


# def make_tag(tagname):
#     # Оборачивает входящую строку msg в тег tagname
#     def wrap_a_message(msg):
#         return f'<{tagname}>{msg}</{tagname}>'
#
#     return wrap_a_message
#
# header = make_tag('h1')
# print(header('Заголовок')) # выводит <h1>Заголовок</h1>
#
#

'''
Подвиг 2. Используя замыкания функций, объявите внутреннюю 
функцию, которая увеличивает значение своего аргумента на некоторую 
величину n - параметр внешней функции с сигнатурой:
def counter_add(n): ...
Вызовите внешнюю функцию counter_add со значением аргумента 2 и 
результат присвойте переменной cnt. Вызовите внутреннюю функцию через 
переменную cnt со значением k, введенным с клавиатуры:
k = int(input())
Выведите результат на экран.
'''
#
# def counter_add(k):
#     def plusik(n):
#         global k
#         c = n + k
#         print(c)
#     return plusik
#
# k = int(input('k: '))
# n = int(input('n: '))
# cnt = counter_add(k)
# cnt(n)


# def simple_logger(func):
#     def decorated(*args, **kwargs):
#         print(f"You're about to call {func}")
#         result = func(*args, **kwargs)
#         print(f"You just called {func}")
#         return result
#
#     return decorated
#
# @simple_logger
# def hello_world():
#     print("Hello, World!")


# def counter_add(n):
#     m = n
#     def add_n(m):
#         result = n + m
#         return result
#
#     return add_n
#
#
# cnt = counter_add(2)
# k = int(input())


# Sample Input:
#
# 7
# Sample Output:
#
# 12


'''Напишите программу, которая на вход принимает
последовательность целых чисел, и возвращает True,
если все числа ненулевые, и False, если хотя бы одно число равно 0.
'''
# L = list(map(int, input().split()))
#
# print(all(L))

'''
Напишите программу, которая на вход принимает последовательность 
целых чисел и возвращает True, если все числа равны нулю, и False, 
если найдется хотя бы одно ненулевое число. 
Разрешается использование только логических операторов и 
функций all([ ]) и any([ ]).
'''

# L = list(map(int, input().split()))
#
# print(not any(L))


# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 1234567891122
# b = 1234567891122
#
# print(a == b)
# print(a is b)
#

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before is list_id_after)

# text = 'The Zen of Python'
# t = set('The Zen of Python')
# t = len(t)
# print(t)

#
# a = 1, 2, 3, 4, 5, 6, 7, 8
# b = 2, 4, 6, 8, 10, 12
# b = set(b)
# a = set(a)
#
# c = a.symmetric_difference(b)
# print(c)

# some_var = (2,)
#
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# Программа должна выводить «Обе переменные ложные»,
# если они являются таковыми. Дополните условный оператор последним блоком.


# a = int(input())
#
# if type(a) == int and 999 >= a >= 100 and a % 2 == 0 and a % 3 == 0:
#     print("Число удовлетворяет условиям")
#
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print("Число удовлетворяет условиям")

# a, b, c = map(int, input().split())
#
# if c**2 == (a**2 + b**2):
#     print('ДА')
# else:
#     print('НЕТ')
#

# num = input()
#
# if num[-1] == '7':
#     print('ДА')
# else:
#     print('НЕТ')
# print(['НЕТ', 'ДА'][input()[-1] == '7']) # альтернативный подход


# word = input()
#
# if 't' and 'h' and 'o' in word:
#     print('ДА')
# else:
#     print('НЕТ')

# Уфа Астрахань Москва Самара Казань
#
# cities = list(input().split())
#
# if 'Москва' in cities:
#     cities.remove('Москва')
#
# print(*cities)


# счастливое число
# num = list(map(int, input()))
#
# if num[0] + num[1] + num[2] == num[-1] + num[-2] + num[-3]:
#     print('ДА')
# else:
#     print('НЕТ')


#
# def add(a, b):
#     return a + b
#
# def counter(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'Функция {func.__name__} вызывалась {count} раз')
#         return func(*args, **kwargs)
#
#     return inner
#
#
# q = counter(add)
#
# def mult(a, b, c):
#     return a*b*c
#
#
# w = counter(mult)
#
# w(23,56,78)
# print(w)


# numbers = input()
# num = [int(i) for i in numbers.split()]
# m = num[0]
# n = num[1]
#
# if m % n == 0:
#     s = m // n
#     print(f'{s}')
# else:
#     print(f'{m} на {n} нацело не делится')


# weidh, height = map(int, input().split())
#
# def perimetr(weidh, height):
#     print(f'Периметр прямоугольника равен {2*(weidh + height)}')
#
#
# perimetr(weidh, height)
#


# def mail(M):
#     if '@' and '.' in M:
#         print('ДА')
#
# mail(input())
#

# a, b = map(float, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)
#


#
#
# num = map(int, input().split())
#
# def num_list(*num):
#     min_ = min(num)
#     max_ = max(num)
#     sum_ = sum(num)
#     print(f'Min = {min_}, max = {max_}, sum = {sum_}')
#
#
# num_list()

# 23, 45, 67, -34, 0

# N = input()
# w = [N]

#
# w = [23, 45, -34]
# min(w)
# print(min(w))

# # def mail_to():
# #     name = input()
# #     print(f'Уважаемый, {name}! Вы верно выполнили это задание!')
# #
# #
# # mail_to()
#
#
# # def weight(w):
# #     print(f'Предмет имеет вес: {w} кг.')
# #
# #
# # weight(input())
# #
# # def proba_1():
# #    def proba_2():
# #        random_matrix = [
# #            [9, 2, 1],
# #            [2, 5, 3],
# #            [4, 8, 5]
# #        ]
# #        min_value_rows = []
# #        min_index_rows = []
# #        max_value_rows = []
# #        max_index_rows = []
# #
# #        for row in random_matrix:
# #            min_index = 0  # индекс кандидата
# #            min_value = row[min_index]  # значение самого кандидата. можно написать row[], а можно row[min_index]
# #            max_index = 0  # тоже для максимума
# #            max_value = row[max_index]
# #            for index_col in range(len(row)):
# #                if row[index_col] < min_value:
# #                    min_value = row[index_col]  # значение кандидата - это сам элемент
# #                    min_index = index_col  # индекс кандидата - это индекс элемента
# #                if row[index_col] > max_value:
# #                    max_value = row[index_col]  # значение кандидата - это сам элемент
# #                    max_index = index_col
# #            min_value_rows.append(min_value)
# #            min_index_rows.append(min_index)
# #            max_value_rows.append(max_value)
# #            max_index_rows.append(max_index)
# #        return "Minimal elements:", min_value_rows
# #        # print("Their indices:", min_index_rows)
# #        # print("Maximal elements:", max_value_rows)
# #        # print("Their indices:", max_index_rows)
# #
# #
# # f = proba_1()
# # print(f)
#
# #
# # def char_frequency(text):
# #     text = text.lower()
# #     text = text.replace(" ", "")
# #     text = text.replace("\n", "")
# #
# #     count = {}
# #     for char in text:
# #         if char in count:
# #             count[char] += 1
# #         else:
# #             count[char] = 1
# #
# #     for char, cnt in count.items():
# #         print(f"Символ {char} встречается {cnt} раз")
# #
# #
# # text = """
# # У лукоморья дуб зелёный;
# # Златая цепь на дубе том:
# # И днём и ночью кот учёный
# # Всё ходит по цепи кругом;
# # Идёт направо -- песнь заводит,
# # Налево -- сказку говорит.
# # Там чудеса: там леший бродит,
# # Русалка на ветвях сидит;
# # Там на неведомых дорожках
# # Следы невиданных зверей;
# # Избушка там на курьих ножках
# # Стоит без окон, без дверей;
# # Там лес и дол видений полны;
# # Там о заре прихлынут волны
# # На брег песчаный и пустой,
# # И тридцать витязей прекрасных
# # Чредой из вод выходят ясных,
# # И с ними дядька их морской;
# # Там королевич мимоходом
# # Пленяет грозного царя;
# # Там в облаках перед народом
# # Через леса, через моря
# # Колдун несёт богатыря;
# # В темнице там царевна тужит,
# # А бурый волк ей верно служит;
# # Там ступа с Бабою Ягой
# # Идёт, бредёт сама собой,
# # Там царь Кащей над златом чахнет;
# # Там русский дух... там Русью пахнет!
# # И там я был, и мёд я пил;
# # У моря видел дуб зелёный;
# # Под ним сидел, и кот учёный
# # Свои мне сказки говорил.
# # """
# #
# #
# # char_frequency(text)
#
# # def get_rec_N(N):
# #     #print(N)
# #     if N > 0:
# #         get_rec_N(N-1)
# #     print(N)
# #
# # get_rec_N(4)
# #
# # def fact(x):
# #     if x == 1:
# #         return 1
# #     else:
# #         return x * fact(x-1)
# #
# # print(fact(3))
#
# #
# # def fractal_rectangle (A, B, C, D, deep=10):
# #     if deep < 1:    # глубина рекурсии
# #         return      # прекращает функцию,
# #         # если меньше 1 (то есть меньше только - ничего)
#
#
# # # Напишите функцию, которая будет возвращать количество делителей числа а.
# # def get_multipliers(a):
# #    count = 0
# #    for n in range(1, a + 1):
# #        if a % n == 0:
# #            count += 1
# #
# #    return count
# #phone_list = [
# #
# # def multi_(*nums):
# #     mult = 1
# #     for n in nums:
# #         mult *= n
# #
# #     return mult
# #
# #
# # print(multi_())  # 0
# # print(multi_(2))  # 1
# # print(multi_(2, 2))  # 3
# # print(multi_(56, 2, 3))  # 6
# #
# #
# #
# # get_multipliers(5)  # 2
# # get_multipliers(4)  # 3
#
# # def check_palindrome(str_):
# #    str_ = str_.lower()
# #    str_ = str_.replace(" ", "")
# #
# #    if str_ == str_[::-1]:
# #        return True
# #    else:
# #        return False
# #
# # check_palindrome("test")  # False
# # check_palindrome("Кит на море не романтик")  # True
#
#
# # def my_function(a, n):
# #     if a // n:
# #         print("yes")
# #     else:
# #         print("no")
# #
# #
# # my_function(120, 60)
# #
# # def check_num(a, n):
# #    if a % n == 0:
# #        print(f"Число {n} является делителем числа {a}")
# #    else:
# #        print(f"Число {n} не является делителем числа {a}")
# #
# # check_num(4, 2)  # Число 2 является делителем числа 4
# # check_num(5, 2)  # Число 2 не является делителем числа 5
# #
# # number = input(': ') # 1111115553487640865
# # digitToFind = input('Find: ')
#
# # def number_find():
# #     if str(digitToFind) in str(number):
# #         print(f"{digitToFind} is in number {number}")
# #     else:
# #         print('нет')
# #
# #
# # number_find()
#
#
# # num = int(input('Enter your number: '))
# # div = None
# # nums = [5, 7, 9]
# #
# # while num:
# #     div = num % 10
# #     if div in nums:
# #         print('yes')
# #         break
# #     if div not in nums:
# #         print('no')
# #         break
#
# #
# # if i % 2 == 0:
# #     if i % 3 == 0:
# #         if i % 5 == 0:
# #         continue
#
# # for i in range(1, 100):
# #     if i % 2 == 0:
# #         print(f'{i}%2')
# #     if i % 3 == 0:
# #         print(f'{i}%3')
# #         continue
# #     if i % 5 == 0:
# #         print(f'{i}%5')
# #
#
# #
# # text = """
# # У лукоморья дуб зелёный;
# # Златая цепь на дубе том:
# # И днём и ночью кот учёный
# # Всё ходит по цепи кругом;
# # Идёт направо -- песнь заводит,
# # Налево -- сказку говорит.
# # Там чудеса: там леший бродит,
# # Русалка на ветвях сидит;
# # Там на неведомых дорожках
# # Следы невиданных зверей;
# # Избушка там на курьих ножках
# # Стоит без окон, без дверей;
# # Там лес и дол видений полны;
# # Там о заре прихлынут волны
# # На брег песчаный и пустой,
# # И тридцать витязей прекрасных
# # Чредой из вод выходят ясных,
# # И с ними дядька их морской;
# # Там королевич мимоходом
# # Пленяет грозного царя;
# # Там в облаках перед народом
# # Через леса, через моря
# # Колдун несёт богатыря;
# # В темнице там царевна тужит,
# # А бурый волк ей верно служит;
# # Там ступа с Бабою Ягой
# # Идёт, бредёт сама собой,
# # Там царь Кащей над златом чахнет;
# # Там русский дух... там Русью пахнет!
# # И там я был, и мёд я пил;
# # У моря видел дуб зелёный;
# # Под ним сидел, и кот учёный
# # Свои мне сказки говорил.
# # """
# #
# # text = text.lower()
# # text = text.split()
# # count = {}  # для подсчета символов и их количества
# # for word in text:
# #    if word in count:  # если символ уже встречался, то увеличиваем его количество на 1
# #        count[word] += 1
# #    else:
# #        count[word] = 1
# # # Мы используем такой способ работы со словарем, поскольку для того чтобы увеличить
# # # счётчик, нам нужно как бы прочитать значение из словаря, увеличить его на единицу и потом записать обратно в словарь.
# #
# # for char, cnt in count.items():
# #    print(f"в тексте {char}  {cnt} слов ")
# N
#
# # Вводится стоимость одной книги x рублей
# # (вещественное число). Необходимо вывести на экран в
# # строчку через пробел стоимости 2, 3, ... 10 таких книг
# # с точностью до десятых.
# # Программу реализовать при помощи цикла while.
# # Sample Input: 34.6
# # Sample Output: 69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0
#
# # 1) Float вместо привычного int
# # 2) новая переменная, чтобы зафиксировать первое значение
# # 3) сравниваем обычное значение и помноженное в 10 раз.
# # Обратите внимание, что выводится не 10, а 9 значений, значит
# # нужно отказаться от =
# # 4)важное отличие: переменная имеет значение не 1,
# # как обычно,а значение первой цены, мы ведь увеличиваем стоимость
# # 5) завершаем выводом результата с округлением:
# # функция(переменная, степень округления), окончание строки с
# # пробелом в кавычках.
#
# # cost = float(input())
# # n = 1
# # s = cost
# #
# # while n < 10:
# #     s += cost
# # print(round(s, 1), end = ' ')
# #
# #
#
# # matrix = [
# #     [1, 2]
# #    ,[3, 4]
# #    ,[5, 6]
# # ]
# #
# # for row in matrix:
# #    for element in row:
# #        print(element, end = " ")
# #    print() # этот принт относится к циклу for row in matrix:
#
# # ROWS = 3
# # COLS = 4
# #
# # matrix = [
# #     [1, 2, 8, 'reee']
# #    ,[3, 4, 9, 34]
# #    ,[5, 6, 10, 11]
# # ]
# #
# # for i in range(ROWS):
# #    for j in range(COLS):
# #        print(matrix[i][j], end = " ")
# #    print()
# #
#
#
# # *
# # **
# # ***
# #
# # n = 4
# # *
# # **
# # ***
# # ****
# # for n in range (1, 4):
# #     print('*' * n)
#
# # word = input().lower()
# #
# # print(word)
# #
# # if word == word[::-1]:
# #     print('ДА')
# # else:
# #     print('НЕТ')
#
#
# # n = input().split()
# # n1 = n[0]
# # n2 = n[-1]
# #
# # if n1 < n2:
# #     print(n2)
# # else:
# #     print(n1)
# #
# #
#
# # Сергей Михайлович Балакирев
# # fio = list(input().split())
# #
# # name = list(fio[0])
# # name = name[0] + '.'
# # sname = list(fio[1])
# # sname = sname[0] + '.'
# #
# # _fio = fio[2] + ' ' + name + sname
# #
# # print(_fio)
#
#
# #
# # cities = ['Москва', 'Казань', 'Ярославль']
# # cities.insert(1, 'Ульяновск')
# #
# # print(*cities)
#
#
# # s = input('введите целые числа через пробел: ')
# # s = [s]
# # [0] != s[-1]
# #
# # lst = True
# #
# # print(s)
# # print(lst)
#
# # S = 0  # заводим переменную счетчик, в которой мы будем считать сумму
# # N = 11
# #
# # # заводим цикл for в котором мы будем проходить по всем числам от одного до N
# # for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
# #     print("Значение суммы на предыдущем шаге: ", S)
# #     print("Текущее число: ", i)
# #     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
# #     print("Значение суммы после сложения: ", S)
# #     print("---")
# # print("Конец цикла")
# # print()
# # print("Ответ: сумма равна = ", S)
#
# # my_list = [5, 9, 19]
# # my_list_2 = [45, 67, 23]
# # my_list.append(my_list_2)
# #
# #
# # print(my_list)
#
# #
# # a = [5.4, 6.7, 10.4]
# # b = input('введите целые числа через пробел: ')
# #
# # b = [b]
# # lst = a + [b]
# #
# # print(a)
# # print(lst)
#
# # for element in my_list:
# # подставляем его в шаблон для цикла и записываем имя переменной,
# # которое будет использовано для каждого элемента этого объекта.
# # В данном случае это element
# # print('Element', (element)) # записываем необходимые действия в тело цикла

# '''Задание 3.4.3
#
# В задании ниже вам нужно написать код, который выводит на экран обозначение ветра в зависимости от его характера:
#
# Если скорость ветра speed 1-4 м/с, то его обозначение — «weak».
# Скорость 5-10 м/c — «moderate».
# Скорость 11-18 м/c — «strong»
# Наконец, при скорости от 19 м/c обозначение — «hurricane».
# Если вводится значение скорости от 0 и ниже, необходимо вывести сообщение «Error».
#
# Скорость ветра будет храниться в переменной speed. Предположим, её начальное значение — 15.
#
# '''
# speed = int(input())
#
# if speed in range(1, 4):
#     print('weak')
# elif speed in range(5, 10):
#     print('moderate')
# elif speed in range(11, 18):
#     print('strong')
# elif speed > 19:
#     print('hurricane')
# elif speed < 0:
#     print('Error')

# w = str(input())
# if w == w[::-1]:
#     print("Number - палиндром")
# else:
#     print("Number - не палиндром")

# temperature = int(input('t = '))
# isRain = 'Y'
# HardRain = 'N'
#
# if 20 >= temperature <= 30:
#     if isRain == 'Y':
#         print("Футболку, шорты и дождевик")
# elif temperature > 0:
#     if isRain == 'Y':
#         if HardRain == 'Y':
#             print("Пальто, резиновые сапоги и зонт")
#         else:
#             print("Пальто и дождевик")
#     else:
#         print("Пальто")
# else:
#     print("Пуховик")

#
# import random
#
# symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # список символов
# dlina = int(input("Введите длину пароля: ")) # просим длину пароля
# otvet = '' # создаем место для ответа
#
# for i in range(dlina): # выполняем цикл исходя из длины пароля
#     otvet += random.choice(symbols) # добавляем рандомный символ в ответ
#
# print(otvet)
#

# # импортируем tkinter
# import tkinter
# # создаем окно
# window = tkinter.Tk()
# # создаем холст и размещаем его в окне
# canvas = tkinter.Canvas(window)
# canvas.pack()
#
# # координаты левого верхнего
# # угла прямоугольника, в который должен быть вписан круг
# x0 = 50
# y0 = 50
#
# # координаты правого нижнего
# # угла прямоугольника
# x1 = 150
# y1 = 150
#
# # canvas.create_oval(x0, y0, x1, y1)
# canvas.create_oval(0, 0, 200, 200, outline="red")
# canvas.create_oval(50, 50, 150, 150, outline="grey")
#
# window.mainloop()
"""рекурcия матрёшки"""

# void matryoshka(int n);
#
# int main(int argc, char* argv[])
# {
#     matryoshka(7);
#
#     return 0;
# }
#
# void matryoshka(int n)
# {
#     if(n == 1)
#         printf(" Last matryoshka!!! %d\n", n);
#     else
#     {
#     printf(" Top side of matryoshka %d\n", n);
#     matryoshka(n-1);
#     printf(" Bottom side of matryoshka %d\n", n);

# a = float, input()
# b = float, input()
# d = (a if a > b else b)
# print(int(d))


# def even_n():
#     while int(input()) != 1:
#         if a % 2 == 0:
#             print(a)
#         else:
#             continue

# lst = []
# x = list(map(int, input().split()))
#
# def even_n(x):
#     b = [lst.append(i) for i in x if i % 2 == 1]
#     return b
#
#
# print(*lst)


# '''сумма чисел от 1 до n  рекурсия'''
# def sum(n):
#     if n == 1:
#         return 1
#     return 1 + sum(n - 1)
#
#
# print(sum(23))

# def sum_int(N):
#     if N == 1:
#         return 1
#     return N[0] + sum_int(N[0 + 1])
#
#
# print(sum_int(23))
#
# l = [1, 'a', 'b', 0, 15]
#
#
# def filter_list(l):
#     a = []
#
#     for x in l:
#         if isinstance(x, int):
#             a.append(x)
#     print(*a)
#
#
# filter_list(l)
#
# '''чужое'''
# def filter_list(l):
#
#     return [i for i in l if not isinstance(i, str)]

#
# inp = float(input())
# lst = [inp]
#
# for i in range(10):
#     lst.append(round(lst[-1] + inp, 1))
# del lst[0]
# print(*lst)

# a = [x for x in range(-10, -1, 2)]
# a.reverse()
# print(*a[::-1])

# a = list(map(int, input().split())

# a = [8, 11, -2, 4, 0, 13, 19, 12, 7]
# lst = []
#
# for x in a:
#     if x % 2 != 0:
#         lst.append(x)
#
# print(sum(lst))

# def func_out():
#     out = 5
#
#     def func_in():
#         nonlocal out
#         out = 55
#
#     print('func_in.x1 = ', out)
#
#     func_in()
#     print('func_out.x1 = ', out)
#
#     func_out()


# lst = Москва Уфа Караганда Тверь Минск Казань
# '''список городов длины их слов'''
# lst = list(map(str, input().split()))
# a = []
#
# for x in lst:
#     a.append(len(x))
#
# print(*a)


#
# n = int(input())
#
# a = 'ДА'
# b = 'НЕТ'
# c = [a if n % n == 0 and n % 1 == 0 else b]
#
# print(*c)
#
# def X(a):
#     c = a ** 2
#     return c
#
#
# if __name__ == '__main__':
#     print(X(4))
#     print(X(28))
#     print(X(34))
#

# def multi_plus(x, y):
#     c = x * y
#     d = x + y
#     return c, d
#
#
# # print(c)
# if __name__ == '__main__':
#     print(multi_plus(3783464, 5754))

# x = 12
#
# while x > 0:
#     y = x
#     while y > 0:
#         print(y)
#         y -= 2
#     x -= 2
# print('stop')
# '''Предположим у нас есть список с данными о росте и
# весе людей. Задача — отсортировать их по индексу массы
# тела. Он вычисляется по формуле: свой рост
# в сантиметрах возвести в квадрат, потом массу
# тела в килограммах разделить на полученную цифру.'''
# # (вес, рост)
# data = [
#     (82, 1.91),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84)
# ]
#
# sorted(data, key=lambda x: x[0] / (x[1] * 100) ** 2)

# a = ["asd", "bbd", "ddfa", "mcsa"]
#
# # print(len(a[0]), len(a[1]), len(a[2]), len(a[3]))
# print(list(map(len, a)))
#
# a = ["это", "маленький", "текст", "обидно"]
# print(list(map(str.upper, a)))
# print([x.upper() for x in a])
