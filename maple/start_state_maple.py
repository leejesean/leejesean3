import game_framework_maple
import title_state_maple

from pico2d import *


name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    open_canvas()
    image=load_image('kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if (logo_time>1.0):
        logo_time=0
        #game_framework_maple.quit()#->이렇게해주는이유는 바로 끝나잖아
        game_framework_maple.push_state(title_state_maple)#exit를 실행하지않고 ㄱㄱ
    delay(0.01)
    logo_time+=0.01

def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




