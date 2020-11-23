# using range() function

for value in range(1, 5):
    print(value)

# make list using range
numbers = list(range(1,6))
print(numbers)

# step size list
even_numbers = list(range(2,11,2))
print(even_numbers)

# create square list using range and appen
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# Or
new_squares = []
for value in range (1,11):
    new_squares.append(value ** 2)
print(new_squares)

#list compreantion
list_compreantion_square =[value**2 for value in range(1,11)]
print(list_compreantion_square)


