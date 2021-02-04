input.onButtonPressed(Button.A, function () {
    ship.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    shoot = game.createSprite(ship.get(LedSpriteProperty.X), ship.get(LedSpriteProperty.Y))
    shoot.change(LedSpriteProperty.Brightness, 80)
    for (let index = 0; index < 4; index++) {
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
    }
    if (shoot.get(LedSpriteProperty.Y) <= 0) {
        shoot.delete()
    }
})
input.onButtonPressed(Button.B, function () {
    ship.move(1)
})
let enemy: game.LedSprite = null
let shoot: game.LedSprite = null
let ship: game.LedSprite = null
ship = game.createSprite(2, 4)
basic.forever(function () {
    enemy = game.createSprite(randint(0, 4), 0)
    enemy.set(LedSpriteProperty.Brightness, 150)
    basic.pause(100)
    enemy.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        enemy.move(1)
        basic.pause(500)
        if (enemy.isTouching(ship)) {
            game.gameOver()
        }
    }
    if (enemy.isTouchingEdge()) {
        enemy.delete()
    }
})
basic.forever(function () {
	
})
