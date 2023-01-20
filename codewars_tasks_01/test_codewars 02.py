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

def sum_mix(arr):
    for x in arr:
        res = []
        i = 0
        x = int(x)
        y = x[i] + x[i + 1]
        i += 1
    return res.append(y)


print(sum_mix(arr))


