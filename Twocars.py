import pygame
import time
import random
from pygame.locals import *
import os

pygame.init()

#Define some colors
BLACK = (0, 0, 0)

WHITE = (255, 255, 255)
Grey=(146,146,146)
Darkgreen=(9,185,28)
Green = (0, 255, 0)
Red = (255, 0, 0)
Darkred=(211,31,31)
yr=[]
yb=[]
score=0


#set screen size
size = (415,731)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Two Cars")

#to Manage screen update time
clock = pygame.time.Clock() 

#set background image
background_image=pygame.image.load("Background.jpg").convert()
background_image= pygame.transform.scale(background_image, (415,731))
screen.blit(background_image,[0,0])


#import cars
redcar= pygame.image.load("redcar.png").convert()
redcar= pygame.transform.scale(redcar, (55,110))
redcar= redcar.convert_alpha()

bluecar= pygame.image.load("bluecar.png").convert()
bluecar= pygame.transform.scale(bluecar, (55,110))
bluecar= bluecar.convert_alpha()

#import objects
redcircles= pygame.image.load("redcircles.png").convert()
redcircles= pygame.transform.scale(redcircles, (40,40))
redcircles= redcircles.convert_alpha()

bluecircles= pygame.image.load("bluecircles.png").convert()
bluecircles= pygame.transform.scale(bluecircles, (40,40))
bluecircles= bluecircles.convert_alpha()

redrectangles= pygame.image.load("redrectangles.png").convert()
redrectangles= pygame.transform.scale(redrectangles, (40,40))
redrectangles= redrectangles.convert_alpha()

bluerectangles= pygame.image.load("bluerectangles.png").convert()
bluerectangles= pygame.transform.scale(bluerectangles, (40,40))
bluerectangles= bluerectangles.convert_alpha()

objects=[redrectangles,redcircles,bluerectangles,bluecircles]
redobjects=[redrectangles,redcircles]
blueobjects=[bluerectangles,bluecircles]
rectangles=[redrectangles,bluerectangles]
circles= [bluecircles,redcircles]

#import sound
crash_sound= pygame.mixer.Sound("Crash.wav")
beep_sound= pygame.mixer.Sound("beep.wav")


#Functions

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display(text,ty,tsize):
    largeText = pygame.font.Font('freesansbold.ttf',tsize)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (415/2,ty)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)

def message(mess,color,size,x,y):
     font=pygame.font.SysFont(None,size)
     screen_text=font.render(mess,True,color)
     screen.blit(screen_text,(x,y))
     pygame.display.update()
     


def button(text,x,y,w,h,active_color,inactive_color,action):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w > cur[0] > x and y+h> cur[1] > y:
        pygame.draw.rect(screen,active_color,[x,y,w,h])
        if click[0]==1 and action!=None:
            if action=="Quit":
                pygame.quit()
            if action=="Help":
                screen.fill(BLACK)
                message_display("Take circles",200,20)
                message_display("Avoid Squares",300,20)
                message_display("Use left arrow to control red car",400,20)
                message_display("Use right arrow to control blue car",500,20)
                time.sleep(1)
                intro()
            if action== "Credits":
                screen.fill(BLACK)
                message_display("Ali Abdurahman K: B160168ME",200,20)
                message_display("Sreehari Ks: B160422ME",300,20)
                message_display("Sarang P: B160150ME",400,20)
                message_display("Karthik Kv: B160455ME",500,20)
                time.sleep(1)
                intro()
            if action=="Play":
                gameloop()
                
            
    else:
        pygame.draw.rect(screen,inactive_color,[x,y,w,h])
    font=pygame.font.SysFont(None,40)
    screen_text=font.render(text,True,BLACK)
    screen.blit(screen_text,(x+18,y+10))
    
def updateFile():
    global score
    f = open("highscore.txt",'r')
    file = f.readlines()
    high_score = int(file[0])

    if high_score < int(score):
        f.close()
        file = open("highscore.txt", 'w')
        file.write(str(score))
        file.close()
        return score               
    return high_score


def display_score(): #display final score and high score
    global score
    message_display("Your Score : " + str(score),420,30)
    message_display("Your HighScore : " + str(updateFile()),470,30)
    


def intro(): #game Home screen
    run=False
    global score
    score=0
    while run== False:
        screen.blit(background_image,[0,0])
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
        button("Play",55,350,100,50,Green,Darkgreen,action="Play")
        button("Quit",160,450,100,50,Red,Darkred,action="Quit")
        button("Help",270,350,100,50,Green,Darkgreen,action="Help")
        button("Credits",280,600,130,50,WHITE,Grey,action="Credits")
        pygame.display.update()

    


def red_obj(Robj_y,x):
    red_x = [30,135]
    global Robj_x
    global score
    if Robj_y==0:
        Robj=random.choice(redobjects)
        Robj_x = random.choice(red_x)
        yr.clear()
        yr.append(Robj)
        yr.append(Robj_x)
    else:
        Robj=yr[0]
        Robj_x= yr[1]        
    screen.blit(Robj,[Robj_x,Robj_y])
    pygame.display.update()
    
    if Robj==redobjects[0] and x==Robj_x and 520<Robj_y<630:
        pygame.mixer.Sound.play(crash_sound)
        message_display('CRASHED!',731/2,50)
        display_score()
        intro()
        pygame.display.update()
        
    if Robj==redobjects[1] and x==Robj_x and 520<Robj_y<630:
        score = score + 1
        pygame.mixer.Sound.play(beep_sound)
        yr[1]=-40
    if yr[1]!=-40 and Robj_y>630 and Robj==redobjects[1]:
        message_display('Missed a circle',731/2,50)
        display_score()
        intro()
        pygame.display.update()
    pygame.display.update()
   




def blue_obj(Bobj_y,x):
    blue_x = [250,350]
    global Bobj_x
    global score
    if Bobj_y==-100:
        Bobj=random.choice(blueobjects)
        Bobj_x = random.choice(blue_x)
        yb.clear()
        yb.append(Bobj)
        yb.append(Bobj_x)
    else:
        Bobj=yb[0]
        Bobj_x= yb[1]        

    screen.blit(Bobj,[Bobj_x,Bobj_y])
       
    if Bobj==blueobjects[0] and x==Bobj_x and 520<Bobj_y<630:
        pygame.mixer.Sound.play(crash_sound)
        message_display('CRASHED!',731/2,50)
        display_score()
        intro()
        pygame.display.update()

    if Bobj==blueobjects[1] and x==Bobj_x and 520<Bobj_y<630 :
        score = score + 1
        pygame.mixer.Sound.play(beep_sound)
        yb[1]=500
    if yb[1]!=500 and Bobj_y>630 and Bobj==blueobjects[1]:
        message_display('Missed a circle',731/2,50)
        display_score()
        intro()
        pygame.display.update()
    pygame.display.update()
        
        


def gameloop():
    
    global game_over
    global score
    game_over = False
    x = 0
    y = 1
    Robj_y = 0
    Bobj_y = -100
    red_x = [30,135]
    blue_x = [250,350]
    
    while not game_over:
        
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: 
                game_over = True
                
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_LEFT:
                    x=x^1        
                elif event.key == pygame.K_RIGHT:
                    y=y^1
        screen.fill(WHITE)
        screen.blit(background_image,[0,0])
        screen.blit(redcar,(red_x[x],550))
        screen.blit(bluecar,(blue_x[y],550))

        if Robj_y > 840:
            Robj_y = 0
        red_obj(Robj_y,red_x[x])
        Robj_y+=5

        if Bobj_y > 740:
            Bobj_y = -100
        blue_obj(Bobj_y,blue_x[y])
        Bobj_y+=5
        
        message("Score : " + str(score) , WHITE,30,300,20) 
        pygame.display.update() 
        pygame.display.flip()
        clock.tick(120)

intro()  
pygame.quit()
quit()
