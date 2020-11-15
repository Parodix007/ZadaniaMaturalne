# -----------------------------
#! Zadanie 6.2
# letters = []
# for code in range(65, 91):
#     letters.append(chr(code))

# szyfrogramy = []
# odszyfrowane = []

# with open('Dane_PR2/dane_6_2.txt', 'r') as file:
#     for item in file.readlines():
#         szyfrogramy.append(item.strip().split(" "))

# for item in szyfrogramy:
#     if len(item) == 2:
#         newWord = []
#         i = 0
#         code = 0
#         for letter in item[0]:
#             while i < int(item[1]):
#                 if code != 25:
#                     code += 1
#                 else:
#                     code = 0
#                 i+=1
#             newWord.append(letters[letters.index(letter) - code])
#         odszyfrowane.append(''.join(newWord))
    

# with open('zadanie6.1.txt', 'w+') as file:
#     for item in odszyfrowane:
#         file.write(f'{item}\n')

# -----------------------------
#! Zadanie 6.3
