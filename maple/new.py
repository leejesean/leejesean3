__author__ = '이제선'
from pico2d import *

def handle_events():
    global running
    global x
    global movey
    global Frame
    events = get_events()
    # fill here
    for event in events:#이번트들의이벤트를가져와서~
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                x=x+100
                movey=760
                Frame=4
            elif event.key==SDLK_LEFT:
                x=x-100
                movey=665
                Frame=4
            elif event.key==SDLK_ESCAPE:
                running=False

open_canvas()
grass = load_image('배경화면.png')
character = load_image('캐릭터.png')

running = True
x = 400
movey=855
frame = 0
Frame=1
while (running):
    clear_canvas()
    grass.draw(400, 475)
    character.clip_draw(frame * 80, movey, 80, 95, x, 90)#이미지상의위치x,y, 사진크기,위치
    update_canvas()
    frame = (frame +1) % 4

    delay(0.2)
    handle_events()

close_canvas()

