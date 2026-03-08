def on_button_pressed_a():
    global γινόμενο
    γινόμενο = α * β
    basic.show_number(γινόμενο)
input.on_button_pressed(Button.A, on_button_pressed_a)

γινόμενο = 0
β = 0
α = 0
α = 8
β = 4

def on_forever():
    pass
basic.forever(on_forever)
