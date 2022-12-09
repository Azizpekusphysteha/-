import pygame.draw
import math

Grey = (155, 155, 155)
Yellow = (155, 155, 0)
WIDTH = 900
HEIGHT = 800
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rast = 50
SIZE = 50
AAA = 0
bullets = []
sbullets = []
TEXTURE1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

TEXTURE2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 7, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 6, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
A = 0
B = 0
a = TEXTURE2


class Gun:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 1
        self.f2_on = 0
        self.f1_on = 0
        self.an = 1
        self.color = (150, 150, 150)
        self.x = x
        self.y = y

    def move(self):
        dt = 2 / FPS
        self.x += self.vx * dt
        Rect.check_collision_for_bulletXXX(self)
        self.y += self.vy * dt
        Rect.check_collision_for_bulletYYY(self)

    def check_collision_for_bulletXXX(self):
        for i in range(len(Texture)):
            for j in range(len(Texture[i])):
                if Texture[i][j] == 1 or Texture[i][j] == 2 or Texture[i][j] == 6:
                    Rect = pygame.Rect(rast * j, rast * i, SIZE, SIZE)
                    bullet = pygame.Rect(self.x, self.y, self.a, self.a)
                    if Rect.colliderect(bullet):
                        print('попал')
                        if abs(self.y + self.a - (rast * i + SIZE / 2)) < abs(
                                self.x + self.a - (rast * j + SIZE / 2)):
                            print('выполнено')
                            if self.x < (rast * j):
                                self.x = rast * j - self.a - 1
                                self.vx *= -1
                            if self.x > (rast * j):
                                self.x = rast * j + SIZE + 1
                                self.vx *= -1

    def check_collision_for_bulletYYY(self):
        for i in range(len(Texture)):
            for j in range(len(Texture[i])):
                if Texture[i][j] == 1 or Texture[i][j] == 2 or Texture[i][j] == 6:
                    Rect = pygame.Rect(rast * j, rast * i, SIZE, SIZE)
                    bullet = pygame.Rect(self.x, self.y, self.a, self.a)
                    if Rect.colliderect(bullet):
                        print('попал')
                        if abs(self.y + self.a - (rast * i + SIZE / 2)) > abs(
                                self.x + self.a - (rast * j + SIZE / 2)):
                            if self.y < (rast * i):
                                self.y = rast * i - self.a - 1
                                self.vy *= -1
                            if self.y > (rast * i):
                                self.y = rast * i + SIZE + 1
                                self.vy *= -1

        def draw(self):
            pygame.draw.rect(screen, Yellow, (self.x, self.y, self.a, self.a))


class Sniper:
    def __init__(self, a, color, x, y, vx=0, vy=0, x2=0, y2=0, AAA=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = a
        self.color = color
        self.x2 = x2
        self.y2 = y2
        self.AAA = AAA

    def draw_walls(self):
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] == 1 or a[i][j] == 2 or a[i][j] == 6:
                    screen.blit(pygame.image.load('python sniper.jpg'), (rast * j, rast * i))
                if a[i][j] == 8:
                    screen.blit(pygame.image.load('портал питон.jpeg'), (rast * j, rast * i))

    def move_monster_to_sniper(self):
        cost = (self.x - self.x2) / ((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2) ** 1 / 2

        sint = (self.y - self.y2) / ((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2) ** 1 / 2
        self.x2 += self.AAA * cost * 90 / FPS
        self.y2 += self.AAA * sint * 90 / FPS
        for i in range(len((a))):
            for j in range(len((a)[i])):
                if (a)[i][j] == 5:
                    screen.blit(pygame.image.load('ключ 2.jpg'), (rast * j, rast * i))
                    Key = pygame.Rect(rast * j, rast * i, SIZE, SIZE)
                    sniper = pygame.Rect(self.x, self.y, self.a, self.a)
                    if Key.colliderect(sniper):
                        (a)[i][j] = 0
                        self.AAA = 50
                if (a)[i][j] == 7:
                    screen.blit(pygame.image.load('пистолет питон.jpg'), (rast * j, rast * i))
                    gun = pygame.Rect(rast * j, rast * i, SIZE, SIZE)
                    sniper = pygame.Rect(self.x, self.y, self.a, self.a)

    def open_door(self):
        if self.AAA == 50:
            for i in range(len(a)):
                for j in range(len((a)[i])):
                    if (a)[i][j] == 6:
                        if (self.x - j * rast) ** 2 + (self.y - i * rast) ** 2 < rast ** 2:
                            (a)[i][j] = 0

    def moveXXXright(self):
        dt = 1 / FPS
        Sniper.check_sniper_collisionXXX(self)
        self.x += self.vx * dt

    def moveXXXleft(self):
        dt = 1 / FPS
        Sniper.check_sniper_collisionXXX(self)
        self.x -= self.vx * dt

    def moveYYYUP(self):
        dt = 1 / FPS
        Sniper.check_sniper_collisionYYY(self)
        self.y -= self.vy * dt

    def moveYYYDOWN(self):
        dt = 1 / FPS
        Sniper.check_sniper_collisionYYY(self)
        self.y += self.vy * dt

    def check_sniper_collisionYYY(self):
        for i in range(len((a))):
            for j in range(len((a)[i])):
                if (a)[i][j] == 1 or (a)[i][j] == 2 or (a)[i][j] == 6:
                    Rect2 = pygame.Rect(rast * j, rast * i, SIZE, SIZE)
                    sniper = pygame.Rect(self.x, self.y, self.a, self.a)
                    if Rect2.colliderect(sniper):
                        if abs(self.y + self.a - (rast * i + SIZE / 2)) > abs(self.x + self.a - (rast * j + SIZE / 2)):
                            if self.y < (rast * i):
                                self.y = rast * i - self.a
                            if self.y > (rast * i):
                                self.y = rast * i + SIZE

    def check_sniper_collisionXXX(self):
        for i in range(len((a))):
            for j in range(len((a)[i])):
                if (a)[i][j] == 1 or (a)[i][j] == 2 or (a)[i][j] == 6:
                    Rect2 = pygame.Rect(rast * j, rast * i, SIZE, SIZE)
                    sniper = pygame.Rect(self.x, self.y, self.a, self.a)
                    if Rect2.colliderect(sniper):
                        if abs(self.y + self.a - (rast * i + SIZE / 2)) < abs(self.x + self.a - (rast * j + SIZE / 2)):
                            if self.x < (rast * j):
                                self.x = rast * j - self.a
                            if self.x > (rast * j):
                                self.x = rast * j + SIZE

    def check(self):
        sniper = pygame.Rect(self.x, self.y, self.a, self.a)
        monster = pygame.Rect(self.x2, self.y2, 50, 50)
        return sniper.colliderect(monster)

    def draw(self):
        pygame.draw.rect(screen, Yellow, (self.x, self.y, self.a, self.a))


def draw_monster(self):
    screen.blit(pygame.image.load('monster python.jpg'), (self.x2, self.y2))


def change_texture():
    if Sniper.portal():
        a.append(TEXTURE2)


finished = False
r = 8
# rects = [Rect(r, Yellow, 110, 102, 30, 30)]
x = 200
y = 50
score = 100
level = 1
gun = Gun(screen, x, y)
snipers = [Sniper(20, Yellow, 500, 90, 500, 500, x, y)]
while not finished:
    screen.fill((0, 0, 0))
    for sniper in snipers:
        sniper.draw_walls()

        if sniper.check() == True:
            finished = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                sniper.open_door()

        sniper.move_monster_to_sniper()

    key = pygame.key.get_pressed()
    for sniper in snipers:
        if key[pygame.K_RIGHT]:
            sniper.moveXXXright()
        if key[pygame.K_LEFT]:
            sniper.moveXXXleft()
        if key[pygame.K_UP]:
            sniper.moveYYYUP()
        if key[pygame.K_DOWN]:
            sniper.moveYYYDOWN()
        sniper.draw()

    pygame.display.update()
