# Zelda Themed Game
#Team
# Septembember 17

 
#initializing + importing pygame
import pygame
import sys

pygame.init()

#importing time for modes
import time

#importing sound mixer
from pygame import mixer
mixer.init()
mixer.music.load("intro.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#drawing surface
size = (800, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Forest Legend")

#getting screen width and height
screenWidth = screen.get_width()
screenHeight = screen.get_height()

#Setting screen centers
centreX = screenWidth / 2
centreY = screenHeight / 2

#Declaring Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
colorlight = (170, 170, 170)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#setfont
fontTitle = pygame.font.SysFont("averey", 30, True)
fontTitlegame = pygame.font.SysFont("joystix", 30, True)
fontTitle2 = pygame.font.SysFont("averey", 20, True)
fontTitle3 = pygame.font.SysFont("averey", 60, True)
fontTitle4 = pygame.font.SysFont("averey", 40, True)
fontTitleBold = pygame.font.SysFont("comicsansms", 30, bold=True)

#setting up the clock object
clock = pygame.time.Clock()
FPS = 100

# Setting loop to run the entire game
main = True
#loop within main to run the introduction screen
intro = True
#loop within main to show final screen, based on losing or winning
final = False
#loop within intro to show different game options
FirstMaze = False

###DRAWING THE MAZE Array
#creating empty array to store board
walls = []
#creating layout of board
board = [
"                                   ",
"                                   ",
"                                   ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W       W                 W       W",
"W       W                 W       W",
"W  WWW  W                 W  WWW  W",
"W  W    W    WWWWWWWWW    W    W  W",
"W  W    W                 W    W  W",
"W  W    W                 W    W  W",
"W  W           WWWW            W  W",
"W                                 W",
"W                                 W",
"W          WWW      WWW           W",
"W  WWW     W          W    WWW    W",
"W          W          W           W",
"W          W          W           W",
"W  WWW     W          W    WWW    W",
"W          WWWWWWWWWWWW           W",
"W                                 W",
"W                                 W",
"W              WWWW               W",
"W  W                           W  W",
"W  W    W                 W    W  W",
"W  W    W                 W    W  W",
"W  W    W    WWWWWWWWW    W    W  W",
"W  WWW  W                 W  WWW  W",
"W       W                 W       W",
"W       W                 W       W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

#maze code
Boardx=0
Boardy=0

#maze code
#Creating rects for board pieces
for row in board:
    for col in row:
        if col == "W":
            wallRect = pygame.Rect(Boardx,Boardy,26,23)
            walls.append(wallRect)
        Boardx += 26
    Boardy += 23
    Boardx = 0


#filling screen
screen.fill(BLACK)

##Images found on intro screen
#loading images into rect
introScreenBackgroundImage = pygame.image.load("introscreenBG.jpg")
introScreenBackgroundRect = introScreenBackgroundImage.get_rect()

#loading images into rect
forestImage = pygame.image.load("forestlegendbanner1.jpg")
forestRect = forestImage.get_rect()
legendImage = pygame.image.load("forestlegendbanner2.jpg")
legendRect = legendImage.get_rect()

#loading image of moving man on intro screen
walkImage = pygame.image.load("walkingRight.gif")
walkRect = walkImage.get_rect()
walkRect.x = 100
walkRect.y = 600
walkDx = 1
walkDy=1

#locations for text on intro screen 
legendRect.x = 400
legendRect.y= 140
forestRect.x= 75
forestRect.y= 50

#images for final screen
#loading images into rect
finalBackgroundImage = pygame.image.load("finalscreen.png")
finalBackgroundRect = introScreenBackgroundImage.get_rect()
gameoverText = pygame.image.load("gameOver.gif")
gameoverRect = gameoverText.get_rect()
gameoverRect.x= 200
gameoverRect.y= 100

#images in maze 1
dirtImage= pygame.image.load("dirt.png")
dirtRect=dirtImage.get_rect()

#adding character to screen
man = pygame.image.load("WalkingF.png")
manRect = man.get_rect()
manRect.x = 100
manRect.y=100
dx = 0
dy = 0
speed = 1

#Opening loops
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            intro = False
    while intro:
        #getting mouse coordinates saving as tuple (used later)
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                main = False
                intro = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q :
                    main = False
                    intro = False
            #adding click to change screen to get to buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #button for first maze
                if 297 <= mouse[0] <= 482 and 309 <= mouse[1] <= 348:
                    intro = False
                    FirstMaze = True
                    #resetting location
                    manRect.x = 100
                    manRect.y = 100
                    dx,dy=(0,0)


        #code for screen design : images, text, etc.
        #loading image onto screen
        screen.blit(introScreenBackgroundImage,introScreenBackgroundRect)
        screen.blit(forestImage, forestRect)
        screen.blit(legendImage,legendRect)
        screen.blit(walkImage,walkRect)
        
        #Adding play buttons
        #Maze 1
        #Rendering/adding rect/location,drawing background rectangle
        level1Text = fontTitle3.render("PLAY",False,GREEN)
        level1Rect = level1Text.get_rect()
        level1Rect.center = (centreX,330)
        pygame.draw.rect(screen,WHITE,level1Rect,0)
        #changing color if hovered on
        if 297 <= mouse[0] <= 484 and 309 <= mouse[1] <= 348:
            pygame.draw.rect(screen,colorlight,level1Rect,0)
        else:
            pygame.draw.rect(screen,WHITE,level1Rect,0)
        #Blitting text into rect
        screen.blit(level1Text,level1Rect)
        pygame.display.flip()

#code for maze 1 goes here
    while FirstMaze :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                main = False
                FirstMaze = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx = 0
                    dy = -speed
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = speed
                elif event.key == pygame.K_LEFT:
                    dx = -speed
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = speed
                    dy = 0
                elif event.key == pygame.K_e:
                    FirstMaze = False
                    final = True
                    
        #clock
        clock.tick(FPS)

        #screen design for first maze goes here
        screen.blit(dirtImage,dirtRect)
        screen.blit(man,manRect)
        manRect.move_ip(dx,dy)

        #code for bottom text
        #displaying score
        message = fontTitlegame.render("Press the 'e' key to exit",False, GREEN)
        messageRect = message.get_rect()
        messageRect.center = (400,50)
        screen.blit(message,messageRect)
        #Use arrows to navigate
        message2 = fontTitlegame.render("Use arrows to navigate, escape the maze to win",False, GREEN)
        message2Rect = message.get_rect()
        message2Rect = (200,20)
        screen.blit(message2,message2Rect)


        
        #code for maze walls
        for wall in walls :
            pygame.draw.rect(screen,GREEN,wall,3)

            #making player bounce of walls
            if manRect.colliderect(wall):  
                if dx>0:                                
                    manRect.right = wall.left 
                elif dx < 0:                           
                    manRect.left = wall.right  
                elif dy>0:                               
                    manRect.bottom = wall.top   
                elif dy<0:                              
                    manRect.top = wall.bottom
                    
        if manRect.x == 770:
            final = True
            FirstMaze = False
        
        pygame.display.update()
                
                
#code for ending screen
    while final :
        #getting mouse coordinates saving as tuple (used later)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                main = False
                final = False               
            #reaction to button click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #button to Exit
                if 297 <= mouse[0] <= 482 and 410 <= mouse[1] <= 448:
                    main = False
                    final = False
                #Button to go back to intro
                elif 297 <= mouse[0] <= 484 and 361 <= mouse[1] <= 398:
                    intro = True
                    final = False

                    
        #screen design for game over screens goes here
        screen.blit(finalBackgroundImage,finalBackgroundRect)
        screen.blit(gameoverText,gameoverRect)

        #button designs
        #Home button
        #Rendering/adding rect/location,drawing background rectangle
        homeText = fontTitle3.render("Home",False,GREEN)
        homeRect = homeText.get_rect()
        homeRect.center = (centreX,380)
        pygame.draw.rect(screen,WHITE,homeRect,0)
        
        #changing color if hovered on
        if 297 <= mouse[0] <= 484 and 361 <= mouse[1] <= 398:
            pygame.draw.rect(screen,colorlight,homeRect,0)
        else:
            pygame.draw.rect(screen,WHITE,homeRect,0)
        #Blitting text into rect
        screen.blit(homeText,homeRect)

        #exit
        #Rendering/adding rect/location,drawing background rectangle
        exitText = fontTitle3.render("Exit",False,GREEN)
        exitRect = exitText.get_rect()
        exitRect.center = (centreX,430)
        pygame.draw.rect(screen,WHITE,exitRect,0)
        
        #changing color if hovered on
        if 297 <= mouse[0] <= 483 and 410 <= mouse[1] <= 448:
            pygame.draw.rect(screen,colorlight,exitRect,0)
        else:
            pygame.draw.rect(screen,WHITE,exitRect,0)
        #Blitting text into rect
        screen.blit(exitText,exitRect)

        #screen update       
        pygame.display.update()

        

pygame.quit()
sys.exit()            
                    
