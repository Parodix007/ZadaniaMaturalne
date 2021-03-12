class Matura:
    def __init__(self,nazwa_pliku):
        self.__plik = nazwa_pliku
    
    def czytaj_plik_panstwa(self):
        tab = []
        with open(self.__plik) as file:
            for i in file.readlines():
                tab.append(i.split(" ")[0])
        return tab
    
    def czytaj_plik_powierzchnia(self):
        tab = []
        with open(self.__plik) as file:
            for i in file.readlines():
                powierzchnia = 0
                lokale = 0
                for j in range(3, len(i.split(" ")), 2):
                    if int(i.split(" ")[j]) != 0:
                        powierzchnia += (int(i.split(" ")[j]) * int(i.split(" ")[j-1]))
                        lokale+=1
                    elif int(i.split(" ")[j]) == 0:
                        break
                tab.append([i.split(" ")[1], powierzchnia, lokale])
        return tab
        
    def czytaj_plik_rozne(self):
        tab = []
        with open(self.__plik) as file:
            for i in file.readlines():
                tab1 = [i.split(" ")[1], []]
                for j in range(3, len(i.split(" ")), 2):
                    if int(i.split(" ")[j]) != 0:
                        tab1[1].append((i.split(" ")[j], i.split(" ")[j-1]))
                    elif int(i.split(" ")[j]) == 0:
                        break
                tab.append(tab1)

        return tab


matura = Matura("Dane_2103/galerie.txt")

#4.1
tab_miasta_panstwa = matura.czytaj_plik_panstwa()

obj_panstwa = { }

for i in range(len(tab_miasta_panstwa)):
    if tab_miasta_panstwa[i] not in obj_panstwa:
        obj_panstwa[tab_miasta_panstwa[i]] = tab_miasta_panstwa.count(tab_miasta_panstwa[i])

with open("wynik4_1.txt", "w+") as file:
    for (key, value) in obj_panstwa.items():
        file.writelines(f'{key}: {value} \n')

#4.2
tab_miasta_powierzchnia = matura.czytaj_plik_powierzchnia()
print(f'miasta, powierzchnie, lokale: \n {tab_miasta_powierzchnia}')

najwieksze = {
    "miasto": tab_miasta_powierzchnia[0][0],
    "liczba": tab_miasta_powierzchnia[0][1]
}
for i in range(1,len(tab_miasta_powierzchnia)):
    if najwieksze["liczba"] < tab_miasta_powierzchnia[i][1]:
        najwieksze["liczba"] = tab_miasta_powierzchnia[i][1]
        najwieksze["miasto"] = tab_miasta_powierzchnia[i][0]

print(najwieksze)

najmniejsze = {
    "miasto": tab_miasta_powierzchnia[0][0],
    "liczba": tab_miasta_powierzchnia[0][1]
}
for i in range(1,len(tab_miasta_powierzchnia)):
    if tab_miasta_powierzchnia[i][1] < najmniejsze["liczba"]:
        najmniejsze["liczba"] = tab_miasta_powierzchnia[i][1]
        najmniejsze["miasto"] = tab_miasta_powierzchnia[i][0]

print(najmniejsze)

tab_rozne_lokale = matura.czytaj_plik_rozne()

miasto_rozne_lokale = {}

for i in tab_rozne_lokale:
    rodzaje = []
    for j in i[1]:
        pole = int(j[0]) * int(j[1])
        takie_same = 0
        for k in range(i[1].index(j), len(i[1])):
            if pole == (int(i[1][k][0]) * int(i[1][k][1])):
                takie_same+=1
        if pole not in rodzaje:
            rodzaje.append(pole)
    miasto_rozne_lokale[i[0]] = len(rodzaje)

print(miasto_rozne_lokale)
