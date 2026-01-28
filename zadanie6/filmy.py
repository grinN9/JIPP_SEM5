# Utwórz słownik filmów. Niech kluczem będzie nazwa filmu, a parą wartości dwie liczby:
# kryteria wiekowe oraz liczba dostępnych biletów
movies = {"Finding Nemo": [5, 2], "Moana": [6, 3], "Batman": [18, 5], "The Lion King": [10, 4]}

# Utwórz pętlę, która będzie działać w nieskończoność
while True:

    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca,
    # a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)
    title = input("Podaj tytuł filmu: ").strip().title()

    # Stwórz instrukcję warunkową if. Jeśli wybrany film jest dostępny w słowniku, kontynuuj
    if title in movies:

        # Zapytaj użytkownika o wiek
        age = int(input("Podaj swój wiek: "))

        # Sprawdź użytkownika pod kątem kwalifikowalności
        min_age = movies[title][0]
        tickets = movies[title][1]

        # Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc
        if age >= min_age:

            # Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmniejsz pulę dostępnych miejsc o 1
            if tickets > 0:
                movies[title][1] -= 1
                print(f"Rezerwacja udana! Zostało biletów na '{title}': {movies[title][1]}")
            else:
                print(f"Brak wolnych miejsc na '{title}'.")
        else:
            print(f"Nie spełniasz kryterium wiekowego. Minimalny wiek dla '{title}' to {min_age}.")
    else:
        print("Nie mamy takiego filmu w repertuarze.")
