
import pygame
from constants import *
from circleshape import *
from player import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(type(screen))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while(1==1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        clock.tick(60)
        dt = (clock.tick(60)/1000)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    #print(type(screen))
if __name__ == "__main__":
    main()
