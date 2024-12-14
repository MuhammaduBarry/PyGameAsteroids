import pygame

from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen to initial dimension
    clock = pygame.time.Clock()


    while True:
        # Event listener to close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60) # -> Limit FPS to 60



if __name__ == "__main__":
    main()