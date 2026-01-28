count = 0

try:
    with open("story.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                count += len(line.split())

    print(f"Liczba słów: {count}")

except FileNotFoundError:
    print("Plik story.txt nie istnieje w tym folderze.")
