from pico2d import *
import game_framework_maple
import title_state_maple

name = "MainState"

boy = None
grass = None
font = None
running = True
x=400
movey=855
frame=0

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
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 80, movey, 80, 95,x, 90)

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
    global movey
    global frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework_maple.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                game_framework_maple.change_state(title_state_maple)
            if event.key == SDLK_RIGHT:
                x=x+80
                movey=760
                frame=4
            elif event.key == SDLK_LEFT:
                x=x-80
                movey=665
                frame=4

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    delay(0.1)





