
# slicing list
players =["chuck", "joe", "dom", "ingrid,"]
print(players[0:3])

print(players[1:3])
#from start
print(players[:3])
#too end
print(players[2:])
# output last 3 player on roster
print(players[-3:])

#sliced for loop
print("sliced for loop example \nHere arte the first tree player on the team:")
for player in players[:3]:
    print(player.title())

# copying list
my_food = ["pizza", "coffee", "salad", "patate"]
friends_food = my_food[:]

print("My favorite food are:")
print(my_food)

print("\nMy friend favorite food are:")
print(friends_food)

my_food.append("spagetti")
friends_food.append("lasagna")

print("My favorite food are:")
print(my_food)

print("\nMy friend favorite food are:")
print(friends_food)