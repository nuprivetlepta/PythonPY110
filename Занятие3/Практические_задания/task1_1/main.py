def task():
    filename = r"C:\Users\rodbely\PycharmProjects\Py110right\Занятие3\Практические_задания\task1_1\input.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            line = line.strip()
            print(line)


if __name__ == "__main__":
    task()
