import json


def task(input_filename: str, output_filename: str) -> None:

    with open(input_filename, 'r') as i:
        json_data = json.load(i)
    with open(output_filename, 'w') as o:
        json.dump(json_data, o, indent=4)






if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
