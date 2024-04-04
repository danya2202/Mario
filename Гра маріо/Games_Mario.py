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
                
                else:
                    self.rect.y -= (self.jumpCount ** 2) / 2

                self.jumpCount -= 2

            else:
                self.isJump = False
                self.jumpCount = 12 
                
    def fire(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, 15, 20, 15, 'fire.png')
        bullets.add(bullet)                  
        
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

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed
        global lost
        if self.rect.y>win_width:
            self.rect.y=0
            self.rect.x=randint(0, win_width-80)
            lost = lost + 1
            print(lost)
    

class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill()
b1 = Bullet(50, 50, 15, 20, 1, 'fire.png' )           
    
   

bullets = sprite.Group()

monsters = sprite.Group()
for i in range(5):
    mon = Enemy(randint(0, win_width-80), 0, 80, 50, randint(1, 5), 'enemy.png')
    monsters.add(mon)
    
background = scale(load('background.png'), (win_width, win_height))
mario = Mario(50, 50, 80, 380, 4, 'Mario.png')
trube = Tube(50, 50, 50, 380, 0, "tube.png")

font.init()
font1 = font.SysFont('Arial', 36)

font2 = font.SysFont('Arial', 80)
txt_lose_game = font2.render('Ти програв!!!!', True, (255, 0, 0))
txt_win_game = font2.render('Ти виграв!!!!', True, (0, 255, 0))

clock = time.Clock()
FPS = 60
lost = 0
score = 0
Game = True
finish = False
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
        if e.type == KEYDOWN:
            if e.key == K_x:
               mario.fire()     
    keys = key.get_pressed()   

    if not finish:
        window.blit(background, (0, 0))
        
        txt_lose = font1.render(f'Пропущено: {lost}', True, (255,255,255))
        window.blit(txt_lose, (10, 50))
        
        txt_win = font1.render(f'Рахунок: {score}', True, (255,255,255))
        window.blit(txt_win, (10, 10))
        
        monsters.draw(window)
        monsters.update()    
            
        bullets.draw(window)
        bullets.update()            
            
        mario.reset()    
        mario.update()
        
        
        if sprite.spritecollide(mario, monsters, False):
            finish = True
            window.blit(txt_lose_game, (200, 200))
        
        
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            mon = Enemy(randint(0, win_width-80), 0, 80, 50, randint(1, 5), 'enemy.png')
            monsters.add(mon) 
            score = score + 1
            
        if score == 10:
            finish = True
            window.blit(txt_win_game, (200, 200))
    
    else:
        finish = False
        score = 0
        lost = 0
       
        for b in bullets:
            b.kill()
            
        for m in monsters:
            m.kill()
         
        time.delay(3000)
        for i in range(5):
            mon = Enemy(randint(0, win_width-80), 0, 80, 50, randint(1, 5), 'enemy.png')
            monsters.add(mon)



    display.update()
    clock.tick(FPS)