import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename, 'r') as i:
        json_data = json.load(i)

    return max(json_data, key=lambda item: item['score'])
    ...  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
