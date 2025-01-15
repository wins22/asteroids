# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroidfield = AsteroidField()
	Shot.containers = (shots, updatable, drawable)

	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	

	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for obj in updatable:
			obj.update(dt)

		# check for collisions
		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game over!")
				return
			for shot in shots:
				if shot.collides_with(asteroid):
					shot.kill()
					asteroid.split()
			
		screen.fill("black")

		# draw the player
		
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60)/1000
		

if __name__ == "__main__":
	main()
