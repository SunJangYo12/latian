import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('ini font')
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 128)

fontOBJ = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceOBJ = fontOBJ.render('hello word!', True, GREEN, BLUE)
textRectOBJ = textSurfaceOBJ.get_rect()
textRectOBJ.center = (200 ,150)

# main
while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceOBJ, textRectOBJ)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
