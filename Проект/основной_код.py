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
r = 35
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
key1 = 0
key10 = 0
key2 = 0
key20 = 0
key3 = 0
key30 = 0
key4 = 0
key40 = 0
level = 0
size = 50
weapon = 1
craziness = 0
stalin_shoot = 1
x0 = 100
y0 = 200
hP = 50
HP = 100
HP0 = 100
chto_to = 0
good = 0
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

texture3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

texture2 = [[1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]]

def draw_walls(texture):
    """
    рисует стены
    """
    for i in range(len(texture)):
        for j in range(len(texture[i])):
            if texture[i][j] == 1:
                if level == 1 or level == 3:
                    if (x - 5 - size * j) ** 2 + (y - 5 - size * i) ** 2 <= 40000:
                        screen.blit(pygame.image.load(
                            'iRR_GK-U1lma2Y5UBqXL5ux9UR4KR4BJ0Z2hHVIm0-bBrfN5Lr4Owz4utX7za9UnyEm124OFwNk5TtjyY-qB0lhN.jpg'),
                                    (size * j, size * i))
                elif level == 2:
                    if (x - 5 - size * j) ** 2 + (y - 5 - size * i) ** 2 <= 110**2:
                        screen.blit(pygame.image.load('crazy block.jpg'), (size * j, size * i))
                else:
                    screen.blit(pygame.image.load('crazy block.jpg'), (size * j, size * i))
                if craziness:
                    screen.blit(pygame.image.load('стена.jpg'), (size * j, size * i))


def check(x, y, texture):
    """
    проверяет, лежит ли точка внутри стены
    """
    zx = int(x / size)
    zy = int(y / size)
    try:
        if texture[zy][zx] == 1:
            return False
        elif texture[zy][zx] == 0:
            return True
    except IndexError:
        print(x, y, zx, zy)


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
        new_ball = snaryad(self.x + 50, self.y, (255, 10, 10), 10, 2)
        new_ball.t = pg.time.get_ticks()
        self.an = math.atan2((y - new_ball.y), (x - new_ball.x))
        new_ball.vx = math.cos(self.an) / 2
        new_ball.vy = math.sin(self.an) / 2
        stalin_bullets.append(new_ball)
        new_ball.draw(screen)

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        так стреляю я
        """
        new_ball = snaryad(self.x + 20, self.y + 20, (10, 120, 10), 5, 2)
        new_ball.t = pg.time.get_ticks()
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = 2 * math.cos(self.an)
        new_ball.vy = 2 * math.sin(self.an)
        bullets.append(new_ball)
        self.f2_on = 0
        self.f2_power = 5


class snaryad:
    def __init__(self, x, y, color, r, v):
        self.x = x
        self.y = y
        self.radius = r
        self.color = color
        self.vx = v
        self.vy = v
        self.t = 0
    def draw(self, screen):
        """
        рисует снаряд
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def hit(self, obj):
        """
        проверяет, попал ли снаряд в некий объект
        """
        return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.radius + obj.radius) ** 2

    def flight1(self):
        """
        задаёт передвижение снарядов, отскакивающих от стен
        """
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (
                check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.x += self.vx
            self.y += self.vy
        if not (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (
                check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.vx *= -0.9
            self.y += self.vy
            self.x += self.vx
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and not (
                check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
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
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (
                check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
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
    def __init__(self, x, y, v, level, pic, size, hp, craziness=0):
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
        self.image = pygame.image.load('crazy ball green.jpg')
        self.cr = craziness

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
        return (self.x + self.size / 2 - obj.x) ** 2 + (self.y + self.size / 2 - obj.y) ** 2 <= (self.size / 2) ** 2

    def npc_motion(self):
        """
        задаёт движение нпс с отклонением от стен
        """
        if self.x <= self.v or self.x >= WIDTH - self.size - 1:
            self.vx = 0
        if self.y <= self.v or self.y >= HEIGHT - self.size - 1:
            self.vy = 0
        elif (check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v,
                                                                            self.y + self.size, texture)) and (
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            if (self.vx) ** 2 >= (self.v / 4) ** 2:
                self.x += self.vx
            else:
                self.vx = self.v / 4
                self.x += self.vx
        elif not (check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v,
                                                                                self.y + self.size, texture)) and (
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            self.x -= self.v
        elif (check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v,
                                                                            self.y + self.size, texture)) and not (
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            self.x += self.v
        if (check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and (
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x,
                                                                                          self.y + self.size + self.v,
                                                                                          texture)):
            self.y += self.vy
        elif not (check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and (
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x,
                                                                                          self.y + self.size + self.v,
                                                                                          texture)):
            self.y += self.v
        elif (check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and not (
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x,
                                                                                          self.y + self.size + self.v,
                                                                                          texture)):
            self.y -= self.v
        self.Y += [self.y]  # сохраняем все ходы в массив, чтобы потом обратно идти
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
        return ((self.x + self.size / 2) - (x + 20)) ** 2 + ((self.y + self.size / 2) - (y + 20)) ** 2 <= (
                    self.size / 2 + 20) ** 2

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
        k = 50 / self.hp0
        pygame.draw.rect(screen, (0, 255, 0), (x, y - 10, self.hp * k, 10))
        pygame.draw.rect(screen, (255, 0, 0), (x + self.hp * k, y - 10, 50 - self.hp * k, 10))

    def draw_crazy_ball(self):
        screen.blit(self.image, (self.x, self.y))

    def check_collision_ball(self):
        global t4, x, y, craziness, speed, HP
        if self.contact():
            if not check(x + 20, y + 20, texture3):
                x += 50
                y += 50
            HP -= 25
            self.x = 600
            self.y = 300
            self.cr = 1
            craziness = 1
            speed = 3

    def tablet(self):
        if self.cr == 1:
            global x0, y0, craziness, speed
            if (x0 == 100) and (y0 == 200):
                x0 = randint(100, 900)
                y0 = randint(100, 600)
            screen.blit(pygame.image.load('tablet.jpg'), (x0, y0))
            if ((x + 20) - (x0 + 20)) ** 2 + ((y + 20) - (y0 + 20)) ** 2 <= 50 ** 2:
                self.cr = 0
                craziness = 0
                x0 = 100
                y0 = 200
                speed = 1


class Winds:
    def __init__(self, r):
        self.r = r

    def move_winds(self):
        v = 4
        self.r += v

    def draw_winds(self):
        pygame.draw.circle(screen, (150, 150, 150), (WIDTH, HEIGHT / 2), self.r, 10)


def buttons_shooting(keys, x, y):
    """
    стрельба с помощью клавиатуры
    """
    if keys[pygame.K_LEFT]:
        bullet1 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10, 2)
        bullet1.vx *= -1
        bullet1.vy *= 0
        sbullets.append(bullet1)
    if keys[pygame.K_RIGHT]:
        bullet2 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10, 2)
        bullet2.vx *= 1
        bullet2.vy *= 0
        sbullets.append(bullet2)
    if keys[pygame.K_DOWN]:
        bullet3 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10, 2)
        bullet3.vx *= 0
        bullet3.vy *= 1
        sbullets.append(bullet3)
    if keys[pygame.K_UP]:
        bullet4 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10, 2)
        bullet4.vx *= 0
        bullet4.vy *= -1
        sbullets.append(bullet4)


def walking(keys, x, y, speed):
    """
    перемещение персонажа
    """
    if keys[pygame.K_d] and check(x + 40 + speed, y, texture) and check(x + 40 + speed, y + 40, texture) and x < WIDTH - 40 - speed:
        x += speed
    if keys[pygame.K_a] and check(x - speed, y, texture) and check(x - speed, y + 40, texture) and x > speed:
        x -= speed
    if keys[pygame.K_w] and check(x, y - speed, texture) and check(x + 40, y - speed, texture) and y > speed:
        y -= speed
    if keys[pygame.K_s] and check(x, y + 40 + speed, texture) and check(x + 40, y + 40 + speed, texture) and y < HEIGHT - 41 - speed:
        y += speed
    return [x, y]


def shtryh():
    """
    создаёт штриховку на заднем фоне
    """
    for i in range(70):
        for j in range(20):
            color = (0, 0, 0)
            pygame.draw.rect(screen, color, (j * 50, i * 20, 50, 20), 1)


def portal():
    global key10, key20, key30, key40, t, p, kt, speed, running, final, good
    pygame.draw.circle(screen, (60, 60, 60), (390, 240), 36)
    pygame.draw.circle(screen, (40, 40, 40), (390, 240), 28)
    pygame.draw.circle(screen, (20, 20, 20), (390, 240), 20)
    pygame.draw.circle(screen, (60, 60, 60), (390, 460), 36)
    pygame.draw.circle(screen, (40, 40, 40), (390, 460), 28)
    pygame.draw.circle(screen, (20, 20, 20), (390, 460), 20)
    pygame.draw.circle(screen, (60, 60, 60), (610, 240), 36)
    pygame.draw.circle(screen, (40, 40, 40), (610, 240), 28)
    pygame.draw.circle(screen, (20, 20, 20), (610, 240), 20)
    pygame.draw.circle(screen, (60, 60, 60), (610, 460), 36)
    pygame.draw.circle(screen, (40, 40, 40), (610, 460), 28)
    pygame.draw.circle(screen, (20, 20, 20), (610, 460), 20)
    pygame.draw.circle(screen, (120, 120, 120), (500, 350), 120)
    pygame.draw.circle(screen, (100, 100, 100), (500, 350), 100)
    pygame.draw.circle(screen, (80, 80, 80), (500, 350), 80)
    pygame.draw.circle(screen, (60, 60, 60), (500, 350), 60)
    pygame.draw.circle(screen, (40, 40, 40), (500, 350), 40)
    pygame.draw.circle(screen, (20, 20, 20), (500, 350), 20)
    if key10 and key20 and key30 and key40:
        if p <= 1:
            pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
            p += 1 / 30
        elif p <= 2:
            pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
            pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
            p += 1 / 30
        elif p <= 3:
            pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
            pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
            pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
            p += 1 / 30
        elif p <= 4:
            pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
            pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
            pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
            pygame.draw.circle(screen, (0, 0, 60), (500, 350), 60)
            p += 1 / 30
        elif p <= 5:
            pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
            pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
            pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
            pygame.draw.circle(screen, (0, 0, 60), (500, 350), 60)
            pygame.draw.circle(screen, (0, 0, 40), (500, 350), 40)
            p += 1 / 30
        elif p <= 6:
            pygame.draw.circle(screen, (0, 0, 120), (500, 350), 120)
            pygame.draw.circle(screen, (0, 0, 100), (500, 350), 100)
            pygame.draw.circle(screen, (0, 0, 80), (500, 350), 80)
            pygame.draw.circle(screen, (0, 0, 60), (500, 350), 60)
            pygame.draw.circle(screen, (0, 0, 40), (500, 350), 40)
            pygame.draw.circle(screen, (0, 0, 20), (500, 350), 20)
            p += 1 / 30
    if key1:
        if (x - 610) ** 2 + (y - 460) ** 2 <= 56 ** 2:
            key10 = 1
        if key10:
            pygame.draw.circle(screen, (255, 0, 0), (610, 460), 20)
    if key2:
        if (x - 390) ** 2 + (y - 240) ** 2 <= 56 ** 2:
            key20 = 1
        if key20:
            pygame.draw.circle(screen, (255, 255, 0), (390, 240), 20)
    if key3:
        if (x - 390) ** 2 + (y - 460) ** 2 <= 56 ** 2:
            key30 = 1
        if key30:
            pygame.draw.circle(screen, (255, 0, 255), (390, 460), 20)
    if key4:
        if (x - 610) ** 2 + (y - 240) ** 2 <= 56 ** 2:
            key40 = 1
        if key40:
            pygame.draw.circle(screen, (0, 255, 0), (610, 240), 20)
    if 6 <= p <= 7:
        screen.blit(pygame.image.load('Портал.png'), (244, 94))
        key10 = 0
        key20 = 0
        key30 = 0
        key40 = 0
        if 530 >= x >= 470 and 380 >= y >= 320:
            running = False
            final = True
            good = 1

def levels():
    global key1, key2, key3, key4, texture
    if level == 0:
        lvl0()
        portal()
    elif level == 1:
        texture[0][19] = 0
        texture[6][19] = 1
        lvl1()
        if not key1:
            if (x - WIDTH + 60) ** 2 + (y - HEIGHT + 60) ** 2 <= 200 ** 2:
                screen.blit(pygame.image.load('old_key.png'), (WIDTH - 40, HEIGHT - 40))
        if x >= WIDTH - 60 and y >= HEIGHT - 60:
            key1 = 1
    elif level == 2:
        global chto_to
        screen.fill((0, 0, 0))
        screen.blit(screen, (0, 0))
        pygame.draw.circle(screen, (0, 0, 20), (x + 20, y + 20), 110)
        pygame.draw.circle(screen, (0, 0, 30), (x + 20, y + 20), 100)
        pygame.draw.circle(screen, (0, 0, 40), (x + 20, y + 20), 90)
        pygame.draw.circle(screen, (0, 0, 50), (x + 20, y + 20), 80)
        shtryh()
        texture = texture2
        draw_walls(texture2)
        if not key2:
            if not npc2 and chto_to < 1000:
                pygame.draw.circle(screen, (200, 200, 0), (920, 70), 30)
                screen.blit(pygame.image.load('old_key.png'), (900, 50))
                chto_to += 1
            if (x - 900) ** 2 + (y - 50) ** 2 <= 110 ** 2:
                screen.blit(pygame.image.load('old_key.png'), (900, 50))
        if 940 >= x >= 900 and 50 >= y >= 10:
            key2 = 1
    elif level == 3:
        texture[0][19] = 1
        texture[6][19] = 0
        lvl1()
        if not key3:
            if (x - WIDTH + 90) ** 2 + (y - HEIGHT / 2 + 60) ** 2 <=  200** 2:
                screen.blit(pygame.image.load('old_key.png'), (WIDTH - 70, HEIGHT / 2 - 40))
        if x >= WIDTH - 90 and HEIGHT / 2 >= y >= HEIGHT / 2 - 90:
            key3 = 1
    elif level == 4:
        if not craziness:
            screen.fill((0, 0, 50))
            screen.blit(screen, (0, 0))
            shtryh()
            texture = texture0
            draw_walls(texture0)
        else:
            screen.fill((0, 50, 150))
            screen.blit(screen, (0, 0))
            shtryh()
            texture = texture3
            draw_walls(texture3)
        for ball in balls:
            ball.monster_attack(x, y)
            ball.draw_crazy_ball()
            ball.check_collision_ball()
            ball.tablet()
        if not key4:
            if craziness:
                screen.blit(pygame.image.load('old_key.png'), (WIDTH - 100, HEIGHT - 100))
                if x >= WIDTH - 100 and y >= HEIGHT - 100:
                    key4 = 1


def lvl1():
    screen.fill((0, 0, 0))
    screen.blit(screen, (0, 0))
    pygame.draw.circle(screen, (10, 10, 10), (x + 20, y + 20), 200)
    pygame.draw.circle(screen, (20, 20, 20), (x + 20, y + 20), 190)  # рисуем освещение вокруг
    pygame.draw.circle(screen, (30, 30, 30), (x + 20, y + 20), 180)
    pygame.draw.circle(screen, (40, 40, 40), (x + 20, y + 20), 170)
    shtryh()
    draw_walls(texture1)


def lvl0():
    screen.fill((0, 0, 50))
    screen.blit(screen, (0, 0))
    shtryh()
    draw_walls(texture0)


def my_hp(x, y):
    k = 50 / HP0
    pygame.draw.rect(screen, (0, 255, 0), (x - 5, y - 10, HP * k, 10))
    pygame.draw.rect(screen, (255, 0, 0), (x - 5 + HP * k, y - 10, 50 - HP * k, 10))


breeze = True
Exit = pygame.image.load('exit_door.png')
Exit1 = pygame.image.load('exit_door_180.png')
Exx = WIDTH - 80
Exy = HEIGHT - 103
texture = texture0
attack = False
gun = Gun(screen, x, y)
ts = 0
tl = 0
tm = 0
t = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
score = 100
score2 = 0
stalin = NPC(WIDTH - 100, 50, 1, 1, 'эндермен.png', 50, 1)
stalin2 = NPC(WIDTH - 100, 50, 1, 2, 'эндермен.png', 50, 12)
balls = [NPC(200, 200, 1, 4, 'crazy ball green.jpg', 50, 1000)]
wind1 = Winds(0)
Wind += [wind1]
npc_gun = Gun(screen, stalin.x, stalin.y)
npc1 += [stalin]
npc2 += [stalin2]
l = 1
while True:
    if running:
        levels()
        gun.x = x
        gun.y = y
        if pg.time.get_ticks() > (t + 1300):
            t = pg.time.get_ticks()
            ghost = NPC(WIDTH - 150, 100, 1, 1, '50.png', 50, 45)
            npc.append(ghost)
        for np in npc:
            if level == 1:  # условие, чтобы призрак появлялся только на определённом уровне
                if (x - np.x) ** 2 + (y - np.y) ** 2 <= 1100 ** 2:
                    np.monster_attack(x, y)
                if (x - np.x) ** 2 + (y - np.y) ** 2 <= 40000:
                    np.draw(screen, 1)
                    np.HP(np.x, np.y)
                if np.contact():  # условие, чтобы мы умирали при пересечении с призраком
                    if pg.time.get_ticks() > (t + 100):
                        t = pg.time.get_ticks()
                        HP -= 4
                    if HP <= 0:
                        running = False
                        final = True
                if not np.contact():
                    if pg.time.get_ticks() > (tl + 500):
                        tl = pg.time.get_ticks()
                        HP += 1
                for bullet in bullets:  # убийство призрака
                    if np.hit(bullet):
                        np.hp -= 1
                        if np.hp == 0:
                            npc.remove(np)
        for np in npc1:
            if level == 1:
                if (np.x - x) ** 2 + (np.y - y) ** 2 <= 40000:
                    np.draw(screen, 1)
                    if np.contact():
                        weapon = 2  # получили новое оружие
                        score2 += 70
                        npc1.remove(np)  # при контакте мы его убираем
                        stalin_shoot = 0  # чтобы не стрелял после исчезновения
                    if stalin_shoot:  # он будет в нас стрелять при приближении
                        if ((x + 20) - (stalin.x + stalin.size / 2)) ** 2 + (
                                (y + 20) - (stalin.y + stalin.size / 2)) ** 2 <= 40000:
                            if pg.time.get_ticks() > (t1 + 1800):  # стреляет раз в 1.8 секунды
                                t1 = pg.time.get_ticks()
                                npc_gun.fire1()
        for new_ball in stalin_bullets:
            if (new_ball.x - (x + 20)) ** 2 + (new_ball.y - (y + 20)) ** 2 <= 400:  # мы погибаем при попадании его пули
                if pg.time.get_ticks() > (tm + 300):
                    tm = pg.time.get_ticks()
                    HP -= 50
                if HP <= 0:
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
                if (x + 20 - stalin2.x) ** 2 + (y + 20 - stalin2.y) ** 2 <= 135**2:
                    stalin2.draw(screen, 2)
                    stalin2.HP(stalin2.x, stalin2.y)
                for sbullet in sbullets:
                    if stalin2.hit(sbullet):
                        stalin2.hp -= 1
                        sbullets.remove(sbullet)
                        if stalin2.hp == 0:
                            npc2.remove(stalin2)
        if craziness == 1:
            pygame.draw.circle(screen, (0, 200, 0), (x + 20, y + 20), r, 6)
            pygame.draw.circle(screen, (0, 150, 0), (x + 20, y + 20), r-6, 6)
            pygame.draw.circle(screen, (0, 100, 0), (x + 20, y + 20), r-12, 6)
            if 35 <= r < 40:
                r += 1
            elif r == 40:
                r = 34
            elif 30 < r <= 34:
                r -= 1
            elif r == 30:
                r = 35
        screen.blit(pygame.image.load('40.png'), (x, y))
        if HP < 100:
            my_hp(x, y)
            if not craziness:
                if pg.time.get_ticks() > (t + 500):
                    HP += 2
                    t = pg.time.get_ticks()
        if HP <= 0:
            running = False
            final = True
        if level == 3:
            for wind in Wind:
                if t3 <= pg.time.get_ticks() <= (t3 + 1300):
                    wind.draw_winds()
                    wind.move_winds()
                    if (wind.r - 10) ** 2 <= (WIDTH - x - 20) ** 2 + (HEIGHT / 2 - y - 20) ** 2 <= wind.r ** 2:
                        if check(x, y, texture) and check(x, y + 40, texture) and 0 < x and check_for_wind(x + 20,
                                                                                                           y + 20,
                                                                                                           texture):
                            an = math.atan2((y - 350), (x - 1000))
                            x += 4 * math.cos(an)
                            y += 4 * math.sin(an)
                            breeze = False
                        elif check_for_wind(x + 20, y + 20, texture):
                            pygame.draw.rect(screen, (150, 0, 0), (x, y, 40, 40))
                            HP -= 10

                elif pg.time.get_ticks() > (t3 + 1300):
                    breeze = True
                    wind.r = 0
                    t3 = pg.time.get_ticks()
        if not craziness:
            if level == 1 or level == 3:
                if (x + 20 - Exx) ** 2 + (y + 20 - Exy) ** 2 <= 40000:
                    screen.blit(Exit, (Exx, Exy))
            elif level == 2:
                if (x + 20 - Exx) ** 2 + (y + 20 - Exy) ** 2 <= 110**2:
                    screen.blit(Exit, (Exx, Exy))
            else:
                screen.blit(Exit, (Exx, Exy))
        if level == 4:
            if craziness:
                if pg.time.get_ticks() > (t4 + 700):
                    HP -= 1
                    t4 = pg.time.get_ticks()
            else:
                if HP < 100:
                    if pg.time.get_ticks() > (t4 + 100):
                        HP += 1
                        t4 = pg.time.get_ticks()


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
                    if pg.time.get_ticks() > (ts + 400) and score > 0:
                        ts = pg.time.get_ticks()
                        buttons_shooting(keys, x, y)
                        score2 -= 1  # чтобы у нового оружия было ограничение на патроны
        if breeze:
            walk = walking(keys, x, y, speed)
            x = walk[0]
            y = walk[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:  # стреляем при нажатии мышкой
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
            if pg.time.get_ticks() > (bullet.t + 1200):  # полёт и частота выстрелов обычных снарядов
                bullets.pop(bullets.index(bullet))
        for new_ball in stalin_bullets:
            if (x + 20 - new_ball.x) ** 2 + (y + 20 - new_ball.y) ** 2 <= 40000:
                new_ball.draw(screen)
            new_ball.flight1()
            if pg.time.get_ticks() > (new_ball.t + 1200):  # полёт и частота выстрелов снарядов, выпущенных нпс
                stalin_bullets.pop(stalin_bullets.index(new_ball))
        for sbullet in sbullets:
            sbullet.draw(screen)  # полёт снарядов, взрывающих стены
            sbullet.flight2(level)
        if x >= WIDTH - 65 and y <= 50 and level == 1:  # Переход из 1 уровня в 0
            stalin_bullets = []  # убираем все летающие снаряды
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 80  # ставим выход в нужное место и нужную картинку на него
            Exy = HEIGHT - 103
            texture = texture0  # задаём текстуру уровня
            x = WIDTH - 150
            y = HEIGHT - 100 # координаты нашего появления
            level = 0
            speed = 2
            # ниже аналогично
        if 300 <= x <= 315 and 350 >= y >= 300 and level == 2:  # Переход из 2 уровня в 0
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 80
            Exy = HEIGHT - 103
            texture = texture0
            x = 100
            y = 55
            level = 0
            teleportxy = []
        if x >= WIDTH - 65 and HEIGHT / 2 >= y >= HEIGHT / 2 - 50 and level == 3:  # Переход из 3 уровня в 0
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 80
            Exy = HEIGHT - 103
            texture = texture0
            x = 500
            y = 300
            level = 0
        if not craziness:
            if x <= 65 and 197 >= y >= 147 and level == 4:  # Переход из 4 уровня в 0
                bullets = []
                Exit = pygame.image.load('exit_door_180.png')
                Exx = WIDTH - 80
                Exy = HEIGHT - 103
                texture = texture0
                x = WIDTH - 151
                y = 51
                level = 0

        if x >= WIDTH - 105 and y >= HEIGHT - 103 and level == 0:
            bullets = []
            speed = 0.5
            Exit = pygame.image.load('exit_door.png')
            Exx = WIDTH - 30
            Exy = 0
            stalin_shoot = 1
            texture = texture1  # Переход из 0 уровня в 1
            x = 0
            y = HEIGHT - 50
            level = 1
            if not npc1:
                npc1 += [stalin]
        if x <= 65 and y <= 100 and level == 0:  # переход из 0 уровня в 2
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = 300
            Exy = 300
            texture = texture0
            x = 60
            y = 60
            if not npc2:
                npc2 += [stalin2]
            teleportxy += [WIDTH - 100, 50, WIDTH - 100, 50]
            level = 2
        if x <= 65 and y >= HEIGHT - 103 and level == 0:  # переход из 0 уровня в 3
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH - 30
            Exy = HEIGHT / 2 - 50
            texture = texture1
            x = 50
            y = 50
            level = 3
        if x >= WIDTH - 100 and y <= 100 and level == 0:  # переход из 0 уровня в 4
            bullets = []
            Exit = pygame.image.load('exit_door.png')
            Exx = 50
            Exy = 150
            texture = texture0
            x = 50
            y = 50
            level = 4
    if final:
        if not good:
            screen.fill((0, 0, 0))
        else:
            screen.fill((255, 255, 255))
        f1 = pygame.font.Font(None, 60)
        f2 = pygame.font.Font(None, 62)
        text1 = f1.render("Вы умерли", True,
                          (255, 0, 0))
        text2 = f1.render("Вы выиграли!", True,
                          (255, 0, 0))
        if not good:
            screen.blit(text1, (400, 330))
        else:
            screen.blit(text2, (400, 330))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pygame.quit()
                break
    running = True
    pygame.display.update()
