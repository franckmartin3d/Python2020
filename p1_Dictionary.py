# A simple dictionary

alien_0 = {'color': 'green', 'points': 3}

print(alien_0['color'])
print((alien_0['points']))

# acces the value

new_point = alien_0['points']
print(f"You just earned {new_point}")

# add new key/value
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# ######################EXAMPLE######################
#move alien to the right
#Determine how far to move alien based on its current speed.

alien_example ={'x_pos': 0 , 'y_pos': 25 , 'speed': "fast"}
print(f"alien original x-position: {alien_example['x_pos']}")

if alien_example['speed'] == 'slow':
    x_increment = 1
elif alien_example['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#new position is old position + increment
alien_example['x_pos'] = alien_example['x_pos'] + x_increment

print(f"new alien x-position:{alien_example['x_pos']}")


#Removing Key value with del statement
del alien_0['points']
print(alien_0)

# Dictionary sintax
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'c++',
    'phil': 'JS',
    }
language = favorite_language['sarah'].title()
print(f"sarah favorite language is {language}")


# Get method() if key doesnt exist
alien_0.get('points', "points no longer exist")
