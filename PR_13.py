import pygame

pygame.init()
WIDTH = 500 + 5
HEIGHT = 500 + 5
RECT_WIDTH = 55
RECT_HEIGHT = 60
COLOR = (128, 0, 128)
SPEED = 5
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 1 - Rectangle")

x = WIDTH // 2 - RECT_WIDTH // 2
y = HEIGHT // 2 - RECT_HEIGHT // 2
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    pygame.time.delay(SPEED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= SPEED
    if keys[pygame.K_RIGHT] and x < WIDTH - RECT_WIDTH:
        x += SPEED
    if keys[pygame.K_UP] and y > 0:
        y -= SPEED
    if keys[pygame.K_DOWN] and y < HEIGHT - RECT_HEIGHT:
        y += SPEED
    if keys[pygame.K_SPACE]:
        is_jump = True
        jump_count = 10
    win.fill((0, 0, 0))
    pygame.draw.rect(win, COLOR, (x, y, RECT_WIDTH, RECT_HEIGHT))
    pygame.display.update()

pygame.quit()