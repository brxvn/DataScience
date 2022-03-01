SET_1 = {1,2,3,4,5}
SET_2 = {3,4,5,6,7}


def union(set_1, set_2):
    return set_1 | set_2


def intersection(set_1, set_2):
    return set_1 & set_2


def difference(set_1, set_2):
    return set_1 - set_2


def symmetric_difference(set_1, set_2):
    return set_1 ^ set_2


if __name__ == "__main__":
    print(union(SET_1, SET_2))
    print(intersection(SET_1, SET_2))
    print(difference(SET_1, SET_2))
    print(symmetric_difference(SET_1, SET_2))
