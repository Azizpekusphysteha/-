import math
import pygame as pg
import pygame.display
from random import randint

WIDTH, HEIGHT = 1000, 700
FPS = 60
pg.init()
f_score = pg.font.Font(None, 36)
screen = pg.display.set_mode((WIDTH, HEIGHT))
x = 500
y = 300
p = 0
speed = 1
npc = []
npc1 = []
npc2 = []
teleportxy = []
bullets = []
sbullets = []
stalin_bullets = []
Wind = []
running = True
final = False
key1 = 1
key10 = 0
key2 = 1
key20 = 0
key3 = 1
key30 = 0
key4 = 1
key40 = 0
level = 0
size = 50
weapon = 1
stalin_shoot = 1
texX = [[], [], []]
texY = [[], [], []]
texture1 = [[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

texture0 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def draw_walls(texture):
    """
    рисует стены
    """
    for i in range(len(texture)):
        for j in range(len(texture[i])):
            if texture[i][j] == 1:
                if level == 1 or level == 3:
                    if (x - 5 - size * j) ** 2 + (y - 5 - size * i) ** 2 <= 40000:
                        screen.blit(pygame.image.load('iRR_GK-U1lma2Y5UBqXL5ux9UR4KR4BJ0Z2hHVIm0-bBrfN5Lr4Owz4utX7za9UnyEm124OFwNk5TtjyY-qB0lhN.jpg'), (size*j, size*i))
                else:
                    screen.blit(pygame.image.load('стена.jpg'), (size*j, size*i))
def check(x, y, texture):
    """
    проверяет, лежит ли точка внутри стены
    """
    zx = int(x/size)
    zy = int(y/size)
    try:
        if texture[zy][zx] == 1:
            return False
        elif texture[zy][zx] == 0:
            return True
    except IndexError:
        print(x, y, zx, zy)
        #raise IndexError

def check_for_wind(x, y, texture):
    sum = 0
    for i in range(int(x / 50), len(texture1[int(y / 50)])):
        sum += texture[int(y / 50)][i]
    if sum != 0:
        return False
    if sum == 0:
        return True

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
    def fire1(self):
        """
        так стреляют npc
        """
        new_ball = snaryad(self.x + 50, self.y, (255, 10, 10), 10)
        self.an = math.atan2((y - new_ball.y), (x - new_ball.x))
        new_ball.vx = math.cos(self.an)/2
        new_ball.vy = math.sin(self.an)/2
        stalin_bullets.append(new_ball)
        new_ball.draw(screen)

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        так стреляю я
        """
        new_ball = snaryad(self.x + 20, self.y + 20, (10, 120, 10), 5)
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = 2 * math.cos(self.an)
        new_ball.vy = 2 * math.sin(self.an)
        bullets.append(new_ball)
        self.f2_on = 0
        self.f2_power = 5



class snaryad:
    def __init__(self, x, y, color, r):
        self.x = x
        self.y = y
        self.radius = r
        self.color = color
        self.vx = 2
        self.vy = 2
    def draw(self, screen):
        """
        рисует снаряд
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def hit(self, obj):
        """
        проверяет, попал ли снаряд в некий объект
        """
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.radius + obj.radius)**2
    def flight1(self):
        """
        задаёт передвижение снарядов, отскакивающих от стен
        """
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.x += self.vx
            self.y += self.vy
        if not (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.vx *= -0.9
            self.y += self.vy
            self.x += self.vx
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and not (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.vy *= -0.9
            self.x += self.vx
            self.y += self.vy
        if self.x <= 5 or self.x >= WIDTH - 5:
            self.x -= self.vx
            self.vx *= -1
        if self.y <= 5 or self.y >= HEIGHT - 5:
            self.y -= self.vy
            self.vy *= -1

    def flight2(self, level):
        """
        задаёт передвижение снарядов, взрывающих стены
        """
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.x += self.vx
            self.y += self.vy
        if not check(self.x + self.vx, self.y, texture):
            zx = int((self.x + self.vx) // 50)
            zy = int(self.y // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if not check(self.x - self.vx, self.y, texture):
            zx = int((self.x - self.vx) // 50)
            zy = int(self.y // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if not check(self.x, self.y + self.vy, texture):
            zx = int(self.x // 50)
            zy = int((self.y + self.vy) // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if not check(self.x, self.y - self.vy, texture):
            zx = int(self.x // 50)
            zy = int((self.y - self.vy) // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if self.x <= 5 or self.x >= WIDTH - 5:
            sbullets.remove(self)
        if self.y <= 5 or self.y >= HEIGHT - 5:
            sbullets.remove(self)


class NPC:
    def __init__(self, x, y, v, level, pic, size, hp):
        self.x = x
        self.y = y
        self.v = v
        self.level = level
        self.pic = pic
        self.size = size
        self.rest = False
        self.x0 = x
        self.y0 = y
        self.X = [self.x0]
        self.Y = [self.y0]
        self.hp = hp
        self.hp0 = hp
    def traectory1(self, xmin, xmax):
        """
        задаёт первую траекторию движения нпс в спокойном состоянии
        """
        if not self.rest:
            self.x += self.v
            if self.x <= xmin or self.x >= xmax:
                self.v *= -1
    def draw(self, screen, level0):
        """
        прорисовывает нпс
        """
        if level == level0:
            screen.blit(pygame.image.load(self.pic), (self.x, self.y))
    def hit(self, obj):
        """
        проверяет, пересёкся ли нпс с другим обьектом (например, пулей)
        """
        return (self.x + self.size/2 - obj.x) ** 2 + (self.y + self.size/2 - obj.y) ** 2 <= (self.size/2)**2

    def npc_motion(self):
        """
        задаёт движение нпс с отклонением от стен
        """
        if self.x <= self.v or self.x >= WIDTH - self.size - 1:
            self.vx = 0
        if self.y <= self.v or self.y >= HEIGHT - self.size - 1:
            self.vy = 0
        elif (check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v, self.y + self.size, texture)) and (
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            if (self.vx)**2 >= (self.v/4)**2:
                self.x += self.vx
            else:
                self.vx = self.v/4
                self.x += self.vx
        elif not(check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v, self.y + self.size, texture)) and (
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            self.x -= self.v
        elif (check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v, self.y + self.size, texture)) and not(
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            self.x += self.v
        if (check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and (
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x, self.y + self.size + self.v, texture)):
            self.y += self.vy
        elif not(check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and (
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x, self.y + self.size + self.v, texture)):
            self.y += self.v
        elif (check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and not(
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x, self.y + self.size + self.v, texture)):
            self.y -= self.v
        self.Y += [self.y]   #сохраняем все ходы в массив, чтобы потом обратно идти
        self.X += [self.x]

    def monster_attack(self, x, y):
        """
        задаёт движение нпс при атаке
        """
        self.an = math.atan2((y - self.y), (x - self.x))
        self.vx = self.v * math.cos(self.an)
        self.vy = self.v * math.sin(self.an)
        self.npc_motion()
    def monster_come_back(self, l):
        """
        задаёт возвращение нпс обратно после прекращения атаки по обратному маршруту
        """
        if l > -1:
            self.x = self.X[l]
            self.y = self.Y[l]
        self.X.remove(self.X[l])
        self.Y.remove(self.Y[l])
    def contact(self):
        """
        проверяет, пересёкся ли персонаж с нпс (для персонажа я отдельного класса не сделал, потому что зачем?)
        """
        return ((self.x + self.size/2) - (x + 20)) ** 2 + ((self.y + self.size/2) - (y + 20)) ** 2 <= (self.size/2 + 20)**2

    def teleport(self, x, y):
        if pg.time.get_ticks() < (t2 + 500):
            pygame.draw.rect(screen, (100, 0, 0), (x, y, 50, 50))
        elif pg.time.get_ticks() < (t2 + 1000):
            pygame.draw.rect(screen, (150, 0, 0), (x, y, 50, 50))
        elif pg.time.get_ticks() < (t2 + 1500):
            pygame.draw.rect(screen, (200, 0, 0), (x, y, 50, 50))
        elif pg.time.get_ticks() < (t2 + 2000):
            pygame.draw.rect(screen, (250, 0, 0), (x, y, 50, 50))
        elif pg.time.get_ticks() < (t2 + 2500):
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
            self.x = x
            self.y = y
    def HP(self, x, y):
        k = 50/self.hp0
        pygame.draw.rect(screen, (0, 255, 0), (x, y - 10, self.hp * k, 10))
        pygame.draw.rect(screen, (255, 0, 0), (x + self.hp * k, y - 10, 50 - self.hp * k, 10))

class Winds:
    def __init__(self, r):
        self.r = r
    def move_winds(self):
        v = 4
        self.r += v
    def draw_winds(self):
        pygame.draw.circle(screen, (150, 150, 150), (WIDTH, HEIGHT/2), self.r, 10)

def buttons_shooting(keys, x, y):
    """
    стрельба с помощью клавиатуры
    """
    if keys[pygame.K_LEFT]:
        bullet1 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet1.vx *= -1
        bullet1.vy *= 0
        sbullets.append(bullet1)
    if keys[pygame.K_RIGHT]:
        bullet2 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet2.vx *= 1
        bullet2.vy *= 0
        sbullets.append(bullet2)
    if keys[pygame.K_DOWN]:
        bullet3 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet3.vx *= 0
        bullet3.vy *= 1
        sbullets.append(bullet3)
    if keys[pygame.K_UP]:
        bullet4 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet4.vx *= 0
        bullet4.vy *= -1
        sbullets.append(bullet4)


def walking(keys, x, y, speed):
    """
    перемещение персонажа
    """
    if keys[pygame.K_d] and check(x + 41, y, texture) and check(x + 41, y + 40, texture) and x < WIDTH - 42:
        x += speed
    if keys[pygame.K_a] and check(x - 1, y, texture) and check(x - 1, y + 40, texture) and x > 0:
        x -= speed
    if keys[pygame.K_w] and check(x, y - 1, texture) and check(x + 40, y - 1, texture) and y > 0:
        y -= speed
    if keys[pygame.K_s] and check(x, y + 41, texture) and check(x + 40, y + 41, texture) and y < HEIGHT - 42:
        y += speed
    return [x, y]

def shtryh(x, y):
    """
    создаёт штриховку на заднем фоне
    """
    for i in range(70):
        for j in range(20):
            #if ((x) - j*50) ** 2 + ((y) - i*20) ** 2 <= 14400:
            color = (0, 0, 0)
            pygame.draw.rect(screen, color, (j * 50, i * 20, 50, 20), 1)
def portal():
    global key10, key20, key30, key40, t, p
    pygame.draw.circle(screen, (60, 60, 60), (390, 240), 36)
    pygame.draw.circle(screen, (60, 60, 60), (390, 460), 36)
    pygame.draw.circle(screen, (60, 60, 60), (610, 240), 36)
    pygame.draw.circle(screen, (60, 60, 60), (610, 460), 36)
    pygame.draw.circle(screen, (120, 120, 120), (500, 350), 120)
    pygame.draw.circle(screen, (100, 100, 100), (500, 350), 100)
    pygame.draw.circle(screen, (80, 80, 80), (500, 350), 80)
    pygame.draw.circle(screen, (60, 60, 60), (500, 350), 60)
    pygame.draw.circle(screen, (40, 40, 40), (500, 350), 40)
    pygame.draw.circle(screen, (20, 20, 20), (500, 350), 20)
    if key10 and key20 and key30 and key40:
        if p <= 6:
            if p <= 1:
                pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
                p += 1/30
            elif p <= 2:
                pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
                pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
                p += 1/30
            elif p <= 3:
                pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
                pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
                pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
                p += 1/30
            elif p <= 4:
                pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
                pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
                pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
                pygame.draw.circle(screen, (0, 0, 60), (500, 350), 60)
                p += 1/30
            elif p <= 5:
                pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
                pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
                pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
                pygame.draw.circle(screen, (0, 0, 60), (500, 350), 60)
                pygame.draw.circle(screen, (0, 0, 40), (500, 350), 40)
                p += 1/30
            elif p <= 6:
                pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
                pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
                pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
                pygame.draw.circle(screen, (0, 0, 60), (500, 350), 60)
                pygame.draw.circle(screen, (0, 0, 40), (500, 350), 40)
                pygame.draw.circle(screen, (0, 0, 20), (500, 350), 20)
                p += 1 / 30
        if p > 6:
            pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
            pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
            pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
            pygame.draw.circle(screen, (0, 0, 60), (500, 350), 60)
            pygame.draw.circle(screen, (0, 0, 40), (500, 350), 40)
            pygame.draw.circle(screen, (255, 255, 255), (500, 350), 20)
    if key1:
        if (x - 610) ** 2 + (y - 460) ** 2 <= 56 ** 2:
            key10 = 1
        if key10:
            pygame.draw.circle(screen, (255, 255, 0), (610, 460), 20)
    if key2:
        if (x - 390) ** 2 + (y - 240) ** 2 <= 56 ** 2:
            key20 = 1
        if key20:
            pygame.draw.circle(screen, (0, 255, 0), (390, 240), 20)
    if key3:
        if (x - 390) ** 2 + (y - 460) ** 2 <= 56 ** 2:
            key30 = 1
        if key30:
            pygame.draw.circle(screen, (255, 255, 0), (390, 460), 20)
    if key4:
        if (x - 610) ** 2 + (y - 240) ** 2 <= 56 ** 2:
            key40 = 1
        if key40:
            pygame.draw.circle(screen, (0, 255, 0), (610, 240), 20)
def levels():
    global key1, key2, key3, key4
    if level == 0:
        lvl0()
    elif level == 1:
        texture[0][19] = 0
        texture[6][19] = 1
        lvl1()
        if not key1:
            screen.blit(pygame.image.load('old_key.png'), (WIDTH - 40, HEIGHT - 40))
        if x >= WIDTH - 60 and y >= HEIGHT - 60:
            key1 = 1
    elif level == 2:
        lvl0()
        if not key2:
            screen.blit(pygame.image.load('old_key.png'), (WIDTH / 2, HEIGHT / 2))
        if WIDTH / 2 + 40 >= x >= WIDTH / 2 - 50 and HEIGHT / 2 >= y >= HEIGHT / 2 - 50:
            key2 = 1
    elif level == 3:
        texture[0][19] = 1
        texture[6][19] = 0
        lvl1()
        if not key3:
            screen.blit(pygame.image.load('old_key.png'), (WIDTH - 70, HEIGHT / 2 - 40))
        if x >= WIDTH - 90 and HEIGHT / 2 >= y >= HEIGHT / 2 - 90:
            key3 = 1
    elif level == 4:
        lvl0()
        if not key4:
            screen.blit(pygame.image.load('old_key.png'), (WIDTH / 2, HEIGHT / 2))
        if WIDTH / 2 + 40 >= x >= WIDTH / 2 - 50 and HEIGHT / 2 >= y >= HEIGHT / 2 - 50:
            key4 = 1

def lvl1():
    screen.fill((0, 0, 0))
    screen.blit(screen, (0, 0))
    pygame.draw.circle(screen, (10, 10, 10), (x + 20, y + 20), 200)
    pygame.draw.circle(screen, (20, 20, 20), (x + 20, y + 20), 190)  # рисуем освещение вокруг
    pygame.draw.circle(screen, (30, 30, 30), (x + 20, y + 20), 180)
    pygame.draw.circle(screen, (40, 40, 40), (x + 20, y + 20), 170)
    shtryh(x, y)
    draw_walls(texture1)

def lvl0():
    screen.fill((0, 0, 50))
    screen.blit(screen, (0, 0))
    shtryh(x, y)
    draw_walls(texture0)
    portal()

breeze = True
Exit = pygame.image.load('дверь.png')
Exit1 = pygame.image.load('дверь.png')
Exx = WIDTH - 80
Exy = HEIGHT - 103
texture = texture0
attack = False
gun = Gun(screen, x, y)
t = 0
t1 = 0
t2 = 0
t3 = 0
score = 100
score2 = 0
stalin =NPC(WIDTH - 100, 50, 1, 1, 'Stalin.jpg', 50, 1)
ghost = NPC(WIDTH - 150, 100, 0.5, 1, 'Ghost.jpg', 50, 15)
stalin2 =NPC(WIDTH - 100, 50, 1, 2, 'Stalin.jpg', 50, 12)
wind1 = Winds(0)
Wind += [wind1]
npc_gun = Gun(screen, stalin.x, stalin.y)
npc += [ghost]
npc1 += [stalin]
npc2 += [stalin2]
l = 1
while True:
    if running:
        levels()
        gun.x = x
        gun.y = y
        if pg.time.get_ticks() > (t + 2000):
            t = pg.time.get_ticks()
            ghost = NPC(WIDTH - 150, 100, 0.5, 1, 'Ghost.jpg', 50, 15)
            npc.append(ghost)
        for ghost in npc:
            np = ghost
            if level == 1: #условие, чтобы призрак появлялся только на определённом уровне
                if (x - np.x)**2 + (y - np.y)**2 <= 1100**2:
                    np.monster_attack(x, y)
                if (x - np.x) ** 2 + (y - np.y) ** 2 <= 40000:
                    np.draw(screen, 1)
                    np.HP(np.x, np.y)
                if np.contact():   #условие, чтобы мы умирали при пересечении с призраком
                    np.X = []
                    np.Y = []
                    l = 1
                    running = False
                    final = True
                for bullet in bullets:          #убийство призрака
                    if np.hit(bullet):
                        np.hp -= 1
                        if np.hp == 0:
                            npc.remove(np)
        if stalin in npc1:
            np = stalin
            if level == 1:
                if (np.x - x) ** 2 + (np.y - y) ** 2 <= 40000:
                    np.draw(screen, 1)
                    if np.contact():
                        weapon = 2    #получили новое оружие
                        score2 += 15
                        npc1.remove(np) #при контакте мы его убираем
                        print(npc1)
                        stalin_shoot = 0 #чтобы не стрелял после исчезновения
                    if stalin_shoot:     #он будет в нас стрелять при приближении
                        if ((x + 20) - (stalin.x + stalin.size / 2)) ** 2 + ((y + 20) - (stalin.y + stalin.size / 2)) ** 2 <= 40000:
                            if pg.time.get_ticks() > (t1 + 3000): #стреляет раз в 3 секунды
                                t1 = pg.time.get_ticks()
                                npc_gun.fire1()
        for new_ball in stalin_bullets:
            if (new_ball.x - (x + 20)) ** 2 + (new_ball.y - (y + 20)) ** 2 <= 400: #мы погибаем при попадании его пули
                running = False
                final = True
        if stalin2 in npc2:
            if level == 2:
                if stalin2.contact():
                    running = False
                    final = True
                if pg.time.get_ticks() > (t2 + 2500):
                    teleportxy += [x - 5, y - 5]
                    if len(teleportxy) > 4:
                        teleportxy.remove(teleportxy[0])
                        teleportxy.remove(teleportxy[0])
                    t2 = pg.time.get_ticks()
                if pg.time.get_ticks() <= (t2 + 2500):
                    stalin2.teleport(teleportxy[2], teleportxy[3])
                    stalin2.x = teleportxy[0]
                    stalin2.y = teleportxy[1]
                stalin2.draw(screen, 2)
                stalin2.HP(stalin2.x, stalin2.y)
                for sbullet in sbullets:          #убийство призрака
                    if stalin2.hit(sbullet):
                        stalin2.hp -= 1
                        sbullets.remove(sbullet)
                        if stalin2.hp == 0:
                            npc2.remove(stalin2)
        screen.blit(pygame.image.load('11781957.png'), (x, y))
        if level == 3:
            for wind in Wind:
                if (t3 + 0) <= pg.time.get_ticks() <= (t3 + 1300):
                    wind.draw_winds()
                    wind.move_winds()
                    if (wind.r - 10)**2 <= (WIDTH - x - 20)**2 + (HEIGHT/2 - y - 20)**2 <= wind.r**2:
                        if check(x, y, texture) and check(x, y + 40, texture) and 0 < x and check_for_wind(x + 20, y + 20, texture):
                            an = math.atan2((y - 350), (x - 1000))
                            x += 4 * math.cos(an)
                            y += 4 * math.sin(an)
                            breeze = False
                        elif check_for_wind(x + 20, y + 20, texture):
                            pygame.draw.rect(screen, (150, 0, 0), (x, y, 40, 40))
                elif pg.time.get_ticks() > (t3 + 1300):
                    breeze = True
                    wind.r = 0
                    t3 = pg.time.get_ticks()
        if (x + 20 - Exx) ** 2 + (y + 20 - Exy) ** 2 <= 40000:
            screen.blit(Exit, (Exx, Exy))
        if level == 0:
            screen.blit(Exit, (Exx, Exy))
            screen.blit(Exit1, (50, 50))
            screen.blit(Exit1, (50, HEIGHT - 103))
            screen.blit(Exit, (WIDTH - 80, 50))
        screen.blit(f_score.render("Патронов: " + str(score), True, (200, 0, 0)), (0, 0))
        keys = pygame.key.get_pressed()
        if weapon == 2:
            screen.blit(f_score.render("Огн. шаров: " + str(score2), True, (200, 0, 0)), (0, 20))
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                if score2 > 0:
                    if pg.time.get_ticks() > (t + 400) and score > 0:
                        t = pg.time.get_ticks()
                        buttons_shooting(keys, x, y)
                        score2 -= 1      #чтобы у нового оружия было ограничение на патроны
        if breeze:
            walk = walking(keys, x, y, speed)
            x = walk[0]
            y = walk[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN: #стреляем при нажатии мышкой
                if score > 0:
                    gun.fire2_start()
                    gun.fire2_end(event)
                    score -= 1
        for bullet in bullets:
            if level == 1:
                if (x + 20 - bullet.x) ** 2 + (y + 20 - bullet.y) ** 2 <= 40000:
                    bullet.draw(screen)
            else:
                bullet.draw(screen)
            bullet.flight1()
            if pg.time.get_ticks() > (t + 1500):    #полёт и частота выстрелов обычных снарядов
                t = pg.time.get_ticks()
                bullets.pop(bullets.index(bullet))
        for new_ball in stalin_bullets:
            if (x + 20 - new_ball.x) ** 2 + (y + 20 - new_ball.y) ** 2 <= 40000:
                new_ball.draw(screen)
            new_ball.flight1()
            if pg.time.get_ticks() > (t + 1500):    #полёт и частота выстрелов снарядов, выпущенных нпс
                t = pg.time.get_ticks()
                stalin_bullets.pop(stalin_bullets.index(new_ball))
        for sbullet in sbullets:
            sbullet.draw(screen)            #полёт снарядов, взрывающих стены
            sbullet.flight2(level)



        if x >= WIDTH - 65 and y <= 50 and level == 1:  #Переход из 1 уровня в 0
            bullets = [] #убираем все летающие снаряды
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 80          #ставим выход в нужное место и нужную картинку на него
            Exy = HEIGHT -103
            texture = texture0          #задаём текстуру уровня
            x = 500
            y = 300          #координаты нашего появления
            level = 0
            speed = 1
            #ниже аналогично
        if x <= 65 and 197 >= y >= 147 and level == 2:  #Переход из 2 уровня в 0
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 80
            Exy = HEIGHT - 103
            texture = texture0
            x = 500
            y = 300
            level = 0
            teleportxy = []
        if x >= WIDTH - 65 and HEIGHT/2 >= y >= HEIGHT/2 - 50 and level == 3:  #Переход из 3 уровня в 0
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 80
            Exy = HEIGHT -103
            texture = texture0
            x = 500
            y = 300
            level = 0
        if x <= 65 and 197 >= y >= 147 and level == 4:  #Переход из 4 уровня в 0
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 80
            Exy = HEIGHT -103
            texture = texture0
            x = 500
            y = 300
            level = 0

        if x >= WIDTH - 105 and y >= HEIGHT - 103 and level == 0:
            bullets = []
            speed = 0.5
            Exit = pygame.image.load('exit_door.png')
            Exx = WIDTH - 30
            Exy = 0
            stalin_shoot = 1
            texture = texture1                  #Переход из 0 уровня в 1
            x = 0
            y = HEIGHT - 50
            level = 1
            if not npc1:
                npc1 += [stalin]
            for np in npc:
                np.X = [np.x0]
                np.Y = [np.y0]
            print(npc1)
        if x <= 65 and y <= 100 and level == 0: #переход из 0 уровня в 2
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = 50
            Exy = 150
            texture = texture0
            x = 60
            y = 60
            if not npc2:
                npc2 += [stalin2]
            teleportxy += [WIDTH - 100, 50, WIDTH - 100, 50]
            level = 2
        if x <= 65 and y >= HEIGHT - 103 and level == 0: #переход из 0 уровня в 3
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 30
            Exy = HEIGHT/2 - 50
            texture = texture1
            x = 50
            y = 50
            level = 3
        if x >= WIDTH - 100 and y <= 100 and level == 0: #переход из 0 уровня в 4
            bullets = []
            Exit = pygame.image.load('exit_door.png')
            Exx = 50
            Exy = 150
            texture = texture0
            x = 50
            y = 50
            level = 4
    if final:
        screen.fill((0, 0, 0))
        f1 = pygame.font.Font(None, 60)
        f2 = pygame.font.Font(None, 62)
        text1 = f1.render("СМЕРТЬ", True,
                          (255, 0, 0))                          #экран смерти
        text2 = f1.render("Перезапустить", True,
                          (255, 0, 0))
        screen.blit(text1, (200, 200))
        pygame.draw.rect(screen, (250, 250, 0), (150, 500, 305, 45))
        screen.blit(text2, (150, 500))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= event.pos[0] <= 455 and 500 <= event.pos[1] <= 545:   #возрождение при перезапуске
                    final = False
                    texture = texture0
                    for l in range(0, 3):  #чтобы всё, что мы при старой жизни разбомбили,вернулось назад
                        for i in range(0, len(texX[l])):
                            texture[texY[l][i]][texX[l][i]] = 1
                    score = 100
                    score2 = 0
                    level = 0
                    weapon = 1
                    x = 500
                    y = 300              #возвращаем все параметры к исходным
                    l = 1
                    Exx = WIDTH - 80
                    Exy = HEIGHT - 103
                    for np in npc:
                        np.X = [np.x0]
                        np.Y = [np.y0]
    running = True
    pygame.display.update()
