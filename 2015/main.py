def otwieranie_pliku():
	with open('Dane_PR2/liczby.txt') as file:
		return file.readlines()


# Zadanie 4.1
liczby_z_wiecej_0 = []
for liczba in otwieranie_pliku():
	false_ = 0
	true_ = 0
	for item in liczba.strip():
		if bool(int(item)):
			true_+=1
		else:
			false_+=1
	liczby_z_wiecej_0.append(liczba) if false_ > true_ else False

print(f'liczba liczb z wieksza iloscia 0: {len(liczby_z_wiecej_0)}')



#Zadanie 4.2
podzielne_przez_2 = []
podzielne_przez_8 = []

for liczba in otwieranie_pliku():
	if int(liczba, 2) % 2 == 0 and int(liczba, 2) % 8 == 0:
		podzielne_przez_8.append(liczba)
		podzielne_przez_2.append(liczba)
	elif int(liczba, 2) % 8 == 0:
		podzielne_przez_8.append(liczba)
	elif int(liczba, 2) % 2 == 0:
		podzielne_przez_2.append(liczba)

print(f'podzielne przez 2: {len(podzielne_przez_2)}')
print(f'podzielne przez 8: {len(podzielne_przez_8)}')


#Zadanie 4.3
wszystkie_liczby = []
wiersz = 1
for liczby in otwieranie_pliku():
	wszystkie_liczby.append((wiersz, int(liczby,2)))
	wiersz+=1

liczby = [x[1] for x in wszystkie_liczby]
liczby.sort()
print(f'najmniejsza: {liczby[0]}\nnajwieksza: {liczby[-1]}')

wiersz = []

for item in wszystkie_liczby:
	if liczby[0] == item[1]:
		wiersz.append(item)
	elif liczby[-1] == item[1]:
		wiersz.append(item)

print(wiersz)

print(f'najmniejsza w wierszu: {wiersz[0][0]}')
print(f'najwieksza w wierszu: {wiersz[1][0]}')