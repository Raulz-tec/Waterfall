import pygame

pygame.init()
window = pygame.display.set_mode(size=(800, 500))

while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()  # End pygame
