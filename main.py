def on_button_pressed_a():
    ship.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global shoot
    shoot = game.create_sprite(ship.get(LedSpriteProperty.X), ship.get(LedSpriteProperty.Y))
    shoot.change(LedSpriteProperty.BRIGHTNESS, 80)
    for index in range(4):
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
    if shoot.get(LedSpriteProperty.Y) <= 0:
        shoot.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    ship.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

enemy: game.LedSprite = None
shoot: game.LedSprite = None
ship: game.LedSprite = None
ship = game.create_sprite(2, 4)

def on_forever():
    global enemy
    enemy = game.create_sprite(randint(0, 4), 0)
    enemy.set(LedSpriteProperty.BRIGHTNESS, 150)
    enemy.turn(Direction.RIGHT, 90)
    basic.pause(100)
    for index2 in range(4):
        enemy.move(1)
        basic.pause(500)
        if enemy.is_touching(ship):
            enemy.delete()
            game.game_over()
        else:
            pass
    if enemy.is_touching_edge():
        enemy.delete()
basic.forever(on_forever)
