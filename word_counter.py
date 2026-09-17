def word_counter():
    try:
        file_name = input("Enter the file name: ")
        file = open(file_name)

    except FileNotFoundError:
        print("File not found!")
        return

    text = file.read()

    words = text.split()
    lines = text.splitlines()

    print(
        f"Number of words: {len(words)} \nNumber of characters: {len(text)} \nNumber of lines: {len(lines)}"
    )

    file.close()


word_counter()
