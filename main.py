import pygame, sys
from logger import log_state, log_event
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    timer = pygame.time.Clock()
    # delta time since last frame was drawn
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    yourPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    theField = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroidObject in asteroids:
            if asteroidObject.collides_with(yourPlayer):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for drawableObject in drawable:
            drawableObject.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60)/1000
        # print(dt)

if __name__ == "__main__":
    main()
