def run():
    dict = {x: x**3 for x in range(1, 101) if x % 3 != 0}
    print(dict)


if __name__ == '__main__':
    run()