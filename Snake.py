import curses
from random import randint

curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(20,60) #(y,x)
win.keypad(1)
win.border(0)
win.nodelay(1)

score = 0
snake = [(4,10),(4,9),(4,8)]
food = (10,20)
win.addch(food[0],food[1],"O")

ESC = 27
key = curses.KEY_RIGHT
while key != ESC:
    win.addstr(0,2,"Score = "+ str(score) + " ")
    win.timeout(100)

    prev_key = key
    event = win.getch()
    key = event if event != 1 else prev_key

    if key not in [curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_UP,curses.KEY_DOWN,ESC]:
        key = prev_key

    #calculate next coordinates
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    snake.insert(0,(y,x))

    #check border
    if y == 0 or x == 0 or x == 59 or y == 19:break

    #check run on itself
    if snake[0] in snake[1:] : break

    #check if snake has eaten
    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18),randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0],food[1],"O")
    else:
        #moving the snake
        last = snake.pop()
        win.addch(last[0],last[1]," ")

    win.addch(snake[0][0],snake[0][1],"*")

curses.endwin()
print(f"Score = {score}")