from pygame import *
from random import randint

win_width = 700
win_height = 700
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))

window.fill((200,255,255))
clock= time.Clock()
FPS=60
game = True
img_racket = 'ракетки.jpg'
#подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.Font(None, 80)
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 36)

class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update1(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_width - 80:
           self.rect.y += self.speed
    def update2(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

Player1 = Player(img_racket, 5, 300, 70, 100, 10)
Player2 = Player(img_racket, 645, 300, 70, 100, 10)
while game:
    clock.tick(FPS)
    display.update()
    for e in event.get():
        if e.type == QUIT:
            game=False
    window.fill((200,255,255))
    Player1.update1()
    Player1.reset()
    Player2.update2()
    Player2.reset()

