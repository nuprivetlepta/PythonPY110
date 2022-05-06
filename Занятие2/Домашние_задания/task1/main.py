from itertools import count
if __name__ == "__main__":
    a = int(input('Введите начальное число прогрессии: '))
    b = int(input('Введите знаменатель: '))
    c = int(input('Введите количество шагов: '))
    geoma = (a * (b**i) for i in count(1, 1))
    for i in range(c):
        print(next(geoma), end=',')



# def geoma():
#     a = 1
#     counter = 1
#     while True:
#         yield counter
#         counter *= a
#         a += 1
#
#
# if __name__ == "__main__":
#     abs_ = geoma()
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))
#     print(next(abs_))