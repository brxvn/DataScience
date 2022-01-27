import random
import os


def play(random_word):
    os.system("clear")
    dashboard = ["_"] * len(random_word)
    print(dashboard)
    while True:
        letter = input("Ingrese una letra: ").upper()
        if len(letter) > 1:
            print("Solo puede ingresar una letra")
        elif letter in random_word:
            for i in range(len(random_word)):
                if random_word[i] == letter:
                    dashboard[i] = letter
            os.system("clear")
            print(dashboard)
        else:
            os.system("clear")
            print("No esta en la palabra")
            print(dashboard)
        if "_" not in dashboard:
            print("Felicitaciones, ganaste")
            break



def show_random_word(word, random_word):
    return word[random_word]


def normalize(s): # It removes the accents of a string
    replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as file:
        for line in file:
            words.append(line.strip().upper())
    return words


def run():
    words = read()
    random_word = show_random_word(words, random.randrange(1, len(words)))
    play(normalize(random_word))


if __name__ == '__main__':
    run()