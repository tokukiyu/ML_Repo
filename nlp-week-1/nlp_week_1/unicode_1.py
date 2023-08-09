path_1 = 'unicode_text.txt'
with open(path_1, encoding='latin2') as text_latin2:
    # print('\nPlain Text from path_1 using Latin-2 encoding with code points:')
    for line in text_latin2:
        line = line.strip()
        # print(line.encode('unicode_escape'))


with open(path_1, encoding='utf8') as text_utf8:
    print("\nPlain Text from path_1 using UTF-8 encoding:")
    for line in text_utf8:
        line = line.strip()
        print(line)
