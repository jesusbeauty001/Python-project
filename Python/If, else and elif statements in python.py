# if statements = a block of code that will execute if it's condition is true
# if, else and elif 

age = int(input("How old are you?: "))

if age == 100:
    print("You are century old")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")
