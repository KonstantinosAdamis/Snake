import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font for score display
font = pygame.font.Font(None, 30)

def draw_snake(snake):
    """Draw the snake on the screen."""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    """Draw the food (apple) on the screen."""
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def get_new_food_position(snake):
    """Find a new position for the food that is not occupied by the snake."""
    empty_spaces = [(x, y) for x in range(0, WIDTH, CELL_SIZE) for y in range(0, HEIGHT, CELL_SIZE) if (x, y) not in snake]
    return random.choice(empty_spaces) if empty_spaces else None

def main():
    running = True
    snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake body
    direction = RIGHT
    food = get_new_food_position(snake)
    score = 0

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Move snake
        new_head = (snake[0][0] + direction[0] * CELL_SIZE, snake[0][1] + direction[1] * CELL_SIZE)
        snake.insert(0, new_head)

        # Check collision with food
        if new_head == food:
            food = get_new_food_position(snake)
            score += 1
        else:
            snake.pop()  # Remove last segment if no food eaten

        # Check collision with walls or itself
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake[1:]):  # Collision with itself
            running = False

        # Draw elements
        draw_snake(snake)
        draw_food(food)

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)  # Controls the speed of the game

    pygame.quit()

if __name__ == "__main__":
    main()
