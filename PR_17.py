import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Практична №17 - Ворог на одному рівні")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
ORANGE = (255, 150, 50)
PURPLE = (200, 50, 255)
YELLOW = (255, 255, 100)
DARK_GREEN = (34, 139, 34)

def create_desert_background(width, height):
    bg = pygame.Surface((width, height))
    for i in range(height):
        r = min(255, 200 + int(i / 4))
        g = min(150, 100 + int(i / 5))
        b = min(100, 50 + int(i / 6))
        pygame.draw.line(bg, (r, g, b), (0, i), (width, i))
    pygame.draw.circle(bg, (255, 220, 100), (WIDTH - 80, 80), 55)
    pygame.draw.circle(bg, (255, 255, 150), (WIDTH - 80, 80), 45)

    for _ in range(5):
        bx = random.randint(100, 300)
        by = random.randint(40, 100)
        pygame.draw.line(bg, (50, 50, 50), (bx, by), (bx + 10, by - 5), 2)
        pygame.draw.line(bg, (50, 50, 50), (bx + 10, by - 5), (bx + 20, by), 2)

    for i in range(height - 120, height):
        color_ratio = (i - (height - 120)) / 120
        sand_color = (210 + int(30 * color_ratio), 180 + int(20 * color_ratio), 140 + int(10 * color_ratio))
        pygame.draw.line(bg, sand_color, (0, i), (width, i))

    pygame.draw.rect(bg, DARK_GREEN, (40, height - 130, 15, 80))
    pygame.draw.rect(bg, DARK_GREEN, (45, height - 155, 10, 40))
    pygame.draw.rect(bg, DARK_GREEN, (WIDTH - 90, height - 140, 18, 90))
    pygame.draw.rect(bg, DARK_GREEN, (WIDTH - 85, height - 170, 12, 45))
    pygame.draw.rect(bg, DARK_GREEN, (WIDTH - 95, height - 155, 12, 35))
    return bg

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 55
        self.speed = 5
        self.health = 100
        self.max_health = 100
        self.direction = 1
        self.image_right = self.create_player_image(1)
        self.image_left = self.create_player_image(-1)
        self.image = self.image_right

    def create_player_image(self, direction):
        surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.ellipse(surf, BLUE, (5, 15, 35, 40))
        pygame.draw.rect(surf, (150, 150, 200), (8, 25, 29, 25))
        pygame.draw.circle(surf, (255, 220, 180), (22, 12), 13)
        pygame.draw.ellipse(surf, (180, 180, 200), (12, 0, 20, 16))
        if direction == 1:
            pygame.draw.circle(surf, BLACK, (18, 10), 3)
            pygame.draw.circle(surf, BLACK, (26, 10), 3)
        else:
            pygame.draw.circle(surf, BLACK, (19, 10), 3)
            pygame.draw.circle(surf, BLACK, (27, 10), 3)
        pygame.draw.circle(surf, WHITE, (17, 9), 1)
        pygame.draw.circle(surf, WHITE, (25, 9), 1)
        pygame.draw.arc(surf, BLACK, (16, 13, 12, 8), 0, math.pi, 2)
        if direction == 1:
            pygame.draw.line(surf, (192, 192, 192), (38, 35), (48, 25), 5)
            pygame.draw.line(surf, (139, 69, 19), (36, 33), (40, 38), 6)
        else:
            pygame.draw.line(surf, (192, 192, 192), (7, 35), (-3, 25), 5)
            pygame.draw.line(surf, (139, 69, 19), (9, 33), (5, 38), 6)
        return surf

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.direction = -1
            self.image = self.image_left
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
            self.direction = 1
            self.image = self.image_right

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        bar_width = 60
        health_width = bar_width * (self.health / self.max_health)
        pygame.draw.rect(win, RED, (self.x + 5, self.y - 15, bar_width, 8))
        pygame.draw.rect(win, GREEN, (self.x + 5, self.y - 15, health_width, 8))

    def hit(self, damage):
        self.health -= damage
        return self.health <= 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.radius = 6
        self.vel = 12 * direction
        self.damage = 15

    def draw(self, win):
        pygame.draw.circle(win, ORANGE, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(win, YELLOW, (int(self.x), int(self.y)), self.radius - 2)
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), self.radius - 4)

    def update(self):
        self.x += self.vel

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)

class Goblin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.vel = 2.5
        self.health = 20
        self.max_health = 20
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, PURPLE, (5, 15, 40, 35))
        pygame.draw.ellipse(self.image, (100, 50, 200), (8, 20, 34, 28))
        pygame.draw.circle(self.image, (100, 150, 50), (25, 12), 11)
        pygame.draw.circle(self.image, RED, (20, 10), 4)
        pygame.draw.circle(self.image, RED, (30, 10), 4)
        pygame.draw.circle(self.image, BLACK, (20, 10), 2)
        pygame.draw.circle(self.image, BLACK, (30, 10), 2)
        pygame.draw.arc(self.image, BLACK, (20, 14, 10, 8), 0, math.pi, 2)
        pygame.draw.line(self.image, WHITE, (23, 18), (23, 22), 2)
        pygame.draw.line(self.image, WHITE, (27, 18), (27, 22), 2)
        pygame.draw.polygon(self.image, (100, 150, 50), [(8, 5), (0, 0), (12, 10)])
        pygame.draw.polygon(self.image, (100, 150, 50), [(42, 5), (50, 0), (38, 10)])
        pygame.draw.line(self.image, (139, 69, 19), (45, 30), (55, 20), 5)

    def move_towards_player(self, player_x):
        if self.x < player_x:
            self.x += self.vel
        elif self.x > player_x:
            self.x -= self.vel
        if self.x < 10:
            self.x = 10
        if self.x > WIDTH - self.width - 10:
            self.x = WIDTH - self.width - 10

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        bar_width = 50
        health_width = bar_width * (self.health / self.max_health)
        pygame.draw.rect(win, ORANGE, (self.x, self.y - 12, bar_width, 6))
        pygame.draw.rect(win, PURPLE, (self.x, self.y - 12, health_width, 6))

    def hit(self, damage):
        self.health -= damage
        return self.health <= 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Bird:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 30)
        self.y = random.randint(50, 180)
        self.width = 30
        self.height = 20
        self.vel_x = random.choice([-2, -1.5, 1.5, 2])
        self.vel_y = random.choice([-1, 1])
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (100, 100, 100), (5, 5, 20, 12))
        pygame.draw.circle(self.image, (120, 120, 120), (22, 8), 7)
        pygame.draw.circle(self.image, BLACK, (24, 6), 2)
        pygame.draw.circle(self.image, WHITE, (23.5, 5.5), 1)
        pygame.draw.polygon(self.image, ORANGE, [(27, 7), (32, 8), (27, 9)])
        pygame.draw.ellipse(self.image, (80, 80, 80), (8, 2, 12, 8))

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.vel_x = -self.vel_x
        if self.y <= 30 or self.y >= 200:
            self.vel_y = -self.vel_y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
clock = pygame.time.Clock()
bg = create_desert_background(WIDTH, HEIGHT)
player_y = HEIGHT - 105
player = Player(WIDTH // 2 - 22, player_y)
goblin = Goblin(100, player_y)
birds = [Bird() for _ in range(4)]
bullets = []
shoot_cooldown = 0
SHOOT_DELAY = 12
score = 0
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

run = True
while run:
    clock.tick(60)
    if shoot_cooldown > 0:
        shoot_cooldown -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    player.move(keys)
    goblin.move_towards_player(player.x)
    for bird in birds:
        bird.move()
    if (keys[pygame.K_f] or keys[pygame.K_SPACE]) and shoot_cooldown == 0:
        bullets.append(Bullet(player.x + player.width // 2, player.y + player.height // 2, player.direction))
        shoot_cooldown = SHOOT_DELAY
    for bullet in bullets[:]:
        bullet.update()
        if bullet.x > WIDTH or bullet.x < 0:
            bullets.remove(bullet)
    for bullet in bullets[:]:
        if bullet.get_rect().colliderect(goblin.get_rect()):
            bullets.remove(bullet)
            if goblin.hit(bullet.damage):
                score += 20
                goblin = Goblin(random.randint(50, WIDTH - 100), player_y)
                goblin.health = 20
                goblin.max_health = 20
            break

    for bullet in bullets[:]:
        for bird in birds[:]:
            if bullet.get_rect().colliderect(bird.get_rect()):
                bullets.remove(bullet)
                birds.remove(bird)
                birds.append(Bird())
                score += 5
                break
    if player.get_rect().colliderect(goblin.get_rect()):
        if player.hit(10):
            run = False
        if player.x < goblin.x:
            goblin.x += 40
            player.x -= 20
        else:
            goblin.x -= 40
            player.x += 20
        player.x = max(0, min(player.x, WIDTH - player.width))
        goblin.x = max(10, min(goblin.x, WIDTH - goblin.width - 10))
    for bird in birds[:]:
        if player.get_rect().colliderect(bird.get_rect()):
            player.hit(2)
            birds.remove(bird)
            birds.append(Bird())
    win.blit(bg, (0, 0))
    player.draw(win)
    goblin.draw(win)
    for bird in birds:
        bird.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    score_text = font.render(f"SCORE: {score}", True, ORANGE)
    win.blit(score_text, (WIDTH // 2 - 60, 10))
    health_text = small_font.render(f"HP: {player.health}", True, WHITE)
    win.blit(health_text, (10, 10))
    goblin_health_text = small_font.render(f"Goblin HP: {goblin.health}", True, RED)
    win.blit(goblin_health_text, (WIDTH - 120, 10))
    controls_text = small_font.render("← → move | F/SPACE shoot", True, WHITE)
    win.blit(controls_text, (WIDTH // 2 - 110, HEIGHT - 25))

    pygame.display.update()

pygame.quit()