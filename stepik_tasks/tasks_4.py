'''
8 11 -1
'''


#
# a, b, c = map(int, input().split())
# # Определяю наименьшее число с помощь условного оператора
# if a < b:  # Если a меньше b
#     if a < c:  # Сравниваю a и c
#         print(a)  # Если а меньше вывожу результат
# if b < c:  # Если а больше b тогда остается сравнить b и c
#     print(b)  # Если b меньше то вывожу b
# else:
#     print(c)  # Иначе вывожу с

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def insert_left(self, next_value):
    if self.left_child is None:
        self.left_child = BinaryTree(next_value)
    else:
        new_child = BinaryTree(next_value)
        new_child.left_child = self.left_child
        self.left_child = new_child
    return self


def insert_right(self, next_value):
    if self.right_child is None:
        self.right_child = BinaryTree(next_value)
    else:
        new_child = BinaryTree(next_value)
        new_child.right_child = self.right_child
        self.right_child = new_child
    return self
