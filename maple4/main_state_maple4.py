from pico2d import *
import game_framework_maple
import title_state_maple
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
magicx=0
jump=0
isJump=False
gravity=0
RIGHT_RUN,LEFT_RUN,RIGHT_STAND,LEFT_STAND,RIGHT_JUMP,LEFT_JUMP,RIGHT_ATTACK,LEFT_ATTACK,RIGHT_SKILL,LEFT_SKILL,RIGHT_SKILL2,LEFT_SKILL2,RIGHT_SKILL3,LEFT_SKILL3  = 1,2,3,4,5,6,7,8,9,10,11,12,13,14 #사진순서대로~
TRUE ,FALSE=1,0
state=RIGHT_STAND
right=TRUE

class Grass:
    def __init__(self):
        self.image = load_image('background.png')
    def draw(self):
        self.image.draw(400,475)
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
         self.frame = (self.frame + 1) % 8
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
#------------------------------------------------------------------------------
def enter():
    global boy, grass,magic,magic2,magic3
    boy=Boy()
    grass = Grass()
    magic=Magic()
    magic2=Magic2()
    magic3=Magic3()

def exit():
   global boy, grass,magic,magic2,magic3
   del(boy)
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

        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                right=TRUE
                state=RIGHT_STAND
            elif event.key == SDLK_LEFT:
                right=FALSE
                state=LEFT_STAND

################################실행############################
        if  state==RIGHT_RUN:
            x=x+17.5
            movey=760
            magicx=0#여기버그
        elif state==LEFT_RUN:
            x=x-17.5
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

#매직함수
    if isMagic == TRUE and state==RIGHT_SKILL:
        magicx=magicx+45.5
        if magicx>300:
            magicx=0
            isMagic = FALSE
    if isMagic == TRUE and state==LEFT_SKILL:
        magicx=magicx-45.5
        if magicx<-300:#바로위보면 이해!
            magicx=0
            isMagic = FALSE

    if isMagic2 == TRUE and state==RIGHT_SKILL2:
        count2=count2+1
        if count2==7:
            count2=0
            isMagic2 = FALSE
    if isMagic2 == TRUE and state==LEFT_SKILL2:
        count2=count2+1
        if count2==7:
            count2=0
            isMagic2 = FALSE

    if isMagic3 == TRUE and state==RIGHT_SKILL3:
        count3=count3+1
        if count3==19:
            count3=0
            isMagic3 = FALSE
    if isMagic3 == TRUE and state==LEFT_SKILL3:
        count3=count3+1
        if count3==19:
            count3=0
            isMagic3 = FALSE

#점프-함수
    if isJump == TRUE:
        y = y+ jump
        jump = jump-gravity
        # count=count+1
        if y<105:
            jump=0
            gravity=0
            isJump = FALSE
            if(isJump == FALSE and right == TRUE):#여기부분이 버그~
                state = RIGHT_STAND
            elif(isJump == FALSE and right == FALSE):
                state = LEFT_STAND


def update():
    boy.update()
    magic.update()
    magic2.update()
    magic3.update()

def draw():
    clear_canvas()
    grass.draw()
    magic.draw()
    magic2.draw()
    magic3.draw()
    boy.draw()
    update_canvas()
    delay(0.111)





