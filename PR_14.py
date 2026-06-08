import pygame
import math

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Практична №14 - Анімація персонажа")
def create_sky_background(width, height):
    bg = pygame.Surface((width, height))
    for i in range(height):
        color_ratio = i / height
        r = int(50 + 100 * color_ratio)
        g = int(100 + 100 * color_ratio)
        b = int(180 + 75 * color_ratio)
        pygame.draw.line(bg, (r, g, b), (0, i), (width, i))

    sun_x, sun_y = width - 80, 80
    pygame.draw.circle(bg, (255, 255, 100), (sun_x, sun_y), 40)
    pygame.draw.circle(bg, (255, 255, 50), (sun_x, sun_y), 35)

    cloud_color = (240, 240, 250, 200)
    cloud_positions = [(100, 80), (300, 60), (50, 150), (400, 120)]
    for cx, cy in cloud_positions:
        pygame.draw.ellipse(bg, cloud_color, (cx, cy, 60, 40))
        pygame.draw.ellipse(bg, cloud_color, (cx + 30, cy - 10, 70, 45))
        pygame.draw.ellipse(bg, cloud_color, (cx + 60, cy, 50, 35))

    pygame.draw.rect(bg, (34, 139, 34), (0, height - 120, width, 120))
    pygame.draw.rect(bg, (50, 205, 50), (0, height - 120, width, 10))
    return bg

def create_player_standing():
    surf = pygame.Surface((60, 71), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, (100, 200, 255), (10, 20, 40, 50))
    pygame.draw.circle(surf, (255, 220, 180), (30, 15), 15)
    pygame.draw.circle(surf, (0, 0, 0), (25, 12), 2)
    pygame.draw.circle(surf, (0, 0, 0), (35, 12), 2)
    pygame.draw.arc(surf, (0, 0, 0), (20, 15, 20, 10), 0, math.pi, 2)
    pygame.draw.ellipse(surf, (139, 69, 19), (20, 2, 20, 15))
    return surf

def create_player_walk(color_variant):
    surf = pygame.Surface((60, 71), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, color_variant, (10, 20, 40, 50))
    pygame.draw.circle(surf, (255, 220, 180), (30, 15), 15)
    pygame.draw.circle(surf, (0, 0, 0), (25, 12), 2)
    pygame.draw.circle(surf, (0, 0, 0), (35, 12), 2)
    pygame.draw.circle(surf, (0, 0, 0), (30, 20), 3)
    pygame.draw.ellipse(surf, (139, 69, 19), (20, 2, 20, 15))
    pygame.draw.line(surf, (0, 0, 200), (20, 65), (15, 71), 5)
    pygame.draw.line(surf, (0, 0, 200), (40, 65), (45, 71), 5)
    return surf

walk_right = [create_player_walk((70, 170, 230)) for _ in range(6)]
walk_left = [create_player_walk((90, 190, 250)) for _ in range(6)]
player_stand = create_player_standing()
bg = create_sky_background(WIDTH, HEIGHT)
clock = pygame.time.Clock()
x, y = 50, HEIGHT - 120
width, height = 60, 71
speed = 5
left, right = False, False
anim_count = 0
run = True

def draw_window():
    global anim_count
    win.blit(bg, (0, 0))
    if anim_count + 1 >= 30:
        anim_count = 0
    if left:
        win.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        win.blit(player_stand, (x, y))
    pygame.display.update()
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        left, right = True, False
    elif keys[pygame.K_RIGHT] and x < WIDTH - width:
        x += speed
        left, right = False, True
    else:
        left, right = False, False
        anim_count = 0
    draw_window()

pygame.quit()