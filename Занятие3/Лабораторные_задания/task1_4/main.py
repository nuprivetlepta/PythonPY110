INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open (INPUT_FILE, 'r') as f:# TODO перезаписать содержимое одного файла в другой
        for line in f:
            line = (line.upper()).strip()
            with open(OUTPUT_FILE, 'a') as f:
                f.write(line+'\n')

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
