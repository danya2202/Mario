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
    jumpCount = 12
    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.x += 5
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_SPACE]:
            self.isJump = True

        if self.isJump is True:
            if self.jumpCount >= -12:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) / 2
                
                
                elif sprite.collide_rect(mario, plat):
                    pass
                
                else:
                    self.rect.y -= (self.jumpCount ** 2) / 2

                self.jumpCount -= 2

            else:
                self.isJump = False
                self.jumpCount = 12     
        
        
        
class Enemy_1(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
        if self.rect.x <= 100: 
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'
        
class Tube(GameSprite):
    def update(self):
        None    

class Platform(GameSprite):
    def update(self):
        None    

 
        
background = scale(load('background.png'), (win_width, win_height))
mario = Mario(50, 50, 50, 380, 5, 'Mario.png')
trube = Tube(50, 50, 50, 380, 0, "tube.png")
monster = Enemy_1(50, 50, 150, 380, 5, "enemy.png")
platform1 = Platform(50, 50, 50, 300, 0, "platform.png")
platform2 = Platform(50, 50, 90, 300, 0, "platform.png")
platform3 = Platform(50, 50, 130, 300, 0, "platform.png")
platform4 = Platform(50, 50, 170, 300, 0, "platform.png")
platform5 = Platform(50, 50, 210, 300, 0, "platform.png")
platforms = sprite.Group()
platforms.add(platform1)
platforms.add(platform2)
platforms.add(platform3)
platforms.add(platform4)
platforms.add(platform5)

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
        
        for plat in platforms:
            plat.reset()
            
        if sprite.collide_rect(mario, monster):    
            finish = True
   
        
        
        
        
        
        trube.reset()
        trube.update()
        
        monster.reset()
        monster.update()

        mario.reset()
        mario.update()

    
      



    display.update()
    clock.tick(FPS)