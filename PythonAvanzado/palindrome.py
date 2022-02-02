def is_palindrome(word : str) -> bool:
    """
    Return True if the word is a palindrome, False otherwise.
    """
    word = word.lower().replace(" ", "")
    return word == word[::-1]


def run():
    print(is_palindrome(1000))


if __name__ == "__main__":
    run()