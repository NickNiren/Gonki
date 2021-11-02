import pygame
background_color = (0,130,23)
screen = pygame.display.set_mode((750, 1000))
pygame.display.set_caption("Gonki")
screen.fill(background_color)
pygame.display.flip()
#car
car = pygame.Surface((50,100))
playerX = 300
carImage = pygame.image.load("car.png")
carBox = pygame.Rect(0, 0, 50, 100)
#main loop
running = True
while running:
    screen.fill(background_color)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
            playerX -= .5
    if keys[pygame.K_d]:
            playerX += .5

    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            running = False
    car.blit(carImage, (0,0))
    car.blit(carBox, (0,0))
    screen.blit(car, (playerX,650))
    if playerX <= 0:
        playerX = 0
    elif playerX >= 700:
        playerX = 700
    pygame.display.update()