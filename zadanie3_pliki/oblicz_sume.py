total = 0

try:
    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line: 
                total += int(line)

    print("Suma:", total)

except FileNotFoundError:
    print("Plik numbers.txt nie istnieje w tym folderze.")
except ValueError:
    print("Błąd konwersji: w pliku jest linia, która nie jest liczbą całkowitą.")
