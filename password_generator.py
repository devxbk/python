import random


def password_genrator():
    try:
        length = int(input("Enter password length (8-15): "))
        if length < 8 or length > 15:
            print("Length must be between 8 and 15.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    all_chars = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "=",
        "+",
        "[",
        "]",
        "{",
        "}",
        "|",
        ";",
        ":",
        "'",
        '"',
        ",",
        ".",
        "<",
        ">",
        "/",
        "?",
        "\\",
        "`",
        "~",
    ]

    choice = input(" Inclusion of special characters (y/n)? : ").lower()

    password = []

    for i in range(length):

        if choice == "n":
            chars = len(all_chars) - 32
        else:
            chars = len(all_chars)

        rand_num = random.randint(0, (chars - 1))
        rand_char = all_chars[rand_num]
        password.append(rand_char)

    print(f"Your password is: {''.join(map(str, password))}")


password_genrator()
