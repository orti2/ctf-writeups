indices = [17, 4, 1, 4, 2, 2, 0, 15, 20, 17, 15, 11, 4]
characters = []

for num in indices:
    char_code = num + 97
    character = chr(char_code)
    characters.append(character)

result = ''.join(characters)
print(result)
