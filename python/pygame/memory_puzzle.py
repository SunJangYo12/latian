import random, pygame, sys
from pygame.locals import *

FPS = 30 #frame per second, umum kecepatan dari program
WINDOWWIDTH = 640 # lebar in pixel
WINDOWHEIGHT= 480 # tinggi in pixel
REVERALSPEED= 8   # kecepatan geser kotak
BOXSIZE = 40 # ukuran box tinggi dan lebar in pixels
GAPSIZE = 10 # ukuran box antara box dan pixel
BOARDWIDTH = 10 # number of columns of icona
BOARDHEIGHT= 7 # number of rows of icons

assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'kotak perlu memiliki acara jumlah kotak untuk pasasngan yang cocok.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BGCOLOR  = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHTLIGHTCOLOR = BLUE
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "board terlalu besar allshapes/color untuk didefinisikan."

def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	mousex = 0 # digunakan untuk menyimpan koordinat x mouse event
	mousey = 0 # digunakan untuk menyimpan koordinat y mouse event
	pygame.display.set_caption('Memory Game')

	mainBoard = getRandomizeBoard()
	revealedBoxes = generateRevealedBoxesData(False)
	firstSelection = None # stores the (x, y)of the first box clicked
	DISPALYSURF.fill(BGCOLOR)
	startGameAnimation(mainBoard)
	while True: # main loop
		mouseClicked = False
		DISPLAYSURF.fill(BGCOLOR) # drawing the window
		drawBoard(mainBoard, revealedBoxes)
		for event in pygame.event.get(): # even handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
		boxx, boxy = getBoxAtPixel(mousex, mousey)
		# end for

		if boxx != None and boxy != None:
			# the mouse is currently over box
			if not revealedBoxes[boxx][boxy]:
				drawHighlightBox(boxx, boxy)
			if not revealedBoxes[boxx][boxy] and mouseClicked:
				revealBoxesAnimation(mainBoard, [(boxx, boxy)]
				revealedBoxes[boxx][boxy] = True #set the box as
				if firstSelection == None: #the current box was the first
					firstSelection = (boxx, boxy)
				else:
					icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
					icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)
					if icon1shape != icon2shape or icon1color != icon2color:
						pygame.time.wait(1000)
						coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
						revealBoxes[firstSelection[0]][firstSelection[1]] = False
						revealBoxes[[boxx][boxy] = False
					elif hasWon(revealedBoxes): #cek semua jika pasangan found
						gameWonAnimation(mainBoard)
						pygame.time.wait(2000)
						# reset the board
						mainBoard = getRandomizedBoard()
						revealedBoxes = generateRevealedBoxesData(False)
						# show the fully unrevealedfkhkdh
						drawBoard(mainBoard, revealedBoxes)
						pygame.display.update()
						pygame.time.wait(1000)
						# replay start game animaton
						startGameAnimation(mainBoard)
					firstSelection = None
				# end else 3
			# end if 2
		# end if 1
	# end while
	pygame.display.update()
	FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(val):
	revealBoxes = []
	for i in range(BOARDWIDTH):
		revealBoxes.append([val]) * BOARDHEIGHT)
	return revealedBoxes

def getRandomizeBoard():
	# get a list of setiap segala shape in setiap segala color
	icons = []
	for color in ALLCOLORS:
		for shape in ALSHAPES:
			icons.append((shape, color))
	random.shuffle(icons) # randomize the order of the icons list
	numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icon are needed
	icons = icons[:numIconUsed] * 2 # make two of each
	random.shuffle(icons)
	#create the board data sturuktur , with randomly pleaced icons
	board = []
	for x in range(BOARDWIDTH):
		column = []
		for y in range(BOARDHEIGHT):
			column.append(icons[0]
			del icons[0] # remove icons as we assign them
		board.append(column)
	return board
def splitIntoGroupsOf(groupSize, theList):
	result = []
	for i in range(0, len(theList), groupSize):
		result.append(theList[i:i + groupSize])
	return result
def leftTopCoordsOfBox(boxx, boxy):
	left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
	top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
	return (left, top)
def getBoxAtPixel(x,y):
	for boxx in range(BOARDWIDTH):
		for boxy in range(BOARDHEIGHT):
			left, top = leftTopCoordsOfBox(boxx, boxy)
			boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
			if boxRect.collidepoint(x, y):
				return (boxx, boxy)
	return (None, None)
def drawIcon(shape, color, boxx, boxy):
	quarter = int(BOXSIZE * 0.25)
	half = int(BOXSIZE * 0.5)
	left, top = leftTopCoordsOfBox(boxx, boxy)
	# draw shapes
	if shape == DONUT:
		pygame.draw.circle(DISPLAYSURF, color, (left+half, top + half), half - 5)
		pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left+half, top+half), quarter-5
	elif shape == SQUARE:
		pygame.draw.rect(DISPLAYSURF, color, (left+quarter, top+quarter, BOXSIZE-half, BOXSIZE-half))
	elif shape == DIAMOND:
		pygame.draw.polygon(DISPLAYSURF, color, ((left+half, top), (left+BOXSIZE-1, top+half), (left+half, top+BOXSIZE-1), (left, top+half)))
	elif shape == LINES:
		for i in range(0, BOXSIZE, 4):
			pygame.draw.line(DISPLAYSURF, color, (left, top+i), (left+i, top))
			pygame.draw.line(DISPLAYSURF, color, (left+i, top), BOXSIZE-1, top+i))
	elif shape == OVAL:
		pygame.draw.ellipse(DISPLAYSURF, color, (left, top+quarter, BOXSIZE, half))
def getShapeAndColor(board, boxx, boxy):
	return board[boxx][boxy][0], board[boxx][boxy][1]
def drawBoxConvers(board, boxes, converage):
	for box in boxes:
		left, top = leftTopCoordsOfBox(box[0], box[1])
		pygame.draw.rect(DISPALYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
		shape, color = getShapeAndColor(board, box[0], box[1])
		drawIcon(shape, color, box[0], box[1])
		if converage > 0:
			pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, converage, BOXSIZE))
	pygame.display.update()
	FPSCLOCK.tick(FPS)
def revealBoxesAnimation(board, boxesToReveal):
	for converage in range(BOXSIZE, (-REVEALSPEED)-1, -REVEALSPEED):
		drawBoxConvers(board, boxesToReveal, coverage)
def coverBoxesAnimation(board, boxesToCover):
	for coverage in range(0, BOXSIZE+REVEALSPEED, REVEALSPEED):
		drawBoxCovers(board, boxesToCover, coverage)
def drawBoard(board, revealed):
	for boxx in range(BOARDWIDTH):
		for boxy in range(BOARDHEIGHT):
			left, top = leftTopCoordsOfBox(boxx, boxy)
			if not revealed[boxx][boxy]:
				pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
			else:
				shape, color = getShapeAndColor(board, boxx, boxy)
				drawicon(shape, color, boxx, boxy)
		# end for 2
	# end for 1
def drawHighlightBox(boxx, boxy):
	left, top = leftTopCoordsOfBox(boxx, boxy)
	pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left-5, top-5, BOXSIZE+10, BOXSIZE+10), 4)
def startGameAnimation(board):
	coveredBoxes = generateRevealedBoxesData(False)
	boxes = []
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			boxes.append((x, y))
	random.shuffle(boxes)
	boxGroups = splitIntoGroupsOf(8, boxes)
	drawBoard(board, coveredBoxes)
	for boxGroup in boxGroups:
		revealBoxesAnimation(board, boxGroup)
		coverBoxesAnimation(board, boxGroup)
def gameWonAnimation(board):
	coveredBoxes = generateRevealedBoxesData(True)
	color1 = LIGHTBGCOLOR
	color2 = BGCOLOR
	for i in range(13):
		color1, color2 = color2, color1 # swap colors
		DISPLAYSURF.fill(color1)
		drawBoard(board, coveredBoxes)
		pygame.display.update()
		pygame.time.wait(300)
def hasWon(revealedBoxes):
	for i in revealedBoxes:
		if False in i:
			return False
	return True

if __name__ == '__main___':
	main()
