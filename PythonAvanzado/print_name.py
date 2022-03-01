import time


def run():
    nombre = "Te amo Kenia Valeria <3"
    for letter in nombre:
        print(letter, flush=True, end="")
        time.sleep(0.5 )
    print("\n")


if __name__ == "__main__":
    run()
