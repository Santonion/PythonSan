import pygame
from pygame.locals import *

# Startar Pygame
pygame.init()

# Gör ett fönster för spelet
window_width = 1550
window_height = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ryo vs Ken")

# Karaktärernas utseende
ryo_image = pygame.image.load('DefaultP1.png')
ken_image = pygame.image.load('DeufaltP2.png')

# Backgrunden
background_image = pygame.image.load('background.png')

# positionen när spelet börjar
ryo_x = 125
ryo_y = 500
ken_x = 1100
ken_y = 500



# Lop för att röra spelarna
while True:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            # Move Ryo using the arrow keys
            if event.key == pygame.K_a:
                ryo_x -= 10
            elif event.key == pygame.K_d:
                ryo_x += 10
            elif event.key == pygame.K_w:
                ryo_y -= 10
            elif event.key == pygame.K_s:
                ryo_y += 10
            # Move Ken using the WASD keys
            elif event.key == pygame.K_LEFT:
                ken_x -= 10
            elif event.key == pygame.K_RIGHT:
                ken_x += 10
            elif event.key == pygame.K_UP:
                ken_y -= 10
            elif event.key == pygame.K_DOWN:
                ken_y += 10

    # Backgrund och spelarens bilder printas gång på gång
    window.blit(background_image, (-120, 70))
    window.blit(ryo_image, (ryo_x, ryo_y))
    window.blit(ken_image, (ken_x, ken_y))
    pygame.display.update()

    # Gör en klocka för att skapa tidspress
    clock = pygame.time.Clock()

    # FPS
    clock.tick(60)

    # Mängden liv
    ryo_health = 100
    ken_health = 100

    # Slut på spelet
    if ryo_health <= 0:
        print("Ken wins!")
        game_over = True
    elif ken_health <= 0:
        print("Ryo wins!")
        game_over = True

    ryo_rect = Rect(200, 500, 50, 50)
    ken_rect = Rect(200, 0, 50, 50)

    # Fixar så att karaktärerna skadar varandra när dom rörsvid
    ryo_rect = ryo_image.get_rect()
    ryo_rect.x = ryo_x
    ryo_rect.y = ryo_y
    ken_rect = ken_image.get_rect()
    ken_rect.x = ken_x
    ken_rect.y = ken_y
    if ryo_rect.colliderect(ken_rect):
        ryo_health -= 10
        ken_health -= 10