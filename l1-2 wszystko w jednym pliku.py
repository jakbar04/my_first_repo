#Biblioteki użyte w programie: random-funkcja losująca liczby, math-moduł matematyczny
import random
import math

class Vector:
    #Funkcja-konstruktor klasy Vector generująca nowy obiekt-wektor o domyślnym rozmiarze (3) i zerowych elementach 
    def __init__(self, rozmiar = 3):
        self.rozmiar = rozmiar
        self.elementy = [0] * rozmiar

    #Funkcja-setter klasy Vector ustanawiająca wartości losowe wektora (z przedziału min_los i max_los podanych jako argumenty funkcji)
    def elementy_losowe(self, min_los, max_los):
        for i in range(self.rozmiar):
            self.elementy[i] = random.randint(min_los, max_los)
    
    #Funkcja-setter klasy Vector ustanawiająca wartości wektora z listy podanej jako argument funkcji
    def elementy_z_listy(self, lista):
        if len(lista) != self.rozmiar:
            print("Lista ma inny rozmiar niż wektor")
        else:
            self.elementy = lista

    #Funkcja-operator klasy Vector pozwalająca za pomocą znaku + (plusa) dodać do elementów jednego wektora elementy drugiego
    def __add__(self, other):
        if self.rozmiar != other.rozmiar:
            raise ValueError("Wektory przy dodawaniu muszą mieć takie same rozmiary")
        result = Vector(self.rozmiar)
        result.elementy = [self.elementy[i] + other.elementy[i] for i in range(self.rozmiar)]
        return result
    
    #Funkcja-operator klasy Vector pozwalająca za pomocą znaku - (minusa) odjąć od elementów jednego wektora elementy drugiego
    def __sub__(self, other):
        if self.rozmiar != other.rozmiar:
            raise ValueError("Wektory przy odejmowaniu muszą mieć takie same rozmiary")
        result = Vector(self.rozmiar)
        result.elementy = [self.elementy[i] - other.elementy[i] for i in range(self.rozmiar)]
        return result
    
    #Funkcja-setter klasy Vector zwracająca pomnożony każdy element wektora przez wartość (skalar) podany jako argument funkcji
    def mnozenie_przez_skalar(self, skalar):
        result = Vector(self.rozmiar)
        result.elementy = [element * skalar for element in self.elementy]
        return result

    #Funkcja-getter klasy Vector zwracająca długość wektora (jako pierwiastek kwadratowy sumy kwadratów wszystkich jego elementów)
    def dlugosc(self):
        sum_of_squares = sum(element ** 2 for element in self.elementy)
        return math.sqrt(sum_of_squares)
    
    #Funkcja-getter klasy Vector zwracająca sumę wszystkich jego elementów
    def suma_elementow(self):
        return sum(self.elementy)

    #Funkcja-getter klasy Vector zwracająca iloczyn skalarny dwóch wektorów
    def iloczyn_skalarny(self, other):
        if self.rozmiar != other.rozmiar:
            print("Wektory przy iloczynie skalarnym muszą mieć takie same rozmiary")
        else:
            return sum(self.elementy[i] * other.elementy[i] for i in range(self.rozmiar))

    #Funkcja-getter klasy Vector zwracająca reprezentację tekstową wektora
    def __str__(self):
        return f"Elementy wektora {self.elementy}"
    
    #Funkcja-getter klasy Vector zwracająca operatorem [] dla wektora wartość jego indeksu (podanego jako argument funkcji)
    def __getitem__(self, indeks):
        return self.elementy[indeks]
    
    #Funkcja-getter klasy Vector zwracająca True lub False jako wynik sprawdzania przynależnosci do wektora elementu (podanego jako argument funkcji)
    def __contains__(self, element):
        return element in self.elementy


#Uruchamiane przy starcie
    
#Utworzenie nowego obiektu-wektora1 klasy Vector o 5 (zerowych) elementach
wektor1 = Vector(5)
print("Wektor1 po utworzeniu", wektor1.elementy)

#Wygenerowanie wartość losowych (z przedziału 1-10) dla wektora1
wektor1.elementy_losowe(1, 10)
print("Wektor1 po losowaniu elementów", wektor1.elementy)

#Próba wczytania listy 3-elementowej jako elementy wektora1
lista1 = [1, 2, 3]
wektor1.elementy_z_listy(lista1)
print("Wektor1 po wczytaniu listy", wektor1.elementy)

#Wczytanie listy 5-elementowej jako elementy wektora1. Od tej pory wektor1 funkcjonuje jako [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
wektor1.elementy_z_listy(lista2)
print("Wektor1 po wczytaniu listy", wektor1.elementy)

#Próba dodania wektora 3-elementowego (wektora_dodawanego) i wektora 5-elementowego (wektora1)
wektor_dodawany = Vector(3)
wektor_dodawany.elementy_losowe(2, 20)
print("Wektor-dodawany", wektor_dodawany.elementy)
try:
    suma_wektorow = wektor1 + wektor_dodawany
    print("Suma wektorów", suma_wektorow.elementy)
except ValueError as e:
    print("Error:", e)

#Odejmowanie wektora 5-elementowego (wektora_odejmowanego) od wektora 5-elementowego (wektora1)
wektor_odejmowany = Vector(5)
wektor_odejmowany.elementy_losowe(2, 20)
print("Wektor_odejmowany", wektor_odejmowany.elementy)
try:
    roznica_wektorow = wektor1 - wektor_odejmowany
    print("Różnica wektorów", roznica_wektorow.elementy)
except ValueError as e:
    print("Error:", e)

#Mnożenie wszystkich elementów wektora 5-elementowego (wektora1) przez wartość 2 (skalar)
wektor_przez_skalar = wektor1.mnozenie_przez_skalar(2)
print("Przemnożony wektor1 przez skalar (wartość 2)", wektor_przez_skalar.elementy)

#Wyznaczenie długości wektora1 jako pierwiastek kwadratowy sumy kwadratów wszystkich jego elementów
dlugosc_wektora = wektor1.dlugosc()
print("Długość wektora1", dlugosc_wektora)

#Wyznaczenie sumy wektora1 poprzez zsumowanie wszystkich jego elementów
suma_wektora = wektor1.suma_elementow()
print("Suma elementów wektora1", suma_wektora)

#Utworzenie nowego obiektu-wektora2 klasy Vector o 2 (losowanych) elementach
#Próba wyznaczenia iloczynu skalarnego wektora 5-elementowego (wektora1) oraz wektora 2-elementowego (wektora2)
wektor2 = Vector(2)
wektor2.elementy_losowe(1, 10)
print("Wektor2 po losowaniu elementów", wektor2.elementy)
iloczyn_skalarny = wektor1.iloczyn_skalarny(wektor2)
print("Iloczyn skalarny wektora1 oraz wektora 2", iloczyn_skalarny)

#Utworzenie nowego obiektu-wektora3 klasy Vector o 5 (losowanych) elementach
#Wyznaczenie iloczynu skalarnego wektora 5-elementowego (wektora1) oraz wektora 5-elementowego (wektora3)
wektor3 = Vector(5)
wektor3.elementy_losowe(1, 10)
print("Wektor3 po losowaniu elementów", wektor3.elementy)
iloczyn_skalarny = wektor1.iloczyn_skalarny(wektor3)
print("Iloczyn skalarny wektora1 oraz wektora 3 to", iloczyn_skalarny)

#Przedstawienie wektora1 w postaci tekstowej
print("Reprezentacja tekstowa wektora1.", wektor1)

#Wyznaczenie wartości elementu wektora1 o indeksie 2 operatorem []
print("Element wektora1 o indeksie 2 to", wektor1[2])

#Sprawdzenie przynależnosci do wektora1 elementów o wartościach 1 oraz 7
print("Czy 1 to element wektora1?", 1 in wektor1)
print("Czy 7 to element wektora1?", 7 in wektor1) 