def task() -> list:
    temp_tuple = (0, 36.6, 100)

    return list(map(lambda x: x * 9/5 + 32, temp_tuple))  # TODO  вернуть список температур по Фаренгейту
    return [(lambda x: x * 9 / 5 + 32)(x) for x in temp_tuple]

    f = lambda i: i * 9 / 5 + 32
    for a in temp_tuple:
        a = f(a)
        print(a)

    f = lambda i: i * 9 / 5 + 32
    return [f(i) for i in temp_tuple]

if __name__ == "__main__":
    print(task())
