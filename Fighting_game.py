import pygame

pygame.init()

# Background image
walkRight = pygame.image.load('DefaultP1.png')
walkLeft = pygame.image.load('DefaultP1.png')
bg = pygame.image.load("background.png")
idle = [pygame.image.load('DefaultP1.png'), pygame.image.load('Default animation P1 1.png'), pygame.image.load('DefaultP1.png')]
standcount = True

clock = pygame.time.Clock()

# Jump
isJump = False
jumpcount = 10

# Window
display_width = 1550
display_height = 1000
win = pygame.display.set_mode((display_width, display_height))

# Title & Icon
pygame.display.set_caption("Fighter Street")
icon = pygame.image.load('DefaultP1.png')
pygame.display.set_icon(icon)

# Player 1
player1_x = 50
player1_y = 430
player1_vel = 10

# Player 1 Image
player1_IMG = pygame.image.load('DefaultP1.png')

# Player 2
player2_x = 1200
player2_y = 430
player2_vel = 10

# Player 2 Image
player2_IMG = pygame.image.load('DeufaltP2.png')

# Player Movement
left = False
right = False
walkcount = 0


def player1(x, y):
    global standcount
    global walkcount
    win.blit(bg, (0, 0))

    if walkcount + 1 >= 9:
        walkcount = 0

    if standcount + 1 >= 9:
        standcount = 0

    if left:
        win.blit(idle[walkcount // 3], (x, y))
        walkcount += 1
    elif right:
        win.blit(idle[walkcount // 3], (x, y))
        walkcount += 1
    elif standcount:
        p = 0
        for frame in idle:
            win.blit(idle[p], (x, y))
            p += 1
            if p >= 2:
                p = 0
                continue

    pygame.display.update()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player1_x > player1_vel - 25:
        player1_x -= player1_vel
        left = True
        right = False
    elif keys[pygame.K_d] and player1_x < 1260:
        player1_x += player1_vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkcount = 0
        standcount = True

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False

    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            player1_y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            isJump = False
            jumpcount = 10

    player1(player1_x, player1_y)
    pygame.display.update()

    # Limit FPS to 60
    clock.tick(60)

# Quit pygame
pygame.quit()
