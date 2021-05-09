"""
1. Add comments to this code to describe each line.
2. Change the caption/title of the window.
3. What variable controls the game loop?
4. Where is a cast used?
5. Name 2 constants used in the code.
"""
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('My Game Window')

run = True

while run:

	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

pygame.QUIT()
