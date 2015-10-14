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
jump=0
isJump=False
gravity=0
RIGHT_RUN,LEFT_RUN,RIGHT_STAND,LEFT_STAND,RIGHT_JUMP,LEFT_JUMP  = 1, 2,3, 4,5,6 #사진순서대로~
TRUE ,FALSE=1,0
state=RIGHT_STAND
right=TRUE

class Grass:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400,475)

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

    def draw(self):
        self.image.clip_draw(self.frame * 80, movey, 80, 95,x, y)

def enter():
    global boy, grass
    boy=Boy()
    grass = Grass()

def exit():
   global boy, grass
   del(boy)
   del(grass)

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
    global bool
    global state
    global right
    global jump
    global isJump
    global gravity
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework_maple.quit()

######################키조작#########################
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

        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                state=RIGHT_STAND
                right=TRUE
            elif event.key == SDLK_LEFT:
                state=LEFT_STAND
                right=FALSE
#####################실행###########################
        if  state==RIGHT_RUN:
            x=x+17.5
            movey=760
        elif state==LEFT_RUN:
            x=x-17.5
            movey=665
        elif state==RIGHT_STAND:
            movey=860
        elif state==LEFT_STAND:
            movey=955
        elif state==RIGHT_JUMP:
           if isJump == FALSE:
                movey=475
                jump = 25.0
                gravity = 0.25
                isJump = TRUE
        elif state==LEFT_JUMP:
           if isJump == FALSE:
                movey=570
                jump = 25.0
                gravity = 0.25
                isJump = TRUE

        if isJump == TRUE:#점프---------------------------------------음수가안되는듯하다 버그발생!
            y = y+ jump
            jump = jump-gravity
            if y<10:
                isJump == FALSE

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    delay(0.11)





