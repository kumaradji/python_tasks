# from dataclasses import dataclass, field
# from pprint import pprint
#
#
# class Thing:
#     def __init__(self, name, weight, price, dims=None):
#         if dims is None:
#             dims = []
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.dims = dims
#
#     def __repr__(self):
#         return f"Thing: {self.__dict__}"
#
#
# @dataclass
# class ThingData:
#     name: str
#     price: float = 0
#     weight: int = 0
#     dims: list = field(default_factory=list)
#
#
# #  __init__(), __repr__(), __eq__()
#
# t = Thing("Учебник по Python", 100, 1000)
# t.dims.append(10)
# print(t.dims)
# pprint(ThingData.__dict__)

#
# d = list(map(int, input().split()))

# def get_biggest_city(*args: str):
#     return max(args, key=len)
#
#
# args = list(map(str, input().split()))
# a = get_biggest_city(*args)
# print(a)
#
# '''
# Питер Москва Самара Воронеж
# '''
# def get_data_fig(*args, **kwargs):
#     que = ('type', 'color', 'closed', 'width')
#     p = 0
#     for x in args:
#         p += x
#     lst_out = [p]
#     for x in que:
#         if x in kwargs.keys():
#             lst_out.append(kwargs[x])
#
#     return sum(args), *lst_out
#
#
# get_data_fig(*args, **kwargs)
# print(get_data_fig(3, 2, type=False, color=0, closed=False, width=0))
# print(get_data_fig(3, 2, color=2, closed=True))
# print(get_data_fig(1, 23, 4, 5, 5, 7, width=2, type=True, color=1, closed=False))

# ----------------------------
#
# (5, False, 0, False, 0)
# (5, 2, True)
# (45, True, 1, False, 2)


# a = input().split()
# b1 = str(a[0][::2]).upper()
# b2 = str(a[1][::2]).upper()
#
# print(b1[:len(b2)] == b2)

a = input().split()
b1 = str(a[0][::2]).upper()
b2 = str(a[1][::2]).upper()

b1 = b1[:len(b2)]
print(b1)
print(b2)
