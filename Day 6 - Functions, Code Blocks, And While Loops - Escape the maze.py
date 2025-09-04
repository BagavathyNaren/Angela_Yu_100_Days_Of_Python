# Defining and calling functions

print("I am back")

num_char = len("I'm waiting")

print(num_char)


def my_function():
    print("Connect to MCP Server")
    print("Integrate MCP and A2A with Agentic AI Frameworks")

my_function()

# Maze Challenge

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

"""


Challenge Reeborg's world

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
turn_around() 
turn_right()
move()
turn_around()
turn_left()
move()
turn_right()
move()
turn_right()
move()



Hurdle Challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for set in range(6):
    jump()
    


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
IsAtGoal = at_goal()
if (IsAtGoal == True):
    pause()
while (IsAtGoal == False):
    CheckGoal = at_goal()
    if(CheckGoal  == True):
        IsAtGoal = CheckGoal
    else:
        jump()
    

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while not at_goal():
    jump()
    

Hurdle 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()     
    else:
        move()
    

        # Hurdle Four

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()     
    else:
        move()



"""

    




    