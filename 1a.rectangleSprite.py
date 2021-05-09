"""
1. What does this code do?
2. What is the square called that appears on the screen?
3. Change the colour of the square.
4. Change the colour of the background
5. Add another square on the screen at a different position and of a different colour.
6. define a variable for your colour and use that instead of the numbers.
7. Add comments to the line that draws the squares onto the screen
8. Add comments to the lines that redraw the pygame screen.
"""
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('shooter')

x = 200
y = 200
colour = (100,20,155)
myBlock = pygame.Rect(x, y, 60, 60)


run = True

while run:

	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	# draw the screen
	screen.fill((0,0,0))
	pygame.draw.rect(screen, colour, myBlock)
	pygame.display.flip()

pygame.QUIT()
