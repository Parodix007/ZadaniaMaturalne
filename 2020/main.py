class Matura2020:
    __file_name = './Dane_PR2/pary.txt'
    def __init__(self):
        pass
    
    def get_even_numbers(self):
        array_of_numbers = []
        with open(self.__file_name) as file:
            for line in file.readlines():
                liczba = int(line.split(" ")[0])
                if liczba % 2 == 0:
                    array_of_numbers.append(liczba)
        return array_of_numbers

    def check_if_prime(self, number):
        for num in range(2,number):
            if number % num:
                continue
            else:
                return False
        return True
    
    def get_strings(self):
        array_of_strings = []
        with open(self.__file_name) as file:
            for line in file.readlines():
                string = line.split(" ")[1]
                array_of_strings.append(string.strip("\n"))
        return array_of_strings

    def search_for_pattern(self, string_):
        patterns = []
        
        for item in set(string_):
            amount = 1
            
            for i in range(list(string_).index(item)+1, len(string_)):
                if string_[i] == item:
                    amount+=1
                else:
                    break
            
            if amount >= 2:
                patterns.append((item, amount))
        
        if len(patterns) > 0:
            top = patterns[0]
            
            for tup in patterns:
                if tup[1] > top[1]:
                    top = tup
                elif tup[1] == top[1]:
                    if list(string_).index(tup[0]) < list(string_).index(top[0]):
                        top = tup
            number = list(string_).index(top[0])
            return (string_[number: number + top[1]], top[1])
        else:
            return (string_[0], 1)





# Zadanie 4.1
Maturka4_1 = Matura2020()

list_of_even_numbers = Maturka4_1.get_even_numbers()
numbers_and_sums = []
for even_number in list_of_even_numbers:
    list_of_prime = []
    for num in range(2, even_number):
        if Maturka4_1.check_if_prime(num) == True:
            list_of_prime.append(num)
    list_of_sums = []
    for value in list_of_prime:
        for i in range(list_of_prime.index(value), len(list_of_prime)):
            if value + list_of_prime[i] == even_number:
                list_of_sums.append((value, list_of_prime[i]))

    if len(list_of_sums) >= 2:
        correct_tup = list_of_sums[0]
        for tup in list_of_sums:
            if (correct_tup[1] - correct_tup[0]) < (tup[1] - tup[0]):
                correct_tup = tup
        numbers_and_sums.append((even_number, correct_tup))
    elif len(list_of_sums) == 1:
        numbers_and_sums.append((even_number ,list_of_sums))

#print(numbers_and_sums)

#Zadanie 4.2
Maturka4_2 = Matura2020()
strings = Maturka4_2.get_strings()

for item in strings:
    print(Maturka4_2.search_for_pattern(item))
