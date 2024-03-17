import pygame
import sys
import random
import time
import math

class Player(pygame.sprite.Sprite):#
    def __init__(self, image, y_lim = 200):#создание и определение его свойств
        self.y_lim = y_lim
        pygame.sprite.Sprite.__init__(self)#создание спрайта
        self.image = image #pygame.Surface((50, 50))#создать поверхность
        self.image.set_colorkey((0, 0, 0))
        #self.image.fill((255, 20, 50))#создать цвет
        self.rect = self.image.get_rect()#создать рамку для движения
        self.rect.center = (240, 288)#где появиться

    def update(self, image, x_dir, y_dir):#def=метод функция для движения
        self.rect.x = self.rect.x + 1*x_dir#двигаться вправо
        if self.rect.x > width + 10:#если вышел за пределы вернуться
            self.rect.x = 0
        if self.rect.x < 0:#если вышел за пределы вернуться
            self.rect.x = width
        self.rect.y = self.rect.y + 1*y_dir#двигаться вниз
        if self.rect.y > length - self.y_lim:#если вышел за пределы вернуться
            self.rect.y = length - self.y_lim
        if self.rect.y < 0:#если вышел за пределы вернуться
            self.rect.y = 0
        self.image = image
        self.image.set_colorkey((0, 0, 0))

pygame.init() # запуск движка
pygame.mixer.init()
length=640
width=1000
xdir = 0
ydir = 0
xdir2 = 0
ydir2 = 0
distance = 0
sigma_distance = 0
gigachad_score = 0
sigma_score = 0
text2 = ""
screen=pygame.display.set_mode((width,length))
clock=pygame.time.Clock()
background=pygame.image.load("background.png")
player_img = pygame.image.load("Player_1.png").convert()
player_img2 = pygame.image.load("Player_2.png").convert()
ball_img = pygame.image.load("ball.png").convert()
player=Player(player_img)
player2=Player(player_img2)
ball=Player(ball_img, y_lim=0)
sprites=pygame.sprite.Group()#создать группу спрайтов
sprites.add(player, player2, ball)#добавить его в группу
player.rect.y = 320
player.rect.x = 950
player2.rect.y = 320
player2.rect.x = 25
ball.rect.y = 320
ball.rect.x = 500
ball_x = random.randint(1,2)
ball_y = random.randint(1,2)
ball_y_speed = ball_y
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 100)
coeff = 1
if ball_x == 1:
    ball_x = -1
else:
    ball_x = 1
if ball_y == 1:
    ball_y = -1
else:
    ball_y = 1
while 1:
    clock.tick(288)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:  # если нажата клавиша
            moving = 0
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_DOWN:
                ydir = 1
            elif event.key == pygame.K_UP:
                ydir = -1
            if event.key == pygame.K_s:
                ydir2 = 1
            elif event.key == pygame.K_w:
                ydir2 = -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ydir = 0
            if event.key == pygame.K_DOWN:
                ydir = 0
            if event.key == pygame.K_s:
                ydir2 = 0
            if event.key == pygame.K_w:
                ydir2 = 0

    if ball.rect.y < 5 or ball.rect.y > 600:
        ball_y*=(-1)
    if ((abs(player.rect.centerx - ball.rect.centerx) < 20 and abs(player.rect.centery - ball.rect.centery) < 100) and ball_x > 0):
        coeff = abs(player.rect.centery - ball.rect.centery)/30
        ball_y *= (-1)
        ball_y_speed = ball_y * coeff
        ball_x *= (-1)
    if ((abs(player2.rect.centerx - ball.rect.centerx) < 20 and abs(player2.rect.centery - ball.rect.centery) < 100) and ball_x < 0):
        coeff = abs(player2.rect.centery - ball.rect.centery) / 30
        ball_y *= (-1)
        ball_y_speed = ball_y * coeff
        ball_x *= (-1)
    ball_y_speed = ball_y * coeff
    if ball.rect.x < 5:
        gigachad_score += 1
        ball.rect.y = 320 + 20*random.randint(-10, 10)
        ball.rect.x = 500 + 20*random.randint(-10, 10)
        ball_x = random.randint(-5, 5)
        if ball_x == 0:
            ball_x = 1
        coeff = 2*random.randint(-5, 5)
    elif ball.rect.x > 995:
        sigma_score += 1
        ball.rect.y = 320 + 20*random.randint(-10, 10)
        ball.rect.x = 500 + 20*random.randint(-10, 10)
        coeff = 2*random.randint(-5, 5)
        ball_x = random.randint(-5, 5)
        if ball_x == 0:
            ball_x = 1
    text = str(sigma_score) + " - " + str(gigachad_score)
    text_screen = font.render(text, True, (255, 255, 255))
    if sigma_score > 4:
        text2 = "BLUE WON"
        ball_x = 0
        ball_y = 0
        player.y_lim = 100000
        player2.y_lim = 100000
        ball.rect.y = 50000
        player.rect.x = 1000
        player2.rect.x = 1000
        text_screen2 = font2.render(text2, True, (0, 0, 255))
    elif gigachad_score > 4:
        text2 = "RED WON"
        ball_x = 0
        ball_y = 0
        ball.rect.y = 50000
        player.y_lim = 100000
        player2.y_lim = 100000
        player.rect.x = 1000
        player2.rect.x = 1000
        text_screen2 = font2.render(text2, True, (255, 0, 0))
    else:
        text_screen2 = font.render(text2, True, (255, 255, 255))
    player.update(player_img, xdir, ydir)
    player2.update(player_img2, xdir2, ydir2)
    ball.update(ball_img, ball_x, ball_y_speed)
    screen.blit(background, (0, 0))
    screen.blit(text_screen, (465, 10))
    screen.blit(text_screen2, (250, 250))
    sprites.draw(screen)
    pygame.display.flip()
pygame.quit()