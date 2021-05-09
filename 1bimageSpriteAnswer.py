"""

"""
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('myGameSprite')

# picture being loaded
x = 200
y = 200
scale = 0.5
img = pygame.image.load('img/player/idle/alien0.png')
# what does this line do?
img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
rect = img.get_rect()
rect.center = (x, y)

img2 = pygame.image.load('img/player/idle/alien1.png')
img2 = pygame.transform.scale(img2, (int(img2.get_width() * scale), int(img2.get_height() * scale)))
rect2 = img2.get_rect()
rect2.center = (200, 400)


run = True

while run:

	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	# draw the screen
	screen.blit(img, rect)
	screen.blit(img2, rect2)
	pygame.display.flip()

pygame.QUIT()
