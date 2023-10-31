def count_lines_words_chars(filename):
    lines = 0
    words = 0
    characters = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)

        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {characters}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

if __name__ == "__main__":
    file_name = input("Enter the filename: ")
    count_lines_words_chars(file_name)
