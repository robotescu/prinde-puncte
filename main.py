x=0
y=0
def on_button_pressed_ab():
    punct_x = randint(0,4)
    punct_y = randint(0,4)
    led.plot(punct_x, punct_y)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def inclina_dreapta():
    global x
    global y
    led.unplot(x, y)
    x = x+1
    led.plot(x, y)
input.on_gesture(Gesture.TILT_RIGHT, inclina_dreapta)
def inclina_stanga():
    global x
    global y
    led.unplot(x, y)
    x = x-1
    led.plot(x, y)
input.on_gesture(Gesture.TILT_LEFT, inclina_stanga)
def inclina_sus():
    global x
    global y
    led.unplot(x, y)
    y = y-1
    led.plot(x, y)
input.on_gesture(Gesture.LOGO_DOWN, inclina_sus)
def inclina_jos():
    global x
    global y
    led.unplot(x, y)
    y = y+1
    led.plot(x, y)
input.on_gesture(Gesture.LOGO_UP, inclina_jos)
