"""
Here there are 2 new methods in the MySprite class getxPos() and getyPos()
also the frame rate and clock are set up - inside the while loop clock tick is added
variables for x and y and dx and dy are set.
each time the frame is drawn the players position is updated.
Why does this mean that the player is a blur?
How can we fix this?
How can we stop the image leaving the screen on the right?
How can we make the image reappear on the left?
How can we move the sprite up or down instead of left and right?
extension - can you create a move method that is included in the soldier class?
"""
import pygame

pygame.init()

# set frame rate and initialise clock
clock = pygame.time.Clock()
FPS = 60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('myGame')

x = 0
y = 0

# change in x and y
dx = 4
dy = 0


class MySprite(pygame.sprite.Sprite):
	def __init__(self, x, y, scale):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/player/idle/alien1.png')
		self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def draw(self):
		screen.blit(self.image, self.rect)

	def getxPos(self):
		return self.rect.center[0]

	def getyPos(self):
		return self.rect.center[1]



player = MySprite(200, 200, 0.5)
player2 = MySprite(400, 400, 0.5)


run = True

while run:
	clock.tick(FPS)
	x = player.getxPos() + dx
	y = player.getyPos() + dy

	player.rect.center = (x,y)
	player.draw()
	player2.draw()


	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.QUIT()
