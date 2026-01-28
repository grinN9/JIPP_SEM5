name = input("Podaj imię: ")
age = input("Podaj wiek: ")

with open("user.txt", "w", encoding="utf-8") as file:
    file.write(f"Imię: {name}\nWiek: {age}")