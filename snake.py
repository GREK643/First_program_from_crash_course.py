#first program that i wrote and i'm really proud
import random as rn
import curses as cs

s = cs.initscr()
cs.curs_set(0)
sh, sw = s.getmaxyx()
w = cs.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(175)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2]
]

food = [sh/2,sh/2]
w.addch(int(food[0]), int(food[1]), cs.ACS_PI)

key = cs.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        cs.endwin()
        quit()

    new_head = [snake[0][0],snake[0][1]]

    if key == cs.KEY_DOWN:
        new_head[0] += 1
    if key == cs.KEY_UP:
        new_head[0] -= 1
    if key == cs.KEY_LEFT:
        new_head[1] -= 1
    if key == cs.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0,new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                rn.randint(1,sh-1),
                rn.randint(1,sw-1)
             ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], cs.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]),' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), cs.ACS_CKBOARD)