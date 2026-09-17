import random


def password_generator():
    try:
        length = int(input("Enter password length (8-15): "))
        if length < 8 or length > 15:
            print("Length must be between 8 and 15.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    lowercase = [
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
    ]

    uppercase = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    special_chars = [
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

    if choice == "n":
        chars = numbers + lowercase + uppercase
    elif choice == "y":
        chars = numbers + lowercase + uppercase + special_chars
    else:
        print("Invalid choice, Please enter 'y' or 'n' ")
        return

    password = []

    for i in range(length):
        rand_num = random.randint(0, (len(chars) - 1))
        rand_char = chars[rand_num]
        password.append(rand_char)

    print(f"Your password is: {''.join(map(str, password))}")


password_generator()
