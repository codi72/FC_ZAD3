opcja = ""
saldo = 1000.00
magazyn = {
    "mleko": {"cena": 2.50, "ilosc": 10},
    "chleb": {"cena": 3.00, "ilosc": 5},
    "masło": {"cena": 4.00, "ilosc": 2},
    "ser": {"cena": 5.00, "ilosc": 1},
    "olej": {"cena": 8.00, "ilosc": 6},
}
historia_akcji = []

while opcja != "koniec":
    opcja = input("\nPodaj opcje: ")

    if opcja == "saldo":
        # Program pobiera kwotę do dodania lub odjęcia z konta
        print("\nDostępne opcje dla operacji saldo\n")
        print("dodaj - dodaj kwotę do konta")
        print("odejmij - odejmij kwotę z konta\n")

        opcja_saldo = input("Podaj opcję dla operacji saldo: ")
        if opcja_saldo == "dodaj":
            kwota = float(input("Podaj kwotę do dodania: "))
            saldo += kwota
            historia_akcji.append(f"[{opcja} - {opcja_saldo}] Dodano {kwota:.2f} zł")
            print(f"Saldo po operacji: {saldo:.2f} zł")
        elif opcja_saldo == "odejmij":
            kwota = float(input("Podaj kwotę do odjęcia: "))
            saldo -= kwota
            historia_akcji.append(f"[{opcja} - {opcja_saldo}] Odjęto {kwota:.2f} zł")
            print(f"Saldo po operacji: {saldo:.2f} zł")
        else:
            print("Nieprawidłowa opcja dla operacji saldo")

    elif opcja == "sprzedaż":
        nazwa_produktu = input("Podaj nazwe produktu: ")
        ilosc_produktu = int(input("Podaj ilosc produktu: "))
        cena_produktu = int(input("Podaj cene produktu: "))
        if nazwa_produktu in magazyn:
            magazyn[nazwa_produktu]["ilosc"] -= ilosc_produktu
            magazyn[nazwa_produktu]["cena"] = cena_produktu
            message = f"Zaktualizowano produkt {nazwa_produktu}"
            historia_akcji.append(message)
            print(message)
        else:
            magazyn[nazwa_produktu] = {
            "ilosc": ilosc_produktu,
            "cena": cena_produktu,
            }
            message = f"Dodano do magazynu nowy produkt {nazwa_produktu}"
            historia_akcji.append(message)
            print(message)
        saldo += cena_produktu * ilosc_produktu
        """Program pobiera nazwę przedniotu, cenę oraz liczbę sztuk.
        Produkt musi znajdować się w magazynie.
        Obliczenia respektuje względem konta i magazynu"""

    elif opcja == "zakup":
        """Program pobiera nazwę produktu, cenę oraz liczbę sztuk.
        Produkt zostaje dodany do magazynu, jesli go nie było.
        Obliczenia są wykonane odwrotnie do komendy sprzedaż
        Saldo konta po zakończeniu operaji "zakup" nie może być ujemne."""
        produkt = input("Podaj nazwę produktu: ")
        cena = float(input("Podaj cenę produktu: "))
        ilosc = int(input("Podaj ilość produktu: "))
        if saldo < cena * ilosc:
            print("Nie masz wystarczających ilosci pieniędzy na koncie \n")
            continue
        if produkt in magazyn:
            magazyn[produkt]["ilosc"] += ilosc
            saldo -= cena * ilosc
            historia_akcji.append(f"[{opcja}] Zakupiono {ilosc} szt. {produkt} za {cena:.2f} zł")
            print (f"Saldo po operacji: {saldo:.2f} zł\n")
        else:
            magazyn[produkt]={"cena": cena, "ilosc": ilosc,}
            saldo -= cena * ilosc
            historia_akcji.append(f"[{opcja}] Zakupiono {ilosc} szt. {produkt} za {cena:.2f} zł")
            print (f"Saldo po operacji: {saldo:.2f} zł\n")
            
    elif opcja == "konto":
        """Program wyświetla stan konta"""
        print(f"Stan konta: {saldo:.2f} zł")
    elif opcja == "lista":
        """Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością."""
        print("Stan magazynu:\n")
        for produkt, dane in magazyn.items():
            print(f"{produkt} - cena: {dane['cena']:.2f} zł, ilość: {dane['ilosc']}")
    elif opcja == "magazyn":
        """Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę."""
        produkt = input("Podaj nazwę produktu: ")
        if produkt in magazyn:
            print(f"{produkt} - cena: {magazyn[produkt]['cena']:.2f} zł, ilość: {magazyn[produkt]['ilosc']}")
        else:
            print(f"Nie ma {produkt} w magazynie !!!")

    elif opcja == "przegląd":
        """Program pobiera zmienne "od" do "do".
        Jeżeli użytkownik podał pustą wartość "od" lub "do", program powinien wypisać przegląd od początku lub/i
        Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować
        i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres)."""
        
        print("Podaj zakres przeglądu akcji\n")
        od = input("Początek zakresu (od zera): ")
        do = input("Podaj koniec zakresu: ")
        if od == "" and do == "":
            for akcja in historia_akcji:
                print(akcja)
        elif od == "":
            for akcja in historia_akcji[:int(do)]:
                print(akcja)
        elif do == "":
            for akcja in historia_akcji[int(do):]:
                print(akcja)
        elif int(od) > len(historia_akcji) or int(do) > len(historia_akcji):
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia_akcji)}")
        elif int(od) > int(do):
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia_akcji)}")
        elif int(od) == int(do):
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia_akcji)}")
        elif int(od) < 0 or int(do) < 0:
            print(f"Zakres przeglądu jest poza zakresem historii akcji. Liczba wpisów w historii wynosi: {len(historia_akcji)}")
    elif opcja == "koniec":
        """Program kończy działanie"""
        break
    else:
        print("\nNieprawidłowa opcja. Użyj 'koniec' aby wyjść.")