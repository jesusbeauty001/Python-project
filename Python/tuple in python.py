# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Faith",21,"male")

print(student.count("Faith"))
print(student.index("male"))

for x in student:
    print(x)

if "Faith" in student:
    print("Faith is here")