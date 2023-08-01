import re
path_1 = 'unicode_text.txt'
lines_in_text = open(path_1, encoding = 'latin2').readlines()
line_1 = lines_in_text[0]
line_1 = line_1.encode('unicode_escape')
print("\nLine 1 of the Text:", str(line_1))

unicode_in_line_1 = re.search(r"\\u015b\w*", str(line_1))
print("Words with Unicode 'u015b':", unicode_in_line_1.group())