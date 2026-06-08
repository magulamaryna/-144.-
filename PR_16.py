import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Практична №16 - Стрільба вгору")

def create_forest_background(width, height):
    bg = pygame.Surface((width, height))
    for i in range(height):
        color = (int(100 - i / 5), int(150 - i / 4), int(200 - i / 3))
        if color[0] < 0:
            color = (0, 0, 50)
        pygame.draw.line(bg, color, (0, i), (width, i))
    pygame.draw.circle(bg, (255, 255, 100), (width - 60, 60), 40)
    cloud_color = (240, 240, 250)
    pygame.draw.ellipse(bg, cloud_color, (80, 50, 80, 40))
    pygame.draw.ellipse(bg, cloud_color, (120, 40, 70, 45))
    pygame.draw.ellipse(bg, cloud_color, (300, 70, 90, 40))
    for i in range(0, width, 100):
        pygame.draw.rect(bg, (101, 67, 33), (i + 35, height - 150, 15, 150))
        pygame.draw.circle(bg, (34, 139, 34), (i + 42, height - 160), 35)
        pygame.draw.circle(bg, (34, 139, 34), (i + 20, height - 140), 28)
        pygame.draw.circle(bg, (34, 139, 34), (i + 65, height - 140), 28)
    pygame.draw.rect(bg, (34, 139, 34), (0, height - 100, width, 100))
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(height - 100, height)
        pygame.draw.line(bg, (50, 205, 50), (x, y), (x, y - random.randint(5, 15)), 2)
    return bg

def create_player():
    surf = pygame.Surface((50, 60), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, (100, 200, 255), (8, 20, 34, 40))
    pygame.draw.circle(surf, (255, 220, 180), (25, 15), 14)
    pygame.draw.circle(surf, (0, 0, 0), (20, 12), 3)
    pygame.draw.circle(surf, (0, 0, 0), (30, 12), 3)
    pygame.draw.circle(surf, (255, 255, 255), (19, 11), 1)
    pygame.draw.circle(surf, (255, 255, 255), (29, 11), 1)
    pygame.draw.arc(surf, (0, 0, 0), (18, 15, 14, 10), 0, math.pi, 2)
    pygame.draw.ellipse(surf, (139, 69, 19), (15, 0, 20, 18))
    return surf

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 6
        self.vel_y = -10
        self.color = (100, 200, 255)
    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(win, (255, 255, 200), (int(self.x), int(self.y)), self.radius - 2)
    def update(self):
        self.y += self.vel_y

class Enemy:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.vel = random.choice([-2, -1.5, 1.5, 2])
        self.start_x = x
        self.end_x = WIDTH - width
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (180, 50, 50), (5, 10, width - 10, height - 10))
        pygame.draw.circle(self.image, (255, 255, 255), (width // 3, height // 3), 7)
        pygame.draw.circle(self.image, (255, 255, 255), (2 * width // 3, height // 3), 7)
        pygame.draw.circle(self.image, (0, 0, 0), (width // 3, height // 3), 4)
        pygame.draw.circle(self.image, (0, 0, 0), (2 * width // 3, height // 3), 4)
        pygame.draw.line(self.image, (0, 0, 0), (width // 3 - 5, height // 3 - 5), (width // 3 + 5, height // 3 - 2), 3)
        pygame.draw.line(self.image, (0, 0, 0), (2 * width // 3 - 5, height // 3 - 5),
                         (2 * width // 3 + 5, height // 3 - 2), 3)
        pygame.draw.arc(self.image, (0, 0, 0), (width // 3, height // 2, width // 3, height // 4), 0, math.pi, 3)
        pygame.draw.polygon(self.image, (80, 80, 80), [(width // 4, 0), (width // 3, -8), (width // 2, 0)])
        pygame.draw.polygon(self.image, (80, 80, 80), [(3 * width // 4, 0), (2 * width // 3, -8), (width // 2, 0)])
        self.hitbox = (x + 10, y + 10, width - 20, height - 20)
        self.health = 5

    def move(self):
        self.x += self.vel
        if self.x <= self.start_x or self.x >= self.end_x:
            self.vel = -self.vel
        self.hitbox = (self.x + 10, self.y + 10, self.width - 20, self.height - 20)
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        bar_width = self.width
        health_width = bar_width * (self.health / 5)
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 15, bar_width, 6))
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - 15, health_width, 6))
    def hit(self):
        self.health -= 1
        return self.health <= 0

class FlyingEnemy:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 100)
        self.y = random.randint(50, 200)
        self.width = 40
        self.height = 40
        self.vel_x = random.choice([-1.5, 1.5])
        self.vel_y = random.choice([-0.5, 0.5])
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (255, 100, 50), (5, 10, 30, 30))
        pygame.draw.circle(self.image, (255, 255, 255), (self.width // 3, self.height // 3), 5)
        pygame.draw.circle(self.image, (0, 0, 0), (self.width // 3, self.height // 3), 2)
        pygame.draw.polygon(self.image, (255, 100, 50),
                            [(self.width - 10, self.height // 2), (self.width, self.height // 2 - 5),
                             (self.width, self.height // 2 + 5)])
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height - 10)
        self.health = 3
    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x <= 20 or self.x >= WIDTH - self.width - 20:
            self.vel_x = -self.vel_x
        if self.y <= 30 or self.y >= 250:
            self.vel_y = -self.vel_y
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height - 10)
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        bar_width = self.width
        health_width = bar_width * (self.health / 3)
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 12, bar_width, 5))
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - 12, health_width, 5))
    def hit(self):
        self.health -= 1
        return self.health <= 0

clock = pygame.time.Clock()
bg = create_forest_background(WIDTH, HEIGHT)
player_img = create_player()
x = WIDTH // 2 - 25
y = HEIGHT - 80
speed = 5
bullets = []
shoot_cooldown = 0
SHOOT_DELAY = 10
ground_enemies = []
flying_enemies = []
spawn_timer = 0
flying_spawn_timer = 0
score = 0
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

run = True
while run:
    clock.tick(60)
    if shoot_cooldown > 0:
        shoot_cooldown -= 1
    if spawn_timer <= 0 and len(ground_enemies) < 4:
        new_enemy = Enemy(random.randint(50, WIDTH - 100), HEIGHT - 130, 50, 50)
        ground_enemies.append(new_enemy)
        spawn_timer = 90
    else:
        spawn_timer -= 1
    if flying_spawn_timer <= 0 and len(flying_enemies) < 3:
        new_flying = FlyingEnemy()
        flying_enemies.append(new_flying)
        flying_spawn_timer = 120
    else:
        flying_spawn_timer -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < WIDTH - 50:
        x += speed
    if (keys[pygame.K_f] or keys[pygame.K_SPACE]) and shoot_cooldown == 0:
        bullets.append(Bullet(x + 25, y + 10))
        shoot_cooldown = SHOOT_DELAY
    for bullet in bullets[:]:
        bullet.update()
        if bullet.y < 0:
            bullets.remove(bullet)
    for bullet in bullets[:]:
        for enemy in flying_enemies[:]:
            if (enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and
                    enemy.hitbox[1] < bullet.y < enemy.hitbox[1] + enemy.hitbox[3]):
                bullets.remove(bullet)
                if enemy.hit():
                    flying_enemies.remove(enemy)
                    score += 15
                break
    for bullet in bullets[:]:
        for enemy in ground_enemies[:]:
            if (enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and
                    enemy.hitbox[1] < bullet.y < enemy.hitbox[1] + enemy.hitbox[3]):
                bullets.remove(bullet)
                if enemy.hit():
                    ground_enemies.remove(enemy)
                    score += 10
                break

    for enemy in ground_enemies:
        enemy.move()
    for enemy in flying_enemies:
        enemy.move()
    player_rect = pygame.Rect(x, y, 50, 60)
    for enemy in ground_enemies[:]:
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        if player_rect.colliderect(enemy_rect):
            run = False
    for enemy in flying_enemies[:]:
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        if player_rect.colliderect(enemy_rect):
            run = False
    win.blit(bg, (0, 0))
    win.blit(player_img, (x, y))
    for enemy in ground_enemies:
        enemy.draw(win)
    for enemy in flying_enemies:
        enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))
    controls_text = small_font.render("← → move | F/SPACE shoot UP", True, (200, 200, 200))
    win.blit(controls_text, (10, HEIGHT - 30))
    enemies_text = small_font.render(f"Ground: {len(ground_enemies)}  Flying: {len(flying_enemies)}", True,(200, 200, 200))
    win.blit(enemies_text, (10, 50))

    pygame.display.update()

pygame.quit()