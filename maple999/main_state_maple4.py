from pico2d import *
import random
import game_framework_maple
name = "MainState"
boy = None
grass = None
font = None
running = True
x=50
xx=0
tt=0
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
RIGHT_RUN,LEFT_RUN,RIGHT_STAND,LEFT_STAND,RIGHT_JUMP,LEFT_JUMP,RIGHT_ATTACK,LEFT_ATTACK,RIGHT_SKILL,LEFT_SKILL,RIGHT_SKILL2,LEFT_SKILL2,RIGHT_SKILL3,LEFT_SKILL3,RIGHT_DAMAGE,LEFT_DAMAGE,POTAL_STAND,HPUP,MPUP,DEAD,MPDEAD  = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 #사진순서대로~
BOSS_RIGHT_RUN,BOSS_LEFT_RUN,BOSS_RIGHT_JUMPSKILL,BOSS_LEFT_JUMPSKILL,BOSS_RIGHT_MAINSKILL,BOSS_LEFT_MAINSKILL=1,2,3,4,5,6
TRUE ,FALSE=1,0
bkcheck=0
bkx=780
state=RIGHT_STAND
right=TRUE
Dead=FALSE
Touch=FALSE
Touch2=FALSE
isGoRight=FALSE
isGoLeft=FALSE
class Grass:
    def __init__(self):
        self.image = load_image('background3.png')
        self.image2 = load_image('charterbar.png')
        self.bgm=load_music('배경음악보스맵.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
    def draw(self):
        self.image.draw(bkx,320)
        self.image2.draw(400,18)
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
        return self.x+5,self.y+10,self.x+795,self.y+580
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
class Monster:
    def __init__(self):
        self.frame = 0
        self.monsterx,self.monstery=random.randint(300,400),245
        self.speed = 10
        self.hp=700
        self.turn = 1
        self.Daed=0
        self.Damage=0
        self.count=0
        self.count2=0
        self.count3=0
        self.bool=FALSE
        self.bool2=FALSE
        self.bool3=FALSE
        self.count,self.count2,self.count3=0,0,0
        self.damage1,self.damage2,self.damage3=0,0,0
        self.image = load_image('boss.png')
        self.image3 = load_image('bosshp.png')
        self.image4 = load_image('damage1.png')
        self.image5 = load_image('damage2.png')
        self.image6 = load_image('damage3.png')

        self.damage_sound = load_wav('보스데미지.wav')
        self.damage_sound.set_volume(128)
        self.skill_sound = load_wav('보스스킬.wav')
        self.skill_sound.set_volume(128)
        self.skill2_sound = load_wav('보스스킬2.wav')
        self.skill2_sound.set_volume(128)
        self.die_sound = load_wav('보스다이.wav')
        self.die_sound.set_volume(128)

    def update(self):
        print(self.hp)
        print("\n")
        self.count2=self.count2+1#시간초계싼
        self.count3=self.count3+1#시간초계싼
        if self.turn == 1 and self.Damage==FALSE and self.Daed==FALSE and self.hp>600:#오른쪽걸어갈때
            self.movey=8*380
            self.monstery=245
            self.frame = (self.frame + 1 ) % 4
        elif self.turn == -1 and self.Damage==FALSE and self.Daed==FALSE and self.hp>600:#왼쪽걸어갈때
            self.movey=9*380
            self.monstery=245
            self.frame = (self.frame + 1 ) % 4
        elif self.turn == 1 and self.Damage==FALSE and self.Daed==FALSE and self.hp>=400 and self.hp<=600:#오른쪽날아갈때
            self.movey=4*380
            self.monstery=370
            if self.bool == FALSE:
                self.skill_sound.play(1)
            self.bool=TRUE
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == -1 and self.Damage==FALSE and self.Daed==FALSE and self.hp>=400 and self.hp<=600:#왼쪽날아갈때
            self.movey=5*380
            self.monstery=370
            if self.bool == FALSE:
                self.skill_sound.play(1)
            self.bool=TRUE
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == 1 and self.Damage==TRUE and self.Daed==FALSE and self.hp>=400 and self.hp<=600:#오른쪽날아갈때
            self.movey=4*380
            self.monstery=370
            if self.bool == FALSE:
                self.skill_sound.play(1)
            self.bool=TRUE
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == -1 and self.Damage==TRUE and self.Daed==FALSE and self.hp>=400 and self.hp<=600:#왼쪽날아갈때
            self.movey=5*380
            self.monstery=370
            if self.bool == FALSE:
                self.skill_sound.play(1)
            self.bool=TRUE
            self.frame = (self.frame + 1 ) % 1

        elif self.turn == 1 and self.Damage==FALSE and self.Daed==FALSE and 200<=self.hp and self.hp<=400:#오른쪽마법스킬
            self.movey=2*380
            self.monstery=245
            if self.bool2 == FALSE:
                self.skill2_sound.play(1)

            self.bool2=TRUE
            self.frame = (self.frame + 1 ) % 19
        elif self.turn == -1 and self.Damage==FALSE and self.Daed==FALSE and 200<=self.hp and self.hp<=400:#왼쪽마법스킬
            self.movey=3*380
            self.monstery=245
            if self.bool2 == FALSE:
                self.skill2_sound.play(1)
            self.bool2=TRUE
            self.frame = (self.frame + 1 ) % 19
        elif self.turn == 1 and self.Damage==TRUE and self.Daed==FALSE and 200<=self.hp and self.hp<=400:#오른쪽마법스킬
            self.movey=2*380
            self.monstery=245
            if self.bool2 == FALSE:
                self.skill2_sound.play(1)
            self.bool2=TRUE
            self.frame = (self.frame + 1 ) % 19
        elif self.turn == -1 and self.Damage==TRUE and self.Daed==FALSE and 200<=self.hp and self.hp<=400:#왼쪽마법스킬
            self.movey=3*380
            self.monstery=245
            if self.bool2 == FALSE:
                self.skill2_sound.play(1)
            self.bool2=TRUE
            self.frame = (self.frame + 1 ) % 19
        elif self.turn == 1 and self.Damage==FALSE and self.Daed==FALSE and 200>self.hp and self.hp>=1:#마지막 피200남았을때
            self.movey=8*380
            self.monstery=245
            self.frame = (self.frame + 1 ) % 4
        elif self.turn == -1 and self.Damage==FALSE and self.Daed==FALSE and 200>self.hp and self.hp>=1:#마지막 피200남았을때
            self.movey=9*380
            self.monstery=245
            self.frame = (self.frame + 1 ) % 4
        elif self.turn == 1 and self.Damage==TRUE:#오른쪽보고있을때피격
            self.movey=6*380
            self.damage_sound.play(1)
            if self.hp>400 and self.hp<600:
                self.monstery=450
            else:
                self.monstery=245
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == -1 and self.Damage==TRUE:#왼쪽보고있을때피격
            self.movey=7*380
            self.damage_sound.play(1)
            if self.hp>400 and self.hp<600:
                self.monstery=450
            else:
                self.monstery=245
            self.frame = (self.frame + 1 ) % 1
        elif self.turn == 1  and self.Daed==TRUE :#오른쪽보고있을때 죽었을때
            self.movey=0*380
            self.monstery=245
            if self.bool3 == FALSE:
                self.die_sound.play(1)
            self.bool3=TRUE
            self.frame = (self.frame + 1 ) % 12
        elif self.turn == -1 and self.Daed==TRUE :#왼쪽보고있을때 죽었을때
            self.movey=1*380
            self.monstery=245
            if self.bool3 == FALSE:
                self.die_sound.play(1)
            self.bool3=TRUE
            self.frame = (self.frame + 1 ) % 12
        if self.monsterx >700:
            self.turn *=-1
        elif self.monsterx < 120:
            self.turn *=-1
        elif state==RIGHT_RUN and bkcheck==TRUE:
            self.monsterx-=self.speed
        elif state==LEFT_RUN and bkcheck==TRUE:
            self.monsterx+=self.speed
        self.monsterx += self.speed*self.turn

    def draw(self):
        self.image.clip_draw(self.frame * 330,  self.movey, 330, 380,self.monsterx, self.monstery)
        self.image3.clip_draw(0, 0, self.hp, 50,400, 550)
        if self.damage1==TRUE:
            self.image4.clip_draw(0, 0, 126, 47,self.monsterx, self.monstery+38)
        if self.damage2==TRUE:
            self.image5.clip_draw(0, 0, 126, 47,self.monsterx, self.monstery+45)
        if self.damage3==TRUE:
            self.image6.clip_draw(0, 0, 126, 47,self.monsterx, self.monstery+53)
    def get_bb(self):
        return self.monsterx-50,self.monstery-170,self.monsterx+50,self.monstery+20
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
class Ball:
    def __init__(self):
        self.x,self.y =random.randint(0,1000),600
        self.fall_speed = random.randint(5,25)
        self.image = load_image('snow.png')
    def update(self):
        self.y-=self.fall_speed
        if self.y<20:
            self.y=600
    def draw(self):
        self.image.clip_draw(0, 0, 6, 6,self.x, self.y)
class Bigball:
    def __init__(self):
        self.x,self.y =random.randint(0,800),600
        self.fall_speed = random.randint(3,25)
        self.image = load_image('Bigball.png')
    def update(self):
        self.y-=self.fall_speed
        if self.y<20:
            self.y=600
    def draw(self):
        self.image.clip_draw(0, 0, 60, 50,self.x, self.y)
    def get_bb(self):
        return self.x-17,self.y-17,self.x+17,self.y+17
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
class Smallball:
    global xx
    global tt
    def __init__(self):
        self.x,self.y =xx,90
        self.movey=0
        self.frame=0
        self.fall_speed = random.randint(30,40)
        self.image = load_image('smallball.png')
    def update(self):
        if tt==1:#몬스터가오른쪽보고있으면
            self.x+=self.fall_speed
            self.movey=0
            self.frame = (self.frame + 1 ) % 3
        elif tt==-1:#몬스터가오른쪽보고있으면
            self.x-=self.fall_speed
            self.movey=1
            self.frame = (self.frame + 1 ) % 3
        if self.x>750 or self.x<50:
            self.x=xx
    def draw(self):
        self.image.clip_draw(self.frame*40, self.movey*30, 40, 30,self.x,self.y)
    def get_bb(self):
        return self.x-10,self.y-25,self.x+10,self.y-5
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Boy:
    global isGoRight
    global isGoLeft
    def __init__(self):
        self.x, self.y = 50, 90
        self.frame = 0
        self.damage=0
        self.count=0
        self.hp,self.mp=228,235
        self.image = load_image('character.png')
        self.image2 = load_image('charterhp.png')
        self.image3 = load_image('chartermp.png')
        self.image4 = load_image('damage.png')
        self.attack_sound = load_wav('메인캐릭터기본공격.wav')
        self.attack_sound.set_volume(32)
        self.jump_sound = load_wav('메인캐릭터점프.wav')
        self.jump_sound.set_volume(32)
        self.drink_sound = load_wav('메인캐릭터물약.wav')
        self.drink_sound.set_volume(32)
        self.skill_sound = load_wav('메인캐릭터스킬1.wav')
        self.skill_sound.set_volume(32)
        self.skill2_sound = load_wav('메인캐릭터스킬2.wav')
        self.skill2_sound.set_volume(32)
        self.skill3_sound = load_wav('메인캐릭터스킬3.wav')
        self.skill3_sound.set_volume(32)
        self.damage_sound = load_wav('메인캐릭터데미지.wav')
        self.damage_sound.set_volume(32)
    def attack(self):
        self.attack_sound.play(1)
    def jump(self):
        self.jump_sound.play(1)
    def drink(self):
        self.drink_sound.play(1)
    def skill(self):
        self.skill_sound.play(1)
    def skill2(self):
        self.skill2_sound.play(1)
    def skill3(self):
        self.skill3_sound.play(1)
    def damages(self):
        self.damage_sound.play(1)
    def update(self):
        if isGoRight==TRUE or isGoLeft==TRUE:
            self.frame = (self.frame + 1) % 4
        elif state == RIGHT_STAND or state == LEFT_STAND:
            self.frame = 0
        elif state == RIGHT_JUMP or state == LEFT_JUMP:
            self.frame = (self.frame + 1) % 3
        elif state == RIGHT_ATTACK or state == LEFT_ATTACK:
            self.frame = (self.frame + 1) % 3
        elif state == RIGHT_SKILL or state == LEFT_SKILL or state==RIGHT_SKILL2 or state == LEFT_SKILL2 or state == RIGHT_SKILL3 or state == LEFT_SKILL3:
            self.frame = (self.frame + 1) % 4
        elif state == RIGHT_DAMAGE or state == LEFT_DAMAGE or state==MPDEAD:
            self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame * 80, movey, 80, 95,x, y)
        self.image2.clip_draw(0, 0, self.hp, 32,400-235, 90-72)
        self.image3.clip_draw(0, 0, self.mp, 33,400-2, 90-73)
        if self.damage==TRUE:
            self.image4.clip_draw(0, 0, 80,35,x, y+58)
    def get_bb(self):
        return x-30,y-50,x+30,y+50
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Boydead:
    def __init__(self):
        self.frame = 0
        self.image = load_image('dead.png')
        self.die_sound = load_wav('메인캐릭터다이.wav')
        self.die_sound.set_volume(128)
    def die(self):
       self.die_sound.play(1)
    def update(self):
        self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 250,x, y+95)
#------------------------------------------------------------------------------
def enter():
    global boy,boydead, grass,magic,magic2,magic3,monster,team,ball,balls,bigball,bigballs,smallball
    boy=Boy()
    boydead=Boydead()
    grass = Grass()
    magic=Magic()
    magic2=Magic2()
    magic3=Magic3()
    monster=Monster()
    team = [Monster() for i in range(1)]
    ball=Ball()
    balls=[Ball() for i in range(50)]
    bigball=Bigball()
    bigballs=[Bigball() for i in range(11)]
    smallball=Smallball()

def exit():
   global boy,boydead, grass,magic,magic2,magic3,monster,team,ball,balls,bigball,bigballs,smallball
   del(boy)
   del(boydead)
   del(grass)
   del(magic)
   del(magic2)
   del(magic3)
   del(monster)
   del(ball)
   del(balls)
   del(bigball)
   del(bigballs)
   del(smallball)
def pause():
    pass
def resume():
    pass
def handle_events():
    global running
    global x,y
    global jumpy
    global movey
    global frame
    global magicx
    global bool
    global count,count2,count3
    global isMagic,isMagic2,isMagic3
    global state
    global right
    global framemagic
    global jump
    global isJump
    global gravity
    global bkcheck
    global bkx
    global Touch
    global Touch2
    global boy
    global isGoRight
    global isGoLeft
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework_maple.quit()
#------------------------------------키조작-----------------------------------
        elif event.type == SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
               game_framework_maple.quit()
            elif event.key == SDLK_RIGHT:
                right=TRUE
                isGoRight=TRUE
            elif event.key == SDLK_LEFT:
                right=FALSE
                isGoLeft=TRUE
            elif event.key ==SDLK_UP:
                state=POTAL_STAND
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
            elif event.key == SDLK_1:
                state=HPUP
            elif event.key == SDLK_2 :
                state=MPUP
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                isGoRight=FALSE
                state=RIGHT_STAND
            elif event.key == SDLK_LEFT:
                isGoLeft=FALSE
                state=LEFT_STAND
            if event.key == SDLK_o:
                state=RIGHT_STAND
            elif event.key == SDLK_p:
                state=LEFT_STAND
################################실행################################
    if state==RIGHT_STAND:
            movey=860
    elif state==LEFT_STAND:
        movey=955
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
            boy.jump()
    elif state==LEFT_JUMP:
       if isJump == FALSE:
            movey=570
            jump = 35.0
            gravity = 7.0
            isJump = TRUE
            boy.jump()
    elif state==RIGHT_ATTACK:
        movey=0
        boy.attack()
    elif state==LEFT_ATTACK:
        movey=95
        boy.attack()
    elif state==RIGHT_SKILL:
       movey=190
       boy.skill()
       if isMagic == FALSE:
           isMagic = TRUE
    elif state==LEFT_SKILL:
        movey=285
        boy.skill()
        if isMagic == FALSE:
            isMagic = TRUE
    elif state==RIGHT_SKILL2:
       movey=190
       boy.skill2()
       if isMagic2 == FALSE:
           isMagic2 = TRUE
    elif state==LEFT_SKILL2:
        movey=285
        boy.skill2()
        if isMagic2 == FALSE:
            isMagic2 = TRUE
    elif state==RIGHT_SKILL3:
       movey=190
       boy.skill3()
       if isMagic3 == FALSE:
           isMagic3 = TRUE
    elif state==LEFT_SKILL3:
        movey=285
        boy.skill3()
        if isMagic3 == FALSE:
            isMagic3 = TRUE
    elif state==RIGHT_DAMAGE:
        movey=1045
        boy.damages()
        if x<775 and x>25:
            x=x-5
    elif state==LEFT_DAMAGE:
        movey=1140
        boy.damages()
        if x<775 and x>0:
            x=x+5
    elif state==HPUP and boy.hp<235:
        boy.hp=boy.hp+23
        boy.drink()
    elif state==MPUP and boy.mp<228:
        boy.mp=boy.mp+23
        boy.drink()
    elif state==MPDEAD:
        if right==TRUE:
            movey=1045
        if right==FALSE:
            movey=1140
        isMagic=FALSE
        isMagic2=FALSE
        isMagic3=FALSE

#배경화면함
    # if bkx<790 and bkx>10and right==TRUE and x> 400.0:
    #     bkcheck = TRUE
    # elif bkx<790 and bkx>10and right==FALSE and x< 400.0:
    #     bkcheck = TRUE
    # elif bkx>=790 :
    #     bkcheck = FALSE
    #     if x>400 :
    #         x=400
    #         bkcheck=TRUE
    # elif bkx<=10 :
    #    bkcheck = FALSE
    #    if x<400 :
    #        x=400
    #        bkcheck=TRUE

#매직함수
    if isMagic == TRUE and state==RIGHT_SKILL:
        magicx=magicx+45.5
        boy.mp=boy.mp-2
        if magicx>300:
            magicx=0
            isMagic = FALSE
            movey=860
            state = RIGHT_STAND
    if isMagic == TRUE and state==LEFT_SKILL :
        magicx=magicx-45.5
        boy.mp=boy.mp-2
        if magicx<-300:#바로위보면 이해!
            magicx=0
            isMagic = FALSE
            movey=955
            state = LEFT_STAND
    if isMagic2 == TRUE and state==RIGHT_SKILL2 :
        count2= count2 + 1
        boy.mp=boy.mp-7
        if count2==7:
            count2=0
            isMagic2 = FALSE
            movey=860
            state = RIGHT_STAND
    if isMagic2 == TRUE and state==LEFT_SKILL2:
        count2=count2+1
        boy.mp=boy.mp-12
        if count2==7:
            count2=0
            isMagic2 = FALSE
            movey=955
            state = LEFT_STAND
    if isMagic3 == TRUE and state==RIGHT_SKILL3 :
        count3=count3+1
        boy.mp=boy.mp-7
        if count3==20:
            count3=0
            isMagic3 = FALSE
            movey=860
            state = RIGHT_STAND
    if isMagic3 == TRUE and state==LEFT_SKILL3:
        count3=count3+1
        boy.mp=boy.mp-7
        if count3==20:
            isMagic3 = FALSE
            movey=955
            state = LEFT_STAND
            count3=0
#걷기-함수
    if isGoRight== TRUE:
        if x<750 :
            x=x+17.5
            movey=760
            magicx=0
    if isGoLeft== TRUE:
        if x>50 :
            x=x-17.5
            movey=665
            magicx=0
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
            elif right == FALSE:
                movey=955
                state = LEFT_STAND

def collide(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False#아닐때
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False
    if state==DEAD:return False
    return True
    pass

def collide1(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    if state==RIGHT_SKILL2:return False
    if state==LEFT_SKILL2:return False
    if state==RIGHT_SKILL3:return False
    if state==LEFT_SKILL3:return False

    if isMagic==FALSE and state==POTAL_STAND:return False
    if isMagic==FALSE and state==HPUP:return False
    if isMagic==FALSE and state==MPUP:return False
    if state==DEAD:return False
    if state==MPDEAD:return False
    if state==HPUP:return False
    if state==MPUP:return False

    if state==RIGHT_STAND :return False
    if state==RIGHT_RUN :return False
    if state==RIGHT_JUMP:return False
    if state==RIGHT_DAMAGE:return False
    if state==RIGHT_ATTACK:return False

    if state==LEFT_STAND :return False
    if state==LEFT_RUN :return False
    if state==LEFT_JUMP:return False
    if state==LEFT_DAMAGE:return False
    if state==LEFT_ATTACK:return False

    return True
    pass
def collide2(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False


    if state==RIGHT_SKILL:return False
    if state==LEFT_SKILL:return False
    if state==RIGHT_SKILL3:return False
    if state==LEFT_SKILL3:return False

    if state==POTAL_STAND:return False
    if isMagic==FALSE and state==HPUP:return False
    if isMagic==FALSE and state==MPUP:return False
    if state==DEAD:return False
    if state==MPDEAD:return False
    if state==HPUP:return False
    if state==MPUP:return False

    if state==RIGHT_STAND :return False
    if state==RIGHT_RUN :return False
    if state==RIGHT_JUMP:return False
    if state==RIGHT_DAMAGE:return False
    if state==RIGHT_ATTACK:return False

    if state==LEFT_STAND :return False
    if state==LEFT_RUN :return False
    if state==LEFT_JUMP:return False
    if state==LEFT_DAMAGE:return False
    if state==LEFT_ATTACK:return False
    return True
    pass

def collide3(a, b):#충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    if state==RIGHT_SKILL:return False
    if state==LEFT_SKILL:return False
    if state==RIGHT_SKILL2:return False
    if state==LEFT_SKILL2:return False

    if state==POTAL_STAND:return False
    if isMagic==FALSE and state==HPUP:return False
    if isMagic==FALSE and state==MPUP:return False
    if state==DEAD:return False
    if state==MPDEAD:return False
    if state==HPUP:return False
    if state==MPUP:return False

    if state==RIGHT_STAND :return False
    if state==RIGHT_RUN :return False
    if state==RIGHT_JUMP:return False
    if state==RIGHT_DAMAGE:return False
    if state==RIGHT_ATTACK:return False

    if state==LEFT_STAND :return False
    if state==LEFT_RUN :return False
    if state==LEFT_JUMP:return False
    if state==LEFT_DAMAGE:return False
    if state==LEFT_ATTACK:return False
    return True
    pass

def collide4(a, b):#빅볼이랑보이
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:

        return False#아닐때
    if right_a<left_b:

        return False
    if top_a<bottom_b:

        return False
    if bottom_a>top_b:

        return False
    if state==DEAD:return False
    return True
    pass

def collide5(a, b):#스몰볼 충돌처리
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()
    if left_a>right_b:
        return False#아닐때
    if right_a<left_b:
        return False
    if top_a<bottom_b:
        return False
    if bottom_a>top_b:
        return False
    if state==DEAD:return False
    return True
    pass

def update():
    global state
    global movey
    global x
    global tt
    global xx
    global monster
    boy.update()
    boydead.update()
    magic.update()
    magic2.update()
    magic3.update()
    if 200<=monster.hp and monster.hp<=400:
         smallball.update()
    elif 200>=monster.hp:
        smallball.y=600
        print("600으로올라감")
    for ball in balls:
          ball.update()
    for bigball in bigballs:
        for monster in team:
            if 400<=monster.hp and monster.hp<=600:
                bigball.update()
        if collide4(bigball,boy):#빅볼 충돌처리
            boy.damage=TRUE
            boy.hp=boy.hp-5
            if right == TRUE and state==RIGHT_STAND:
                state=RIGHT_DAMAGE
            elif right == FALSE and state==LEFT_STAND:
                state=LEFT_DAMAGE
            elif right == TRUE and state==RIGHT_RUN:
                state=RIGHT_DAMAGE
            elif right == FALSE and state==LEFT_RUN:
                state=LEFT_DAMAGE

    for monster in team:
         monster.update()
         xx=monster.monsterx
         tt=monster.turn

    for monster in team:
        if collide(boy,monster):#몬스터랑 캐릭터 부딪쳤을때!
            boy.damage=TRUE
            boy.hp=boy.hp-2
            if right == TRUE and state==RIGHT_STAND:
                state=RIGHT_DAMAGE
            elif right == FALSE and state==LEFT_STAND:
                state=LEFT_DAMAGE
            elif right == TRUE and state==RIGHT_RUN:
                state=RIGHT_DAMAGE
            elif right == FALSE and state==LEFT_RUN:
                state=LEFT_DAMAGE
            elif right == TRUE and state==RIGHT_ATTACK:
                monster.hp=monster.hp-2#맞았을때+1
                if monster.monsterx<775 and monster.monsterx>25:
                   monster.monsterx=monster.monsterx+150
                if right==TRUE and monster.turn==1:#몬스터피격시따라오게
                    monster.turn *=-1
                elif right==FALSE and monster.turn==-1:
                    monster.turn *=-1
            elif right == FALSE and state==LEFT_ATTACK:
                monster.hp=monster.hp-2#맞았을때+1
                if monster.monsterx<775 and monster.monsterx>25:
                    monster.monsterx=monster.monsterx-150
                if right==TRUE and monster.turn==1:#몬스터피격시따라오게
                    monster.turn *=-1
                elif right==FALSE and monster.turn==-1:
                    monster.turn *=-1

        elif collide1(magic,monster):
            monster.damage1=TRUE
            if right==TRUE and monster.turn==1:#몬스터피격시따라오게
                monster.turn *=-1
            elif right==FALSE and monster.turn==-1:
                monster.turn *=-1
            monster.Damage=TRUE
            monster.count=monster.count+0.05#맞았을때+1
            monster.hp=monster.hp-5#맞았을때+1
            if monster.hp<0:#9번맞으면 죽게된다
                monster.Damage=FALSE
                monster.Daed=TRUE
            if monster.count<4:#맞고 다시 달리게
                monster.count3=0
            if monster.count>4.04:#다섯번째일때는 죽음
                monster.count2=0

        elif collide2(magic2,monster):
            monster.damage2=TRUE
            if right==TRUE and monster.turn==1:#몬스터피격시따라오게
                monster.turn *=-1
            elif right==FALSE and monster.turn==-1:
                monster.turn *=-1
            monster.Damage=TRUE
            monster.count=monster.count+0.05#맞았을때+0.5
            monster.hp=monster.hp-5#맞았을때+1
            if monster.hp<0:
                monster.Damage=FALSE
                monster.Daed=TRUE
            if monster.count<6:#맞고 다시 원상복귀할때
                monster.count3=0
            if monster.count>6.04:#네번째일때는 죽어야하므로 두번째 카운트를초기화해준다
                monster.count2=0

        elif collide3(magic3,monster):
            monster.damage3=TRUE
            if right==TRUE and monster.turn==1:#몬스터피격시따라오게
                monster.turn *=-1
            elif right==FALSE and monster.turn==-1:
                monster.turn *=-1
            monster.Damage=TRUE
            monster.count=monster.count+0.05#맞았을때+0.5
            monster.hp=monster.hp-5#맞았을때+1
            if monster.hp<0:#3번맞으면 죽게된다
                monster.Damage=FALSE
                monster.Daed=TRUE

            if monster.count<8:#맞고 다시 원상복귀할때
                monster.count3=0
            if monster.count>8.04:#네번째일때는 죽어야하므로 두번째 카운트를초기화해준다
                monster.count2=0
            if monster.hp<1:
                monster.count2=0

        elif collide5(smallball,boy):#스몰볼 충돌처리
            boy.damage=TRUE
            boy.hp=boy.hp-8
            if right == TRUE and state==RIGHT_STAND:
                state=RIGHT_DAMAGE
            elif right == FALSE and state==LEFT_STAND:
                state=LEFT_DAMAGE
            elif right == TRUE and state==RIGHT_RUN:
                state=RIGHT_DAMAGE
            elif right == FALSE and state==LEFT_RUN:
                state=LEFT_DAMAGE
#타임-죽을때!-----------------------------------------------------------
        if monster.Damage==TRUE and monster.count3>1.5:
            monster.damage1=FALSE
            monster.damage2=FALSE
            monster.damage3=FALSE
        if monster.Damage==TRUE and monster.count3>3:
            monster.Damage=FALSE
            monster.Daed=FALSE
        elif monster.Daed==TRUE and monster.count2>55:
            team.remove(monster)

#타임-보이피격시 데미지표시사라지게
        if boy.damage==TRUE:
            boy.count=boy.count+1
        if boy.damage==TRUE and boy.count>3:
            boy.count=0
            boy.damage = FALSE
#죽는것+hp+mp컨트롤타워
        if boy.hp<0:
           state=DEAD
           boydead.die()
        if boy.mp<0:
            state=MPDEAD
            if boy.hp<0:
                state=DEAD

def draw():
    clear_canvas()
    grass.draw()
    magic.draw()
    #magic.draw_bb()
    magic2.draw()
   # magic2.draw_bb()
    magic3.draw()
    #magic3.draw_bb()
    for monster in team:
        monster.draw()
       # monster.draw_bb()
    for ball in balls:
        ball.draw()
    for bigball in bigballs:
        if 400<monster.hp and monster.hp<=600:
            bigball.draw()
            #bigball.draw_bb()
        if monster.hp<400:
            bigballs.remove(bigball)
    if 200<=monster.hp and monster.hp<=400:
        smallball.draw()

    if state!=DEAD:
        boy.draw()
        #boy.draw_bb()
    elif state==DEAD:
        boydead.draw()
    update_canvas()
    delay(0.07)