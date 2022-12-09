import pygame.draw
Grey = (155, 155, 155)
Yellow = (155, 155, 0)
RED = (255, 0, 0)
WIDTH = 1000
HEIGHT = 800
FPS = 30
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
A = 0
B = 0
a = TEXTURE2


class Winds:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_winds(self):
        v = 8
        self.x -= v
    def draw_winds(self):
        pygame.draw.rect(screen, Grey, (self.x, self.y, 2*SIZE, 2*SIZE))
    def wind_monster_attack(self, sniper):
        k = 5
        spisok = []


        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] == 2:
                    b = (sniper.x < rast * j) and (sniper.y > rast*i) and ((sniper.y + (sniper.a)/2) < (rast*i + SIZE))
                    spisok.append(b)
        if not any(spisok):
            sniper.x -= k
            if sniper.check_sniper_collisionXXX():
                sniper.color = RED



class Sniper:
    def __init__(self, a, color, x, y, vx = 0, vy = 0):
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
                    else:
                        screen.blit(pygame.image.load('python sniper.jpg'), (rast * j, rast * i))
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
                if (a)[i][j] == 1 or (a)[i][j] == 2 or (a)[i][j] == 6 :
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
                if (a)[i][j] == 1 or (a)[i][j] == 2 or (a)[i][j] == 6 :
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

while not finished:
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    screen.fill((0, 0, 0))
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000

    for sniper in snipers:
        sniper.draw_walls()
        sniper.check_sniper_collisionYYY()
        sniper.check_sniper_collisionXXX()
        for wind in winds:

            if (seconds % 3 > 0.11) and (seconds % 3 < 0.71):
                wind.wind_monster_attack(sniper)
                wind.move_winds()
                wind.draw_winds()
            if (seconds % 3 > 1) and (seconds % 3 < 2):
                sniper.color = Yellow
            if not (seconds % 3 > 0.11) and (seconds % 3 < 0.71):
                wind.x = 800
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
