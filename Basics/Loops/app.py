
# Run through a list 
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("Animal: {}.".format(animal))#

# Print numbers from 0 to 3
for i in range(4):
    print(i)

# Print numbers between 4 and 8 (exclusive)
for i in range(4, 8):
    print(i)

# Print numbers between 4 and 8 (exclusive) with step = 2
for i in range(4, 8, 2):
    print(i)


# Enumerate a list, shows index and animals
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)


## While Loops

x = 0
while x < 4:
    print(x)
    x += 1

# Break out of the loop
x = 0
while x < 4:
    print(x)
    x += 1
    if x == 2:
        break

# Continue to the next iteration
x = 0
while x < 4:
    x += 1
    if x == 2:
        continue
    print(x)

# Infinite loop
while True:
    pass 
    # Do Something Forever

# Infinite loop with break
while True:
    # Do Something Forever
    if condition:
        break


# While loop with else
x = 0
while x < 4:
    print(x)
    x += 1
else:
    print("Else statement")


