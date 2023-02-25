'''
Алгоритм линейного поиска определяется на таких
структурах данных как массивы, списки и надстройки
над ними — очередь и стек.
'''

# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))


'''
Напишите функцию count, которая 
возвращает количество вхождений элемента в массив
'''

# def count(array, element):
#     cnt = 0
#     for a in array:
#         if a == element:
#             cnt += 1
#     return cnt
#
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(count(array, element))


# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находим середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 98))

# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив из 100 элементов
# array = [i for i in range(1, 100)]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счетчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
cnt = 0
for i in range(len(array)):
    idx_min = i

    for j in range(i + 1, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
        cnt += 1
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(cnt)


# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0:
#         count += 1
#         if (array[idx - 1] <= x):
#             break
#         array[idx] = array[idx - 1]
#         idx -= 1
#     array[idx] = x
#
# print(count)
