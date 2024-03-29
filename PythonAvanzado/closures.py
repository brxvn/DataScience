def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Only strings"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hello"))


if __name__ == "__main__":
    run()