import tkinter as tk
import random

# Paramètres de la fenêtre et de la grille
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 20

# Classe principale du jeu
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        # Création du canvas
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Initialisation du jeu
        self.snake = [(20, 20), (20, 40), (20, 60)]
        self.direction = "Down"
        self.running = True
        self.food = self.place_food()
        
        # Affichage initial
        self.draw_snake()
        self.canvas.bind_all("<Key>", self.change_direction)
        
        # Boucle de jeu
        self.update_snake()

    def draw_snake(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green")
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + GRID_SIZE, fy + GRID_SIZE, fill="red")

    def place_food(self):
        return (
            random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
            random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        )

    def update_snake(self):
        if not self.running:
            return

        # Mouvement de la tête
        x, y = self.snake[-1]
        if self.direction == "Up":
            y -= GRID_SIZE
        elif self.direction == "Down":
            y += GRID_SIZE
        elif self.direction == "Left":
            x -= GRID_SIZE
        elif self.direction == "Right":
            x += GRID_SIZE

        new_head = (x, y)
        
        # Vérification des collisions
        if (
            x < 0
            or y < 0
            or x >= WIDTH
            or y >= HEIGHT
            or new_head in self.snake
        ):
            self.running = False
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="red", font=("Arial", 24))
            return

        # Gestion de la nourriture
        self.snake.append(new_head)
        if new_head == self.food:
            self.food = self.place_food()
        else:
            self.snake.pop(0)

        # Redessine le serpent
        self.draw_snake()
        self.root.after(100, self.update_snake)

    def change_direction(self, event):
        if event.keysym in ("Up", "Down", "Left", "Right"):
            opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if self.direction != opposite_directions.get(event.keysym):
                self.direction = event.keysym

# Initialisation de tkinter
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
