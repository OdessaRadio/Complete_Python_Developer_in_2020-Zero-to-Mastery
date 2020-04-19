from datetime import datetime

name = "Sasha"
age = 50
relationship_status = "Single"

relationship_status = 'it\'s complicated'
# print(relationship_status)

birth_year = input("What year were you born?")
year = str((datetime.now()))[:4]

print(year)
print(type(year), type(birth_year))

age = int(year) - int(birth_year)
print(f'You are {age} years old')

# Adding note for technical commit 1