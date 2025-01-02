def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

    words = file_contents.split()
    count = len(words)
    print(count)

    letters = {}
    for char in file_contents.lower():
        if char.isalpha():
            letters.update({char: letters.get(char, 0) + 1})
    print(letters)

    print('--- Begin report of books/frankenstein.txt ---')
    print(count, 'words found in the document')

    for key,value in letters.items():
        letters
        print('The', key, 'character was found', value, 'times')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

main()