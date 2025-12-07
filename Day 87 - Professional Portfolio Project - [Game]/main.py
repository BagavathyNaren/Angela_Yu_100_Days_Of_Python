import turtle
import random

# Set up the game window
window = turtle.Screen()
window.title("Breakout Clone - Python Turtle")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Turn off automatic screen updates for smoother animation

# Game variables
score = 0
lives = 3
level = 1
game_state = "playing"  # "playing", "game_over", "win"
brick_rows = 6
brick_cols = 10
bricks = []

# Colors for the bricks
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = random.choice([-4, -3, 3, 4])  # Horizontal speed
ball.dy = -4  # Vertical speed (negative means going down initially)

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-380, 260)
score_display.write(f"Score: {score}  Lives: {lives}  Level: {level}", 
                    align="left", font=("Courier", 18, "normal"))

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("yellow")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, -280)
instructions.write("Use LEFT and RIGHT arrow keys to move", 
                   align="center", font=("Courier", 12, "normal"))

# Game over/win message
message = turtle.Turtle()
message.speed(0)
message.color("white")
message.penup()
message.hideturtle()
message.goto(0, 0)

# Function to create bricks
def create_bricks():
    global bricks
    bricks = []
    
    # Calculate brick spacing and size
    brick_width = 70
    brick_height = 25
    brick_spacing = 5
    start_x = -((brick_cols * (brick_width + brick_spacing)) // 2) + brick_width // 2
    start_y = 200
    
    for row in range(brick_rows):
        for col in range(brick_cols):
            brick = turtle.Turtle()
            brick.speed(0)
            brick.shape("square")
            brick.color(colors[row % len(colors)])
            brick.shapesize(stretch_wid=1, stretch_len=3.5)
            brick.penup()
            
            # Position the brick
            x = start_x + col * (brick_width + brick_spacing)
            y = start_y - row * (brick_height + brick_spacing)
            brick.goto(x, y)
            
            # Store brick information
            bricks.append({
                "turtle": brick,
                "x": x,
                "y": y,
                "width": brick_width,
                "height": brick_height,
                "points": (brick_rows - row) * 10  # More points for higher rows
            })

# Function to move paddle left
def move_paddle_left():
    x = paddle.xcor()
    if x > -350:  # Keep paddle within left boundary
        x -= 30
    paddle.setx(x)

# Function to move paddle right
def move_paddle_right():
    x = paddle.xcor()
    if x < 350:  # Keep paddle within right boundary
        x += 30
    paddle.setx(x)

# Function to check collision between ball and object
def check_collision(ball, obj_x, obj_y, obj_width, obj_height):
    ball_x, ball_y = ball.xcor(), ball.ycor()
    
    # Check if ball is within the object's boundaries
    if (abs(ball_x - obj_x) < (obj_width/2 + 10) and 
        abs(ball_y - obj_y) < (obj_height/2 + 10)):
        return True
    return False

# Function to update score display
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}  Lives: {lives}  Level: {level}", 
                        align="left", font=("Courier", 18, "normal"))

# Function to reset ball position
def reset_ball():
    ball.goto(0, -230)
    ball.dx = random.choice([-4, -3, 3, 4])
    ball.dy = -4

# Function to check game status
def check_game_status():
    global game_state
    
    if lives <= 0:
        game_state = "game_over"
        message.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        message.goto(0, -50)
        message.write(f"Final Score: {score}", align="center", font=("Courier", 24, "normal"))
    elif len(bricks) == 0:
        game_state = "win"
        message.write("LEVEL COMPLETE!", align="center", font=("Courier", 36, "normal"))
        message.goto(0, -50)
        message.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 24, "normal"))

# Function to start a new level
def new_level():
    global level, game_state
    level += 1
    game_state = "playing"
    message.clear()
    create_bricks()
    reset_ball()
    update_score()

# Function to restart the game
def restart_game():
    global score, lives, level, game_state
    score = 0
    lives = 3
    level = 1
    game_state = "playing"
    message.clear()
    create_bricks()
    reset_ball()
    update_score()

# Keyboard bindings
window.listen()
window.onkeypress(move_paddle_left, "Left")
window.onkeypress(move_paddle_right, "Right")
window.onkeypress(restart_game, "r")
window.onkeypress(new_level, "n")

# Create initial bricks
create_bricks()

# Main game loop
def game_loop():
    global score, lives, ball, game_state
    
    if game_state == "playing":
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # Border checking - left and right walls
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.dx *= -1  # Reverse horizontal direction
            
        # Border checking - top wall
        if ball.ycor() > 290:
            ball.dy *= -1  # Reverse vertical direction
            
        # Border checking - bottom wall (missed the paddle)
        if ball.ycor() < -290:
            lives -= 1
            update_score()
            reset_ball()
            
            if lives > 0:
                # Brief pause to reset
                window.update()
                turtle.time.sleep(1)
        
        # Paddle collision
        if check_collision(ball, paddle.xcor(), paddle.ycor(), 100, 20):
            # Adjust bounce angle based on where the ball hits the paddle
            relative_intersect = (paddle.xcor() - ball.xcor()) / 50
            ball.dx = -relative_intersect * 4  # Adjust horizontal speed
            ball.dy *= -1  # Reverse vertical direction
            ball.sety(paddle.ycor() + 20)  # Move ball above paddle to prevent sticking
        
        # Brick collisions
        for brick_info in bricks[:]:  # Iterate over a copy of the list
            brick = brick_info["turtle"]
            if check_collision(ball, brick_info["x"], brick_info["y"], 
                               brick_info["width"], brick_info["height"]):
                
                # Remove the brick
                brick.hideturtle()
                bricks.remove(brick_info)
                
                # Add to score
                score += brick_info["points"]
                update_score()
                
                # Determine bounce direction
                # Check which side of the brick was hit
                if abs(ball.xcor() - brick_info["x"]) > brick_info["width"]/2 - 5:
                    ball.dx *= -1  # Hit left or right side
                else:
                    ball.dy *= -1  # Hit top or bottom side
                
                # Play a "brick break" effect by changing ball color temporarily
                original_color = ball.color()
                ball.color("yellow")
                window.update()
                ball.color(original_color[0])
                break  # Only break one brick per frame
        
        # Check game status
        check_game_status()
    
    # Update the screen
    window.update()
    
    # Continue the game loop
    window.ontimer(game_loop, 20)

# Start the game loop
game_loop()

# Keep the window open
window.mainloop()