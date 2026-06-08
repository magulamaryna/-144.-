import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Практична №18 - Уникни метеоритів!")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
ORANGE = (255, 150, 50)
YELLOW = (255, 255, 100)
CYAN = (0, 255, 255)
PURPLE = (150, 50, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
BROWN = (101, 67, 33)

def create_space_background(width, height):
    bg = pygame.Surface((width, height))
    for i in range(height):
        r = 5 + i // 40
        g = 3 + i // 50
        b = 20 + i // 25
        pygame.draw.line(bg, (r, g, b), (0, i), (width, i))

    for _ in range(200):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 2)
        brightness = random.randint(150, 255)
        pygame.draw.circle(bg, (brightness, brightness, brightness), (x, y), size)
    return bg

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 40
        self.speed = 6
        self.health = 100
        self.max_health = 100
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed

    def draw(self, win):
        points = [
            (self.x + self.width // 2, self.y),
            (self.x + self.width, self.y + self.height),
            (self.x, self.y + self.height)
        ]
        pygame.draw.polygon(win, CYAN, points)
        pygame.draw.polygon(win, BLUE, points, 2)
        pygame.draw.circle(win, WHITE, (self.x + self.width // 2, self.y + 10), 6)
        pygame.draw.rect(win, ORANGE, (self.x + self.width // 2 - 4, self.y + self.height - 8, 8, 8))
        bar_width = 50
        health_width = bar_width * (self.health / self.max_health)
        pygame.draw.rect(win, RED, (self.x + 5, self.y - 12, bar_width, 6))
        pygame.draw.rect(win, GREEN, (self.x + 5, self.y - 12, health_width, 6))

    def hit(self, damage):
        self.health -= damage
        return self.health <= 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Meteor:
    def __init__(self):
        self.size = random.randint(20, 45)
        self.width = self.size
        self.height = self.size
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(-150, -50)
        self.vel_y = random.randint(3, 10)
        self.vel_x = random.choice([-2, -1, 0, 1, 2])

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x < -50:
            self.x = -50
        if self.x > WIDTH - self.width + 50:
            self.x = WIDTH - self.width + 50

    def draw(self, win):
        pygame.draw.circle(win, GRAY, (self.x + self.width // 2, self.y + self.height // 2), self.width // 2)
        pygame.draw.circle(win, DARK_GRAY, (self.x + self.width // 2, self.y + self.height // 2), self.width // 2 - 2)
        for _ in range(3):
            cx = self.x + random.randint(5, self.width - 5)
            cy = self.y + random.randint(5, self.height - 5)
            pygame.draw.circle(win, BROWN, (cx, cy), random.randint(2, 5))
        for i in range(3):
            pygame.draw.circle(win, ORANGE, (self.x + self.width // 2, self.y + self.height + i * 3), 3 - i)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        return self.y > HEIGHT + 100

class StarBonus:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 15)
        self.y = random.randint(-100, -20)
        self.width = 15
        self.height = 15
        self.vel_y = random.randint(2, 5)

    def move(self):
        self.y += self.vel_y

    def draw(self, win):
        cx, cy = self.x + 7, self.y + 7
        pygame.draw.line(win, YELLOW, (cx, cy - 7), (cx, cy + 7), 2)
        pygame.draw.line(win, YELLOW, (cx - 7, cy), (cx + 7, cy), 2)
        pygame.draw.line(win, YELLOW, (cx - 5, cy - 5), (cx + 5, cy + 5), 2)
        pygame.draw.line(win, YELLOW, (cx + 5, cy - 5), (cx - 5, cy + 5), 2)
        pygame.draw.circle(win, YELLOW, (cx, cy), 3)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        return self.y > HEIGHT + 50

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 4
        self.vel_y = -12

    def draw(self, win):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(win, YELLOW, (int(self.x), int(self.y)), self.radius - 1)

    def update(self):
        self.y += self.vel_y

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

clock = pygame.time.Clock()
bg = create_space_background(WIDTH, HEIGHT)
player = Player(WIDTH // 2 - 17, HEIGHT - 80)
meteors = []
stars = []
bullets = []
meteor_spawn_timer = 0
star_spawn_timer = 0
shoot_cooldown = 0
score = 0
high_score = 0
game_over = False
font_big = pygame.font.Font(None, 48)
font_med = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

def reset_game():
    global player, meteors, stars, bullets, score, game_over, meteor_spawn_timer, star_spawn_timer
    player = Player(WIDTH // 2 - 17, HEIGHT - 80)
    meteors.clear()
    stars.clear()
    bullets.clear()
    score = 0
    game_over = False
    meteor_spawn_timer = 0
    star_spawn_timer = 0
run = True
while run:
    clock.tick(60)
    if shoot_cooldown > 0:
        shoot_cooldown -= 1
    if meteor_spawn_timer > 0:
        meteor_spawn_timer -= 1
    if star_spawn_timer > 0:
        star_spawn_timer -= 1
    if not game_over and meteor_spawn_timer == 0:
        meteors.append(Meteor())
        meteor_spawn_timer = random.randint(25, 45)
    if not game_over and star_spawn_timer == 0 and random.random() < 0.15:
        stars.append(StarBonus())
        star_spawn_timer = random.randint(80, 120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()
            if event.key == pygame.K_ESCAPE:
                run = False
    keys = pygame.key.get_pressed()
    if not game_over:
        player.move(keys)
        if (keys[pygame.K_f] or keys[pygame.K_SPACE]) and shoot_cooldown == 0:
            bullets.append(Bullet(player.x + player.width // 2, player.y))
            shoot_cooldown = 10
        for meteor in meteors[:]:
            meteor.move()
            if meteor.is_off_screen():
                meteors.remove(meteor)
        for star in stars[:]:
            star.move()
            if star.is_off_screen():
                stars.remove(star)
        for bullet in bullets[:]:
            bullet.update()
            if bullet.y < 0:
                bullets.remove(bullet)
        for bullet in bullets[:]:
            for meteor in meteors[:]:
                if bullet.get_rect().colliderect(meteor.get_rect()):
                    if bullet in bullets:
                        bullets.remove(bullet)
                    if meteor in meteors:
                        meteors.remove(meteor)
                        score += 10
                    break

        for meteor in meteors[:]:
            if player.get_rect().colliderect(meteor.get_rect()):
                if meteor in meteors:
                    meteors.remove(meteor)
                player.hit(15)
                if player.health <= 0:
                    game_over = True
                    if score > high_score:
                        high_score = score
                break

        for star in stars[:]:
            if player.get_rect().colliderect(star.get_rect()):
                if star in stars:
                    stars.remove(star)
                score += 5
                player.health = min(player.health + 10, player.max_health)
    win.blit(bg, (0, 0))
    for meteor in meteors:
        meteor.draw(win)
    for star in stars:
        star.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    player.draw(win)

    score_text = font_med.render(f"SCORE: {score}", True, WHITE)
    win.blit(score_text, (WIDTH // 2 - 60, 10))
    high_text = font_small.render(f"BEST: {high_score}", True, YELLOW)
    win.blit(high_text, (WIDTH // 2 - 40, 45))
    health_text = font_small.render(f"HP: {player.health}", True, GREEN)
    win.blit(health_text, (10, 10))
    meteor_text = font_small.render(f"METEORS: {len(meteors)}", True, ORANGE)
    win.blit(meteor_text, (10, 40))
    controls_text = font_small.render("←↑↓→ move | F/SPACE shoot", True, WHITE)
    win.blit(controls_text, (WIDTH // 2 - 120, HEIGHT - 25))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        win.blit(overlay, (0, 0))
        go_text = font_big.render("GAME OVER", True, RED)
        win.blit(go_text, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
        final_text = font_med.render(f"YOUR SCORE: {score}", True, WHITE)
        win.blit(final_text, (WIDTH // 2 - 100, HEIGHT // 2))
        restart_text = font_small.render("Press R to restart | ESC to quit", True, YELLOW)
        win.blit(restart_text, (WIDTH // 2 - 160, HEIGHT // 2 + 50))

    pygame.display.update()

pygame.quit()