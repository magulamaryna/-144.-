import pygame
import math

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Практична №15 - Стрільба")

def create_space_background(width, height):
    bg = pygame.Surface((width, height))
    bg.fill((10, 10, 30))

    import random
    for _ in range(200):
        x, y = random.randint(0, width), random.randint(0, height)
        r = random.randint(1, 3)
        pygame.draw.circle(bg, (255, 255, 200), (x, y), r)
    pygame.draw.circle(bg, (150, 100, 50), (width // 2, height + 50), 150)
    return bg

def create_player():
    surf = pygame.Surface((50, 60), pygame.SRCALPHA)
    pygame.draw.rect(surf, (0, 150, 255), (10, 20, 30, 40))
    pygame.draw.rect(surf, (0, 100, 200), (15, 25, 20, 30))
    pygame.draw.circle(surf, (255, 220, 180), (25, 15), 12)
    pygame.draw.rect(surf, (200, 200, 255), (18, 10, 14, 8))
    return surf
class Bullet:
    def __init__(self, x, y, facing):
        self.x, self.y = x, y
        self.radius = 8
        self.color = (255, 100, 255)
        self.vel = 12 * facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius - 3)
clock = pygame.time.Clock()
bg = create_space_background(WIDTH, HEIGHT)
player = create_player()
x, y = WIDTH // 2 - 25, HEIGHT - 80
speed = 5
left, right = False, False
last_move = 'right'
bullets = []
shoot_delay = 0
MAX_BULLETS = 6
run = True
while run:
    clock.tick(30)
    if shoot_delay > 0:
        shoot_delay += 1
    if shoot_delay > 10:
        shoot_delay = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        left, right = True, False
        last_move = 'left'
    elif keys[pygame.K_RIGHT] and x < WIDTH - 50:
        x += speed
        left, right = False, True
        last_move = 'right'
    else:
        left, right = False, False
    if keys[pygame.K_f] and shoot_delay == 0 and len(bullets) < MAX_BULLETS:
        facing = 1 if last_move == 'right' else -1
        bullets.append(Bullet(x + 25, y + 30, facing))
        shoot_delay = 1
    for bullet in bullets[:]:
        if 0 < bullet.x < WIDTH:
            bullet.x += bullet.vel
        else:
            bullets.remove(bullet)
    win.blit(bg, (0, 0))
    if left:
        win.blit(pygame.transform.flip(player, True, False), (x, y))
    else:
        win.blit(player, (x, y))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

pygame.quit()