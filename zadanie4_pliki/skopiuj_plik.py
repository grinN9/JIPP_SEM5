try:
    with open("numbers.txt", "r", encoding="utf-8") as source:
        content = source.read()

    with open("copy.txt", "w", encoding="utf-8") as target:
        target.write(content)

    print("Skopiowano zawartość do pliku copy.txt")

except FileNotFoundError:
    print("Plik numbers.txt nie istnieje w tym folderze.")
