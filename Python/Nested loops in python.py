# nested loops = The "inner loops" will finish all of it's iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many colums?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end= "")
    print()