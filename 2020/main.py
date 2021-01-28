def open_file():
    with open("./Dane_PR2/pary.txt") as file:
        return file.readlines()

# Zadanie 4.1
array_of_numbers = []
for line in open_file():
    liczba = int(line.split(" ")[0])
    if liczba % 2 == 0:
        print(liczba)

for number in array_of_numbers:
    