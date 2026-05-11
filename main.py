from asteroid import Asteroid
from player import Player
import pygame
import sys
from logger import log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_RADIUS, PLAYER_SPEED, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED
from logger import log_state
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"""Starting Asteroid Game...
    Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}""")
    
    #Create the groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Adding the new instances to the groups via player class.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    #only updatable group is needed for the asteroid field, since it doesn't have a draw function
    AsteroidField.containers = (updatable,)

    #instantiate a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #AsteroidField object instance, which will handle the spawning of asteroids
    asteroid_field = AsteroidField()
    
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #FPS = 60
    pygame.time.Clock()
    dt = 0
    
    #Creating two groups
    # main_group = pygame.sprite.Group(updatable, drawable)
    #Creating group for asteroid
    asteroid_group = pygame.sprite.Group()
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        log_state()
        screen.fill("black")
        #hook the update function to the player object, so that it can handle input and update its state
        # player.update(dt)
        updatable.update(dt)
        #Check for collisions between the player and asteroids:
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                
        #New loop for collisons between bullets and asteroids!:
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    #call split asteroid method
                    asteroid.split()
        #need to render the player, before flipping the display to show the changes(now loooping over the group instead)
        # player.draw(screen)
        #Explicitly only drawable group
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000.0  # Convert milliseconds to seconds
        # print(f"Delta time: {dt:.4f} seconds")
    

if __name__ == "__main__":
    main()