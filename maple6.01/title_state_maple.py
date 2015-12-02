import game_framework_maple
import main_state_maple

from pico2d import *

name = "TitleState"
image = None

def enter():
    global image
    image=load_image('title.png')

def exit():
    global image
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework_maple.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework_maple.quit()

            # elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            #     game_framework_maple.change_state(main_state_maple)#chage는 exit를실행!


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()


logo_time=0
def update():
    global logo_time
    if (logo_time>0.2):
        logo_time=0
        game_framework_maple.push_state(main_state_maple)#exit를 실행하지않고 ㄱㄱ
    delay(0.01)
    logo_time+=0.01


def pause():
    pass


def resume():
    pass






