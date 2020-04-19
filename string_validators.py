if __name__ == '__main__':
    s = input()

    # Alphanumeric
    print(any(map(lambda x: x.isalnum(), s)))

    # Alphabetical
    print(any(map(lambda x: x.isalpha(), s)))

    # Digits
    print(any(map(lambda x: x.isdigit(), s)))

    # Lowercase
    print(any(map(lambda x: x.islower(), s)))

    # Upper
    print(any(map(lambda x: x.isupper(), s)))
