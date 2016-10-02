import pygame,sys ,random, time
from pygame.locals import *

WINDOWHEIGHT = 240
WINDOWWIDTH = 480
ROADWIDTH = 50
#DIVIDERSPACING = 100
WHITE = (255,255,255) 
COLOR1 = (128,128,128)
COLOR2 = (128,128,0)
COLOR3 = (25,25,25)
BLUE = (0,0,128)
X1 = 70
X2 = 160
Y = 0
X_VEHICLE1 = 5 
X_VEHICLE2 = 90
X_VEHICLE3 = 175
Y_VEHICLE1 = -50
Y_VEHICLE2 = -100
Y_VEHICLE3 = -500
X_CAR = 100	 
Y_CAR = 400
def main():
	global FPS,FPSCLOCK,DISPLAY,Y,X_CAR,Y_CAR,Y_VEHICLE1,Y_VEHICLE2,Y_VEHICLE3
	pygame.init()
	FPS = 70
	FPSCLOCK = pygame.time.Clock()
	DISPLAY = pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH))
	pygame.display.set_caption("CAR GAME")
	#i = 1
	carImg = pygame.image.load("car.png")
	while True :
		DISPLAY.fill(WHITE)
		pygame.draw.rect(DISPLAY,COLOR1,(X1,Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X1,2*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X1,4*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X1,6*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X1,8*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X1,10*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X2,Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X2,2*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X2,4*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X2,6*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X2,8*ROADWIDTH+Y,10,ROADWIDTH))
		pygame.draw.rect(DISPLAY,COLOR1,(X2,10*ROADWIDTH+Y,10,ROADWIDTH))
		
		DISPLAY.blit(carImg,(X_CAR,Y_CAR))
		
		car = pygame.Rect(X_CAR,Y_CAR,42,65)
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and event.type != KEYUP:
				if pygame.key.get_pressed()[K_RIGHT]:
					pygame.draw.rect(DISPLAY,COLOR2,(X_CAR,Y_CAR,60,ROADWIDTH/(1.5)))
					X_CAR = X_CAR + 10
				elif pygame.key.get_pressed()[K_LEFT]:
					X_CAR = X_CAR - 10
			pygame.display.update()
		vehicle1 = pygame.draw.rect(DISPLAY,COLOR3,(X_VEHICLE1,Y_VEHICLE1,65,50))
		vehicle2 = pygame.draw.rect(DISPLAY,COLOR3,(X_VEHICLE2,Y_VEHICLE2,65,50))
		vehicle3 = pygame.draw.rect(DISPLAY,COLOR3,(X_VEHICLE3,Y_VEHICLE3,65,50))
		pygame.display.update()
		if Y<40 :
			Y=Y+1
		else:
			Y = Y-100
		speed_vehicle1 = random.randint(1,3)
		speed_vehicle2 = random.randint(1,3)
		speed_vehicle3 = random.randint(1,3)
		Y_VEHICLE1 = Y_VEHICLE1 + speed_vehicle1
		Y_VEHICLE3 = Y_VEHICLE3 + speed_vehicle3
		Y_VEHICLE2 = Y_VEHICLE2 + speed_vehicle2
		fontObj = pygame.font.Font("freesansbold.ttf",17)
		
		if Y_VEHICLE1 >480 :
			Y_VEHICLE1 = -50
		if Y_VEHICLE2 > 480 :
			Y_VEHICLE2 = -100
		if Y_VEHICLE3 > 480 :
			Y_VEHICLE3 = -200
		if vehicle1.bottom == car.top and ((car.right <= vehicle1.right and car.right >= vehicle1.left) or (car.left >= vehicle1.left and car.left <= vehicle1.right)):
			DISPLAY.fill((0,0,0))
			textsurface = fontObj.render("Car Craashed in 1st lane!!",True,WHITE,BLUE)
			textrect = textsurface.get_rect()
			textrect.center = (120,240)
			DISPLAY.blit(textsurface,textrect)
			pygame.display.update()
			time.sleep(5)
			pygame.quit()
		elif vehicle2.bottom == car.top and ((car.right <= vehicle2.right and car.right >= vehicle2.left) or (car.left >= vehicle2.left and car.left <= vehicle2.right)):
			DISPLAY.fill((0,0,0))
			textsurface = fontObj.render("Car Craashed in 2nd lane!!",True,WHITE,BLUE)
			textrect = textsurface.get_rect()
			textrect.center = (120,240)
			DISPLAY.blit(textsurface,textrect)
			pygame.display.update()
			time.sleep(5)
			pygame.quit()
		elif vehicle3.bottom == car.top and ((car.right <= vehicle3.right and car.right >= vehicle3.left) or (car.left >= vehicle3.left and car.left <= vehicle3.right)):
			DISPLAY.fill((0,0,0))
			textsurface = fontObj.render("Car Craashed in 3rd lane!!",True,WHITE,BLUE)
			textrect = textsurface.get_rect()
			textrect.center = (120,240)
			DISPLAY.blit(textsurface,textrect)
			pygame.display.update()
			time.sleep(5)
			pygame.quit()
		FPSCLOCK.tick(FPS+10)
		
	
if __name__ == '__main__':
	main()