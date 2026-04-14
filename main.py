import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

image = pygame.image.load('assests/images/AustraliaImage.png')

# scale image to fit window
image = pygame.transform.smoothscale(image, (800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()