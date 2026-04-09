import pygame
from logger import log_state
from player import Player
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
    yourPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        yourPlayer.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60)/1000
        # print(dt)

if __name__ == "__main__":
    main()
