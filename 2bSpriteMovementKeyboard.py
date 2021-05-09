"""

"""
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

# set frame rate and initialise clock
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('myGameSprite')

# picture being loaded
# initial sprite location
x = 200
y = 200

# change in x and y
# to speed the sprite up increase the value of dx or dy
# to slow the sprite down decrease the value of dx or dy
dx = 5
dy = 0

# sprite scaling
scale = 0.5
# sprite image being loaded
player = pygame.image.load('img/player/idle/alien0.png')
# image scaled
player = pygame.transform.scale(player, (int(player.get_width() * scale), int(player.get_height() * scale)))
# rect associated with the sprite
rect = player.get_rect()
# sprite positioned
rect.center = (x, y)


run = True

while run:

	clock.tick(FPS)

	x += dx

	# if x becomes larger than the screen width it is set back to 20
	# this makes it appear on the left hand side of the screen
	if x > SCREEN_WIDTH:
		x = 20

	rect.center = (x,y)

	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False





	# draw the screen
	# this redraws the background of the screen
	# and stops the sprite looking blurred
	screen.fill((0,0,0))
	screen.blit(player, rect)
	pygame.display.flip()

pygame.QUIT()
