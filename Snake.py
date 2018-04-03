import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Variables
window_size = width,height = 720,600 # setting the window size
score = 0
scoreHOLD = 0
DIRECTION = 'RIGHT'
CHANGE_TO = DIRECTION
FoodSPAWN = True
foodPos = [random.randrange(1,width/10)*10,random.randrange(1,height/10)*10]
fps = 10
gameON = True
# Colors
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

gameSurface = pygame.display.set_mode(window_size) # creating the surface with defined window size
pygame.display.set_caption('Snake Game')

# Functions
def showScore(score):
	sFont = pygame.font.SysFont('monaco', 40)
	sSurf = sFont.render("The score: {0}".format(score),True,black)
	sRect = sSurf.get_rect()
	gameSurface.blit(sSurf,sRect)

def gameOver(score):
	gFont = pygame.font.SysFont('monaco',80)
	gSurf = gFont.render('Game Over! ' + str(score),True, red)
	gRect = gSurf.get_rect()
	gameSurface.blit(gSurf,gRect)
	pygame.display.update()

fpsController = pygame.time.Clock()

snakePos = [360,300]
snakeBody = [[360,300],[350,300],[340,300]]

# Draw Snake

while gameON:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				CHANGE_TO = 'RIGHT'

			elif event.key == pygame.K_LEFT or event.key == ord('a'):
				CHANGE_TO = 'LEFT'

			elif event.key == pygame.K_UP or event.key == ord('w'):
				CHANGE_TO = 'UP'

			elif event.key == pygame.K_DOWN or event.key == ord('s'):
				CHANGE_TO = 'DOWN'

			elif event.type == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	if CHANGE_TO == 'RIGHT' and not DIRECTION == 'LEFT':
		DIRECTION = 'RIGHT'
	if CHANGE_TO == 'LEFT' and not DIRECTION == 'RIGHT':
		DIRECTION = 'LEFT'
	if CHANGE_TO == 'UP' and not DIRECTION == 'DOWN':
		DIRECTION = 'UP'
	if CHANGE_TO == 'DOWN' and not DIRECTION == 'UP':
		DIRECTION = 'DOWN'

	if DIRECTION == 'RIGHT':
		snakePos[0] += 10
	if DIRECTION == 'LEFT':
		snakePos[0] -= 10
	if DIRECTION == 'UP':
		snakePos[1] -= 10
	if DIRECTION == 'DOWN':
		snakePos[1] += 10

	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		score += 1
		FoodSPAWN = False
	else:
		del snakeBody[-1]

	if FoodSPAWN == False:
		foodPos = [random.randrange(1,width/10)*10,random.randrange(1,height/10)*10]
	FoodSPAWN = True

	gameSurface.fill(white)

	for pos in snakeBody:
		pygame.draw.rect(gameSurface, green, pygame.Rect(pos[0],pos[1],10,10))
	pygame.draw.rect(gameSurface, red, pygame.Rect(foodPos[0],foodPos[1],10,10))

	showScore(score)
	pygame.display.flip()
	if score%20 == 0 and not score == 0:
		if not scoreHOLD == score:
			fps+=5
			scoreHOLD = score
	# Boundries

	if snakePos[0] == 0 or snakePos[1] == 0:
		gameOver(score)
		gameON = False
	if snakePos[0] == width or snakePos[1] == height:
		gameOver(score)
		gameON = False

	fpsController.tick(fps)
	print(str(snakePos[0]) + " ")
	print(snakePos[1])