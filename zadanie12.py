print('zadanie12')
koszyk = [
    {'nazwa': 'mleko', 'ilosc':2, 'cena':4.0},
    {'nazwa': 'chleb', 'ilosc':5, 'cena':2.5},
    {'nazwa': 'maslo', 'ilosc':50, 'cena':10.0},
]
# liczenie sumy wartosc produktow w koszyku
def suma_koszyka(koszyk):
    sum = 0
    for poz in koszyk:
        c = poz['cena']
        il = poz['ilosc']
        poz_cen = c * il
        sum = sum + poz_cen
    return sum

sum = suma_koszyka(koszyk)

print('podstawowa wartosc koszyka to {}' .format(sum))

print ('ilosc niepowtarzalnych produktow w koszyku to {0}' .format(len(koszyk)))
if len(koszyk) >3:
    sum_r1 = sum*0.95
    print('wartosc koszyka po rabacie 5% to {0}'.format(sum_r1))
elif sum>500:
    sum_r2 = sum*0.9
    print('wartosc koszyka po rabacie 10% to {0}'.format(sum_r2))
else:
    print('Brak znizek, wartosc koncowa koszka to {0}'.format(sum))
