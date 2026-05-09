from player import Player
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_RADIUS
from player import Player
from logger import log_state

def main():
    print(f"""Starting Asteroid Game...
    Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}""")
    
    #instantiate a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #FPS = 60
    pygame.time.Clock()
    dt = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        log_state()
        screen.fill("black")
        #hook the update function to the player object, so that it can handle input and update its state
        player.update(dt)
        #need to render the player, before flipping the display to show the changes
        player.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000.0  # Convert milliseconds to seconds
        # print(f"Delta time: {dt:.4f} seconds")
    

if __name__ == "__main__":
    main()