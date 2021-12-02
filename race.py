import pygame, sys
from pygame.locals import *
import time, random
import threading

# some fundamental stuff
pygame.init()
FramePerSec = pygame.time.Clock()
background_color = (0,130,23)
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Gonki")
#screen.fill(background_color)
pygame.display.flip()
clock = pygame.time.Clock()
score = 0
track = pygame.image.load("track1.png")
trackY = 0

#fonts
font = pygame.font.Font(None, 50)
subFont = pygame.font.Font(None, 20)
dead = font.render("GAME OVER", True, "Red")

#car
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (50, 500)
    def move(self):
        keys = pygame.key.get_pressed()
        # retrieves the coordinates of the left corner
        # spirte's rectangle
        # to make sure it is in the window still. 
        if self.rect.left > 0:
            if keys[pygame.K_a]:
                    self.rect.move_ip(-3, 0)
        # same thing but it's with the right corner
        # of the rectangle
        if self.rect.right < 400:
            if keys[pygame.K_d]:
                    self.rect.move_ip(3, 0)
#rocks
class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, 600), (0 - random.randint(300,900)))

    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 200), 0)

# creating variables for our classes
rock = [Rocks() for _ in range(5)]
#I have no idea how the for loop above makes unique rock objects, but stackover user
#Greg Hewgill did at https://stackoverflow.com/questions/1807026/initialize-a-list-of-objects-in-python
user = Player()
# we can add more obstacles / enemies in this group
obstacles = pygame.sprite.Group()
obstacles.add(rock)
# grouping ALL sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(user)
all_sprites.add(rock)
def nextTrack():
    rand = random.randint(1,10)
    #i wish python had switches. idk maybe it does, but not like c# :(
    if(rand == 1):
        nextT = pygame.image.load("track1.png")
    if(rand == 2):
        nextT = pygame.image.load("track2.png")
    if(rand == 3):
        nextT = pygame.image.load("track3.png")
    if(rand == 4):
        nextT = pygame.image.load("track4.png")
    if(rand == 5):
        nextT = pygame.image.load("track5.png")
    if(rand == 6):
        nextT = pygame.image.load("track6.png")
    if(rand == 7):
        nextT = pygame.image.load("track7.png")
    if(rand == 8):
        nextT = pygame.image.load("track8.png")
    if(rand == 9):
        nextT = pygame.image.load("track9.png")
    if(rand == 10):
        nextT = pygame.image.load("track10.png")
    return nextT
speed = 1
def scrollBackground():
    global trackY
    trackY += speed
    screen.blit(track, (0,trackY))
    try:
        screen.blit(nextT, (0,trackY - 600)) 
    except:
        pass
    return trackY
first = True
scoreFactor = 1
#main loop
running = True
while running:  
    clock.tick(320)
    try:
        pixel_col = pygame.Surface.get_at(screen, (user.rect.right, 500))
    except:
        pass
    #print(pixel_col)
    if pixel_col == (34, 177, 76, 255):
        print("SLOWED")
        scoreFactor = 0
    else:
        scoreFactor = 1
    score += round((speed * scoreFactor), 1)
    screen.fill((0,0,0))
    scrollBackground()
    if ((trackY) > 600 or first == True):
        first = False
        try:
            track = nextT
        except:
            pass
        speed += 0.1
        nextT = nextTrack()   
        trackY = 0
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            running = False   
    # THIS WILL MOVE THE SPRITES + its hitboxes
    # it's so short and sexy mmmm
    for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()
    # if collision occurs with the user and obstacle
    if pygame.sprite.spritecollideany(user, obstacles):
          screen.fill("Black")
          screen.blit(dead, (100, 250))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          running = False
          sys.exit() 
    leaderboard = subFont.render("Score: " + str(score), True, "Black")
    speedL = subFont.render("Speed: " + str(round(speed, 1)), True, "Black")
    screen.blit(leaderboard, (10, 10))  
    screen.blit(speedL, (10, 20))         
    pygame.display.update()