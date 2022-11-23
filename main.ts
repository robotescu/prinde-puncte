input.onGesture(Gesture.LogoUp, function () {
    led.unplot(x, y)
    y = y + 1
    led.plot(x, y)
})
input.onGesture(Gesture.TiltLeft, function () {
    led.unplot(x, y)
    x = x - 1
    led.plot(x, y)
})
input.onButtonPressed(Button.AB, function () {
    punct_x = randint(0, 4)
    punct_y = randint(0, 4)
    led.plot(punct_x, punct_y)
})
input.onGesture(Gesture.TiltRight, function () {
    led.unplot(x, y)
    x = x + 1
    led.plot(x, y)
})
input.onGesture(Gesture.LogoDown, function () {
    led.unplot(x, y)
    y = y - 1
    led.plot(x, y)
})
let punct_y = 0
let punct_x = 0
let y = 0
let x = 0
x = 2
y = 2
led.plot(x, y)
