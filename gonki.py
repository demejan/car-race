import pygame, time
from random import randrange

pygame.init()
window = pygame.display.set_mode((500, 397))
clock = pygame.time.Clock()

fon = pygame.image.load('images/track.png')
car = pygame.image.load('images/porsh.png')
car2 = pygame.image.load('images/enemy.png')
fony = 0

class Enemy():
    def __init__(self):
        self.image = car2
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = -100
        self.speed = 3
        self.score = 0
        
    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= 397:
            self.rect.y = -100
            self.rect.x = randrange(155,310)
            self.score += 1

    def collision(self, a):
        if self.rect.colliderect(a.rect):
            crash()
        


class Player():
    def __init__(self):
        self.image = car
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 300
        self.speed = 4

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if self.rect.x <= 155:
            self.rect.x = 155

        if key[pygame.K_d]:
            self.rect.x += self.speed
        if self.rect.x >= 310:
            self.rect.x = 310

        if key[pygame.K_w]:
            self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.rect.y = 0

        if key[pygame.K_s]:
            self.rect.y += self.speed
        if self.rect.y >= 297:
            self.rect.y = 297

red = (255,0,0)
def crash():
    font = pygame.font.Font(None, 80)
    text = font.render('Авария', True, red)
    window.blit(text, (150,50))
    pygame.display.update()
    time.sleep(2)
    game()

def ochki(score):
    font = pygame.font.Font(None, 30)
    text = font.render('Score: '+str(score), True, red)
    window.blit(text, (10,10))
    pygame.display.update()

def win():
    font = pygame.font.Font(None, 80)
    text = font.render('Ты выиграл!', True, red)
    window.blit(text, (100,90))
    pygame.display.update()
    
def game():
    global fony
    player = Player()
    enemy = Enemy()

    while True:
        
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        player.update()
        enemy.update()

        enemy.collision(player)

        
        #отрисовка фона
        window.blit(fon, (0,fony))
        window.blit(fon, (0,fony-397))
        fony += 2
        if fony >= 397:
            fony = 0
        
        #отрисовка машины
        window.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
        window.blit(player.image, (player.rect.x, player.rect.y))

        ochki(enemy.score)

        #выйгрыш
        if enemy.score == 10:
            win()
            break

        pygame.display.update()
        clock.tick(128)



game()


