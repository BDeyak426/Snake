import pygame
import time
import random

# Initialize the game
pygame.init()

# Set the width and height of the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the snake and food initial positions
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Set the initial direction of the snake
direction = "RIGHT"
change_to = direction

# Set the initial score
score = 0

# Function to display the score
def show_score(choice=1):
    font = pygame.font.SysFont("monaco", 24)
    score_text = font.render("Score: " + str(score), True, white)
    if choice == 1:
        window.blit(score_text, (10, 10))
    else:
        window.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2))

# Main game loop
game_over = False
while not game_over:
    # Handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = "RIGHT"

    # Validate the direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Update the snake position
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Respawn food if eaten
    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawn = True

    # Update the game window
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))
    show_score()
    pygame.display.update()

    # Delay for smooth gameplay
    pygame.time.Clock().tick(30)

pygame.quit()