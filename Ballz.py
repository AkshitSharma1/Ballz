# Debug mode has been added.Debug data to be written in files.
# High score will be soon stored in files.

## Import all nesscary packages
import sys,ctypes
import pygame,sys,os,random,time
import os.path
from pygame.locals import *
pygame.init()
pygame.mixer.init()
# OPTIONAL TWO LINES FOR FULL SCREEN

LED = pygame.display.set_mode((500,500))#,pygame.FULLSCREEN
pygame.display.set_caption("Ballz")

#pygame.display.toggle_fullscreen()
def NewInstall():
    os.makedirs("Data")
    UserName = ""
    '''
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                 if event.key==K_a:
                    UserName+="a"
                 if event.key==K_b:
                    UserName+="b"
                 if event.key==K_c:
                    UserName+="c"
                 if event.key==K_d:
                    UserName+="d"
                 if event.key==K_e:
                    UserName+="e"
                 if event.key==K_f:
                    UserName+="f"
                 if event.key==K_g:
                    UserName+="g"
                 if event.key==K_h:
                    UserName+="h"
                 if event.key==K_i:
                    UserName+="i"
                 if event.key==K_j:
                    UserName+="j"
                 if event.key==K_k:
                    UserName+="k"
                 if event.key==K_l:
                    UserName+="l"
                 if event.key==K_m:
                    UserName+="m"
                 if event.key==K_n:
                    UserName+="n"
                 if event.key==K_o:
                    UserName+="o"
                 if event.key==K_p:
                    UserName+="p"
                 if event.key==K_q:
                    UserName+="q"
                 if event.key==K_r:
                    UserName+="r"
                 if event.key==K_s:
                    UserName+="s"
                 if event.key==K_t:
                    UserName+="t"
                 if event.key==K_u:
                    UserName+="u"
                 if event.key==K_v:
                    UserName+="v"
                 if event.key==K_w:
                    UserName+="w"
                 if event.key==K_x:
                    UserName+="x"
                 if event.key==K_y:
                    UserName+="y"
                 if event.key==K_z:
                    UserName+="z"
                 if event.key==K_BACKSPACE:
                    UserName =  UserName[:len(UserName)-1]
                 if len(UserName)==1:
                    UserName = UserName.upper()
                 if event.key==K_RETURN:
                     if len(UserName)==0:
                         NewInstall()
                 print UserName
                 '''
        
                    
if not os.path.isdir("Data"):
    NewInstall()

def Debug(Str): # This function will write text into debug.txt
    print os.getcwd()
    os.chdir("Data")
    Handle = open("debug.txt","a+")
    Handle.write(Str)
    Handle.write("\n")
    Handle.close()
    os.chdir("..")



Ball = "Img\Ball.png"
Villain = "Img\Hut.png"

global HighScore #Variable to store loaded high score IN Session

HS = open("score","a+")
Storagez = int(HS.read())
t = int(Storagez)
HighScore = t

#os.chdir("..")

#Background = pygame.image.load("bg4.jpg")
BackgroundX = 0
BackgroundY = 0

REQ = 0
Counter = 0
Score = 0
Vibration = 0

Welcome = pygame.image.load("Img\StartScreen.jpg")
font = pygame.font.SysFont("comicsansms", 72)


BG = pygame.image.load("Img\Background1.jpg").convert()


'''def Debug(Str): # This function will write text into debug.txt
    Handle = open("debug.txt","a")
    # TO DO: Introduce a method in Translate() class to encode score everytime
    Handle.write(Str)
    Handle.close()'''
Debug("-------------------------Program started------------------------ #")
Debug("Screen size: "+str(LED) +" #")


def ButtonClick(Display,Color,PosX,PosY,Height,Width):
    Button = pygame.Rect(PosX,PosY,Height,Width)
    pygame.draw.rect(Display,Color,Button)
    


def GameOver():
    pygame.mixer.music.stop()
    # Get the high score
    global HighScore
    global Score # Get this session score
    Debug("Game over! ")
    Debug("Player died with score: "+str(Score)+" #")
    Debug("\n")
    
           
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        IMG = pygame.image.load("Img\dead.png")
        dead = font.render("HIGH SCORE:", True, (255,255,255))
        
        
        LED.blit(IMG,(0,0))
        LED.blit(dead,(150,250))
        key = pygame.key.get_pressed()

        
        dead1 = font.render(""+str(HighScore + 1), True, (255,255,255))
        LED.blit(dead1,(330,250))

        if key[pygame.K_r]:
            Debug("Restarting game..")
            Bomb.setup(300)
            global Score,PREVScore,text1
         
            Score = 0

            text1 = font.render(""+str(Score),True,(0,0,0))

            global Star #start screen
            Star = False #break da loop
            break
        pygame.display.flip()
             


class Bomb(pygame.sprite.Sprite):
    
    def __init__(self):
        
        
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.Surface((50,300))
        self.image1.fill((255,255,255))
        self.rect = self.image1.get_rect()
        self.rect.x = 0
        self.rect.y = -300
      
        
     

        
    def setup(self,X):
        global REQ
        if REQ==3:
           
            self.rect.centerx = random.randrange(int(X-100),int(X+100))
            if self.rect.centerx > 450: self.rect.centerx -= random.randrange(70,180)
            if self.rect.centerx < 50: self.rect.centerx += random.randrange(200,400)
        if REQ==2:
            self.rect.x = random.randrange(int(X-50),int(X+50))
        if REQ==1:
            self.rect.x = X
        #Debug("Making the brick fall at:"+str(self.rect.x))
        RANDX = random.randrange(0,255)
        RANDY = random.randrange(0,255)
        RANDZ = random.randrange(0,255)
        
        self.image1.fill((RANDX,RANDY,RANDZ))
        
        #self.rect.centerx = random.randrange(30,470)
        self.rect.y = -300
    def update(self):
        global XPlus,XMinus
        global Counter,REQ
        if Counter == REQ:
            if REQ==1:
                self.rect.y += 2
                Counter = 0
            else:
                self.rect.y += 2
                Counter = 0
        LED.blit(self.image1,self.rect)

    def getY(self):
        return self.rect.y

    def setSHAPEX(self,X):
        self.image1 = pygame.Surface((X,100))

        



class King(pygame.sprite.Sprite):
    
    def __init__(self,Image,X,Y):
        
        
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(Image) #Load the sprite to be played from
        self.rect = self.image1.get_rect()
        self.rect.centerx = X
        self.rect.bottom = Y
        self.speedx = 0
        self.speedy = 0

        
    def update(self):
        global REQ
        global BackgroundX
        global Vibration
        
        key = pygame.key.get_pressed()
        bhaag = 1


        if REQ==1:
            if self.rect.x > 430: self.rect.x -= 3
        else:
            if self.rect.x > 430: self.rect.x -= 2
        if self.rect.x < 10: self.rect.x += 2
        if key[pygame.K_d]:
            if REQ==1:
                self.rect.x += 2
                
            else:
                self.rect.x += bhaag
                
                
            self.rect.x += bhaag
        elif key[pygame.K_a]: # bhaag left mei
            if REQ==1:
                self.rect.x -= 2
               
            else:
                self.rect.x -= 2
        if REQ==1:
            if Vibration==1:
                self.rect.x += 1
                #BackgroundX += 10
                
            if Vibration==2:
                self.rect.x -= 1
                #BackgroundX -= 10
            if Vibration==3:
                Vibration = -10
               
        
        LED.blit(self.image1,self.rect)

    def getX(self):
        return self.rect.x

King = King(Ball,300,500)
Bomb = Bomb()
Bomb.setup(300) # Set it up
global Score,text1
font = pygame.font.SysFont("comicsansms", 24)
text = font.render("Score:", True, (0, 0, 0))
text1 = font.render(""+str(Score),True,(0,0,0))
print os.getcwd()

def CheckScore(SessionScore,StoredScore):
    
    K = StoredScore
    Y = SessionScore
    if int(K)<int(Y):
        Debug("UPDATE: User's current score is greater than stored one ")
        global HighScore
        HighScore = SessionScore
        temp = open("score","a+")
        temp.truncate()
        temp.write(str(Y))
        Debug("Score has been updated")
    
        
        
       
def Start():
    
    global Score,Counter
    LED.fill((0,0,0))
    Score = 0 # Reset the score to prevent cheating
    Debug("Resetted Score variable to prevent cheating ")
    Counter = 0
    while Star==False:
        '''Button = pygame.Rect(200,200,50,50)
        pygame.draw.rect(LED,(255,255,255),Button)'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            '''if event.type == pygame.MOUSEBUTTONDOWN:
               mouse = pygame.mouse.get_pos()
               if Button.collidepoint(mouse):
                    global Star
                    Star = True # Break the loop
                    print "true"
                    break'''
        LED.blit(Welcome,(0,0))
           
        py = pygame.key.get_pressed()
        if py[K_e]:
            global REQ,Star
            Music = pygame.mixer.music.load("Music/Background.mp3")
            pygame.mixer.music.play(-1)
            
            REQ = 3
            Debug("Game difficulty: Easy")
            Star = True
            break
        if py[K_m]:
            Music = pygame.mixer.music.load("Music/Background.mp3")
            pygame.mixer.music.play(-1)
            
            global REQ,Star
            REQ = 2
            Debug("Game difficulty: Medium")
            Star = True
            break
        if py[K_h]:
            Music = pygame.mixer.music.load("Music/Background.mp3")
            pygame.mixer.music.play(-1)
            Debug("Game difficulty: HARD ")
            global REQ,Star
            REQ = 1
            Star = True
            break
            

                    
        pygame.display.flip()

def BackScroll(Condition): #Manages the background scrolling effect.
    global BackgroundX,BackgroundY,BG
    IMGHeight = BG.get_height()
    IMGWidth =BG.get_width()
    if Condition=="U": #Request to scroll up
        BackgroundY -= 2
    if BackgroundY < 0 - IMGHeight + 500:
        Debug("BGREPORT: BackgroundY is going to be reseted to 0 #")
        BackgroundY = 00
    print BackgroundY
    

global Star,Pause,HighScore
Pause = False
Star = False
while True:
    BackScroll("U")
    Vibration += 1
    d = pygame.key.get_pressed()
    if d[K_ESCAPE]:
        Star = False
    if Star==False:
        Debug("Need to call Start()")
        print "false"
        Start()
    global Score,KingX
    KingX = King.getX()
    
    
    
    LED.fill((255,255,255))
    #if Counter == 1:
    LED.blit(BG,(BackgroundX,BackgroundY))
    LED.blit(text,(0,0))
    LED.blit(text1,(75,0))
    if pygame.sprite.collide_rect(King,Bomb):
         Debug("Player collided with brick.")
         GameOver() 
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        d = pygame.key.get_pressed()
        if d[K_p]:
            pygame.time.wait(1000)
    Y = Bomb.getY()
    if Y > 500:
        #BrickMissed.play()
        CheckScore(Score,HighScore)
        
        text1 = font.render(""+str(Score + 1),True,(0,0,0))
       # if Score == 10: Bomb.setSHAPEX(100)
        Score += 1
        print Score
        Debug("Player managed to pass the brick")
        Bomb.setup(KingX)

    Counter += 1
  
   
    Bomb.update()
    King.update()
    pygame.display.flip()



    


        
        
