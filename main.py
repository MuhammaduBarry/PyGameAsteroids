import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen to initial dimension
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000 # Gives player a smooth movement
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Player object
    player = Player(x, y)

    while True:
        # Event listener to close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Group
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        updatable.add(player)
        drawable.add(player)

        for player in updatable:
            player.update(dt)

        screen.fill("black")
        
        for player in drawable:
            player.draw(screen)

        pygame.display.flip()

        clock.tick(60) # -> Limit FPS to 60



if __name__ == "__main__":
    main()