import sys

import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen to initial dimension
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000 # Gives player a smooth movement
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    # Containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shoots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    # Create objects
    asteroid_field = AsteroidField()
    player = Player(x, y)
    
    while True:
        # Event listener to close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Updates sprite
        for sprite in updatable:
            sprite.update(dt)

        screen.fill("black")
        
        # Draws sprite
        for sprite in drawable:
            sprite.draw(screen)

        # Detect collision
        for asteroid in asteroids:
            if asteroid.collision_with(player):
                print("Game Over!")
                sys.exit(1)

            for shot in shoots:
                if asteroid.collision_with(shot):
                    asteroid.split()
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip()

        clock.tick(60) # -> Limit FPS to 60



if __name__ == "__main__":
    main()