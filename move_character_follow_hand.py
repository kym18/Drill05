
from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def character_move(target_x, target_y):
    global x, y, dir
    global arrow_x, arrow_y
    speed = 30

    #캐릭터 이동시키기
    t = 0.1  # 보간 계수 (0.0에서 1.0 사이의 값)
    x = (1 - t) * x + t * target_x
    y = (1 - t) * y + t * target_y

    if(arrow_x > x):
        dir = 1  #right
    elif(arrow_x < x):
        dir = -1  #left

    # 화살표 위치바꾸기
    dis = math.sqrt((arrow_x - x) ** 2 + (arrow_y - y) ** 2)
    if dis < 10:
        arrow_x, arrow_y = random_hand_position()


def random_hand_position():
    return random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
arrow_x, arrow_y = random_hand_position()  # 초기 화살표
dir = 1

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character_move(arrow_x, arrow_y)
    if dir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

    arrow.draw(arrow_x, arrow_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.05)


close_canvas()
