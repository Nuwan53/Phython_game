import random
from tkinter import Tk, Canvas, Label

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.direction = "right"

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
            square = canvas.create_rectangle(0, 0, SPACE_SIZE, SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

class Food:
    def __init__(self, canvas):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if snake.direction == "up":
        y -= SPACE_SIZE
    elif snake.direction == "down":
        y += SPACE_SIZE
    elif snake.direction == "left":
        x -= SPACE_SIZE
    elif snake.direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food.__init__(canvas)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    opposite_directions = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    if new_direction != opposite_directions.get(snake.direction):
        snake.direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    if [x, y] in snake.coordinates[1:]:
        return True
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2,
                       text="GAME OVER", fill="red", font=("Arial", 40))

# GUI Setup
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0

label = Label(window, text="Score:0", font=("Arial", 24), bg=BACKGROUND_COLOR, fg=SNAKE_COLOR)
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create snake and food
snake = Snake(canvas)
food = Food(canvas)

# Bind key events
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

# Start game
next_turn(snake, food)

window.mainloop()