# Zadanie 4.1
with open('Dane_PR2/sygnaly.txt') as file:
    index = 1
    for item in file.readlines():
        if index == 40:
            index = 0
            #print(item[9], end='')
        index+=1


# Zadanie 4.2

with open('Dane_PR2/sygnaly.txt') as file:
    slowa = []
    rezultat = {
        "slowo":"",
        "ilosc":0
    }
    for item in file.readlines():
        item = item.strip()
        obiekt = {}
        for litera in item:
            if litera not in obiekt:
                obiekt[litera] = 1
        if rezultat["ilosc"] < len(obiekt):
            rezultat["slowo"] = item
            rezultat["ilosc"] = len(obiekt)


# Zadanie 4.3
with open('Dane_PR2/sygnaly.txt') as file:
    slowa = []
    for item in file.readlines():
        item = item.strip()
        err = False

        for litera in item:
            for litera2 in item:
                if not (-10 <= ord(litera2) - ord(litera) <= 10):
                    err = True
                    break              
            if err:
                break
        
        slowa.append(item) if not err else False
