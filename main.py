### William Fung, wsf, TP1 Code

#https://www.pygame.org/docs/
import pygame, sys
import os
import random
import math
import string
import copy

pygame.mixer.pre_init(22050, -16, 2, 4096)
pygame.init()
pygame.mixer.init(22050, -16, 2, 4096)

size = gameWidth, gameHeight = 800,600
sideBarWidth = 200 #Sidebar

win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

timePassed = 0

pygame.display.set_caption("TouPou") #Change Later

#################################################
# Project Classes and Subclasses
#################################################

## Player classes ##
##Touhou
class Player(object):    
    def __init__(self, x, y, width, height):
        #positions
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.powerUpP = False
        self.powerUpB = False
        self.lives = 10
        self.hitbox = 0,0,0,0
        self.isDisabled = False

    def hit(self):
        self.lives -= 1
        
    def draw(self, win):
        win.blit(self.player, (self.x + self.width/2, self.y))
        
        #for debugging reasons
        hitboxWidth = self.width
        hitboxHeight = self.height
        self.hitbox = (self.x + hitboxWidth/2 + self.width/2, self.y +
         hitboxHeight/2,
        hitboxWidth, hitboxWidth)
        color = (0, 255, 0)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class ReimuP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #Load images here
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51905/
        pic = 'pictures/touhou player sprites/reimu_player.png'
        self.player = pygame.image.load(pic)
        self.vel = 10
        
    def draw(self, win):
        win.blit(self.player, (self.x + self.width/2, self.y))
        
        #for debugging reasons
        hitboxWidth = self.width/2
        hitboxHeight = self.height/2
        self.hitbox = (self.x + hitboxWidth/2 + self.width/2, self.y +
         hitboxHeight/2,
        hitboxWidth, hitboxWidth)
        color = (0, 255, 0)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class MarisaP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #Load images here
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/
        pic = 'pictures/touhou player sprites/marisa_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width/2),
         round(self.height/2)))
        self.vel = 10
    
    def draw(self, win):
        win.blit(self.player, (self.x + self.width/3, self.y + self.height/2))
        
        #for debugging reasons
        hitboxWidth = self.width/4
        hitboxHeight = self.height/4
        self.hitbox = (self.x + self.width/3 + hitboxWidth/2, 
        self.y + self.height/2 + hitboxHeight/2, hitboxWidth, hitboxHeight)
        color = (0, 255, 0)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class AliceP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #Load images here
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/
        pic = 'pictures/touhou player sprites/alice_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*1.5),
         round(self.height*1.5)))
        self.vel = 15
    
    def draw(self, win):
        win.blit(self.player, (self.x + self.width/2, self.y))
        
        #for debugging reasons
        hitboxWidth = self.width*.75
        hitboxHeight = self.height*.75
        self.hitbox = (self.x + hitboxWidth/2 + self.width/2, self.y +
         hitboxHeight/2,
        hitboxWidth, hitboxWidth)
        color = (0, 255, 0)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class AyaP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #Load images here
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/
        pic = 'pictures/touhou player sprites/aya_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*1.5),
         round(self.height*1.5)))
        self.vel = 10
    
    def draw(self, win):
        win.blit(self.player, (self.x + self.width/2, self.y))
        
        #for debugging reasons
        hitboxWidth = self.width*.75
        hitboxHeight = self.height*.75
        self.hitbox = (self.x + hitboxWidth/2 + self.width/2, self.y +
         hitboxHeight/2,
        hitboxWidth, hitboxWidth)
        color = (0, 255, 0)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class CirnoP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #Load images here
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/
        pic = 'pictures/touhou player sprites/cirno_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*1.5),
         round(self.height*1.5)))
        self.vel = 20
    
    def draw(self, win):
        win.blit(self.player, (self.x + self.width/2, self.y))
        
        #for debugging reasons
        hitboxWidth = self.width*.75
        hitboxHeight = self.height*.75
        self.hitbox = (self.x + hitboxWidth/2 + self.width/2, self.y +
         hitboxHeight/2,
        hitboxWidth, hitboxWidth)
        color = (0, 255, 0)
        #pygame.draw.rect(win, color, self.hitbox, 2)

##Pokemon
class CharizardP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = 'pictures/pokemon sprites/charizard_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*2),
         round(self.height*2)))
        self.vel = 10
        
class BlastoiseP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = 'pictures/pokemon sprites/blastoise_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*2),
         round(self.height*2)))
        self.vel = 10
        
class VenusaurP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = 'pictures/pokemon sprites/venusaur_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*2),
         round(self.height*2)))
        self.vel = 10
        self.angle = math.pi/8
        
class PikachuP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = 'pictures/pokemon sprites/pikachu_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*2),
         round(self.height*2)))
        self.vel = 20

class MewtwoP(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = 'pictures/pokemon sprites/mewtwo_player.png'
        player = pygame.image.load(pic)
        self.player = pygame.transform.scale(player, (round(self.width*2),
         round(self.height*2)))
        self.vel = 15

## Enemy classes ##
##Pokemon
class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = 0,0,0,0
        self.tempVelL = 0
        self.tempVelR = 0
        self.place = 0
        self.expTimer = 0
    
    def hit(self, pow):
        self.health -= pow
        
    def draw(self, win):
        win.blit(self.front, (self.x, self.y))
        self.move()
        color = (0,255,0)
        
        hitboxSize = self.size/2
        self.hitbox = (self.x + hitboxSize/2, self.y + hitboxSize/2,
        hitboxSize, hitboxSize)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
        #health bars
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], 
        self.hitbox[1] - 20, 50, 10))
        
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], 
        self.hitbox[1] - 20, self.health*50/self.totalHealth, 10))
        
    def move(self):
        if self.begin > self.end:
            self.x += self.velL
            if self.x < self.end:
                self.begin = self.end
                self.end = random.randint(self.width, 
                gameWidth - self.width - sideBarWidth)
        else:
            self.x += self.velR
            if self.x > self.end:
                self.begin = self.end
                self.end = random.randint(self.width, 
                gameWidth - self.width - sideBarWidth)

class CharizardE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = 2*width
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/pokemon sprites/charizard_enemy.png')
        self.front = pygame.transform.scale(pic,(self.size, self.size)) #self.front
        self.health = health
        self.totalHealth = health
        self.spaceBtwnFlames = 10
        self.angle = 2*math.pi/self.spaceBtwnFlames
        self.isRam = False
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -5
        self.velR = 5
        self.isFireSpin = True
        self.count = 0
    
    def attack(self):
        attack = random.choice([0,1,2,3])
        if attack == 0:
            self.flamethrowerMove()
        elif attack == 1:
            self.blastBurnMove()
        elif attack == 2:
            self.fireSpinMove()
        elif attack == 3:
            self.flareBlitzMove()
    
    def flamethrowerMove(self):
        numFlames = 3
        for flame in range(numFlames):
            flameX = math.sin(self.angle*(flame - 1))
            flameY = math.cos(self.angle*(flame - 1))
            pokeEProjs.append(flamethrower(enemy.x + self.width, enemy.y +
             self.height, flameX, flameY))
    
    def blastBurnMove(self):
        self.spaceBtwnFlames = 8
        numFlames = 8
        for flame in range(numFlames):
            flameX = math.sin(self.angle*(flame - 4))
            flameY = math.cos(self.angle*(flame - 4))
            pokeEProjs.append(blastBurn(enemy.x + self.width, enemy.y +
             self.height, flameX, flameY))
    
    def fireSpinMove(self):
        flameX = math.sin(self.count)
        flameY = 1
        self.count += 1
        pokeEProjs.append(blastBurn(enemy.x + self.width, enemy.y + self.height, flameX, flameY))
        self.isFireSpin = True
        
    def flareBlitzMove(self):
        self.isRam = True
        
    def move(self):
        if not self.isRam:
            if self.begin > self.end:
                self.x += self.velL
                if self.x < self.end:
                    self.begin = self.end
                    self.end = random.randint(self.width, 
                    gameWidth - self.width - sideBarWidth)
            else:
                self.x += self.velR
                if self.x > self.end:
                    self.begin = self.end
                    self.end = random.randint(self.width, 
                    gameWidth - self.width - sideBarWidth)
        if self.isRam:
            count = 0
            if self.y >= gameHeight:
                self.x %= gameWidth - sideBarWidth - 50
                self.y %= gameHeight
                self.isRam = False
            elif self.y <= self.size and count == 1:
                self.y = self.size
            else:
                self.y += 20
    
    def recoil(self):
        if self.isRam:
            self.health -= self.health*(.1)

class BlastoiseE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = 2*width
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/pokemon sprites/blastoise_enemy.png')
        self.front = pygame.transform.scale(pic,(self.size, self.size))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -5
        self.velR = 5
        self.isWaterGun = False
        self.isWaterBomb = False
        self.waterGunCount = 0
        self.waterBombCount = 0
        
    def attack(self):
        attack = random.choice([0, 1, 2])
        if attack == 0:
            self.waterGunMove()
        elif attack == 1:
            self.waterBombMove()
        else: pass
    
    def waterGunMove(self):
        waterX = 0
        waterY = 1
        pokeEProjs.append(waterGun(enemy.x - self.width/2, enemy.y +
            self.height, waterX, waterY))
        pokeEProjs.append(waterGun(enemy.x + self.width/2, enemy.y +
            self.height, waterX, waterY))
        self.isWaterGun = True
        self.waterGunCount += 1
    
    def waterBombMove(self, dirX = 0, dirY = 1, vel = 2, sizeX = 32, sizeY = 32):
        sizeX = 32
        sizeY = 32
        pokeEProjs.append(waterBomb(enemy.x, enemy.y + self.height, dirX, dirY, vel, sizeX, sizeY))
        self.isWaterBomb = True
        
    def waterBombMove2(self, x, y):
        balls = 8
        for i in range(balls):
            angle = 2*math.pi/balls*i
            dirX = math.cos(angle)
            dirY = math.sin(angle)
            size = 16
            vel = 3
            pokeEProjs.append(waterBomb(x, y, dirX, dirY, vel, size, size))
        self.isWaterBomb = False
        self.waterBombCount += 1

class VenusaurE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = 2*width
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/pokemon sprites/venusaur_enemy.png')
        self.front = pygame.transform.scale(pic,(self.size, self.size))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -5
        self.velR = 5
        self.isRazorLeaf = False
        self.count = 0
        
    def attack(self):
        attack = random.choice([0, 1, 2, 3, 4])
        if attack == 0 or attack == 1:
            self.razorLeafMove()
        elif attack == 2 or attack == 3:
            self.petalDanceMove()
        else:
            self.synthesisMove()
            
    def razorLeafMove(self):
        grassX = 0
        grassY = 1
        pokeEProjs.append(razorLeaf(enemy.x - self.width/2, enemy.y +
            self.height, grassX, grassY))
        pokeEProjs.append(razorLeaf(enemy.x + self.width/2, enemy.y +
            self.height - self.height, grassX, grassY))
        self.isRazorLeaf = True
        self.count += 1
    
    def petalDanceMove(self):
        num = 8
        angle = math.pi/4
        for i in range(num):
            grassX = math.cos(angle*i)
            grassY = math.sin(angle*i)
            pokeEProjs.append(petalDance(enemy.x, enemy.y, grassX, grassY))
    
    def synthesisMove(self):
        if self.health + self.totalHealth*.33 > self.totalHealth:
            self.health = self.totalHealth
        else:
            self.health += self.totalHealth*.33

class PikachuE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = 1.5*width
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/pokemon sprites/pikachu_enemy.png')
        self.front = pygame.transform.scale(pic,(round(self.size), round(self.size)))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -10
        self.velR = 10
        self.isThunder = False
        self.count = False
        
    def attack(self):
        attack = random.choice([0, 1, 2, 3, 4])
        if attack == 0 or attack == 1:
            self.thundershockMove()
        elif attack == 2 or attack == 3:
            self.electroballMove()
        elif attack == 4:
            self.thunderMove()
        
    def thundershockMove(self):
        shock = 3
        for i in range(shock):
            electX = random.randint(-100,100)/100
            electY = random.randint(-100,100)/100
            pokeEProjs.append(thundershock(enemy.x, enemy.y, electX, electY))
        
    def electroballMove(self):
        pokeEProjs.append(electroball(enemy.x, enemy.y, 0, 1))
        
    def thunderMove(self):
        size = 32
        y = enemy.y
        while y + size < gameHeight:
            y += size
            pokeEProjs.append(thunder(enemy.x, y, 0, 0))
        self.isThunder = True
        self.count += 1
        
class MewtwoE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = 1.5*width
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/pokemon sprites/mewtwo_enemy.png')
        self.front = pygame.transform.scale(pic,(round(self.size), round(self.size)))
        self.health = health
        self.totalHealth = health
        self.isTeleport = False
        self.isShadowBall = False
        self.sBCount = 0
        self.disableTimer = 0
        
    def attack(self):
        attack = random.choice([0, 0, 1, 2, 2, 3, 4])
        if attack == 0 or attack == 1:
            self.shadowBallMove()
        elif attack == 2 or attack == 3:
            self.shadowBallMove2()
        elif attack == 4:
            self.disableMove()
        
    def shadowBallMove(self):
        num = 8
        angle = math.pi/4
        for i in range(num):
            psyX = math.cos(angle*i + self.sBCount*num)
            psyY = math.sin(angle*i + self.sBCount*num)
            pokeEProjs.append(shadowBall(enemy.x, enemy.y, psyX, psyY))
        self.isShadowBall = True
        self.sBCount += 1
    
    def shadowBallMove2(self):
        angle = random.choice([0, math.pi/4, math.pi/2, -math.pi/4])
        num = 5
        for psy in range(num):
            psyX = math.sin(angle*(psy - 2))
            psyY = math.cos(angle*(psy - 2))
            pokeEProjs.append(shadowBall(enemy.x + self.width, enemy.y +
             self.height, psyX, psyY))
             
    def disableMove(self): #So that character cannot attack for 3 seconds
        player1.isDisabled = True
        if isTwoPlayer:
            player2.isDisabled = True
        
    def move(self):
        if self.isTeleport:
            self.x = random.randint(self.width, 
            gameWidth - self.width - sideBarWidth - 50)
            self.y = random.randint(self.height, gameHeight - self.height)
            self.isTeleport = False
## Touhou Enemies
class ReimuE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = 2*width
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/touhou enemy sprites/reimu_enemy.png')
        self.front = pygame.transform.scale(pic,(self.size, self.size))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -5
        self.velR = 5
        
    def attack(self):
        attack = random.choice([0, 1])
        if attack == 0:
            self.orbMove1()
        if attack == 1:
            self.orbMove2()
            
    def orbMove1(self):
        num = 16
        angle = math.pi/8
        for i in range(num):
            orbX = math.cos(angle*i)
            orbY = math.sin(angle*i)
            touEProjs.append(orb1(enemy.x, enemy.y, orbX, orbY))
    
    #accelerating bullets
    def orbMove2(self):
        num = 8
        angle = math.pi/4
        for i in range(num):
            orbX = math.cos(angle*i)
            orbY = math.sin(angle*i)
            touEProjs.append(orb2(enemy.x, enemy.y, orbX, orbY))
            
class MarisaE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = width/1.5
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/touhou enemy sprites/marisa_enemy.png')
        self.front = pygame.transform.scale(pic,(round(self.size), round(self.size)))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -5
        self.velR = 5
        self.isStar2 = False
        self.star2Count = 0
        
    def attack(self):
        attack = random.choice([0, 1])
        if attack == 0:
            self.starMove1()
        if attack == 1:
            self.starMove2()
    
    def starMove1(self):
        num = 16
        angle = math.pi/8
        for i in range(num):
            starX = math.cos(angle*i)
            starY = math.sin(angle*i)
            touEProjs.append(star1(enemy.x, enemy.y, starX, starY))
    
    #random scatter of bullets
    def starMove2(self):
        angle = math.pi/8
        for i in range(-1,2):
            x = random.randint(0,100)/100*angle
            starX = math.sin(x*i)
            starY = math.cos(x*i)
            touEProjs.append(star2(enemy.x, enemy.y, starX, starY))
        self.isStar2 = True
        self.star2Count += 1
    
class AliceE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = width/1.5
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/touhou enemy sprites/alice_enemy.png')
        self.front = pygame.transform.scale(pic,(round(self.size), round(self.size)))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -10
        self.velR = 10
        self.isSonic2 = False
        self.sonic2Count = 0
        
    def attack(self):
        attack = random.choice([0, 1])
        if attack == 0:
            self.sonicMove1()
        if attack == 1:
            self.sonicMove2()
    
    def sonicMove1(self):
        num = 16
        angle = math.pi/8
        for i in range(num):
            sonicX = math.cos(angle*i)
            sonicY = math.sin(angle*i)
            touEProjs.append(sonic1(enemy.x, enemy.y, sonicX, sonicY))
            
    def sonicMove2(self):
        angle = math.pi/4*self.sonic2Count
        sonicX = math.cos(angle)
        sonicY = math.sin(angle)
        touEProjs.append(sonic2(enemy.x, enemy.y, sonicX, sonicY))
        self.isSonic2 = True
        self.sonic2Count += 1

class AyaE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = width/1.5
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/touhou enemy sprites/aya_enemy.png')
        self.front = pygame.transform.scale(pic,(round(self.size), round(self.size)))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -5
        self.velR = 5
        
    def attack(self):
        attack = random.choice([0, 1])
        if attack == 0:
            self.windMove1()
        if attack == 1:
            self.windMove2()
    
    def windMove1(self):
        num = 16
        angle = math.pi/8
        for i in range(num):
            windX = math.cos(angle*i)
            windY = math.sin(angle*i)
            touEProjs.append(wind1(enemy.x, enemy.y, windX, windY))
    
    def windMove2(self):
        touEProjs.append(wind2(enemy.x, enemy.y, 0, 1))
            
class CirnoE(Enemy):
    #Load images here
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.size = width/1.5
        #pokemonmysterydungeonexplorersoftimedarkness/sheet/26252/?source=genre
        pic = pygame.image.load('pictures/touhou enemy sprites/cirno_enemy.png')
        self.front = pygame.transform.scale(pic,(round(self.size), round(self.size)))
        self.health = health
        self.totalHealth = health
        self.begin = self.x
        self.end = random.randint(self.width, gameWidth - self.width - sideBarWidth)
        self.velL = -10
        self.velR = 10
        self.disableTimer = 0
        
    def attack(self):
        attack = random.choice([0, 0, 0, 1, 1, 1, 2])
        if attack == 0:
            self.iceMove1()
        if attack == 1:
            self.iceMove2()
        if attack == 2:
            self.freezeMove()
    
    def iceMove1(self):
        num = 16
        angle = math.pi/8
        for i in range(num):
            iceX = math.cos(angle*i)
            iceY = math.sin(angle*i)
            touEProjs.append(ice1(enemy.x, enemy.y, iceX, iceY))
            
    def iceMove2(self):
        touEProjs.append(ice2(enemy.x, enemy.y, 0, 1))
            
    def freezeMove(self): #So that character cannot attack for 3 seconds
        player1.isDisabled = True
        if isTwoPlayer:
            player2.isDisabled = True

## Player Touhou Projectile classes ##
class bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, win):
        win.blit(self.bullet, (self.x + 1.5*self.width, self.y))

class yyorb(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51905/
        pic = 'pictures/projectiles/reimu_projectile.png'
        self.bullet = pygame.image.load(pic)
        self.width = 15
        self.height = 15
        self.vel = 20
    
    def draw(self, win):
        win.blit(self.bullet, (self.x + self.width, self.y))
        
class star(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51905/
        pic = 'pictures/projectiles/marisa_projectile.png'
        self.bullet = pygame.image.load(pic)
        self.width = 18
        self.height = 20
        self.vel = 20
    
    def draw(self, win):
        win.blit(self.bullet, (self.x, self.y))

class sonic(bullet):
    def __init__(self, x, y,):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51905/
        self.width = 28
        self.height = 28
        pic = 'pictures/projectiles/alice_projectile.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 30
    
    def draw(self, win):
        win.blit(self.bullet, (self.x, self.y))
        
class wind(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51905/
        self.width = 32
        self.height = 16
        pic = 'pictures/projectiles/aya_projectile.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 20
    
    def draw(self, win):
        win.blit(self.bullet, (self.x, self.y))

class ice(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51905/
        self.width = 24
        self.height = 48
        pic = 'pictures/projectiles/cirno_projectile.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 20
        
    def draw(self, win):
        win.blit(self.bullet, (self.x + self.width/3, self.y - self.height/2))

## Player Pokemon Projectile classes ##
class fire(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.width = 18
        self.height = 20
        pic = 'pictures/projectiles/blastBurn.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 20
        self.velX = 0
        
class water(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.width = 16
        self.height = 16
        pic = 'pictures/projectiles/waterBomb.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 20
        self.velX = 0
        
class leaf(bullet):
    def __init__(self, x, y, velX):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.width = 32
        self.height = 32
        pic = 'pictures/projectiles/razorLeaf2.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 30
        self.velX = velX*3
        
    def draw(self, win):
        win.blit(self.bullet, (self.x + self.width/2, self.y))

class electric(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.width = 16
        self.height = 32
        pic = 'pictures/projectiles/thundershock2.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 20
        self.velX = 0
    
    def draw(self, win):
        win.blit(self.bullet, (self.x + self.width/2, self.y))    
        
class thunder2(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.width = 32
        self.height = 32
        pic = 'pictures/projectiles/thunder.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 30
        self.velX = 0
        
    def draw(self, win):
        win.blit(self.bullet, (self.x + self.width/4, self.y)) 

class shadow(bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.width = 25
        self.height = 25
        pic = 'pictures/projectiles/shadowball.png'
        bullet = pygame.image.load(pic)
        self.bullet = pygame.transform.scale(bullet,(self.width, self.height))
        self.vel = 20
        self.velX = 0
    
    def draw(self, win):
        win.blit(self.bullet, (self.x + self.width/1.5, self.y))

## Enemy Pokemon Projectile classes ##
        
class flamethrower(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        pic = 'pictures/projectiles/flamethrower.png'
        self.flameTBullet = pygame.image.load(pic)
        self.size = 15 #size of png
        self.vel = 2
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
    
    def draw(self, win):
        win.blit(self.flameTBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSize = self.size/2
        self.hitbox = (self.x + hitboxSize, self.y + hitboxSize,
        hitboxSize, hitboxSize)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class blastBurn(bullet):
    def __init__(self, x, y, dirX, dirY,):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        pic = 'pictures/projectiles/blastBurn.png'
        self.bBurnBullet = pygame.image.load(pic)
        self.sizeX = 18
        self.sizeY = 20
        self.vel = 4
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
    
    def draw(self, win):
        win.blit(self.bBurnBullet, (self.x, self.y))
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class waterGun(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 8
        self.sizeY = 32
        pic = 'pictures/projectiles/waterGun.png'
        self.waterGBullet = pygame.image.load(pic)
        self.vel = 3
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0

    def draw(self, win):
        win.blit(self.waterGBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/3, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class waterBomb(bullet):
    def __init__(self, x, y, dirX, dirY, vel, sizeX, sizeY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = sizeX
        self.sizeY = sizeY
        pic = 'pictures/projectiles/waterBomb.png'
        waterBBullet = pygame.image.load(pic)
        self.waterBBullet = pygame.transform.scale(waterBBullet,(self.sizeX, self.sizeY))
        self.vel = vel
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        
    def draw(self, win):
        win.blit(self.waterBBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class razorLeaf(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/razorLeaf.png'
        razorLBullet = pygame.image.load(pic)
        self.razorLBullet = pygame.transform.scale(razorLBullet,(self.sizeX, self.sizeY))
        self.vel = 8
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        
    def draw(self, win):
        win.blit(self.razorLBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class petalDance(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/petalDance.png'
        petalDBullet = pygame.image.load(pic)
        self.petalDBullet = pygame.transform.scale(petalDBullet,(self.sizeX, self.sizeY))
        self.vel = 5
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        
    def draw(self, win):
        win.blit(self.petalDBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class thundershock(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 24
        self.sizeY = 24
        pic = 'pictures/projectiles/thundershock.png'
        thunderSBullet = pygame.image.load(pic)
        self.thunderSBullet = pygame.transform.scale(thunderSBullet,(self.sizeX, self.sizeY))
        self.vel = 15
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        
    def draw(self, win):
        win.blit(self.thunderSBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class electroball(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 24
        self.sizeY = 24
        pic = 'pictures/projectiles/electroball.png'
        eleBullet = pygame.image.load(pic)
        self.eleBullet = pygame.transform.scale(eleBullet,(self.sizeX, self.sizeY))
        self.vel = 20
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        
    def draw(self, win):
        win.blit(self.eleBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class thunder(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/thunder.png'
        thunderBullet = pygame.image.load(pic)
        self.thunderBullet = pygame.transform.scale(thunderBullet,(self.sizeX, self.sizeY))
        self.vel = 0
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        
    def draw(self, win):
        win.blit(self.thunderBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY
        self.hitbox = (self.x + hitboxSizeX/2, self.y,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class shadowBall(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/shadowBall.png'
        shadBullet = pygame.image.load(pic)
        self.shadBullet = pygame.transform.scale(shadBullet,(self.sizeX, self.sizeY))
        self.vel = 10
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        
    def draw(self, win):
        win.blit(self.shadBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY
        self.hitbox = (self.x + hitboxSizeX/2, self.y,
        hitboxSizeX, hitboxSizeY)
        # pygame.draw.rect(win, color, self.hitbox, 2)
        
class orb1(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 16
        self.sizeY = 16
        pic = 'pictures/projectiles/reimu_projectile.png'
        orbBullet = pygame.image.load(pic)
        self.orbBullet = pygame.transform.scale(orbBullet,(self.sizeX, self.sizeY))
        self.vel = 5
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.orbBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class orb2(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        self.sizeX = 16
        self.sizeY = 16
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        pic = 'pictures/projectiles/reimu_projectile2.png'
        orbBullet = pygame.image.load(pic)
        self.orbBullet = pygame.transform.scale(orbBullet,(self.sizeX, self.sizeY))
        self.dirX = dirX
        self.dirY = dirY
        self.vel = 2
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.orbBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class star1(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 18
        self.sizeY = 20
        pic = 'pictures/projectiles/marisa_projectile.png'
        starBullet = pygame.image.load(pic)
        self.starBullet = pygame.transform.scale(starBullet,(self.sizeX, self.sizeY))
        self.vel = 5
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.starBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class star2(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/marisa_projectile2.png'
        starBullet = pygame.image.load(pic)
        self.starBullet = pygame.transform.scale(starBullet,(self.sizeX, self.sizeY))
        self.vel = 10
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.starBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class sonic1(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/alice_projectile2.png'
        sonicBullet = pygame.image.load(pic)
        self.sonicBullet = pygame.transform.scale(sonicBullet,(self.sizeX, self.sizeY))
        self.vel = 10
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.sonicBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class sonic2(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/alice_projectile4.png'
        sonicBullet = pygame.image.load(pic)
        self.sonicBullet = pygame.transform.scale(sonicBullet,(self.sizeX, self.sizeY))
        self.vel = 10
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.sonicBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class wind1(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/aya_projectile2.png'
        windBullet = pygame.image.load(pic)
        self.windBullet = pygame.transform.scale(windBullet,(self.sizeX, self.sizeY))
        self.vel = 10
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.windBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)

class wind2(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 32
        self.sizeY = 32
        pic = 'pictures/projectiles/aya_projectile3.png'
        windBullet = pygame.image.load(pic)
        self.windBullet = pygame.transform.scale(windBullet,(self.sizeX, self.sizeY))
        self.vel = 20
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.windBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class ice1(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 24
        self.sizeY = 24
        pic = 'pictures/projectiles/cirno_projectile3.png'
        iceBullet = pygame.image.load(pic)
        self.iceBullet = pygame.transform.scale(iceBullet,(self.sizeX, self.sizeY))
        self.vel = 10
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.iceBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/2
        hitboxSizeY = self.sizeY/2
        self.hitbox = (self.x + hitboxSizeX/2, self.y + hitboxSizeY/2,
        hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)
        
class ice2(bullet):
    def __init__(self, x, y, dirX, dirY):
        super().__init__(x,y)
        #images
        #https://www.spriters-
        # resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/85692/
        self.sizeX = 50
        self.sizeY = 100
        pic = 'pictures/projectiles/cirno_projectile2.png'
        iceBullet = pygame.image.load(pic)
        self.iceBullet = pygame.transform.scale(iceBullet,(self.sizeX, self.sizeY))
        self.vel = 5
        self.dirX = dirX
        self.dirY = dirY
        self.hitbox = 0,0,0,0
        self.dx = 0
        
    def draw(self, win):
        win.blit(self.iceBullet, (self.x, self.y))
        
        color = (0,255,0)
        hitboxSizeX = self.sizeX/3
        hitboxSizeY = self.sizeY
        self.hitbox = (self.x + hitboxSizeX, self.y, hitboxSizeX, hitboxSizeY)
        #pygame.draw.rect(win, color, self.hitbox, 2)

### powerUp classes

class powerUpP(object):
    def __init__(self):
        self.size = 16
        self.x = random.randint(self.size, gameWidth - self.size - sideBarWidth)
        self.y = self.size
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51907/
        pic = pygame.image.load('pictures/projectiles/powerUpP.png')
        self.P = pygame.transform.scale(pic,(self.size, self.size))
        self.vel = 5
        self.hitbox = 0,0,0,0
        self.timer = 0
        self.visible = True
    
    def draw(self, win):
        win.blit(self.P, (self.x, self.y))
        
        color = (0,255,0)
        self.hitbox = (self.x, self.y, self.size, self.size)
        # pygame.draw.rect(win, color, self.hitbox, 2)
        
class powerUpB(object):
    def __init__(self):
        self.size = 16
        self.x = random.randint(self.size, gameWidth - self.size - sideBarWidth)
        self.y = self.size
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51907/
        pic = pygame.image.load('pictures/projectiles/powerUpB.png')
        self.P = pygame.transform.scale(pic,(self.size, self.size))
        self.vel = 5
        self.hitbox = 0,0,0,0
        self.timer = 0
        self.visible = True
    
    def draw(self, win):
        win.blit(self.P, (self.x, self.y))
        
        color = (0,255,0)
        self.hitbox = (self.x, self.y, self.size, self.size)

##
##
#### mainloop ####
##
##

## Pygame initialization
    
run = True

#Screens
isTitleScreen = True
pokemonHover = False
touhouHover = False
isTouhou = False
isPokemon = False

isGameplayScreen = False
isOnePlayer = False
isTwoPlayer = False

isCharacterTouhouScreen = False
isCharacterPokemonScreen = False
isSelectingAnother = False

isGameplay = False

isGameover = False
isLeaderboard = False


#Touhou backgrounds
#https://www.spriters-resource.com/pc_computer/T.html
pic = pygame.image.load('pictures/Backgrounds/bg1.png')
bg1 = pygame.transform.scale(pic,(gameWidth - sideBarWidth, gameHeight))
#https://www.spriters-resource.com/pc_computer/T.html
pic = pygame.image.load('pictures/Backgrounds/bg2.png')
bg2 = pygame.transform.scale(pic,(gameWidth - sideBarWidth, gameHeight))
touhouBackground = random.choice([bg1, bg2])

Mixer = pygame.mixer
musicCount = 0




def playTitleMusic():
    global musicCount
    Mixer.music.stop()
    Mixer.music.load('music/titleScreen.mp3')
    #https://www.youtube.com/watch?v=k-7dlQl3rwI 
    Mixer.music.play(-1) #Plays title theme
    musicCount += 1

def playMusic():
    global musicCount
    if isTouhou:
        track1 = 'music/Another Border of Life.mp3'
        track2 = "music/Reimu's Theme.mp3"
        touhouTrack = random.choice([track1, track2])
        Mixer.music.stop()
        Mixer.music.load(touhouTrack)
        Mixer.music.play(-1)
        #https://www.youtube.com/watch?v=95YQQrqkX3k&t=83s
        #https://www.youtube.com/watch?v=bBde0Kz-Bcc
        musicCount += 1
    elif isPokemon:
        track3 = 'music/Dialgas Fight to the Finish.mp3'
        track4 = 'music/Trainer Battle.mp3'
        pokemonTrack = random.choice([track3, track4])
        Mixer.music.stop()
        Mixer.music.load(pokemonTrack)
        Mixer.music.play(-1)
        #https://www.youtube.com/watch?v=nxS8YDjTpeg
        #https://www.youtube.com/watch?v=xQzsFzmT4W0
        musicCount += 1

def playGOMusic():
    global musicCount
    Mixer.music.stop()
    Mixer.music.load('music/Game Over.mp3')
    #https://www.youtube.com/watch?v=CV-yd-GWCXM
    Mixer.music.play(-1) 
    musicCount += 1

#Sounds
explosionSound = Mixer.Sound('music/explosion.wav')
expTimer = 0
isExploding = False

def explosion(enemy):
    explosionSound.play()
    pic = pygame.image.load('pictures/projectiles/explosion3.png')
    #http://pngimg.com/imgs/weapons/explosion/
    enemy.front = pygame.transform.scale(pic,(round(enemy.size), round(enemy.size)))
    

#Pokemon backgrounds
#https://www.spriters-resource.com/pc_computer/T.html
pic = pygame.image.load('pictures/Backgrounds/bg3.png')
bg3 = pygame.transform.scale(pic,(gameWidth - sideBarWidth, gameHeight))
#https://www.spriters-resource.com/pc_computer/T.html
pic = pygame.image.load('pictures/Backgrounds/bg4.png')
bg4 = pygame.transform.scale(pic,(gameWidth - sideBarWidth, gameHeight))
pokemonBackground = random.choice([bg3, bg4])

#read and write file function from:
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "a+") as f:
        f.write(contents)

def eraseFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

isInserting = False

def appendScore():
    nameScore = input + ' : ' + str(score) + '\n'
    if isTouhou:
        if isOnePlayer:
            writeFile('touhou_high_scores1.txt', nameScore)
            scores = readFile('touhou_high_scores1.txt')
        elif isTwoPlayer:
            writeFile('touhou_high_scores2.txt', nameScore)
            scores = readFile('touhou_high_scores2.txt')
    elif isPokemon:
        if isOnePlayer:
            writeFile('pokemon_high_scores1.txt', nameScore)
            scores = readFile('pokemon_high_scores1.txt')
        elif isTwoPlayer:
            writeFile('pokemon_high_scores2.txt', nameScore)
            scores = readFile('pokemon_high_scores2.txt')
    reorganize(scores)
    return

def reorganize(file):
    # print(file)
    nameScores = []
    scores = []
    for line in file.split('\n'):
        temp = []
        for word in line.split(' : '):
            if word.isalpha():
                temp.append(word)
            elif word.isdigit():
                temp.append(word)
                scores.append(int(word))
        nameScores.append(tuple(temp))
    # print(nameScores)
    nameScores = nameScores[:-1]
    scores.sort()
    scores = scores[::-1]
    newContents = ''
    for num in scores:
        for tup in nameScores:
            name = tup[0]
            score = tup[1]
            if int(num) == int(score):
                temp = name + ' : ' + str(score) + '\n'
                newContents += (temp)
                nameScores.pop(nameScores.index(tup))
    # print(newContents)
    if isTouhou:
        if isOnePlayer:
            eraseFile('touhou_high_scores1.txt', newContents)
        elif isTwoPlayer:
            eraseFile('touhou_high_scores2.txt', newContents)
    elif isPokemon:
        if isOnePlayer:
            eraseFile('pokemon_high_scores1.txt', newContents)
        elif isTwoPlayer:
            eraseFile('pokemon_high_scores2.txt', newContents)
    
score = 0
enemyLevel = 1
input = ''
isUnsure = False

#initalize Players
players = []
player1 = None
player2 = None
tempPlayers = [] #players in order
#touhou
def touhouPlayers():
    size = 25
    for char in tempPlayers:
        if char == touhouChars[0]:
            reimuWidth = 32
            reimuHeight = 48
            playerReimu = ReimuP((gameWidth - sideBarWidth)/2, 
            gameHeight - reimuHeight, reimuWidth, reimuHeight)
            players.append(playerReimu)
        elif char == touhouChars[1]:
            marisaWidth = 60
            marisaHeight = 124
            playerMarisa = MarisaP((gameWidth - sideBarWidth)/2, 
            gameHeight - marisaHeight, marisaWidth, marisaHeight)
            players.append(playerMarisa)
        elif char == touhouChars[2]:
            players.append(AliceP((gameWidth - sideBarWidth)/2, 
            gameHeight - size, size, size))
        elif char == touhouChars[3]:
            players.append(AyaP((gameWidth - sideBarWidth)/2, 
            gameHeight - size, size, size))
        elif char == touhouChars[4]:
            players.append(CirnoP((gameWidth - sideBarWidth)/2, 
            gameHeight - size, size, size))
    return players
    
#pokemon
def pokemonPlayers():
    size = 32
    for char in tempPlayers:
        if char == pokemonChars[0]:
            players.append(CharizardP((gameWidth - sideBarWidth)/2, 
            gameHeight - size, size, size))
        elif char == pokemonChars[1]:
            players.append(BlastoiseP((gameWidth - sideBarWidth)/2,
             gameHeight - size, size, size))
        elif char == pokemonChars[2]:
            players.append(VenusaurP((gameWidth - sideBarWidth)/2, 
            gameHeight - size, size, size))
        elif char == pokemonChars[3]:
            players.append(PikachuP((gameWidth - sideBarWidth)/2, 
            gameHeight - size*.5, size*.5, size*.5))
        elif char == pokemonChars[4]:
            players.append(MewtwoP((gameWidth - sideBarWidth)/2, 
            gameHeight - size, size, size))
    return players

#initialize Enemy
isAttacking = True
charizardHealth = 200
blastoiseHealth = 200
venusaurHealth = 300
pikachuHealth = 100
mewtwoHealth = 400
def pokemonEnemies(num):
    size = 32
    startX = random.randint(size, gameWidth - size - sideBarWidth - 50)
    if num == 0:
        return CharizardE(startX, size, size, size, charizardHealth)
    elif num == 1:
        return BlastoiseE(startX, size, size, size, blastoiseHealth)
    elif num == 2:
        return VenusaurE(startX, size, size, size, venusaurHealth)
    elif num == 3:
        return PikachuE(startX, size, size, size, pikachuHealth)
    elif num == 4:
        return MewtwoE(startX, size, size, size, mewtwoHealth)

reimuHealth = 200
marisaHealth = 200
aliceHealth = 250
ayaHealth = 150
cirnoHealth = 400
def touhouEnemies(num):
    if num == 0:
        sizeX = 32
        sizeY = 48
        startX = random.randint(sizeX, gameWidth - sizeY - sideBarWidth - 50)
        return ReimuE(startX, sizeY, sizeX, sizeY, reimuHealth)
    elif num == 1:
        size = 108
        startX = random.randint(size, gameWidth - size - sideBarWidth - 50)
        return MarisaE(startX, size, size, size, marisaHealth)
    elif num == 2:
        size = 90
        startX = random.randint(size, gameWidth - size - sideBarWidth - 50)
        return AliceE(startX, size, size, size, aliceHealth)
    elif num == 3:
        size = 100
        startX = random.randint(size, gameWidth - size - sideBarWidth - 50)
        return AyaE(startX, size, size, size, ayaHealth)
    elif num == 4:
        size = 80
        startX = random.randint(size, gameWidth - size - sideBarWidth - 50)
        return CirnoE(startX, size, size, size, cirnoHealth)

#initialize lists
touPProjs = []
pokePProjs = []
touEProjs = []
pokeEProjs = []
enemies = []
powerUps = []
powerUpTs = [] #power up timer
#names of char
touhouChars = ['reimu', 'marisa', 'alice', 'aya', 'cirno']
touApou = [[10, 10, 10, 10, 20], #pokemon across, touhou down
            [10, 20, 5, 20, 5], 
            [5, 5, 20, 20, 10], 
            [10, 10, 20, 5, 10],
            [20, 10, 30, 20, 20]]
pouAtou = [[10, 10, 10, 10, 20], #pokemon across, touhou down
            [10, 10, 15, 15, 5], 
            [15, 15, 10, 10, 5], 
            [10, 10, 5, 15, 15],
            [20, 20, 20, 20, 20]]
pokeEBools = [[False]*5 for i in range(5)]
touEBools = [[False]*5 for i in range(5)]
touhouProjs = ['yyorb', 'star', 'sonic', 'wind', 'ice']
pokemonChars = ['charizard', 'blastoise', 'venusaur', 'pikachu', 'mewtwo']
touBools = [False]*5
pokeBools = [False]*5
touSelectBools = [False]*5
pokeSelectBools = [False]*5

##
## Redrawing game window
##

def redrawGameWindow():
    if isTitleScreen:
        if musicCount == 0:
            playTitleMusic()
        #https://www.spriters-resource.com/pc_computer/swr/sheet/24196/
        pic = pygame.image.load('pictures/Backgrounds/title_screen.png')
        titleScreen = pygame.transform.scale(pic,(gameWidth, gameHeight))
        win.blit(titleScreen, (0,0))
        
        #Title
        font = pygame.font.SysFont('comicsans', 130, True)
        title = font.render('TouPou', 1, (255,255,200))
        win.blit(title, (gameWidth*1.5/6, gameHeight*1.5/6))
        
        #Pokemon
        if pokemonHover:
            #https://commons.wikimedia.org/wiki/
            # File:International_Pokémon_logo.svg
            pic = pygame.image.load('pictures/Backgrounds/Pokemon_Logo.png')
            pokemon = pygame.transform.scale(pic,(round(gameWidth/2.75 + 60),
            round(gameHeight/7 + 60)))
            win.blit(pokemon, (gameWidth/16 - 30, gameHeight*3.5/6 - 30))
        else:
            pic = pygame.image.load('pictures/Backgrounds/Pokemon_Logo.png')
            pokemon = pygame.transform.scale(pic,(round(gameWidth/2.75),
            round(gameHeight/7)))
            win.blit(pokemon, (gameWidth/16, gameHeight*3.5/6))
        
        #Versus
        font = pygame.font.SysFont('comicsans', 65, True)
        versus = font.render('vs', 1, (0,0,0))
        win.blit(versus, (gameWidth*2.75/6, gameHeight*3.85/6))
        
        #Touhou
        if touhouHover:
            #https://joke-battles.fandom.com/wiki/Category:Touhou_Project
            pic = pygame.image.load('pictures/Backgrounds/Touhou_Logo.png')
            touhou = pygame.transform.scale(pic,(round(gameWidth/2.75 + 60),
            round(gameHeight/7 + 60)))
            win.blit(touhou, (gameWidth*3.5/6 - 30, gameHeight*3.5/6 - 30))
        else:
            pic = pygame.image.load('pictures/Backgrounds/Touhou_Logo.png')
            touhou = pygame.transform.scale(pic,(round(gameWidth/2.75),
            round(gameHeight/7)))
            win.blit(touhou, (gameWidth*3.5/6, gameHeight*3.5/6))
        
        pygame.display.update()
    
    elif isGameplayScreen:
        #https://www.spriters-resource.com/pc_computer/swr/sheet/24196/
        pic = pygame.image.load('pictures/Backgrounds/title_screen.png')
        titleScreen = pygame.transform.scale(pic,(gameWidth, gameHeight))
        win.blit(titleScreen, (0,0))
        
        #Choose Gameplay:
        font = pygame.font.SysFont('comicsans', 65, True)
        text = font.render('Choose Gameplay', 1, (0,0,0))
        win.blit(text, (gameWidth*2.5/12, gameHeight*1/6))
        
        #one player mode
        font = pygame.font.SysFont('comicsans', 50, True)
        text = font.render('One Player Mode', 1, (0,0,0))
        win.blit(text, (gameWidth*1.75/6, gameHeight*3.5/6))
        
        #two player mode
        font = pygame.font.SysFont('comicsans', 50, True)
        text = font.render('Two Player Mode', 1, (0,0,0))
        win.blit(text, (gameWidth*1.75/6, gameHeight*4.25/6))
        
        #Back Button
        font = pygame.font.SysFont('comicsans', 25, True)
        versus = font.render('Back', 1, (255,255,255))
        win.blit(versus, (gameWidth*5.5/6, gameHeight*11/12))
        
        pygame.display.update()
    
    elif isCharacterTouhouScreen:
        #https://www.spriters
        #-resource.com/pc_computer/touhoueiyashouimperishablenight/sheet/34557/
        pic = pygame.image.load('pictures/Backgrounds/touhou_char_bg.png')
        titleScreen = pygame.transform.scale(pic,(gameWidth, gameHeight))
        win.blit(titleScreen, (0,0))
        
        #Choose a Character
        if not isSelectingAnother:
            font = pygame.font.SysFont('comicsans', 65, True)
            text = font.render('Choose a Character', 1, (255,255,255))
            win.blit(text, (gameWidth*2/12, gameHeight*1/6))
        
        elif isSelectingAnother:
            font = pygame.font.SysFont('comicsans', 50, True)
            text = font.render('Choose Another Character', 1, (255,255,255))
            win.blit(text, (gameWidth*2/12, gameHeight*1/6))
        
        #select touhou character
        for char in range(len(touhouChars)):
            if touSelectBools[char]:
                #https://www.spriters-resource.com/pc_computer/touhou
                c = ('pictures/touhou enemy sprites/' + touhouChars[char] + 
                 '_enemy.png')
                pic = pygame.image.load(c)
                size = 120
                tou = pygame.transform.scale(pic,(size, size))
                win.blit(tou, (gameWidth*(2*char)/10 - 10, gameHeight*1/2 - 10))
            else:
                #https://www.spriters-resource.com/pc_computer/touhou
                c = ('pictures/touhou enemy sprites/' + touhouChars[char] + 
                 '_enemy.png')
                pic = pygame.image.load(c)
                size = 100
                tou = pygame.transform.scale(pic,(size, size))
                win.blit(tou, (gameWidth*(2*char)/10, gameHeight*1/2))
        
        #Back Button
        font = pygame.font.SysFont('comicsans', 25, True)
        versus = font.render('Back', 1, (255,255,255))
        win.blit(versus, (gameWidth*5.5/6, gameHeight*11/12))
        
        pygame.display.update()
        
    elif isCharacterPokemonScreen:
        #https://www.spriters
        #-resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/59170/
        pic = pygame.image.load('pictures/Backgrounds/pokemon_char_bg.png')
        titleScreen = pygame.transform.scale(pic, (gameWidth, gameHeight))
        win.blit(titleScreen, (0,0))
        
        #Choose a Character
        if not isSelectingAnother:
            font = pygame.font.SysFont('comicsans', 65, True)
            text = font.render('Choose a Character', 1, (0,0,0))
            win.blit(text, (gameWidth*2/12, gameHeight*1/6))
        
        elif isSelectingAnother:
            font = pygame.font.SysFont('comicsans', 50, True)
            text = font.render('Choose Another Character', 1, (0,0,0))
            win.blit(text, (gameWidth*2/12, gameHeight*1/6))
        
        #select pokemon character
        for char in range(len(pokemonChars)):
            if pokeSelectBools[char]:
                #https://www.spriters-resource.com
                c = ('pictures/pokemon sprites/' + pokemonChars[char] + 
                 '_enemy.png')
                pic = pygame.image.load(c)
                size = 120
                poke = pygame.transform.scale(pic,(size, size))
                win.blit(poke, (gameWidth*(2*char)/10 - 10, 
                gameHeight*1/2 - 10))
            else:
                #https://www.spriters-resource.com
                c = ('pictures/pokemon sprites/' + pokemonChars[char] + 
                 '_enemy.png')
                pic = pygame.image.load(c)
                size = 100
                poke = pygame.transform.scale(pic,(size, size))
                win.blit(poke, (gameWidth*(2*char)/10, gameHeight*1/2))
        
        #Back Button
        font = pygame.font.SysFont('comicsans', 25, True)
        versus = font.render('Back', 1, (0,0,0))
        win.blit(versus, (gameWidth*5.5/6, gameHeight*11/12))
        
        pygame.display.update()
    
    elif isGameplay:
        #Play Music
        if musicCount == 1:
            playMusic()
        
        #GamePlay
        if isTouhou:
            win.blit(touhouBackground, (0,0))
            color = (255,255,255)
        
        elif isPokemon:
            win.blit(pokemonBackground, (0,0))
            color = (0,0,0)
        
        if len(players) == 0:
            if isTouhou:
                touhouPlayers()
            elif isPokemon:
                pokemonPlayers()
        
        if len(players) == 1:
            player1 = players[0]
            player1.draw(win)
        else:
            player1 = players[0]
            player2 = players[1]
            player1.draw(win)
            player2.draw(win)
        
        if isTouhou:
            for touPProj in touPProjs:
                touPProj.draw(win)
            
            for pokeEProj in pokeEProjs:
                pokeEProj.draw(win)
        
        elif isPokemon:
            for pokePProj in pokePProjs:
                pokePProj.draw(win)
            
            for touEProj in touEProjs:
                touEProj.draw(win)
        
        for enemy in enemies:
            enemy.draw(win)
        
        for powerUp in powerUps:
            if powerUp.visible:
                powerUp.draw(win)

            
        #Sidebar
        sideBarX = gameWidth - sideBarWidth
        dim = (sideBarX, 0, sideBarWidth, gameHeight)
        color = (139, 131, 120)
        pygame.draw.rect(win, color, dim)
        
        #Display Logo:
        if isTouhou:
            #https://joke-battles.fandom.com/wiki/Category:Touhou_Project
            pic = pygame.image.load('pictures/Backgrounds/Touhou_Logo.png')
            touhou = pygame.transform.scale(pic,(round(sideBarWidth),
            round(gameHeight/8)))
            win.blit(touhou, (sideBarX, 25))
            
        elif isPokemon:
            #https://commons.wikimedia.org/wiki/
            # File:International_Pokémon_logo.svg
            pic = pygame.image.load('pictures/Backgrounds/Pokemon_Logo.png')
            pokemon = pygame.transform.scale(pic,(round(sideBarWidth),
            round(gameHeight/8)))
            win.blit(pokemon, (sideBarX, 25))
            
        
        #game timer
        font = pygame.font.SysFont('comicsans', 30, True)
        color = (0, 0, 0)
        gameTimer = font.render('Game Timer: ', 1, color)
        win.blit(gameTimer, (gameWidth - sideBarWidth + 5, 125))
        
        timerDisplay = font.render(str(timePassed), 1, color)
        win.blit(timerDisplay, (gameWidth - sideBarWidth + 50, 150))
        
        #Enemy Level
        enemy_level = font.render('Enemy Level: ', 1, color)
        win.blit(enemy_level, (gameWidth - sideBarWidth + 5, 225))
        
        levelDisplay = font.render(str(enemyLevel), 1, color)
        win.blit(levelDisplay, (gameWidth - sideBarWidth + 50, 250))
        
        #Current Pow:
        powFont = pygame.font.SysFont('comicsans', 25, True)
        currentPow = powFont.render('Current Status: ', 1, color)
        win.blit(currentPow, (gameWidth - sideBarWidth + 5, 325))
        
        #https://www.spriters-
        # resource.com/pc_computer/touhoufuujinrokumountainoffaith/sheet/51907/
        Ppic = pygame.image.load('pictures/projectiles/powerUpP.png')
        Bpic = pygame.image.load('pictures/projectiles/powerUpB.png')
        stop = pygame.image.load('pictures/projectiles/stop.png')
        pUpSize = 16
        if player1.powerUpP:
            powerUpPDisplay = pygame.transform.scale(Ppic, (pUpSize, pUpSize))
            win.blit(powerUpPDisplay, (gameWidth - sideBarWidth + 25, 350))
        
        if isTwoPlayer and player2.powerUpP:
            powerUpPDisplay = pygame.transform.scale(Ppic, (pUpSize, pUpSize))
            win.blit(powerUpPDisplay, (gameWidth - sideBarWidth + 25, 350))
        
        if player1.powerUpB:
            powerUpBDisplay = pygame.transform.scale(Bpic, (pUpSize, pUpSize))
            win.blit(powerUpBDisplay, (gameWidth - sideBarWidth + 50, 350))
        
        if isTwoPlayer and player2.powerUpB:
            powerUpBDisplay = pygame.transform.scale(Bpic, (pUpSize, pUpSize))
            win.blit(powerUpBDisplay, (gameWidth - sideBarWidth + 50, 350))
        
        if player1.isDisabled:
            stopDisplay = pygame.transform.scale(stop, (pUpSize, pUpSize))
            win.blit(stopDisplay, (gameWidth - sideBarWidth + 75, 350))
            
        if isTwoPlayer and player2.isDisabled:
            stopDisplay = pygame.transform.scale(stop, (pUpSize, pUpSize))
            win.blit(stopDisplay, (gameWidth - sideBarWidth + 75, 350))
        
        #Player1 Lives
        health1 = font.render(tempPlayers[0] + ' Lives: ', 1, color)
        win.blit(health1, (gameWidth - sideBarWidth + 5, 400))
        
        health1Display = font.render(str(player1.lives), 1, color)
        win.blit(health1Display, (gameWidth - sideBarWidth + 50, 425))
        
        if isOnePlayer:
            #Score
            s = font.render('Score:', 1, color)
            win.blit(s, (gameWidth - sideBarWidth + 5, 500))
            
            scoreDisplay = font.render(str(score), 1, color)
            win.blit(scoreDisplay, (gameWidth - sideBarWidth + 50, 525))
            
        elif isTwoPlayer:
            #Player2 Lives
            health2 = font.render(tempPlayers[1] + ' Lives: ', 1, color)
            win.blit(health2, (gameWidth - sideBarWidth + 5, 475))
            
            health2Display = font.render(str(player2.lives), 1, color)
            win.blit(health2Display, (gameWidth - sideBarWidth + 50, 500))
            
            #Score
            s = font.render('Score:', 1, color)
            win.blit(s, (gameWidth - sideBarWidth + 5, 550))
            
            scoreDisplay = font.render(str(score), 1, color)
            win.blit(scoreDisplay, (gameWidth - sideBarWidth + 50, 575))
        
        pygame.display.update()
            
    elif isGameover:
        if musicCount == 2:
            playGOMusic()
        #Screen
        if isTouhou:
        #https://www.spriters
        #-resource.com/pc_computer/touhoueiyashouimperishablenight/sheet/34557/
            pic = pygame.image.load('pictures/Backgrounds/touhou_char_bg.png')
            titleScreen = pygame.transform.scale(pic,(gameWidth, gameHeight))
            win.blit(titleScreen, (0,0))
            color = (255,255,255)
            
            
        elif isPokemon:
        #https://www.spriters
        #-resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/59170/
            pic = pygame.image.load('pictures/Backgrounds/pokemon_char_bg.png')
            titleScreen = pygame.transform.scale(pic, (gameWidth, gameHeight))
            win.blit(titleScreen, (0,0))
            color = (0,0,0)
            
        #Gameover!
        font = pygame.font.SysFont('comicsans', 65, True)
        text = font.render('Game Over!', 1, color)
        win.blit(text, (gameWidth*3.5/12, gameHeight*1/6))
        
        font = pygame.font.SysFont('comicsans', 45, True)
        text = font.render('Leaderboard', 1, color)
        win.blit(text, (gameWidth*4/12, gameHeight*3/6))
        
        pygame.display.update()
    
    elif isLeaderboard:
        #Leaderboard
        if isTouhou:
        #https://www.spriters
        #-resource.com/pc_computer/touhoueiyashouimperishablenight/sheet/34557/
            pic = pygame.image.load('pictures/Backgrounds/touhou_char_bg.png')
            titleScreen = pygame.transform.scale(pic,(gameWidth, gameHeight))
            win.blit(titleScreen, (0,0))
            color = (255,255,255)
            
            if isOnePlayer:
                scores = readFile('touhou_high_scores1.txt')
            elif isTwoPlayer:
                scores = readFile('touhou_high_scores2.txt')
            i = 0
            for line in scores.split('\n'):
                if i < 15:
                    font = pygame.font.SysFont('comicsans', 25, True)
                    text = font.render(line, 1, color)
                    win.blit(text, (gameWidth*1.5/12, 
                    gameHeight*(i/2 + 3.25)/12))
                i += 1
                    
        elif isPokemon:
        #https://www.spriters
        #-resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/sheet/59170/
            pic = pygame.image.load('pictures/Backgrounds/pokemon_char_bg.png')
            titleScreen = pygame.transform.scale(pic, (gameWidth, gameHeight))
            win.blit(titleScreen, (0,0))
            color = (0,0,0)
            
            if isOnePlayer:
                scores = readFile('pokemon_high_scores1.txt')
            elif isTwoPlayer:
                scores = readFile('pokemon_high_scores2.txt')
            i = 0
            for line in scores.split('\n'):
                if i < 15:
                    font = pygame.font.SysFont('comicsans', 25, True)
                    text = font.render(line, 1, color)
                    win.blit(text, (gameWidth*1.5/12, 
                    gameHeight*(i/2 + 3.25)/12))
                i += 1
        
        #Leaderboard:
        font = pygame.font.SysFont('comicsans', 65, True)
        text = font.render('LeaderBoard:', 1, color)
        win.blit(text, (gameWidth*3/12, gameHeight*1/12))
        
        #Leaderboard box:
        leaderboardBox = (gameWidth/12, gameHeight*3/12, gameWidth*10/12,
        gameHeight*8/12)
        color = color
        pygame.draw.rect(win, color, leaderboardBox, 2)
        
        #Your Score:
        font = pygame.font.SysFont('comicsans', 25, True)
        text = font.render('Your Score:', 1, color)
        win.blit(text, (gameWidth*4/12, gameHeight*2/12))
        
        #Score Display:
        font = pygame.font.SysFont('comicsans', 25, True)
        text = font.render(str(score), 1, color)
        win.blit(text, (gameWidth*6.5/12, gameHeight*2/12))
        
        #Your Name:
        font = pygame.font.SysFont('comicsans', 25, True)
        text = font.render('Your Name:', 1, color)
        win.blit(text, (gameWidth*4/12, gameHeight*2.5/12))
        
        #Name Display:
        font = pygame.font.SysFont('comicsans', 25, True)
        text = font.render(input, 1, color)
        win.blit(text, (gameWidth*6.5/12, gameHeight*2.5/12))
        
        #Return To Title Screen:
        font = pygame.font.SysFont('comicsans', 25, True)
        text = font.render('Return to Title Screen', 1, color)
        win.blit(text, (gameWidth*1/24, gameHeight*22.5/24))
        
        if not isUnsure:
            #Clear LeaderBoard
            font = pygame.font.SysFont('comicsans', 25, True)
            text = font.render('Clear Leaderboard', 1, color)
            win.blit(text, (gameWidth*9/12, gameHeight*22.5/24))
        
        if isUnsure:
            #Are You Sure?
            font = pygame.font.SysFont('comicsans', 25, True)
            text = font.render('Are You Sure?', 1, color)
            win.blit(text, (gameWidth*9/12, gameHeight*22.5/24))
        pygame.display.update()

##
## Run Function
##
def makeEnemy(num):
    for i in range(max): #place num
        for j in range(max): #enemy num
            if isTouhou:
                if len(set(pokeEBools[i])) == 1: #make sure all False
                    if j == num:
                        pokeEBools[i][j] = True
                        return
            elif isPokemon:
                if len(set(touEBools[i])) == 1: #make sure all False
                    if j == num:
                        touEBools[i][j] = True
                        return

while run:
    #time
    min = 60
    time = clock.tick(min)
    timePassed += 1
    
    keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    mousePressed = pygame.mouse.get_pressed()
    
    if isTitleScreen:
        if (mousePos[0] >= gameWidth/16 and
         mousePos[0] <= gameWidth/16 + gameWidth/2.75):                    
            if (mousePos[1] >= gameHeight*3.5/6 and
             mousePos[1] <= gameHeight*3.5/6 + gameHeight/7):
                pokemonHover = True
                touhouHover = False
        elif (mousePos[0] >= gameWidth*3.5/6 and
         mousePos[0] <= gameWidth*3.5/6 + gameWidth/2.75):                    
            if (mousePos[1] >= gameHeight*3.5/6 
            and mousePos[1] <= gameHeight*3.5/6 + gameHeight/7):
                touhouHover = True
                pokemonHover = False
        else:
            pokemonHover = False
            touhouHover = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mousePos[0] >= gameWidth/16 and
                mousePos[0] <= gameWidth/16 + gameWidth/2.75):                    
                    if (mousePos[1] >= gameHeight*3.5/6 and
                    mousePos[1] <= gameHeight*3.5/6 + gameHeight/7):
                        isPokemon = True
                        isGameplayScreen = True
                        isTitleScreen = False
                elif (mousePos[0] >= gameWidth*3.5/6 and
                mousePos[0] <= gameWidth*3.5/6 + gameWidth/2.75):                    
                    if (mousePos[1] >= gameHeight*3.5/6 
                    and mousePos[1] <= gameHeight*3.5/6 + gameHeight/7):
                        isTouhou = True
                        isGameplayScreen = True
                        isTitleScreen = False
            elif event.type == pygame.QUIT:
                run = False
                Mixer.music.stop()
    
    elif isGameplayScreen:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mousePos[0] >= gameWidth*1.25/6 and
                mousePos[0] <= gameWidth*1.25/6 + gameWidth*3.5/6):                    
                    if (mousePos[1] >= gameHeight*3.5/6 and
                    mousePos[1] <= gameHeight*3.5/6 + gameHeight*35/600):
                        isOnePlayer = True
                        if isTouhou:
                            isCharacterTouhouScreen = True
                            isGameplayScreen = False
                        else:
                            isCharacterPokemonScreen = True
                            isGameplayScreen = False
                        
                if (mousePos[0] >= gameWidth*1.25/6 and
                mousePos[0] <= gameWidth*1.25/6 + gameWidth*3.5/6):                    
                    if (mousePos[1] >= gameHeight*4.25/6 
                    and mousePos[1] <= gameHeight*4.25/6 + gameHeight*35/600):
                        isTwoPlayer = True
                        if isTouhou:
                            isCharacterTouhouScreen = True
                            isGameplayScreen = False
                        else:
                            isCharacterPokemonScreen = True
                            isGameplayScreen = False
                
                elif (mousePos[0] >= gameWidth*5.5/6 and
                mousePos[0] <= gameWidth*5.5/6 + gameWidth*5/60):                    
                    if (mousePos[1] >= gameHeight*11/12 
                    and mousePos[1] <= gameHeight*11/12 + gameHeight*2/60):
                        isTouhou = False
                        isPokemon = False
                        isTitleScreen = True
                        isGameplayScreen = False

            elif event.type == pygame.QUIT:
                run = False
                Mixer.music.stop()
    
    elif isCharacterTouhouScreen:
        numChar = 5
        size = 100
        for i in range(numChar):
            if (mousePos[0] >= gameWidth*(2*i)/10 and
            mousePos[0] <= gameWidth*(2*i)/10 + size):                    
                if (mousePos[1] >= gameHeight*1/2 and
                mousePos[1] <= gameHeight*1/2 + size):
                    touSelectBools[i] = True
                else:
                    touSelectBools[i] = False
            else:
                touSelectBools[i] = False
        
        if isOnePlayer:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(numChar):
                        if (mousePos[0] >= gameWidth*(2*i)/10 and
                        mousePos[0] <= gameWidth*(2*i)/10 + size):                    
                            if (mousePos[1] >= gameHeight*1/2 and
                            mousePos[1] <= gameHeight*1/2 + size):
                                touBools[i] = True
                                tempPlayers.append(touhouChars[i])
                                isGameplay = True
                                isCharacterTouhouScreen = False
                    if (mousePos[0] >= gameWidth*5.5/6 and
                    mousePos[0] <= gameWidth*5.5/6 + gameWidth*5/60):                    
                        if (mousePos[1] >= gameHeight*11/12 
                        and mousePos[1] <= gameHeight*11/12 + gameHeight*2/60):
                            isOnePlayer = False
                            isTwoPlayer = False
                            isCharacterTouhouScreen = False
                            isGameplayScreen = True
                elif event.type == pygame.QUIT:
                    run = False
                    Mixer.music.stop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(numChar):
                        if (mousePos[0] >= gameWidth*(2*i)/10 and
                        mousePos[0] <= gameWidth*(2*i)/10 + size):                    
                            if (mousePos[1] >= gameHeight*1/2 and
                            mousePos[1] <= gameHeight*1/2 + size):
                                if touBools[i] == False:
                                    touBools[i] = True
                                    tempPlayers.append(touhouChars[i])
                                else:
                                    break
                                isSelectingAnother = not isSelectingAnother
                                if not isSelectingAnother:
                                    isGameplay = True
                                    isCharacterTouhouScreen = False
                    if (mousePos[0] >= gameWidth*5.5/6 and
                    mousePos[0] <= gameWidth*5.5/6 + gameWidth*5/60):                    
                        if (mousePos[1] >= gameHeight*11/12 
                        and mousePos[1] <= gameHeight*11/12 + gameHeight*2/60):
                            isOnePlayer = False
                            isTwoPlayer = False
                            isCharacterTouhouScreen = False
                            isGameplayScreen = True
                elif event.type == pygame.QUIT:
                    run = False
                    Mixer.music.stop()
        
    elif isCharacterPokemonScreen:
        numChar = 5
        size = 100
        for i in range(numChar):
            if (mousePos[0] >= gameWidth*(2*i)/10 and
            mousePos[0] <= gameWidth*(2*i)/10 + size):                    
                if (mousePos[1] >= gameHeight*1/2 and
                mousePos[1] <= gameHeight*1/2 + size):
                    pokeSelectBools[i] = True
                else:
                    pokeSelectBools[i] = False
            else:
                pokeSelectBools[i] = False
        
        if isOnePlayer:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(numChar):
                        if (mousePos[0] >= gameWidth*(2*i)/10 and
                        mousePos[0] <= gameWidth*(2*i)/10 + size):                    
                            if (mousePos[1] >= gameHeight*1/2 and
                            mousePos[1] <= gameHeight*1/2 + size):
                                pokeBools[i] = True
                                tempPlayers.append(pokemonChars[i])
                                isGameplay = True
                                isCharacterPokemonScreen = False
                    if (mousePos[0] >= gameWidth*5.5/6 and
                    mousePos[0] <= gameWidth*5.5/6 + gameWidth*5/60):                    
                        if (mousePos[1] >= gameHeight*11/12 
                        and mousePos[1] <= gameHeight*11/12 + gameHeight*2/60):
                            isOnePlayer = False
                            isTwoPlayer = False
                            isCharacterPokemonScreen = False
                            isGameplayScreen = True
                elif event.type == pygame.QUIT:
                    run = False
                    Mixer.music.stop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(numChar):
                        if (mousePos[0] >= gameWidth*(2*i)/10 and
                        mousePos[0] <= gameWidth*(2*i)/10 + size):                    
                            if (mousePos[1] >= gameHeight*1/2 and
                            mousePos[1] <= gameHeight*1/2 + size):
                                if pokeBools[i] == False:
                                    pokeBools[i] = True
                                    tempPlayers.append(pokemonChars[i])
                                else:
                                    break
                                isSelectingAnother = not isSelectingAnother
                                if not isSelectingAnother:
                                    isGameplay = True
                                    isCharacterPokemonScreen = False
                    if (mousePos[0] >= gameWidth*5.5/6 and
                    mousePos[0] <= gameWidth*5.5/6 + gameWidth*5/60):                    
                        if (mousePos[1] >= gameHeight*11/12 
                        and mousePos[1] <= gameHeight*11/12 + gameHeight*2/60):
                            isOnePlayer = False
                            isTwoPlayer = False
                            isCharacterPokemonScreen = False
                            isGameplayScreen = True
                if event.type == pygame.QUIT:
                    run = False
                    Mixer.music.stop()
        
    elif isGameplay:
        #Movement
        if len(players) == 1:
            player1 = players[0]
        else:
            player1 = players[0]
            player2 = players[1]
        # print(players)
        
        ## One Player
        if keys[pygame.K_LEFT] and player1.x > player1.vel - player1.width:
            player1.x -= player1.vel
        
        elif (keys[pygame.K_RIGHT]
        and player1.x < gameHeight - player1.vel - player1.height):
            player1.x += player1.vel
        
        if keys[pygame.K_UP] and player1.y > player1.vel - player1.height:
            player1.y -= player1.vel
        
        elif (keys[pygame.K_DOWN]
        and player1.y < gameHeight - player1.vel):
            player1.y += player1.vel
        
        #Player Bullets
        if not player1.isDisabled:
            if isOnePlayer:
                if keys[pygame.K_x]:
                    #touhou
                    x = player1.x + player1.width//2
                    y = player1.y + player1.height//2
                    if touBools[0]: #Reimu
                        touPProjs.append(yyorb(round(x), round(y)))
                    elif touBools[1]: #Marisa
                        touPProjs.append(star(round(x), round(y)))
                    elif touBools[2]: #Alice
                        if player1.powerUpP:
                            for i in range(-1,2):
                                touPProjs.append(sonic(round(x + i*player1.width),
                                round(y + player1.height//2 + i*player1.height)))
                        else:
                            touPProjs.append(sonic(round(x), round(y)))
                    elif touBools[3]: #Aya
                        touPProjs.append(wind(round(x), round(y)))
                    elif touBools[4]: #Cirno
                        touPProjs.append(ice(round(x), round(y)))
                    
                    #pokemon
                    elif pokeBools[0]: #Charizard
                        pokePProjs.append(fire(round(x), round(y)))
                    elif pokeBools[1]: #Blastoise
                        if player1.powerUpP:
                            pokePProjs.append(water(round(x - player1.width/2),
                             round(y)))
                            pokePProjs.append(water(round(x + player1.width/2),
                             round(y)))
                        elif not player1.powerUpP:
                            pokePProjs.append(water(round(x), round(y)))
                    elif pokeBools[2]: #Venusaur
                        if player1.powerUpP:
                            for i in range(-1,2):
                                pokePProjs.append(leaf(round(x + 
                                i*(player1.width)), round(y + i*(player1.height)), i))
                        pokePProjs.append(leaf(round(x), round(y), 0))
                    elif pokeBools[3]: #Pikachu
                        if player1.powerUpP:
                            pokePProjs.append(thunder2(round(x), round(y)))
                        else:
                            pokePProjs.append(electric(round(x), round(y)))
                    elif pokeBools[4]: #MewTwo
                        pokePProjs.append(shadow(round(x), round(y)))
        
        for touPProj in touPProjs:
            #touPProj hits enemy
            for enemy in enemies:
                if (touPProj.y < enemy.hitbox[1] + enemy.hitbox[3]
                and touPProj.y + touPProj.height > enemy.hitbox[1]):
                    if (touPProj.x + touPProj.width > enemy.hitbox[0] and 
                    touPProj.x < enemy.hitbox[0] + enemy.hitbox[2]):
                        max = 5
                        #Determining power of move on specific enemy
                        for i in range(max): #enemy num
                            for j in range(max): #player num
                                if touPProj in touPProjs:
                                    if pokeEBools[enemy.place][i]:
                                        if touBools[j]:
                                            if player1.powerUpP:
                                                pow = touApou[j][i]*2
                                            else:
                                                pow = touApou[j][i]
                                            enemy.hit(pow)
                                            # print(pow)
                                            if enemy.health < 1:
                                                if enemy.expTimer == 0:
                                                    score += 1000
                                                    explosion(enemy)
                                                if enemy.expTimer%10 == 0:
                                                    enemies.pop(enemies.index(enemy))
                                                    pokeEBools[enemy.place][i] = False
                                                enemy.expTimer += 1
                                            score += 10
                                            touPProjs.pop(touPProjs.index(touPProj))
            
            #touPProj movement
            if touPProj.y < gameHeight and touPProj.y > 0:
                touPProj.y -= touPProj.vel
            else:
                try:
                    touPProjs.pop(touPProjs.index(touPProj))
                except:
                    break
        
        for pokePProj in pokePProjs:
            #touPProj hits enemy
            for enemy in enemies:
                if (pokePProj.y < enemy.hitbox[1] + enemy.hitbox[3]
                and pokePProj.y + pokePProj.height > enemy.hitbox[1]):
                    if (pokePProj.x + pokePProj.width > enemy.hitbox[0] and 
                    pokePProj.x < enemy.hitbox[0] + enemy.hitbox[2]):
                        max = 5
                        #Determining power of move on specific enemy
                        for i in range(max): #enemy num
                            for j in range(max): #player num
                                if pokePProj in pokePProjs:
                                    if touEBools[enemy.place][i]:
                                        if pokeBools[j]:
                                            if player1.powerUpP:
                                                pow = pouAtou[j][i]*2
                                            else:
                                                pow = pouAtou[j][i]
                                            enemy.hit(pow)
                                            # print(pow)
                                            if enemy.health < 1:
                                                if enemy.expTimer == 0:
                                                    score += 1000
                                                    explosion(enemy)
                                                elif enemy.expTimer%5 == 0:
                                                    enemies.pop(enemies.index(enemy))
                                                    touEBools[enemy.place][i] = False
                                                enemy.velL = 0
                                                enemy.velR = 0
                                                enemy.expTimer += 1
                                            score += 10
                                            pokePProjs.pop(pokePProjs.index(pokePProj))
            
            #touPProj movement
            if pokePProj.y < gameHeight and pokePProj.y > 0:
                pokePProj.x += pokePProj.velX
                pokePProj.y -= pokePProj.vel
            else:
                try:
                    pokePProjs.pop(pokePProjs.index(pokePProj))
                except:
                    break
        
        #Enemies
        max = 5
        num = random.choice([0, 0, 1, 1, 2, 2, 3, 3, 4]) #0, 0, 1, 1, 2, 2, 3, 3, 4
        if len(enemies) < max:
            twosec = 20
            if timePassed%twosec == 0:
                if isTouhou:
                    enemy = pokemonEnemies(num)
                if isPokemon:
                    enemy = touhouEnemies(num)
                enemies.append(enemy)
                enemy.place = enemies.index(enemy)
                makeEnemy(num)
        
        #Enemy Bullets
        if isAttacking:
            for enemy in enemies:
                threesec = 30
                if timePassed%threesec == 0:
                    enemy.attack()
                    
                if isinstance(enemy, CharizardE):
                    if enemy.isFireSpin:
                        if timePassed%2 == 0:
                            enemy.fireSpinMove()
                        if enemy.count == 10:
                            enemy.isFireSpin = False
                            enemy.count = 0
                
                if isinstance(enemy, BlastoiseE):
                    if enemy.isWaterGun:
                        if timePassed%5 == 0:
                            enemy.waterGunMove()
                        if enemy.waterGunCount == 6:
                            enemy.isWaterGun = False
                            enemy.waterGunCount = 0
                    elif timePassed%50 == 0:
                        for proj in pokeEProjs:
                            if enemy.isWaterBomb:
                                if isinstance(proj, waterBomb):
                                    enemy.waterBombMove2(proj.x, proj.y)
                                    pokeEProjs.pop(pokeEProjs.index(proj))
                    if enemy.waterBombCount == 1:
                        enemy.isWaterBomb = False
                        enemy.waterBombCount = 0
                
                if isinstance(enemy, VenusaurE):
                    if enemy.isRazorLeaf:
                        if timePassed%5 == 0:
                            enemy.razorLeafMove()
                        if enemy.count == 4:
                            enemy.isRazorLeaf = False
                            enemy.count = 0
                
                if isinstance(enemy, PikachuE):
                    if enemy.isThunder:
                        if timePassed%5 == 0:
                            enemy.thunderMove()
                        if enemy.count >= 2:
                            enemy.isThunder = False
                            enemy.count = 0
                    if timePassed%5 == 0:
                        for proj in pokeEProjs:
                            if isinstance(proj, thunder):
                                pokeEProjs.pop(pokeEProjs.index(proj))
                
                if isinstance(enemy, MewtwoE):
                    if timePassed%50 == 0:
                        enemy.isTeleport = True
                    if enemy.isShadowBall:
                        if timePassed%5 == 0:
                            enemy.shadowBallMove()
                        if enemy.sBCount == 2:
                            enemy.isShadowBall = False
                            enemy.sBCount = 0
                    if player1.isDisabled:
                        enemy.disableTimer += 1
                        if enemy.disableTimer%30 == 0:
                            player1.isDisabled = False 
                            enemy.disableTimer = 0
                
                if isinstance(enemy, MarisaE):
                    if enemy.isStar2:
                        if timePassed%2 == 0:
                            enemy.starMove2()
                        if enemy.star2Count == 4:
                            enemy.isStar2 = False
                            enemy.star2Count = 0
                
                if isinstance(enemy, AliceE):
                    if enemy.isSonic2:
                        if timePassed%2 == 0:
                            enemy.sonicMove2()
                        if enemy.sonic2Count == 7:
                            enemy.isSonic2 = False
                            enemy.sonic2Count = 0
                
                if isinstance(enemy, CirnoE):
                    if player1.isDisabled:
                        enemy.disableTimer += 1
                        if enemy.disableTimer%30 == 0:
                            player1.isDisabled = False 
                            enemy.disableTimer = 0
                    
        if isTouhou:
            for pokeEProj in pokeEProjs:
                if (pokeEProj.x < gameWidth - sideBarWidth - 20 and pokeEProj.x > 20 
                    and pokeEProj.y < gameHeight - 20 and pokeEProj.y > 20):
                    pokeEProj.x += pokeEProj.dirX*pokeEProj.vel
                    pokeEProj.y += pokeEProj.dirY*pokeEProj.vel
                else:
                    pokeEProjs.pop(pokeEProjs.index(pokeEProj))
        
            for pokeEProj in pokeEProjs:
                if (pokeEProj.hitbox[1] < player1.hitbox[1] +
                player1.hitbox[3] and pokeEProj.hitbox[1] + 
                pokeEProj.hitbox[3] > player1.hitbox[1]):
                    if (pokeEProj.hitbox[0] + pokeEProj.hitbox[2] >
                    player1.hitbox[0] and pokeEProj.hitbox[0] <
                    player1.hitbox[0] + player1.hitbox[2]):
                        if player1.lives > 1:
                            if not player1.powerUpB:
                                player1.hit()
                            pokeEProjs.pop(pokeEProjs.index(pokeEProj))
                        else:
                            isGameplay = False
                            isGameover = True
        
        elif isPokemon:
            for touEProj in touEProjs:
                if (touEProj.x < gameWidth - sideBarWidth - 20 and touEProj.x > 20 
                    and touEProj.y < gameHeight - 20 and touEProj.y > 20):
                        if isinstance(touEProj, orb2):
                            if (touEProj.x < gameWidth - sideBarWidth 
                                and touEProj.x > 0 
                                and touEProj.y < gameHeight and touEProj.y > 0):
                                touEProj.x += touEProj.dirX*touEProj.dx
                                touEProj.y += touEProj.dirY*touEProj.dx
                                touEProj.dx += 1
                            else:
                                touEProjs.pop(touEProjs.index(touEProj))
                                touEProj.dx = 0
                                enemy.isOrb2 = False
                        touEProj.x += touEProj.dirX*touEProj.vel
                        touEProj.y += touEProj.dirY*touEProj.vel
                else:
                    touEProjs.pop(touEProjs.index(touEProj))
        
            for touEProj in touEProjs:
                if (touEProj.hitbox[1] < player1.hitbox[1] +
                player1.hitbox[3] and touEProj.hitbox[1] + 
                touEProj.hitbox[3] > player1.hitbox[1]):
                    if (touEProj.hitbox[0] + touEProj.hitbox[2] >
                    player1.hitbox[0] and touEProj.hitbox[0] <
                    player1.hitbox[0] + player1.hitbox[2]):
                        if player1.lives > 1:
                            if not player1.powerUpB:
                                player1.hit()
                            touEProjs.pop(touEProjs.index(touEProj))
                        else:
                            isGameplay = False
                            isGameover = True
        
        #PowerUps
        #generation
        timer = 100
        if timePassed%timer == 0:
            x = random.choice([0,1])
            if x == 0:
                powerUps.append(powerUpB())
            elif x == 1:
                powerUps.append(powerUpP())
        for pow in powerUps:
            if pow.y < gameHeight:
                pow.y += pow.vel
            else:
                powerUps.pop(powerUps.index(pow))
        #contact with player
        for pow in powerUps:
            if (pow.hitbox[1] < player1.hitbox[1] + player1.hitbox[3]
            and pow.hitbox[1] + pow.hitbox[3] > player1.hitbox[1]):
                if (pow.hitbox[0] + pow.hitbox[2] > player1.hitbox[0]
                    and pow.hitbox[0] < player1.hitbox[0] +
                    player1.hitbox[2]):
                    if isinstance(pow, powerUpP):
                        player1.powerUpP = True
                        if player2 != None:
                            player2.powerUpP = True
                    elif isinstance(pow, powerUpB):
                        player1.powerUpB = True
                        if player2 != None:
                            player2.powerUpB = True
                        if touBools[4] or pokeBools[4]:
                            for enemy in enemies:
                                isAttacking = False
                                enemy.tempVelL = enemy.velL
                                enemy.tempVelR = enemy.velR
                                enemy.velL = 0
                                enemy.velR = 0
                    pow.visible = False
                    score += 100
                    powerUpTs.append(pow)
                    powerUps.pop(powerUps.index(pow))
        
        for pow in powerUpTs:
            # print(powerUpTs)
            pow.timer += 1
            # print(pow.timer)
            if touBools[3]:
                sec = 100
            else:
                sec = 50
            if pow.timer%sec == 0:
                if isinstance(pow, powerUpP):
                    # print(0)
                    powerUpTs.pop(powerUpTs.index(pow))
                    temp = copy.copy(powerUpTs)
                    if len(temp) == 0 or isinstance(temp[0], powerUpB):
                        player1.powerUpP = False
                        if player2 != None:
                            player2.powerUpP = False
                        # print(1)
                elif isinstance(pow, powerUpB):
                    # print(2)
                    if touBools[4] or pokeBools[4]:
                        for enemy in enemies:
                            isAttacking = True
                            enemy.velL = enemy.tempVelL
                            enemy.velR = enemy.tempVelR
                            enemy.tempVelL = 0
                            enemy.tempVelR = 0
                    powerUpTs.pop(powerUpTs.index(pow))
                    temp = copy.copy(powerUpTs)
                    if len(temp) == 0 or isinstance(temp[0], powerUpP):
                        player1.powerUpB = False
                        if player2 != None:
                            player2.powerUpB = False
                        # print(3)
        
        #player enemy collision:
        for enemy in enemies:
            if (player1.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3]
            and player1.hitbox[1] + player1.hitbox[3] > enemy.hitbox[1]):
                if (player1.hitbox[0] + player1.hitbox[2] > 
                enemy.hitbox[0] and player1.hitbox[0] < 
                enemy.hitbox[0] + enemy.hitbox[2]):
                    if player1.lives > 1:
                        if not player1.powerUpB:
                            player1.hit()
                    else:
                        isGameplay = False
                        isGameover = True
                    try:
                        enemy.recoil()
                        if enemy.health < 1:
                            enemies.pop(enemies.index(enemy))
                            score += 1000
                            explosion(enemy.x,enemy.y)
                            touEBools[enemy.place][i] = False
                    except:
                        continue
                    # print(enemy.health)
        
        ## Two Player
        if isTwoPlayer:
            #enable multiplayer control
            if keys[pygame.K_a] and player2.x > player2.vel:
                player2.x -= player2.vel
            
            elif (keys[pygame.K_d]
            and player2.x < gameHeight - player1.vel - player1.height):
                player2.x += player2.vel
            
            if keys[pygame.K_w] and player2.y > player2.vel:
                player2.y -= player2.vel
            
            elif (keys[pygame.K_s]
            and player2.y + player2.height < gameHeight - player2.vel):
                player2.y += player2.vel
            
            #Player Bullets
            if not player1.isDisabled:
                if keys[pygame.K_COMMA]:
                    x = player1.x + player1.width//2
                    y = player1.y + player1.height//2
                    if isinstance(player1, ReimuP):
                        touPProjs.append(yyorb(round(x), round(y)))
                    elif isinstance(player1, MarisaP):
                        touPProjs.append(star(round(x), round(y)))
                    elif isinstance(player1, AliceP):
                        if player1.powerUpP:
                            for i in range(-1,2):
                                touPProjs.append(sonic(round(player1.x + 
                                player1.width//2 + i*player1.width),
                                round(player1.y + player1.height//2 +
                                i*player1.height)))
                        else:
                            touPProjs.append(sonic(round(x), round(y)))
                    elif isinstance(player1, AyaP):
                        touPProjs.append(wind(round(x), round(y)))
                    elif isinstance(player1, CirnoP):
                        touPProjs.append(ice(round(x), round(y)))
                    
                    elif isinstance(player1, CharizardP):
                        pokePProjs.append(fire(round(x), round(y)))
                    elif isinstance(player1, BlastoiseP):
                        if player1.powerUpP:
                            pokePProjs.append(water(round(x - player1.width/2),
                             round(y)))
                            pokePProjs.append(water(round(x + player1.width/2),
                             round(y)))
                        elif not player1.powerUpP:
                            pokePProjs.append(water(round(x), round(y)))
                    elif isinstance(player1, VenusaurP):
                        if player1.powerUpP:
                            for i in range(-1,2):
                                pokePProjs.append(leaf(round(x + i*(player1.width)),
                                 round(y + i*(player1.height)), i))
                        pokePProjs.append(leaf(round(x), round(y), 0))
                    elif isinstance(player1, PikachuP):
                        if player1.powerUpP:
                            pokePProjs.append(thunder2(round(x), round(y)))
                        else:
                            pokePProjs.append(electric(round(x), round(y)))
                    elif isinstance(player1, MewtwoP):
                        pokePProjs.append(shadow(round(x), round(y)))
            
            if not player2.isDisabled:
                if keys[pygame.K_TAB]:
                    x = player2.x + player2.width//2
                    y = player2.y + player2.height//2
                    if isinstance(player2, ReimuP):
                        touPProjs.append(yyorb(round(x), round(y)))
                    elif isinstance(player2, MarisaP):
                        touPProjs.append(star(round(x), round(y)))
                    elif isinstance(player2, AliceP):
                        if player2.powerUpP:
                            for i in range(-1,2):
                                touPProjs.append(sonic(round(player2.x + 
                                player2.width//2 + i*player2.width),
                                round(player1.y + player1.height//2 +
                                i*player2.height)))
                        else:
                            touPProjs.append(sonic(round(x), round(y)))
                    elif isinstance(player2, AyaP):
                        touPProjs.append(wind(round(x), round(y)))
                    elif isinstance(player2, CirnoP):
                        touPProjs.append(ice(round(x), round(y)))
                        
                    elif isinstance(player2, CharizardP):
                        pokePProjs.append(fire(round(x), round(y)))
                    elif isinstance(player2, BlastoiseP):
                        if player2.powerUpP:
                            pokePProjs.append(water(round(x - player2.width/2),
                             round(y)))
                            pokePProjs.append(water(round(x + player2.width/2),
                             round(y)))
                        elif not player2.powerUpP:
                            pokePProjs.append(water(round(x), round(y)))
                    elif isinstance(player2, VenusaurP):
                        if player2.powerUpP:
                            for i in range(-1,2):
                                pokePProjs.append(leaf(round(x + i*(player2.width)),
                                 round(y + i*(player2.height)), i))
                        pokePProjs.append(leaf(round(x), round(y), 0))
                    elif isinstance(player2, PikachuP):
                        if player2.powerUpP:
                            pokePProjs.append(thunder2(round(x), round(y)))
                        else:
                            pokePProjs.append(electric(round(x), round(y)))
                    elif isinstance(player2, MewtwoP):
                        pokePProjs.append(shadow(round(x), round(y)))
            
            for touPProj in touPProjs:
                #touPProj hits enemy
                for enemy in enemies:
                    if (touPProj.y < enemy.hitbox[1] + enemy.hitbox[3]
                    and touPProj.y + touPProj.height > enemy.hitbox[1]):
                        if (touPProj.x + touPProj.width > enemy.hitbox[0] and 
                        touPProj.x < enemy.hitbox[0] + enemy.hitbox[2]):
                            max = 5
                            #Determining power of move on specific enemy
                            for i in range(max): #enemy num
                                for j in range(max): #player num
                                    if touPProj in touPProjs:
                                        if pokeEBools[enemy.place][i]:
                                            if touBools[j]:
                                                if player2.powerUpP:
                                                    pow = touApou[j][i]*2
                                                else:
                                                    pow = touApou[j][i]
                                                enemy.hit(pow)
                                                #print(pow)
                                                if enemy.health < 1:
                                                    if enemy.expTimer == 0:
                                                        score += 1000
                                                        explosion(enemy)
                                                    if enemy.expTimer%10 == 0:
                                                        enemies.pop(enemies.index(enemy))
                                                        pokeEBools[enemy.place][i] = False
                                                    enemy.expTimer += 1
                                                score += 10
                                                touPProjs.pop(touPProjs.index(touPProj))
                
                #touPProj movement
                if touPProj.y < gameHeight and touPProj.y > 0:
                    touPProj.y -= touPProj.vel
                else:
                    try:
                        touPProjs.pop(touPProjs.index(touPProj))
                    except:
                        break
            
            for pokePProj in pokePProjs:
                #touPProj hits enemy
                for enemy in enemies:
                    if (pokePProj.y < enemy.hitbox[1] + enemy.hitbox[3]
                    and pokePProj.y + pokePProj.height > enemy.hitbox[1]):
                        if (pokePProj.x + pokePProj.width > enemy.hitbox[0] and 
                        pokePProj.x < enemy.hitbox[0] + enemy.hitbox[2]):
                            max = 5
                            #Determining power of move on specific enemy
                            for i in range(max): #enemy num
                                for j in range(max): #player num
                                    if pokePProj in pokePProjs:
                                        if touEBools[enemy.place][i]:
                                            if pokeBools[j]:
                                                if player2.powerUpP:
                                                    pow = pouAtou[j][i]*2
                                                else:
                                                    pow = pouAtou[j][i]
                                                enemy.hit(pow)
                                                # print(pow)
                                                if enemy.health < 1:
                                                    if enemy.expTimer == 0:
                                                        score += 1000
                                                        explosion(enemy)
                                                    if enemy.expTimer%10 == 0:
                                                        enemies.pop(enemies.index(enemy))
                                                        pokeEBools[enemy.place][i] = False
                                                    enemy.expTimer += 1
                                                score += 10
                                                pokePProjs.pop(pokePProjs.index(pokePProj))
                
                #touPProj movement
                if pokePProj.y < gameHeight and pokePProj.y > 0:
                    pokePProj.x += pokePProj.velX
                    pokePProj.y -= pokePProj.vel
                else:
                    try:
                        pokePProjs.pop(pokePProjs.index(pokePProj))
                    except:
                        break
            
            #Enemy Bullets
            if isTouhou:
                for pokeEProj in pokeEProjs:
                    if (pokeEProj.hitbox[1] < player2.hitbox[1] +
                    player2.hitbox[3] and pokeEProj.hitbox[1] + 
                    pokeEProj.hitbox[3] > player2.hitbox[1]):
                        if (pokeEProj.hitbox[0] + pokeEProj.hitbox[2] >
                        player2.hitbox[0] and pokeEProj.hitbox[0] <
                        player2.hitbox[0] + player2.hitbox[2]):
                            if player2.lives > 1:
                                player2.hit()
                                pokeEProjs.pop(pokeEProjs.index(pokeEProj))
                            else:
                                isGameplay = False
                                isGameover = True
            elif isPokemon:
                for touEProj in touEProjs:
                    if (touEProj.hitbox[1] < player1.hitbox[1] +
                    player1.hitbox[3] and touEProj.hitbox[1] + 
                    touEProj.hitbox[3] > player1.hitbox[1]):
                        if (touEProj.hitbox[0] + touEProj.hitbox[2] >
                        player1.hitbox[0] and touEProj.hitbox[0] <
                        player1.hitbox[0] + player1.hitbox[2]):
                            if player1.lives > 1:
                                if not player1.powerUpB:
                                    player1.hit()
                                touEProjs.pop(touEProjs.index(touEProj))
                            else:
                                isGameplay = False
                                isGameover = True
            
            for enemy in enemies:
                if isinstance(enemy, MewtwoE):
                    if player2.isDisabled:
                        enemy.disableTimer += 1
                        if enemy.disableTimer%30 == 0:
                            player2.isDisabled = False 
                            enemy.disableTimer = 0  
                if isinstance(enemy, CirnoE):
                    if player2.isDisabled:
                        enemy.disableTimer += 1
                        if enemy.disableTimer%30 == 0:
                            player2.isDisabled = False 
                            enemy.disableTimer = 0
            
            #PowerUps
            for pow in powerUps:
                if (pow.hitbox[1] < player2.hitbox[1] + player2.hitbox[3]
                and pow.hitbox[1] + pow.hitbox[3] > player2.hitbox[1]):
                    if (pow.hitbox[0] + pow.hitbox[2] > player2.hitbox[0]
                        and pow.hitbox[0] < player2.hitbox[0] +
                        player2.hitbox[2]):
                        if isinstance(pow, powerUpP):
                            player1.powerUpP = True
                            player2.powerUpP = True
                        elif isinstance(pow, powerUpB):
                            player1.powerUpB = True
                            player2.powerUpB = True
                            if touBools[4]:
                                for enemy in enemies:
                                    enemy.tempVelL = enemy.velL
                                    enemy.tempVelR = enemy.velR
                                    enemy.velL = 0
                                    enemy.velR = 0
                                    isAttacking = True
                        pow.visible = False
                        score += 100
                        powerUpTs.append(pow)
                        powerUps.pop(powerUps.index(pow))
            
            for pow in powerUpTs:
                # print(powerUpTs)
                pow.timer += 1
                # print(pow.timer)
                if touBools[3]:
                    sec = 100
                else:
                    sec = 50
                if pow.timer%sec == 0:
                    if isinstance(pow, powerUpP):
                        # print(5)
                        powerUpTs.pop(powerUpTs.index(pow))
                        temp = copy.copy(powerUpTs)
                        if len(temp) == 0 or isinstance(temp[0], powerUpB):
                            player1.powerUpP = False
                            player2.powerUpP = False
                            # print(6)
                    elif isinstance(pow, powerUpB):
                        # print(7)
                        if touBools[4]:
                            for enemy in enemies:
                                enemy.velL = enemy.tempVelL
                                enemy.velR = enemy.tempVelR
                                enemy.tempVelL = 0
                                enemy.tempVelR = 0
                                isAttacking = False
                        powerUpTs.pop(powerUpTs.index(pow))
                        temp = copy.copy(powerUpTs)
                        if len(temp) == 0 or isinstance(temp[0], powerUpP):
                            player1.powerUpB = False
                            player2.powerUpB = False
                            # print(8)
            
            #player enemy collision:
            for enemy in enemies:
                if (player2.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3]
                and player2.hitbox[1] + player2.hitbox[3] > enemy.hitbox[1]):
                    if (player2.hitbox[0] + player2.hitbox[2] > 
                    enemy.hitbox[0] and player2.hitbox[0] < 
                    enemy.hitbox[0] + enemy.hitbox[2]):
                        if player2.lives > 1:
                            if not player2.powerUpB:
                                player2.hit()
                        else:
                            isGameplay = False
                            isGameover = True
                        try:
                            enemy.recoil()
                            if enemy.health < 1:
                                enemies.pop(enemies.index(enemy))
                                score += 1000
                                explosion(enemy.x,enemy.y)
                                touEBools[enemy.place][i] = False
                            
                        except:
                            continue
            
        #Make Harder With Time:
        twentysec = 200
        if timePassed%twentysec == 0:
            charizardHealth += 50
            blastoiseHealth += 50
            venusaurHealth += 50
            pikachuHealth += 50
            mewtwoHealth += 50
            reimuHealth += 50
            marisaHealth += 50
            aliceHealth += 50
            ayaHealth += 50
            cirnoHealth += 50
            enemyLevel += 1
            
        #Other
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                Mixer.music.stop()
    
    elif isGameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mousePos[0] >= gameWidth*3.5/12 and
                mousePos[0] <= gameWidth*3.5/12 + gameWidth*22/60):                    
                    if (mousePos[1] >= gameHeight*3/6 and
                    mousePos[1] <= gameHeight*3/6 + gameHeight*25/600):
                        isLeaderboard = True
                        isGameover = False
            if event.type == pygame.QUIT:
                run = False
                Mixer.music.stop()

    elif isLeaderboard:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in string.ascii_letters:
                    input += pygame.key.name(event.key)
                elif pygame.key.name(event.key) == 'return':
                    if not isInserting:
                        appendScore()
                    isInserting = True
                    input = ''
                elif pygame.key.name(event.key) == 'backspace':
                    input = input[:-1]
                else:
                    continue
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if isUnsure == True:
                    if (mousePos[0] >= gameWidth*8/12 and
                    mousePos[0] <= gameWidth*8/12 + gameWidth*13/60):                    
                        if (mousePos[1] >= gameHeight*22.5/24 and
                        mousePos[1] <= gameHeight*22.5/24 + gameHeight*2/60):
                            if isTouhou:
                                if isOnePlayer:
                                    eraseFile('touhou_high_scores1.txt','')
                                elif isTwoPlayer:
                                    eraseFile('touhou_high_scores2.txt','')
                            elif isPokemon:
                                if isOnePlayer:
                                    eraseFile('pokemon_high_scores1.txt','')
                                elif isTwoPlayer:
                                    eraseFile('pokemon_high_scores2.txt','')
                            isUnsure = False
                elif (mousePos[0] >= gameWidth*8/12 and
                mousePos[0] <= gameWidth*8/12 + gameWidth*21/60):                    
                    if (mousePos[1] >= gameHeight*22.5/24 and
                    mousePos[1] <= gameHeight*22.5/24 + gameHeight*2/60):
                        isUnsure = True
                
                if (mousePos[0] >= gameWidth*1/24 and
                mousePos[0] <= gameWidth*1/24 + gameWidth*21/60):                    
                    if (mousePos[1] >= gameHeight*22.5/24 and
                    mousePos[1] <= gameHeight*22.5/24 + gameHeight*2/60):
                        isTitleScreen = True
                        isLeaderboard = False
                        #because i didn't draw init...
                        charizardHealth = 200
                        blastoiseHealth = 200
                        venusaurHealth = 300
                        pikachuHealth = 100
                        mewtwoHealth = 400
                        reimuHealth = 200
                        marisaHealth = 200
                        aliceHealth = 250
                        ayaHealth = 150
                        cirnoHealth = 400
                        enemyLevel = 1
                        score = 0
                        input = ''
                        isUnsure = False
                        isInserting = False
                        isOnePlayer = False
                        isTwoPlayer = False
                        isTouhou = False
                        isPokemon = False
                        timePassed = 0
                        players = []
                        player1 = None
                        player2 = None
                        tempPlayers = []
                        touPProjs = []
                        pokePProjs = []
                        touEProjs = []
                        pokeEProjs = []
                        enemies = []
                        powerUps = []
                        powerUpTs = []
                        touBools = [False]*5
                        pokeBools = [False]*5
                        touSelectBools = [False]*5
                        pokeSelectBools = [False]*5
                        isSelectingAnother = False
                        isAttacking = True
                        pokeEBools = [[False]*5 for i in range(5)]
                        touEBools = [[False]*5 for i in range(5)]
                        musicCount = 0
                        
            elif event.type == pygame.QUIT:
                run = False
                Mixer.music.stop()
    
    redrawGameWindow()


### Sources

#images found in these sites:
#https://www.spriters-resource.com/pc_computer/T.html
#https://www.spriters-resource.com/pc_computer/shintouhoumusou/
#https://www.spriters-resource.com/ds_dsi/
#https://www.spriters-
# resource.com/ds_dsi/pokemonmysterydungeonexplorersofsky/
