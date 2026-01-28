# Zapytaj użytkownika o imię i nazwisko
name = input("Podaj imię i nazwisko: ")

# Zapytaj użytkownika o miasto
city = input("W jakim mieście mieszkasz?: ")

# Zapytaj o wiek
age = input("Ile masz lat?: ")

# Zbuduj tekst wyjściowy
string = "Cześć {}, masz {} lat i mieszkasz w {}."
output = string.format(name, age, city)

# Wyświetl wynik
print(output)