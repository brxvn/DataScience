def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Bryan", "Kenia", "Valeria", "Pedro"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(f"{name}\n")


def run():
    read()
    write()


if __name__ == '__main__':
    run()