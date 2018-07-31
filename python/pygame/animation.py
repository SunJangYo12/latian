import pygame , sys
from pygame.locals import *
import time

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
# soundOBJ = pygame.mixer.Sound('sound/love.wav') # sound
pygame.mixer.music.load('sound/love_moment.mp3') # background music
pygame.mixer.music.play(-1, 0.0)
pygame.display.set_caption('Animation')
WHITE = (255, 255, 255)
orangIMG = pygame.image.load('img/icon.png')
orangx = 10
orangy = 10
direction = 'right'
#soundOBJ.play()
#time.sleep(1)

# main
while True:
	DISPLAYSURF.fill(WHITE)
	if direction == 'right':
		orangx += 5
		if orangx == 280:
			direction = 'down'
	elif direction == 'down':
		orangy += 5
		if orangy == 220:
			direction = 'left'
	elif direction == 'left':
                orangx -= 5
                if orangx == 10:
                        direction = 'up'
	elif direction == 'up':
                orangy -= 5
                if orangy == 10:
                        direction = 'right'
	DISPLAYSURF.blit(orangIMG, (orangx, orangy))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			#soundOBJ.stop()
			pygame.mixer.music.stop()
	pygame.display.update()
	fpsClock.tick(FPS)
