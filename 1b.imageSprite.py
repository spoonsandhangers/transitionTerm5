"""
1. what variable references the sprite image?
2. what line adds the sprite to the screen?
3. what line updates the whole of the pygame display?
4. Add another sprite to the screen at a different location.
5. If you have to this each time you created a player or a badie do you think it would become time consuming?

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


run = True

while run:

	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	# draw the screen
	screen.blit(img, rect)
	pygame.display.flip()

pygame.QUIT()
