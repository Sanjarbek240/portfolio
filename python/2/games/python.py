import pygame
import random

pygame.init()

# Oyna o'lchamlari
WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Dodger")

# Ranglar
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# O'yinchi
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Dushman
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 5

# O'yin sikli
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Klaviatura boshqaruvi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_size:
        player_x += player_speed

    # Dushman harakati
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, WIDTH - enemy_size)

    # To'qnashuvni tekshirish
    if (player_x < enemy_x + enemy_size and
        player_x + player_size > enemy_x and
        player_y < enemy_y + enemy_size and
        player_y + player_size > enemy_y):
        print("Game Over")
        running = False

    # Ekranni yangilash
    win.fill(WHITE)
    pygame.draw.rect(win, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(win, RED, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.display.update()

pygame.quit()
