import pygame
import time
import random
import threading
import sys
reroll = True

background_color = (0,130,23)
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Gonki")
screen.fill(background_color)
pygame.display.flip()
#car
car = pygame.Surface((50,100))
playerX = 300
carImage = pygame.image.load("car.png")
carBox = pygame.Rect(0, 0, 50, 100)
#rocks
class Rocks:
    rock = pygame.Surface(((50,50)), pygame.SRCALPHA)
    rockBox = pygame.draw.circle(rock, (128,128,128), (25,25), 25)
    def __init__(self):       
        self.rockX = random.randint(25,375)
        self.rockY = random.randint(25,200)    
def initRocks():
    rock1 = Rocks()
    rock2 = Rocks()
    rock3 = Rocks()
    rockList = [rock1, rock2, rock3]
    global reroll
    reroll = False
    return rockList
def moveRock(rockList):
    #this function sucks, but we'll fix it later (maybe)
    for y in range(2000):
        screen.blit(rockList[0].rock, (rockList[0].rockX, rockList[0].rockY))
        screen.blit(rockList[1].rock, (rockList[1].rockX, rockList[1].rockY))
        screen.blit(rockList[2].rock, (rockList[2].rockX, rockList[2].rockY))
        for x in rockList:
            x.rockY += 0.1
def rockTimer(end):
  tim = threading.Timer(3.0,rockTimer(False)).start()
  print("poopoo")
  if end == True:
      tim.cancel()
rockTimer(False)
#main loop
running = True
while running:
    screen.fill(background_color)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
            playerX -= .4
    if keys[pygame.K_d]:
            playerX += .4
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            running = False
            rockTimer(True)
            pygame.display.quit()
            sys.exit()        
    car.blit(carImage, (0,0))
    screen.blit(car, (playerX,300))
    if playerX <= 0:
        playerX = 0
    elif playerX >= 350:
        playerX = 350
    pygame.display.update()