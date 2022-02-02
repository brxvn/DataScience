def make_division_by(n):
    def division(x):
        assert type(x) == int, "Only integers"
        return x / n
    return division


def run():
    divide_by_3 = make_division_by(3)
    print(divide_by_3(18))
    divide_by_5 = make_division_by(5)
    print(divide_by_5(100))
    divide_by_18 = make_division_by(18)
    print(divide_by_18(54))


if __name__ == "__main__":
    run()