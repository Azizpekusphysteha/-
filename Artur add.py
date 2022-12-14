import random

import pygame.draw
import math
from random import randint
Grey = (155, 155, 155)
Yellow = (155, 155, 0)
RED = (255, 0, 0)
WIDTH = 1000
HEIGHT = 800
FPS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rast = 50
color = Yellow
SIZE = 50

TEXTURE2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],
            [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

TEXTURE3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 4, 4, 4, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 4, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
Q = 0
a = TEXTURE3
c=0
t = 0
x0 = 100
y0 = 200
class Winds:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_winds(self):
        v = 8
        self.x -= v

    def draw_winds(self):
        pygame.draw.rect(screen, Grey, (self.x, self.y, 2 * SIZE, 2 * SIZE))

    def wind_monster_attack(self, sniper):
        k = 5
        spisok = []

        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] == 2:
                    b = (sniper.x < rast * j) and (sniper.y > rast * i) and (
                                (sniper.y + (sniper.a) / 2) < (rast * i + SIZE))
                    spisok.append(b)
        if not any(spisok):
            sniper.x -= k
            if sniper.check_sniper_collisionXXX():
                sniper.color = RED


class Crazy_balls:
    def __init__(self, x, y, craziness=0):
        self.x = x
        self.y = y
        self.image = pygame.image.load('crazy ball green.jpg')
        self.image2 = pygame.image.load('crazy block.jpg')
        self.cr = craziness
    def move_crazy_ball(self, sniper):
        c = 300
        L = ((self.x - sniper.x) ** 2 + (self.y - sniper.y) ** 2) ** 1/2
        vx = c * ((self.x - sniper.x)/L)
        vy = c * ((self.y - sniper.y)/L)
        self.x -= vx
        self.y -= vy


    def draw_crazy_ball(self):
        screen.blit(self.image, (self.x, self.y))

    def check_collision_ball(self, sniper):
        HERO = pygame.Rect(sniper.x, sniper.y, SIZE, SIZE)
        BALL = pygame.Rect(self.x, self.y, 50, 50)
        if BALL.colliderect(HERO):
            self.x = 700
            self.y = 700
            self.cr = 1
        if self.cr == 1:

            for i in range(len(a)):
                for j in range(len(a[i])):
                    global t
                    if pygame.time.get_ticks() > t:
                        t = pygame.time.get_ticks() + 500

                        sniper.x += randint(-30, 30)
                        sniper.y += randint(-30, 30)
                    if (seconds % 3 > 0.2) and (seconds % 3 < 2):
                        if a[i][j] == 4:
                            a[i][j] = 3
                            screen.blit(self.image2, (rast * j, rast * i))
                        if a[i][j] == 3:
                            a[i][j] = 4






    def tablet(self, sniper):
        HERO = pygame.Rect(sniper.x, sniper.y, SIZE, SIZE)
        if self.cr == 1:
            global x0
            global y0
            if (x0==100) and (y0==200):
                x0 = randint(10, 40)
                y0 = randint(100, 150)
            screen.blit(pygame.image.load('tablet.jpg'), (x0, y0))
            tablet = pygame.Rect(x0, y0, SIZE, SIZE)
            if tablet.colliderect(HERO):
                self.cr = 0
                x0 = 100
                y0 = 200




class Sniper:
    def __init__(self, a, color, x, y, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = a
        self.color = color

    def draw_walls(self):
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 1 or a[i][j] == 2:
                    if a == TEXTURE2:
                        screen.blit(pygame.image.load('wind.jpg'), (rast * j, rast * i))
                    if a == TEXTURE3:
                        screen.blit(pygame.image.load('crazy block.jpg'), (rast * j, rast * i))
                if a[i][j] == 8:
                    screen.blit(pygame.image.load('портал питон.jpeg'), (rast * j, rast * i))




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
                        return True

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.a, self.a))


start_ticks = pygame.time.get_ticks()
finished = False
r = 8
winds = [Winds(600, 350), Winds(800, 550), Winds(900, 900)]
snipers = [Sniper(20, color, 50, 730, 40, 40)]
balls = [Crazy_balls(200, 200)]

while not finished:
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    screen.fill((0, 0, 0))
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000

    for sniper in snipers:
        sniper.draw_walls()
        sniper.check_sniper_collisionYYY()
        sniper.check_sniper_collisionXXX()
        if a == TEXTURE2:
            for wind in winds:

                if (seconds % 3 > 0.11) and (seconds % 3 < 0.71):
                    wind.wind_monster_attack(sniper)
                    wind.move_winds()
                    wind.draw_winds()
                if (seconds % 3 > 1) and (seconds % 3 < 2):
                    sniper.color = Yellow
                if not (seconds % 3 > 0.11) and (seconds % 3 < 0.71):
                    wind.x = 800
        if a == TEXTURE3:
            for ball in balls:
                ball.move_crazy_ball(sniper)
                ball.draw_crazy_ball()
                ball.check_collision_ball(sniper)
                ball.tablet(sniper)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

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