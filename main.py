
import pygame
import sys

from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    score = 0
    dt = 0

    pygame.font.init()
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)
    Player.containers = (updatables, drawables)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="black")
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        updatables.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    
                    asteroid.split()
                    shot.kill()
                    score += ASTEROID_POINTS
                    break

            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit()
            

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
