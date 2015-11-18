from pico2d import *
import random
import game_framework_maple
import main_state_maple
import main_state_maple3
name = "MainState"
boy = None
grass = None
font = None
running = True
x=50
y=95
bkx=400
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
RIGHT_RUN,LEFT_RUN,RIGHT_STAND,LEFT_STAND,RIGHT_JUMP,LEFT_JUMP,RIGHT_ATTACK,LEFT_ATTACK,RIGHT_SKILL,LEFT_SKILL,RIGHT_SKILL2,LEFT_SKILL2,RIGHT_SKILL3,LEFT_SKILL3,RIGHT_DAMAGE,LEFT_DAMAGE  = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 #사진순서대로~
TRUE ,FALSE=1,0
bkcheck=0
bkx=400
state=RIGHT_STAND
right=TRUE
Dead=FALSE
class Grass:
    def __init__(self):
        self.image = load_image('background2.png')
    def draw(self):
        self.image.draw(bkx,320)
class Magic:
    def __init__(self):
        self.image = load_image('magic.png')
        self.frame=0
        self.x=x
        y=95
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
    def get_bb(self):
        return self.x-20,y-10,self.x+20,y+10
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

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
    def get_bb(self):
        return self.x-100,y-100,self.x+100,y+100
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Magic3:
    def __init__(self):
        self.image = load_image('magic3.png')
        self.frame=0
        self.x=0
        self.y=0
    def update(self):
         self.frame = (self.frame + 1) % 20
    def draw(self):
        if(state==RIGHT_SKILL3 and isMagic3== TRUE):
            self.movey=0
            self.image.clip_draw(self.frame * 800, self.movey, 800, 600,400, 300)
        elif(state==LEFT_SKILL3 and isMagic3== TRUE):
            self.movey=0
            self.image.clip_draw(self.frame * 800, self.movey,  800, 600,400, 300)
    def get_bb(self):
        return self.x+10,self.y+10,self.x+780,self.y+580
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Monster:
    def __init__(self):
        self.monsterx, self.monstery = 50, 90
        self.frame = 0
        self.monsterx, self.monstery=random.randint(300,800),80
        self.speed = random.randint(1,20)
        self.turn = 1
        self.Daed=0
        self.Damage=0
        self.count=0
        self.image = load_image('monster2.png')
    def update(self):
        if self.turn == 1 and self.Damage==FALSE and self.Daed==FALSE:
            self.movey=2*40
            self.frame = (self.frame + 1 ) % 4
        elif self.turn == -1and self.Damage==FALSE and self.Daed==FALSE:
            self.movey=6*40
            self.frame = (self.frame + 1 ) % 4
        elif self.turn == 1 and self.Damage==TRUE:
            self.movey=1*40
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == -1 and self.Damage==TRUE:
            self.movey=5*40
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == 1  and self.Daed==TRUE:
            self.movey=0*40
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == -1 and self.Daed==TRUE :
            self.movey=4*40
            self.frame = (self.frame + 1 ) % 1

        if self.monsterx >800:
            self.turn *=-1
        elif self.monsterx < 0:
            self.turn *=-1
        self.monsterx += self.speed*self.turn
    def draw(self):
        self.image.clip_draw(self.frame * 50,  self.movey, 50, 40,self.monsterx, self.monstery)
    def get_bb(self):
        return self.monsterx-10,self.monstery-10,self.monsterx+10,self.monstery+10
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Boy:
    def __init__(self):
        self.x, self.y = 50, 90
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
        elif state == RIGHT_DAMAGE or state == LEFT_DAMAGE :
            self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame * 80, movey, 80, 95,x, y)
    def get_bb(self):
        return x-50,y-50,x+50,y+50
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
#------------------------------------------------------------------------------
def enter():
    global boy, grass,magic,magic2,magic3,monster,team
    boy=Boy()
    grass = Grass()
    magic=Magic()
    magic2=Magic2()
    magic3=Magic3()
    team = [Monster() for i in range(3)]
    monster=Monster()

def exit():
   global boy, grass,magic,magic2,magic3,monster,team
   del(boy)
   del(grass)
   del(magic)
   del(magic2)
   del(magic3)
   del(monster)
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
                game_framework_maple.change_state(main_state_maple3)#chage는 exit를실행!
            elif  event.key == SDLK_o:
                game_framework_maple.change_state(main_state_maple)#chage는 exit를실행!

        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                right=TRUE
                state=RIGHT_STAND
            elif event.key == SDLK_LEFT:
                right=FALSE
                state=LEFT_STAND
################################실행################################
    if  state==RIGHT_RUN and bkcheck == FALSE :
        if x<750 :
            x=x+17.5
        movey=760
        magicx=0
    elif  state==RIGHT_RUN and bkcheck == TRUE :
        bkx=bkx-17.5
        movey=760
        magicx=0#여기버그
    elif state==LEFT_RUN and bkcheck == FALSE :
        if x>50 :
            x=x-17.5
        movey=665
        magicx=0
    elif state==LEFT_RUN and bkcheck == TRUE :
        bkx=bkx+17.5
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
    elif state==RIGHT_DAMAGE:
        movey=1045
        if x<775 and x>25:#보이가밀려감
            x=x-5
    elif state==LEFT_DAMAGE:
        movey=1140
        print("left_damage")
        if x<775 and x>0:
            x=x+5

#배경화면함
    if bkx<790 and bkx>10 and x == 400:
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

#매직함수
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

#점프-함수
    if isJump == TRUE:
        y = y+ jump
        jump = jump-gravity
        # count=count+1
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

def collide(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False#아닐때
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False
    return True
    pass

def collide1(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False
    if isMagic2==TRUE : return False
    if isMagic3==TRUE : return False
    if isMagic==FALSE and state==RIGHT_STAND :return False
    if isMagic==FALSE and state==RIGHT_RUN :return False
    if isMagic==FALSE and state==RIGHT_JUMP:return False
    if isMagic==FALSE and state==RIGHT_DAMAGE:return False
    if isMagic==TRUE and state==RIGHT_DAMAGE:return False#버그해결을위해!

    if isMagic==FALSE and state==LEFT_STAND :return False
    if isMagic==FALSE and state==LEFT_RUN :return False
    if isMagic==FALSE and state==LEFT_JUMP:return False
    if isMagic==FALSE and state==LEFT_DAMAGE:return False
    if isMagic==TRUE and state==LEFT_DAMAGE:return False#버그해결을위해!
    return True
    pass
def collide2(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False
    if isMagic==TRUE : return False
    if isMagic3==TRUE : return False
    if isMagic2==FALSE and state==RIGHT_STAND :return False
    if isMagic2==FALSE and state==RIGHT_RUN :return False
    if isMagic2==FALSE and state==RIGHT_JUMP:return False
    if isMagic2==FALSE and state==RIGHT_DAMAGE:return False
    if isMagic2==TRUE and state==RIGHT_DAMAGE:return False#버그해결을위해!

    if isMagic2==FALSE and state==LEFT_STAND :return False
    if isMagic2==FALSE and state==LEFT_RUN :return False
    if isMagic2==FALSE and state==LEFT_JUMP:return False
    if isMagic2==FALSE and state==LEFT_DAMAGE:return False
    if isMagic2==TRUE and state==LEFT_DAMAGE:return False#버그해결을위해!
    return True
    pass

def collide3(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False
    if isMagic==TRUE : return False
    if isMagic2==TRUE : return False
    if isMagic3==FALSE and state==RIGHT_STAND :return False
    if isMagic3==FALSE and state==RIGHT_RUN :return False
    if isMagic3==FALSE and state==RIGHT_JUMP:return False
    if isMagic3==FALSE and state==RIGHT_DAMAGE:return False
    if isMagic3==TRUE and state==RIGHT_DAMAGE:return False#버그해결을위해!

    if isMagic3==FALSE and state==LEFT_STAND :return False
    if isMagic3==FALSE and state==LEFT_RUN :return False
    if isMagic3==FALSE and state==LEFT_JUMP:return False
    if isMagic3==FALSE and state==LEFT_DAMAGE:return False
    if isMagic3==TRUE and state==LEFT_DAMAGE:return False#버그해결을위해!
    return True
    pass

def update():
    global state
    global movey
    global x
    boy.update()
    magic.update()
    magic2.update()
    magic3.update()
    for monster in team:
         monster.update()
    for monster in team:
         if collide(boy,monster):
            if right == TRUE:
                state=RIGHT_DAMAGE
                if monster.monsterx<775 and monster.monsterx>25:
                   monster.monsterx=monster.monsterx+50
            elif right == FALSE:
                state=LEFT_DAMAGE
                if monster.monsterx<775 and monster.monsterx>25:
                    monster.monsterx=monster.monsterx-50
#--------------------------------------------------------------------------------------------
         elif collide1(magic,monster):
            monster.Damage=TRUE
            monster.count=monster.count+1#맞았을때+1
            print(monster.count)
            if monster.count>3:#3번맞으면 죽게된다
                monster.Damage=FALSE
                monster.Daed=TRUE
#--------------------------------------------------------------------------------------------
         elif collide2(magic2,monster):
            team.remove(monster)

         elif collide3(magic3,monster):
            team.remove(monster)

def draw():
    clear_canvas()
    grass.draw()
    magic.draw()
    magic.draw_bb()
    magic2.draw()
    magic2.draw_bb()
    magic3.draw()
    magic3.draw_bb()
    for monster in team:
        monster.draw()
    for monster in team:
        monster.draw_bb()
    boy.draw()
    boy.draw_bb()
    update_canvas()
    delay(0.1)




