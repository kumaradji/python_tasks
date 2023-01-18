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
s = 'ZpglnRxqenU'


def accum(s):
    str = [char for char in s]
    res = []
    a = 0
    for x in str:
        a += 1
        b = x * a
        b = b.title()
        res.append(b)
    res = '-'.join(res)

    return res


print(accum(s))

# def accum(s):
#     return '-'.join((a * i).title() for i, a in enumerate(s, 1))

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

