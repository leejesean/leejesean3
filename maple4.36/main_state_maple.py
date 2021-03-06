from pico2d import *
import game_framework_maple
import main_state_maple2
name = "MainState"
boy = None
grass = None
font = None
running = True
x=400
y=90
jumpy=0
movey=855
frame=0
count=0
count2=0
count3=0
isMagic=0
isMagic2=0
isMagic3=0
Npcx=100
Npcy=460
Npcx2=750
Npcy2=100
magicx=0
jump=0
bkx=400
TRUE ,FALSE=1,0
isJump=False
bkcheck = 1
gravity=0
RIGHT_RUN,LEFT_RUN,RIGHT_STAND,LEFT_STAND,RIGHT_JUMP,LEFT_JUMP,RIGHT_ATTACK,LEFT_ATTACK,RIGHT_SKILL,LEFT_SKILL,RIGHT_SKILL2,LEFT_SKILL2,RIGHT_SKILL3,LEFT_SKILL3 = 1,2,3,4,5,6,7,8,9,10,11,12,13,14 #사진순서대로~
state=RIGHT_STAND
right=TRUE
class Grass:
    def __init__(self):
        self.image = load_image('background.png')
    def draw(self):
        self.image.draw(bkx,475)
class Magic:
    def __init__(self):
        self.image = load_image('magic.png')
        self.frame=0
        self.x=0
    def update(self):
         self.frame = (self.frame + 1) % 2
         if state == RIGHT_SKILL :
             self.x=x+magicx
         if state == LEFT_SKILL:
             self.x=x+magicx
    def draw(self):
        if(state==RIGHT_SKILL):
            self.movey=41
            self.image.clip_draw(self.frame * 88, self.movey, 88, 41,self.x, y)
        elif(state==LEFT_SKILL):
            self.movey=0
            self.image.clip_draw(self.frame * 88, self.movey, 88, 41,self.x, y)
class Magic2:
    def __init__(self):
        self.image = load_image('magic2.png')
        self.frame=0
        self.x=0
    def update(self):
         self.frame = (self.frame + 1)%8
         if state == RIGHT_SKILL2 :
             self.x=x+130
         if state == LEFT_SKILL2:
             self.x=x-130
    def draw(self):
        if(state==RIGHT_SKILL2 and isMagic2== TRUE):
            self.movey=0
            self.image.clip_draw(self.frame * 354, self.movey, 354, 387,self.x, y+120)
        elif(state==LEFT_SKILL2 and isMagic2== TRUE):
            self.movey=0
            self.image.clip_draw(self.frame * 354, self.movey, 354, 387,self.x, y+120)
class Magic3:
    def __init__(self):
        self.image = load_image('magic3.png')
        self.frame=0
        self.x=0
    def update(self):
         self.frame = (self.frame + 1) % 20
    def draw(self):
        if(state==RIGHT_SKILL3 and isMagic3== TRUE):
            self.movey=0
            self.image.clip_draw(self.frame * 800, self.movey, 800, 600,400,300)
        elif(state==LEFT_SKILL3 and isMagic3== TRUE):
            self.movey=0
            self.image.clip_draw(self.frame * 800, self.movey, 800, 600,400,300)

class Npc:
    def __init__(self):
        self.frame = 0
        self.image = load_image('NPC.png')

    def update(self):
        self.frame = (self.frame + 1 ) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 90,  0, 90, 100,Npcx, Npcy)

class Npc2:
    def __init__(self):
        self.frame = 0
        self.image = load_image('NPC2.png')

    def update(self):
        self.frame = (self.frame + 1 ) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 105,  0, 105, 80,Npcx2, Npcy2)
class Boy:
    def __init__(self):
        self.frame = 0
        self.image = load_image('character.png')
    def update(self):
        if state == RIGHT_RUN or state == LEFT_RUN:
            self.frame = (self.frame + 1) % 4
        elif state == RIGHT_STAND or state == LEFT_STAND:
            self.frame = 0
        elif state == RIGHT_JUMP or state == LEFT_JUMP:
            self.frame = (self.frame + 1) % 3
        elif state == RIGHT_ATTACK or state == LEFT_ATTACK:
            self.frame = (self.frame + 1) % 3
        elif state == RIGHT_SKILL or state == LEFT_SKILL or state==RIGHT_SKILL2 or state == LEFT_SKILL2 or state == RIGHT_SKILL3 or state == LEFT_SKILL3:
            self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame * 80, movey, 80, 95,x, y)
#-----------------------------------------------------------------------------------------------------------------------
def enter():
    global boy, grass,magic,magic2,magic3,npc,npc2
    boy=Boy()
    npc=Npc()
    npc2=Npc2()
    grass = Grass()
    magic=Magic()
    magic2=Magic2()
    magic3=Magic3()

def exit():
   global boy, grass,magic,magic2,magic3,npc,npc2
   del(boy)
   del(npc)
   del(npc2)
   del(grass)
   del(magic)
   del(magic2)
   del(magic3)
def pause():
    pass
def resume():
    pass
def handle_events():
    global running
    global x
    global y
    global jumpy
    global movey
    global frame
    global magicx
    global bool
    global count
    global count2
    global count3
    global isMagic
    global isMagic2
    global isMagic3
    global state
    global right
    global framemagic
    global jump
    global isJump
    global gravity
    global bkcheck
    global bkx
    global Npcx
    global Npcx2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework_maple.quit()
#------------------------------------키조작-----------------------------------
        elif event.type == SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
               game_framework_maple.quit()
            elif event.key == SDLK_RIGHT:
                state=RIGHT_RUN
                right=TRUE
            elif event.key == SDLK_LEFT:
                state=LEFT_RUN
                right=FALSE
            elif event.key == SDLK_x and right == TRUE:
                state=RIGHT_JUMP
            elif event.key == SDLK_x and right == FALSE:
                state=LEFT_JUMP
            elif event.key == SDLK_z and right == TRUE:
                state=RIGHT_ATTACK
            elif event.key == SDLK_z and right == FALSE:
                state=LEFT_ATTACK
            elif event.key == SDLK_a and right == TRUE:
                state=RIGHT_SKILL
            elif event.key == SDLK_a and right == FALSE:
                state=LEFT_SKILL
            elif event.key == SDLK_s and right == TRUE:
                state=RIGHT_SKILL2
            elif event.key == SDLK_s and right == FALSE:
                state=LEFT_SKILL2
            elif event.key == SDLK_d and right == TRUE:
                state=RIGHT_SKILL3
            elif event.key == SDLK_d and right == FALSE:
                state=LEFT_SKILL3
            elif  event.key == SDLK_p:
                game_framework_maple.change_state(main_state_maple2)#chage는 exit를실행!

        elif event.type ==SDL_KEYUP:#뗏을때!
            if event.key == SDLK_RIGHT:
                right=TRUE
                state=RIGHT_STAND
            elif event.key == SDLK_LEFT:
                right=FALSE
                state=LEFT_STAND

##################################실행##############################
        if  state==RIGHT_RUN and bkcheck == FALSE :
            if x<750 :
                x=x+17.5
            movey=760
            magicx=0
        elif state==RIGHT_RUN and bkcheck == TRUE :
            bkx=bkx-17.5
            Npcx=Npcx-17.5
            Npcx2=Npcx2-17.5
            movey=760
            magicx=0#여기버그
        elif state==LEFT_RUN and bkcheck == FALSE :
            if x>50 :
                x=x-17.5
            movey=665
            magicx=0
        elif state==LEFT_RUN and bkcheck == TRUE :
            bkx=bkx+17.5
            Npcx=Npcx+17.5
            Npcx2=Npcx2+17.5
            movey=665
            magicx=0
        elif state==RIGHT_STAND:
            movey=860
        elif state==LEFT_STAND:
            movey=955
        elif state==RIGHT_JUMP:
           if isJump == FALSE:
                movey=475
                jump = 35.0
                gravity = 7.0
                isJump = TRUE
        elif state==LEFT_JUMP:
           if isJump == FALSE:
                movey=570
                jump = 35.0
                gravity = 7.0
                isJump = TRUE
        elif state==RIGHT_ATTACK:
            movey=0
        elif state==LEFT_ATTACK:
            movey=95
        elif state==RIGHT_SKILL:
           movey=190
           if isMagic == FALSE:
               isMagic = TRUE
        elif state==LEFT_SKILL:
            movey=285
            if isMagic == FALSE:
                isMagic = TRUE
        elif state==RIGHT_SKILL2:
           movey=190
           if isMagic2 == FALSE:
               isMagic2 = TRUE
        elif state==LEFT_SKILL2:
            movey=285
            if isMagic2 == FALSE:
                isMagic2 = TRUE
        elif state==RIGHT_SKILL3:
           movey=190
           if isMagic3 == FALSE:
                isMagic3 = TRUE
        elif state==LEFT_SKILL3:
            movey=285
            if isMagic3 == FALSE:
                isMagic3 = TRUE

#매직함수============================================
    if isMagic == TRUE and state==RIGHT_SKILL:
        magicx=magicx+45.5
        if magicx>300:
            magicx=0
            isMagic = FALSE
            movey=860
            state = RIGHT_STAND
    if isMagic == TRUE and state==LEFT_SKILL:
        magicx=magicx-45.5
        if magicx<-300:#바로위보면 이해!
            magicx=0
            isMagic = FALSE
            movey=955
            state = LEFT_STAND
    if isMagic2 == TRUE and state==RIGHT_SKILL2:
        count2= count2 + 1
        if count2==7:
            count2=0
            isMagic2 = FALSE
            movey=860
            state = RIGHT_STAND
    if isMagic2 == TRUE and state==LEFT_SKILL2:
        count2=count2+1
        if count2==7:
            count2=0
            isMagic2 = FALSE
            movey=955
            state = LEFT_STAND
    if isMagic3 == TRUE and state==RIGHT_SKILL3:
        count3=count3+1
        print(count3)
        if count3==20:
            print("3")
            count3=0
            isMagic3 = FALSE
            movey=860
            state = RIGHT_STAND
    if isMagic3 == TRUE and state==LEFT_SKILL3:
        count3=count3+1
        if count3==19:
            count3=0
            isMagic3 = FALSE
            movey=955
            state = LEFT_STAND
#배경화면함수============================================
    if bkx<790 and bkx>10:
        bkcheck = TRUE
    elif bkx>=790 :
        bkcheck = FALSE
        if x>400 :
            x=400
            bkcheck=TRUE
    elif bkx<=10 :
       bkcheck = FALSE
       if x<400 :
           x=400
           bkcheck=TRUE

#점프-함수
    if isJump == TRUE:
        y = y+ jump
        jump = jump-gravity
        if y<=105:
            jump=0
            gravity=0
            isJump = FALSE
            if right == TRUE:#여기부분이 버그~
                movey=860
                state = RIGHT_STAND
                print("점프1")
            elif right == FALSE:
                movey=955
                state = LEFT_STAND
                print("점프2")

def update():
    magic.update()
    magic2.update()
    magic3.update()
    npc.update()
    npc2.update()
    boy.update()
    delay(0.08)
def draw():
    clear_canvas()
    grass.draw()
    magic.draw()
    magic2.draw()
    magic3.draw()
    npc.draw()
    npc2.draw()
    boy.draw()
    update_canvas()






