def main():
    file = 'books/frankenstein.txt'
    print(f"-- Begin report of {file} ---")
    with open(file) as f:
        file_contents = f.read()
        print(f"{count_words(file_contents)} words found in the document")

        for character, count in get_alphabet_character_count_list(file_contents).items():
            print(f"The '{character}' character was found {count} times")

    print("--- End report ---")

def count_words(string):
    words = string.split()
    return len(words)

def get_alphabet_character_count_list(string):
    character_count_list = {}
    characters = character_count_list.keys()
    for character in string:
        if character.isalpha() == False:
            continue
        character = character.lower()
        if character not in characters:
            character_count_list[character] = 1
            continue
        if character in characters:
            character_count_list[character] += 1
            continue

    sorted_character_count_list = dict(sorted(character_count_list.items(), key=lambda item: item[1], reverse=True))

    return sorted_character_count_list

main()
