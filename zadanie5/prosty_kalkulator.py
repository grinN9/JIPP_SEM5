# Utwórz funkcję dodawania dwóch liczb
def add(a, b):
    return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    return a / b


# Wyświetl listę operacji
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

# Pozwól użytkownikowi wybrać żądane działanie
op = input("Please enter choice (a / b / c / d): ").strip().lower()

# Przechwyć 2 liczby i skonwertuj je na liczby
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Logika IF-ELIF-ELSE + wywołanie odpowiedniej funkcji
if op == "a":
    print("Result:", add(num1, num2))
elif op == "b":
    print("Result:", subtract(num1, num2))
elif op == "c":
    print("Result:", multiply(num1, num2))
elif op == "d":
    if num2 == 0:
        print("Error: division by zero!")
    else:
        print("Result:", divide(num1, num2))
else:
    print("Invalid choice!")
