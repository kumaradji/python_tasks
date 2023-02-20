'''
Задание 2.5.8
Создайте вычисляемое свойство для класса Square.

Сделайте метод по вычислению площади свойством.
Сделайте сторону квадрата свойством, которое можно
установить только через сеттер.
В сеттере добавьте проверку условия, что сторона
должна быть неотрицательной.
'''

class Square:
    _side = None

    def __init__(self, side):
        if side > 0:
            self._side = side

    @property  # создаем свойство side при помощи декоратора
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        if side >= 0:
            self._side = side

    @property
    def square(self):
        return self._side ** 2


if __name__ == "__main__":
    q = Square(22)
    print(q.square)
    q.side = 123  # передаём значение в сеттер
    print(q.side)
    print(q.square)  # выводим квадрат из сеттера