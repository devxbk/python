import random


def password_genrator():
    try:
        length = int(input("Enter the  length of the password (max 15): "))
    except ValueError:
        print("Enter a valid length!")

    choice = input(" Inclusion of special characters (y/n)? : ").lower()

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

    password = []

    num_of_char = length

    for i in range(num_of_char):
        loopcount = random.randint(0, 9)
        for j in range(loopcount):
            rand_num = random.randint(0, 9)
            password = password.append(rand_num)

            num_of_char -= 1

        rand_special = random.randint(0, 31)
        special_char = special_chars[rand_special]
        password = password.append(special_char)

        num_of_char -= 1


password_genrator()
