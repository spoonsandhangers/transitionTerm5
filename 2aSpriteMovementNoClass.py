"""
the frame rate and clock are set up - inside the while loop clock tick is added
variables for x and y and dx and dy are set.
each time the frame is drawn the players position is updated.
Why does this mean that the player is a blur?
How can we fix this?
How can we stop the image leaving the screen on the right?
How can we make the image reappear on the left?
How can we move the sprite up or down instead of left and right?

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
	rect.center = (x,y)

	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False



	# draw the screen
	screen.blit(player, rect)
	pygame.display.flip()

pygame.QUIT()
