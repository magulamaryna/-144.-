import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 480, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Практична №19 - Астероїди")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
ORANGE = (255, 150, 50)
YELLOW = (255, 255, 100)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (60, 60, 60)
BROWN = (101, 67, 33)

def create_space_background(width, height):
    bg = pygame.Surface((width, height))
    for i in range(height):
        r = 5 + i // 40
        g = 3 + i // 50
        b = 20 + i // 25
        pygame.draw.line(bg, (r, g, b), (0, i), (width, i))

    for _ in range(250):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 2)
        brightness = random.randint(150, 255)
        pygame.draw.circle(bg, (brightness, brightness, brightness), (x, y), size)

    for _ in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = random.choice([(100, 50, 150), (80, 40, 130), (120, 60, 170)])
        pygame.draw.circle(bg, color, (x, y), random.randint(20, 60))
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
        self.invincible = 0

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
        if self.invincible > 0 and (self.invincible // 3) % 2 == 0:
            pygame.draw.polygon(win, WHITE, points)
        else:
            pygame.draw.polygon(win, CYAN, points)
        pygame.draw.polygon(win, BLUE, points, 2)
        pygame.draw.circle(win, WHITE, (self.x + self.width // 2, self.y + 10), 6)
        pygame.draw.circle(win, YELLOW, (self.x + self.width // 2, self.y + 10), 3)
        if random.randint(0, 5) < 3:
            pygame.draw.rect(win, ORANGE, (self.x + self.width // 2 - 4, self.y + self.height - 8, 8, 8))
            pygame.draw.rect(win, YELLOW, (self.x + self.width // 2 - 2, self.y + self.height - 6, 4, 6))
        bar_width = 60
        health_width = bar_width * (self.health / self.max_health)
        pygame.draw.rect(win, RED, (self.x + 5, self.y - 15, bar_width, 8))
        pygame.draw.rect(win, GREEN, (self.x + 5, self.y - 15, health_width, 8))

    def hit(self, damage):
        if self.invincible == 0:
            self.health -= damage
            self.invincible = 30
            return self.health <= 0
        return False

    def update(self):
        if self.invincible > 0:
            self.invincible -= 1

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Asteroid:
    def __init__(self):
        size_variant = random.choice(['small', 'medium', 'large'])
        if size_variant == 'large':
            self.size = 50
            self.health = 3
            self.score_value = 20
        elif size_variant == 'medium':
            self.size = 35
            self.health = 2
            self.score_value = 10
        else:
            self.size = 20
            self.health = 1
            self.score_value = 5
        self.width = self.size
        self.height = self.size
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(-200, -50)
        self.vel_y = random.randint(2, 6)
        self.vel_x = random.choice([-2, -1, 0, 1, 2])
        self.angle = random.randint(0, 360)
        self.rot_speed = random.choice([-5, -4, -3, 3, 4, 5])
        self.points = self.create_asteroid_shape()

    def create_asteroid_shape(self):
        points = []
        num_points = random.randint(6, 10)
        for i in range(num_points):
            angle = (i / num_points) * 2 * math.pi
            radius = self.size // 2 + random.randint(-5, 5)
            x = self.size // 2 + radius * math.cos(angle)
            y = self.size // 2 + radius * math.sin(angle)
            points.append((x, y))
        return points

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.angle += self.rot_speed
        if self.x < -100:
            self.x = -100
            self.vel_x = -self.vel_x
        if self.x > WIDTH - self.width + 100:
            self.x = WIDTH - self.width + 100
            self.vel_x = -self.vel_x

    def draw(self, win):
        asteroid_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        rotated_points = []
        for point in self.points:
            rad = math.radians(self.angle)
            x = point[0] - self.size // 2
            y = point[1] - self.size // 2
            new_x = x * math.cos(rad) - y * math.sin(rad)
            new_y = x * math.sin(rad) + y * math.cos(rad)
            rotated_points.append((new_x + self.size // 2, new_y + self.size // 2))
        pygame.draw.polygon(asteroid_surf, GRAY, rotated_points)
        pygame.draw.polygon(asteroid_surf, DARK_GRAY, rotated_points, 2)

        for _ in range(self.health + 1):
            cx = random.randint(5, self.size - 5)
            cy = random.randint(5, self.size - 5)
            pygame.draw.circle(asteroid_surf, BROWN, (cx, cy), random.randint(2, 4))
        win.blit(asteroid_surf, (self.x, self.y))
        if self.health > 1:
            bar_width = self.size
            health_width = bar_width * (self.health / 3)
            pygame.draw.rect(win, RED, (self.x, self.y - 8, bar_width, 4))
            pygame.draw.rect(win, GREEN, (self.x, self.y - 8, health_width, 4))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def hit(self):
        self.health -= 1
        return self.health <= 0

    def is_off_screen(self):
        return self.y > HEIGHT + 100

class Bonus:
    def __init__(self, x, y, bonus_type):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.type = bonus_type  # 'health', 'score', 'shield'
        self.vel_y = 3
        if self.type == 'health':
            self.color = GREEN
        elif self.type == 'score':
            self.color = YELLOW
        else:
            self.color = CYAN

    def move(self):
        self.y += self.vel_y

    def draw(self, win):
        cx, cy = self.x + 7, self.y + 7
        pygame.draw.line(win, self.color, (cx, cy - 7), (cx, cy + 7), 2)
        pygame.draw.line(win, self.color, (cx - 7, cy), (cx + 7, cy), 2)
        pygame.draw.line(win, self.color, (cx - 5, cy - 5), (cx + 5, cy + 5), 2)
        pygame.draw.line(win, self.color, (cx + 5, cy - 5), (cx - 5, cy + 5), 2)
        pygame.draw.circle(win, self.color, (cx, cy), 3)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        return self.y > HEIGHT + 50

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 4
        self.vel_y = -14

    def draw(self, win):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(win, YELLOW, (int(self.x), int(self.y)), self.radius - 1)
        pygame.draw.circle(win, WHITE, (int(self.x), int(self.y)), self.radius - 2)

    def update(self):
        self.y += self.vel_y

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)

class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.max_radius = 25
        self.life = 10

    def update(self):
        self.life -= 1
        self.radius = self.max_radius * (1 - self.life / 10)
        return self.life > 0

    def draw(self, win):
        alpha = int(255 * (self.life / 10))
        colors = [(255, 100, 0), (255, 150, 0), (255, 200, 0)]
        for i, color in enumerate(colors):
            r = self.radius - i * 3
            if r > 0:
                pygame.draw.circle(win, color, (int(self.x), int(self.y)), r)
clock = pygame.time.Clock()
bg = create_space_background(WIDTH, HEIGHT)
player = Player(WIDTH // 2 - 17, HEIGHT - 80)
asteroids = []
bonuses = []
bullets = []
explosions = []
asteroid_spawn_timer = 0
bonus_spawn_timer = 0
shoot_cooldown = 0
score = 0
high_score = 0
game_over = False
font_big = pygame.font.Font(None, 48)
font_med = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

def reset_game():
    global player, asteroids, bonuses, bullets, explosions, score, game_over
    player = Player(WIDTH // 2 - 17, HEIGHT - 80)
    asteroids.clear()
    bonuses.clear()
    bullets.clear()
    explosions.clear()
    score = 0
    game_over = False
if high_score == 0:
    high_score = 0
run = True
while run:
    clock.tick(60)
    if shoot_cooldown > 0:
        shoot_cooldown -= 1
    if asteroid_spawn_timer > 0:
        asteroid_spawn_timer -= 1
    if bonus_spawn_timer > 0:
        bonus_spawn_timer -= 1
    if not game_over and asteroid_spawn_timer == 0:
        asteroids.append(Asteroid())
        asteroid_spawn_timer = random.randint(20, 40)
    if not game_over and bonus_spawn_timer == 0 and random.random() < 0.1:
        bonus_type = random.choice(['health', 'score', 'shield'])
        bonuses.append(Bonus(random.randint(0, WIDTH - 15), random.randint(-100, -20), bonus_type))
        bonus_spawn_timer = random.randint(150, 250)
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
        player.update()
        if (keys[pygame.K_f] or keys[pygame.K_SPACE]) and shoot_cooldown == 0:
            bullets.append(Bullet(player.x + player.width // 2, player.y))
            shoot_cooldown = 8
        for asteroid in asteroids[:]:
            asteroid.move()
            if asteroid.is_off_screen():
                asteroids.remove(asteroid)
        for bonus in bonuses[:]:
            bonus.move()
            if bonus.is_off_screen():
                bonuses.remove(bonus)
        for bullet in bullets[:]:
            bullet.update()
            if bullet.y < 0:
                bullets.remove(bullet)
        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                if bullet.get_rect().colliderect(asteroid.get_rect()):
                    if bullet in bullets:
                        bullets.remove(bullet)
                    explosions.append(Explosion(asteroid.x + asteroid.size // 2, asteroid.y + asteroid.size // 2))
                    if asteroid.hit():
                        asteroids.remove(asteroid)
                        score += asteroid.score_value
                        if score > high_score:
                            high_score = score
                        if random.random() < 0.3:
                            bonuses.append(Bonus(asteroid.x, asteroid.y, random.choice(['health', 'score'])))
                    break

        for asteroid in asteroids[:]:
            if player.get_rect().colliderect(asteroid.get_rect()):
                explosions.append(Explosion(asteroid.x + asteroid.size // 2, asteroid.y + asteroid.size // 2))
                asteroids.remove(asteroid)
                if player.hit(asteroid.health * 5):
                    game_over = True
                    if score > high_score:
                        high_score = score
                break

        for bonus in bonuses[:]:
            if player.get_rect().colliderect(bonus.get_rect()):
                bonuses.remove(bonus)
                if bonus.type == 'health':
                    player.health = min(player.health + 20, player.max_health)
                    score += 10
                elif bonus.type == 'score':
                    score += 50
                else:
                    player.invincible = 60
                    score += 15
        for explosion in explosions[:]:
            if not explosion.update():
                explosions.remove(explosion)
    win.blit(bg, (0, 0))
    for asteroid in asteroids:
        asteroid.draw(win)
    for bonus in bonuses:
        bonus.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for explosion in explosions:
        explosion.draw(win)
    player.draw(win)
    score_text = font_med.render(f"SCORE: {score}", True, WHITE)
    win.blit(score_text, (WIDTH // 2 - 70, 10))
    high_text = font_small.render(f"BEST: {high_score}", True, YELLOW)
    win.blit(high_text, (WIDTH // 2 - 50, 45))
    health_text = font_small.render(f"HP: {player.health}", True, GREEN)
    win.blit(health_text, (10, 10))
    asteroid_text = font_small.render(f"ASTEROIDS: {len(asteroids)}", True, ORANGE)
    win.blit(asteroid_text, (10, 40))
    controls_text = font_small.render("←↑↓→ move | F/SPACE shoot", True, WHITE)
    win.blit(controls_text, (WIDTH // 2 - 120, HEIGHT - 25))
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        win.blit(overlay, (0, 0))
        go_text = font_big.render("GAME OVER", True, RED)
        win.blit(go_text, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
        final_text = font_med.render(f"SCORE: {score}", True, WHITE)
        win.blit(final_text, (WIDTH // 2 - 60, HEIGHT // 2))
        restart_text = font_small.render("Press R to restart | ESC to quit", True, YELLOW)
        win.blit(restart_text, (WIDTH // 2 - 160, HEIGHT // 2 + 50))
    pygame.display.update()

pygame.quit()