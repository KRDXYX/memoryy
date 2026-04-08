from pygame import *
from random import randit
import time as to

window = display.set_mode((700, 500))
display.set_caption('galaxy')
clock.tick(FPS)
FPS = 60
rel_tine = False
sch = 0
pr = 0
background = transform.scale(image.load('galaxy.jpg'),(700,500))
font.init()
win = False

font = font.SysFont(None,40)
schet = font.render('Счёт:' + str(sch),True,(255,215,0))
propysk = miss_counter = font.render('Пропущено: ' + str(point_count), True, (255, 255, 255))
win_text = font2.render('YOU WIN!', True, (255, 255, 0))
lose_text = font2.render('YOU LOSE', True, (180, 0, 0))
res = 0
res_gl = 0
fir = font.render(str(res),True,(100,100,100))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    def fire(self)


class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(Player_image, player_x, player_y, player_speed)

def update(self):
    global miss_count
    self.rect.y += self.speed
    if self.rect.y > 500:
        self.rect.y = -65
        self.rect.x = randit(100, 500)
        self.speed = randit(1, 2)
        miss_count += 1

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_image),(15,20))
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()


class Asteroid(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_image), (20,20))
    def update(self):
        self.rect.y += self.speed







player = Player('rocket.png', 300, 435, 5)

monster1 = Enemy('ufo.png', randit(50, 650), 10, randit(1, 2))
monster2 = Enemy('ufo.png', randit(50, 650), 10, randit(1, 2))
monster3 = Enemy('ufo.png', randit(50, 550), 10, randit(1, 2))
monster4 = Enemy('ufo.png', randit(50, 650), 10, randit(1, 2))
monster5 = Enemy('ufo.png', randit(50, 650), 10, randit(1, 2))

monsters = sprite.Group()
monster.add(monster1)
monster.add(monster2)
monster.add(monster3)
monster.add(monster4)
monster.add(monster5)

bullets = sprite.Group()





font = font.Font(None, 35)
point_count = 0
miss_count = 0



    if finish == False
    sprite_list = sprite.spritecollide(makar, monsters, False)
    if sprite_list:
        finish = True









background = transform.scale(image.load('glaxy,jpg'), (800,600))
player = Player('rocket.png', 10,15,5)
Bullet = Bullet('bullet.png', 10, 10, 5)
asteroid = Asteroid('asteroid.png', 100, 100, 6)

monsters = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randit(80, 720), -60, randit(1,3))
    monsters.add(monster)

bullets = sprite.Group()
meteors = sprite.Group()
for i in range(2):
    met = Asteroid('asteroid.png', randit(80, 720),-40, randit(1,5))
    meteors.add(met)


font.init()
font1 = font.SysFont1(None, 40)
font2 = font.SysFont2(None, 100)


lost = 0
score = 0
num_fire = 0
rel_tine = False
last_time = 0

game = True
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    elif e.type == KEYDOWN
        if e.key == K_SPACE:
            if num_fire < 5 and rel_tine == False:
                num_fire += 1
            player.fire()
    if finish != True
        window.blit(background,(0,0))

win.blit(text_lose, (10, 60))
win.blit(text_win, (10, 60))
player.update()
monsters.update()
bullets.update()
meteors.update()

player.reset()
monsters.daew(window)
monster.reset()
bullets.draw(window)
asteroid.draw(window)
asteroid.reset()

if rel_tine == True:

    collides = sprite.groupcollide(monsters, bullets, True, True)
    for c in collides:
        score =_ 1
        new_monster = Enemy('ufo.png', randit(80, 720), -60, randit(1,3))
        monsters.add(new_monster)

        if sprite.spritecollide(player, monsters, False):
            finish = True
            window.blit(lose_text, (200, 200))

        if sprite.spritecollide(player, asteroid, False):
            finish = True
            window.blit(lose_text, (200, 200))

        if score >= 50:
            finish = True
            window.blit(lose_text, (200, 200))

        text_score = font1.render('Счёт: ' + str(score), 1, (125, 0, 214))
        window.blit(text_score, (10,10))

        text_lose = font1.render('Пропущено: ' +str(lost), 1, (0, 214, 182))
        window.bliy(text_lost, (10,50))

display.update()
clock.tick(FPS)




background = transform.scale(image.load('galaxy.jpg'), (700, 500))
