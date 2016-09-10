################################################### IMPORT STATEMENTS
import pygame as p
import random
import sys
black=((0,0,0))
random.seed()
################################################### DRAWING FUNCTIONS FOR HANGMAN
def Stage0(Bg):
        p.draw.line(Bg,black,(600,100),(600,70),5)
        p.draw.line(Bg,black,(600,70),(750,70),5)
        p.draw.line(Bg,black,(750,70),(750,470),5)
        p.draw.line(Bg,black,(650,470),(850,470),5)
        screen.blit(Bg,(0,0))
def Stage1(Bg):
        p.draw.circle(Bg,black,(600,150),50,5)
        screen.blit(Bg,(0,0))
        return
def Stage2(Bg):
        p.draw.line(Bg,black,(600,200),(600,330),5)
        screen.blit(Bg,(0,0))
        return
def Stage3(Bg):
        p.draw.line(Bg,black,(600,330),(550,420),5)
        screen.blit(Bg,(0,0))
def Stage4(Bg):
        p.draw.line(Bg,black,(600,330),(650,420),5)
        screen.blit(Bg,(0,0))
        return
def Stage5(Bg):
        p.draw.line(Bg,black,(600,240),(550,290),6)
        screen.blit(Bg,(0,0))
def Stage6(Bg):
        p.draw.line(Bg,black,(600,240),(650,290),6)
        screen.blit(Bg,(0,0))
def Stage7(Bg):
        p.draw.line(Bg,black,(600,150),(600,70),5)
        p.draw.line(Bg,black,(600,70),(750,70),5)
        p.draw.line(Bg,black,(750,70),(750,470),5)
        p.draw.line(Bg,black,(650,470),(850,470),5)
        p.draw.circle(Bg,black,(570,190),50,5)
        p.draw.line(Bg,black,(600,200),(600,330),5)
        p.draw.line(Bg,black,(600,330),(550,420),5)
        p.draw.line(Bg,black,(600,330),(650,420),5)
        p.draw.line(Bg,black,(600,240),(550,290),6)
        p.draw.line(Bg,black,(600,240),(650,290),6)
        screen.blit(Bg,(0,0))
def backS(Bg,screen):
        Bg.fill(color)
        screen.blit(Bg,(0,0))
############################################## WINDOW CREATION
p.init()
screen=p.display.set_mode((1280,720))
color=((0,0,255))
############################################## ICON AND TITLE CREATION
icon=p.image.load("k.jpg")
p.display.set_caption("HANGMAN-Please Die")
p.display.set_icon(icon)
############################################## START MUSIC
p.mixer.music.load("ema.mp3")
p.mixer.music.play(-1)
############################################# MENU SCREEN TEXT DRAWING
myfont = p.font.SysFont("None", 34)
mytext = myfont.render('PRESS ENTER TO START & PRESS Q TO EXIT', True, (255,255,255))
mytext = mytext.convert_alpha()
screen.blit(mytext,(800//2,650//2))
############################################# MENU SCREEN INTERACTION
mainloop=True
while mainloop:
    for events in p.event.get():
        if events.type==p.QUIT:
            sys.exit()
        if events.type==p.KEYDOWN and events.key==p.K_RETURN:
            mainloop=False
        if events.type==p.KEYDOWN and events.key==p.K_q:
            sys.exit()
    p.display.flip()
############################################# CREATING THE MAIN GAME SCREEN
mainloop=True
Bg=p.Surface((1280,720))
Bg.fill(color)
Bg=Bg.convert()
screen.blit(Bg,(0,0))
############################################ OBTAINING RANDOM WORD FROM WORDLIST
FILE = "wordlist.txt"
file=open(FILE,'r')
words=file.readlines()
words=[x[:-1] for x in words]
word=words[random.randint(0,len(words))]
############################################ FIRST TEXT FIELD
myfont = p.font.SysFont("None", 34)
mytext = myfont.render('GUESS A LETTER', True, (255,255,255))
mytext = mytext.convert_alpha()
screen.blit(mytext,(50,50))
############################################ SECOND TEXT FIELD
myfont = p.font.SysFont("None", 34)
my = myfont.render('_ '*len(word), True, (255,255,255))
my = my.convert_alpha()
screen.blit(my,(50,200))
############################################ INITIALISING DX
dx=350
############################################ THIRD TEXT FIELD
myfont = p.font.SysFont("None", 34)
xt = myfont.render('GUESSED LETTERS:', True, (255,255,255))
xt = xt.convert_alpha()
screen.blit(xt,(50,300))
############################################ FUNCTION TO BLIT ALL THE TEXT FIELDS AFTER REFRESHING THE SCREEN
def blitscreens():
    global dx
    screen.blit(mytext,(50,50))
    screen.blit(my,(50,200))
    screen.blit(xt,(50,300))
############################################ VARIABLES TO STORE GAME DATA
correct_guess=[]
counter=0
guess=[]
############################################ THE MAIN GAME INTERACTION
while mainloop:
    for event in p.event.get():
        if event.type==p.QUIT:
            sys.exit()
        if event.type==p.KEYDOWN:
            if event.key==p.K_ESCAPE:
                sys.exit()
            l=p.key.get_pressed() ###### RECEIVING DATA INPUT FROM KEYBOARD

            for i in range(len(l)):
                if l[i]==1:
                    if i>=256:
                        break
                    s=chr(i)
                    if s in guess:
                        break
                    ################################################################ DRAWING THE ENTERED ALPHABETS IN ORDER
                    myfont = p.font.SysFont("None", 34)
                    m = myfont.render(chr(i), True, (255,255,255))
                    m = m.convert_alpha()
                    screen.blit(m,(50,dx))
                    dx+=25
                    ################################################################ CHECK IF LETTER IS VALID AND FILL UP
                    guess.append(s)
                    if s in word:
                        w=word
                        my.fill(color)
                        screen.blit(my,(50,200))
                        correct_guess.append(s)
                        i=0
                        while i<len(w):
                            if w[i] not in correct_guess:
                                w=w[:i]+'_ '+w[i+1:]
                                i+=1
                            if w[i] in correct_guess:
                                w=w[:i+1]+' '+w[i+1:]
                                i+=1
                            i+=1
                    ################################################################ UPDATE THE BLANKS
                        my = myfont.render(w, True, (255,255,255))
                        my = my.convert_alpha()
                        blitscreens()
                    ################################################################ VICTORY CONDITION CHECK
                        if '_' not in w:
                            Bg.fill(black)
                            Bg=Bg.convert()
                            screen.blit(Bg,(0,0))
                            p.display.flip()
                            myfont = p.font.SysFont("None", 34)
                            mytext = myfont.render('CONGRATULATIONS YOU WIN! Press q to exit', True, (255,255,255))
                            mytext = mytext.convert_alpha()
                            screen.blit(mytext,(800//2,650//2))
                            p.display.flip()
                            ################################################### VICTORY PAGE INTERACTION
                            while True:
                                for e in p.event.get():
                                    if e.type==p.QUIT:
                                        sys.exit()
                                    if e.type==p.KEYDOWN and e.key==p.K_q:
                                        sys.exit()
                                p.display.flip()
                    ################################################################ IF WRONG LETTER
                    else:
                        d={0:Stage0,1:Stage1,2:Stage2,3:Stage3,4:Stage4,5:Stage5,6:Stage6,7:Stage7,8:backS}
                        if counter>=7: ######### IF YOU ARE DEAD
                            mytext.fill(color)
                            my.fill(color)
                            xt.fill(color)
                            blitscreens()
                            f=d[counter+1]
                            f(Bg,screen)
                            f=d[counter]
                            f(Bg)
                            myfont = p.font.SysFont("None", 34)
                            myi = myfont.render("GAME OVER! YOU ARE DEAD! WORD="+word, True, (255,255,255))
                            myi = myi.convert_alpha()
                            screen.blit(myi,(10,500))
                            ################################## DEATH SCREEN INTERACTION
                            while True:
                                for e in p.event.get():
                                    if e.type==p.QUIT:
                                        sys.exit()
                                    if e.type==p.KEYDOWN and e.key==p.K_q:
                                        sys.exit()
                                p.display.flip()
                        ############################################# DRAW THE STAGES BASED ON COUNTER
                        for i in range(counter+1):
                            f=d[i]
                            f(Bg)
                        p.display.flip()
                        ######################################## UPDATE ALL THE ENTERED ALPHABETS
                        dx=350
                        for i in guess:
                            m = myfont.render(i, True, (255,255,255))
                            m = m.convert_alpha()
                            screen.blit(m,(50,dx))
                            dx+=25
                        blitscreens()
                        counter+=1
                ############################################################### UPDATE GAME SCREEN EACH FRAME
    p.display.flip()
################################################################### END OF GAME