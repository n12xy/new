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
SecondMaze = False
ThirdMaze = False

#filling screen
screen.fill(BLACK)

##Images found on intro screen
#loading images into rect
introScreenBackgroundImage = pygame.image.load("introscreenBG.jpg")
introScreenBackgroundRect = introScreenBackgroundImage.get_rect()

#image for walking man
walking = pygame.image.load("WalkingImage.png")
walkingRect=walking.get_rect()
walkingRect.x = 100
walkingRect.y = 600
walkingdx = 2
walkingdy =0

#loading images into rect
forestImage = pygame.image.load("forestlegendbanner1.jpg")
forestRect = forestImage.get_rect()
legendImage = pygame.image.load("forestlegendbanner2.jpg")
legendRect = legendImage.get_rect()

#locations for text images
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
                elif event.key == pygame.K_1:
                    intro = False
                    FirstMaze = True
                elif event.key == pygame.K_2:
                    intro = False
                    SecondMaze = True
                elif event.key == pygame.K_3:
                    ThirdMaze = True
                    intro = False
            #adding click to change screen to get to buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #button for first maze
                if 297 <= mouse[0] <= 482 and 309 <= mouse[1] <= 348:
                    intro = False
                    final = True
                #Button for seconds maze
                elif 297 <= mouse[0] <= 484 and 361 <= mouse[1] <= 398:
                    intro = False
                    SecondMaze = True
                elif 297 <= mouse[0] <= 483 and 410 <= mouse[1] <= 448:
                    intro = False
                    ThirdMaze = True

        #code for screen design : images, text, etc.
        clock.tick(FPS)
        #loading image onto screen
        screen.blit(introScreenBackgroundImage,introScreenBackgroundRect)
        screen.blit(forestImage, forestRect)
        screen.blit(legendImage,legendRect)

        #loading image into screen
        screen.blit(walking,walkingRect)
        walkingRect.move_ip(walkingdx,walkingdy)

        #if statements to prevent wall hits
        if walkingRect.x >= 600:
            walkingdx = -walkingdx

        #Adding play buttons
        #Maze 1
        #Rendering/adding rect/location,drawing background rectangle
        level1Text = fontTitle3.render("Maze 1",False,GREEN)
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

        #Maze 2
        #Rendering/adding rect/location,drawing background rectangle
        level2Text = fontTitle3.render("Maze 2",False,GREEN)
        level2Rect = level2Text.get_rect()
        level2Rect.center = (centreX,380)
        pygame.draw.rect(screen,WHITE,level2Rect,0)
        
        #changing color if hovered on
        if 297 <= mouse[0] <= 484 and 361 <= mouse[1] <= 398:
            pygame.draw.rect(screen,colorlight,level2Rect,0)
        else:
            pygame.draw.rect(screen,WHITE,level2Rect,0)
        #Blitting text into rect
        screen.blit(level2Text,level2Rect)

        #Maze 3
        #Rendering/adding rect/location,drawing background rectangle
        level3Text = fontTitle3.render("Maze 3",False,GREEN)
        level3Rect = level3Text.get_rect()
        level3Rect.center = (centreX,430)
        pygame.draw.rect(screen,WHITE,level3Rect,0)
        
        #changing color if hovered on
        if 297 <= mouse[0] <= 483 and 410 <= mouse[1] <= 448:
            pygame.draw.rect(screen,colorlight,level3Rect,0)
        else:
            pygame.draw.rect(screen,WHITE,level3Rect,0)
        #Blitting text into rect
        screen.blit(level3Text,level3Rect)
        pygame.display.flip()

#code for maze 1 goes here
    while FirstMaze :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                main = False
                FirstMaze = False

        #screen design for first maze goes here
        screen.fill(RED)
        pygame.display.update()
                
#code for maze 2
    while SecondMaze :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                main = False
                SecondMaze = False


        #screen design for second maze goes here
        screen.fill(RED)
        pygame.display.update()
                
#code for maze 3               
    while ThirdMaze:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                main = False
                ThirdMaze = False
                
        #screen design for third maze goes here
        screen.fill(RED)
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
                    
