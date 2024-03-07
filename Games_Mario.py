from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


pos_x = 400
pos_y = 400

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_width, player_height, player_x, player_y, player_speed, image):
        super().__init__()
        self.image = scale(load(image), (player_width, player_height))
        self.speed = player_speed
        self.width = player_width
        self.height = player_height
        
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Mario(GameSprite):
    isJump = False
    jumpCount = 10
    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.x += 5
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_SPACE]:
            self.isJump = True

        if self.isJump is True:
            if self.jumpCount >= -10:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) / 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) / 2

                self.jumpCount -= 1

            else:
                self.isJump = False
                self.jumpCount = 10     
        
        
        
class Enemy_1(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'
        
class Tube(GameSprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        super().__init__()   
        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
                 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))      

 
        
background = scale(load('background.png'), (win_width, win_height))
mario = Mario(50, 50, 50, 380, 5, 'Mario.png')


clock = time.Clock()
FPS = 60

Game = True
finish = False
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    keys = key.get_pressed()   

    if not finish:
        window.blit(background, (0, 0))

        



        mario.reset()
        mario.update()

    
      



    display.update()
    clock.tick(FPS)