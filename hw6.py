#2.Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

filename = "HW5_2.txt"

with open(filename, 'r', encoding='utf-8') as file:
    lines = [line for line in file.readlines() if line != '\n']

    print(f"No empty strings:", len(lines))

    for line, words_cnt in {l: len(l.split()) for l in lines}.items():
        print(f'String {line[:40]}... contains {words_cnt} words')