class Matura2020:
    def __init__(self, file_name):
        self.__file_name = file_name
    
    def get_even_numbers(self):
        array_of_numbers = []
        with open(self.__file_name) as file:
            for line in file.readlines():
                liczba = int(line.split(" ")[0])
                if liczba % 2 == 0:
                    array_of_numbers.append(liczba)
        return array_of_numbers

    def get_prime_numbers(self, number_):
        array_of_prime_numbers = []
        for number in range(1,number_):
            for num in range(1,number):
                for num1 in range(1,num):
                    if num % num1 != 0:
                        continue
                    else:
                        break
                array_of_prime_numbers.append(num)
        return array_of_prime_numbers


# Zadanie 4.1
Maturka = Matura2020("./Dane_PR2/pary.txt")

list_of_even_numbers = Maturka.get_even_numbers()
numbers_and_sums = []
for even_number in list_of_even_numbers:
    prime_numbers = Maturka.get_prime_numbers(even_number)
    print(f"{prime_numbers} \n")
#     z = []
#     for element in prime_numbers:
#         outcome = element - even_number
        
#         for i in range(prime_numbers.index(element), len(prime_numbers)):
#             if prime_numbers[i] == outcome * -1:
#                 z.append((element, prime_numbers[i]))
        
#     if len(z) >= 2:
#         top = z[0]
        
#         for i in range(1,len(z)):
#             if z[i][0] - z[i][1] > top[0] - top[1]:
#                 top = z[i]
#         numbers_and_sums.append([even_number, top])
#     elif len(z) == 1:
#         numbers_and_sums.append(z.insert(0, even_number))

# print(numbers_and_sums)