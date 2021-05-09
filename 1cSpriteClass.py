"""
A class is a blueprint that you can use to create lots of different
instances of an object.
Using this class we can create as many players as we want using only one line of code.
Each player will be initialised by the __init__ constructor method.
To create a player you pass in the x and y coordinates as well as the scale factor.
2 players are created on lines 37 and 38.

In the __init__ method each variable has self. in front of it.
when using these variables inside the class you must always use the self. in front of them
You can access them outside the class by using the objects name then a . then the variable.
e.g. player.rect or player.image

1. Create 2 new players at different places on the screen.  Make sure they are visible when
the program runs.
"""
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('myGame')


class MySprite(pygame.sprite.Sprite):
	def __init__(self, x, y, scale):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/player/idle/alien1.png')
		self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)


player = MySprite(200, 200, 0.5)
player2 = MySprite(400, 400, 0.5)


run = True

while run:

	screen.blit(player.image, player.rect)
	screen.blit(player2.image, player2.rect)


	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.QUIT()
