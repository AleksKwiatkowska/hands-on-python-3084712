NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

# does the same as first while loop but less prone to errors
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

# reverse order of the list
for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate - shows index of the list
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
