import pygame
background_color = (0,130,23)
screen = pygame.display.set_mode((750, 1000))
pygame.display.set_caption("Gonki")
screen.fill(background_color)
pygame.display.flip()
car = pygame.image.load(r'C:\Users\E\Documents\GitHub\Gonki\car.png')
running = True
while running:
    display_surface.blit(image, (0,0))
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            running = False