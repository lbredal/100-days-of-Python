# These code samples are meant to be run in Reeborg's World
# Will not build here because we're lacking Reeborg's magnificent functions

# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Hurdles (1-4)
def jump():
    turn_left()
    while wall_on_right():
        move()
    
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()

    
# Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear() and not right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()

    
# Problem World's from Angela
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
            move()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()
    
