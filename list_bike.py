# create list
bike_list = ['trek', 'canondale', 'giant', 'specialized']

# access element of list
print(bike_list[0].title())

# index position start at 0
print(bike_list[1])

# access last index -1
print(bike_list[-1])

#using value from list
message = f'my road bike is a {bike_list[-2]}'
print(message)

# Modifiying list
bike_list[1] = "crackendale"
print(f"modified list: {bike_list}")

# add element at the end / Append list
bike_list.append("rocky montain")
print(bike_list)

# empty list from scratch
empty_beach_list = []
empty_beach_list.append("bondi")
empty_beach_list.append("curl curl")
empty_beach_list.append("sharkies")
empty_beach_list.append("thiroul")

print(empty_beach_list)

# insert new element in list (at begening)
empty_beach_list.insert(0,"bronte")
print(empty_beach_list)

# remove element by index // del statement

del bike_list[1]
print(bike_list)

# use item after deleting / pop method
popped = empty_beach_list.pop()
print(f"last beach i visited while popping is: {popped}")

# remove by value
motorcycles = ['ducati', 'yamaha', 'honda']
print((motorcycles))

too_expensive ='ducati'
motorcycles.remove(too_expensive)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# sorting list
cars =['bmw', 'audi', 'honda', 'toyota', 'ford', 'subaru']
print(f"cars list unsorted: {cars}")

cars.sort()
print(f"cars list sorted: {cars}")
