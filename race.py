import pygame
background_color = (0,130,23)
screen = pygame.display.set_mode((750, 1000))
pygame.display.set_caption("Gonki")
screen.fill(background_color)
pygame.display.flip()

running = True
while running:
    
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            running = False