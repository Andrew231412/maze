from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_ymaze

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed

class Enemy(GameSprite):
    derection = 'left'
    def update(self, x1, x2):
        if self.rect.x <= x1:
            self.derection = 'right'
        if self.rect.x >= x2:
            self.derection = 'left'
        if self.derection == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
mixer.init()
font = font.Font(None, 90)

mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.3)
mixer.music.play()
# Муз сопровождение
kick = mixer.Sound('kick.ogg')
gold = mixer.Sound('money.ogg')
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
#задай фон сцены
background = transform.scale(image.load('back.jpg'), (700, 500))

player = Player('Walter_White.png', 30, 200, 4, 40, 55)
enemy = Enemy('Gustavo.png', 470, 380, 3, 45, 45)
treasure = GameSprite('met.jpg', 490, 430, 0, 60, 60)

w1 = Wall(200, 160, 150, 90, 50, 600, 10)
w2 = Wall(200, 160, 150, 680, 50, 10, 300)
w3 = Wall(200, 160, 150, 90, 130, 530, 10)
w4 = Wall(200, 160, 150, 90, 130, 10, 300)
w5 = Wall(200, 160, 150, 150, 200, 540, 10)
w6 = Wall(200, 160, 150, 90, 420, 100, 10)
w7 = Wall(200, 160, 150, 190, 290, 10, 140)
w8 = Wall(200, 160, 150, 190, 290, 50, 10)
w9 = Wall(200, 160, 150, 370, 200, 10, 100)

enemy_from_wall = Enemy('Gustavo.png', 240, 290, 2, 30, 30)
#обработай событие «клик по кнопке "Закрыть окно"»

clock = time.Clock()
FPS = 60
game = True
finish = False

win = font.render('You win', True, (255, 215, 0))
lose = font.render('You need to play better', True, (255, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        enemy.update(430, 570)
        enemy.reset()
        enemy_from_wall.update(240, 340)
        enemy_from_wall.reset()
        treasure.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
    
        if sprite.collide_rect(player, treasure):
            finish = True

            gold.play()
            window.blit(win, (230, 200))
        
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, enemy_from_wall) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9):
            finish = True

            kick.play()
            window.blit(lose, (0, 200))
        

    clock.tick(FPS)
    display.update()