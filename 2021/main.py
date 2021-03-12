#4.1
class Matura:
    def __init__(self,nazwa_pliku):
        self.__plik = nazwa_pliku
    
    def czytaj_plik(self):
        tab = []
        with open(self.__plik) as file:
            for i in file.readlines():
                tab.append(i.split(" ")[0])
        return tab


matura = Matura("Dane_2103/galerie_przyklad.txt")

tab_miasta_panstwa = matura.czytaj_plik()

obj_panstwa = { }


for i in range(len(tab_miasta_panstwa)):
    obj_panstwa[tab_miasta_panstwa[i]] = tab_miasta_panstwa.count(tab_miasta_panstwa[i])

print(obj_panstwa)

with open("wynik4_1.txt", "w+") as file:
    for (key, value) in obj_panstwa.items():
        file.writelines(f'{key}: {value} \n')