def run():
    squares = [x**2 for x in range(1, 101) if x % 3 != 0]
    print(squares)


if __name__ == '__main__':
    run()