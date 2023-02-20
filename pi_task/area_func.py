PI = 3.14


def area_circle(r):
    return PI * (r ** 2)


def area_rect(a, b):
    return a * b

# if __name__ == '__main__':
#     # проверяем работоспособность функции, дальнейшая часть не будет импортирована
#     assert area_circle(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
#     assert area_rect(5, 4) == 20
