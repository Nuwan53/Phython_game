from _tkinter import *
import random
from tkinter import Canvas, Label, Tk

GAME_WIDTH = 800
GAME_HEIGHT = 800   
SPEED = 50
SPACE_SIZE = 20
SNAKE_COLOR = "#00FF00" 
FOOD_COLOR = "#FF0000"
BODY_PARTS = 3
background_color = "#000000"    # Black background


class Snake:
    pass

class Food:
    pass

    def __init__(self):
        
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.cordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")   
 
    pass

def next_turn(snake, food):
    # Check if the snake has eaten the food
    if snake.head == food.position:
        snake.grow()
        food.randomize_position(snake.body)
    else:
        snake.move()

def change_direction(snake, new_direction):
    # Prevent the snake from moving in the opposite direction
    if (snake.direction[0] * -1, snake.direction[1] * -1) != new_direction:
        snake.direction = new_direction

def check_collision(snake, width, height):
    # Check if the snake has collided with the walls or itself
    if (snake.head[0] < 0 or snake.head[0] >= width or
        snake.head[1] < 0 or snake.head[1] >= height or
        snake.head in snake.body[1:]):
        return True
    return False

def game_over(snake, width, height):
    # Check if the snake has collided with the walls or itself
    if (snake.head[0] < 0 or snake.head[0] >= width or
        snake.head[1] < 0 or snake.head[1] >= height or
        snake.head in snake.body[1:]):
        return True
    return False


window = Tk()
window.title("Snake Game")
window.resizable(False, False)  

score = 0
direction = 'down'

label = Label(window, text="Score: " + str(score), font=("Arial", 24), bg=background_color, fg=SNAKE_COLOR)
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=background_color)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

Snake = Snake()
Food = Food()

window.mainloop()


