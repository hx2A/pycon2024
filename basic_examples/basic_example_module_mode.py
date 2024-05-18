import py5


def setup():
    py5.size(500, 500, py5.P2D)
    py5.stroke_weight(2)
    py5.rect_mode(py5.CENTER)
    py5.background("gray")
    # py5.get_surface().set_always_on_top(True)


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 50, 50)


def mouse_pressed():
    py5.fill(py5.random(255), py5.random(255), py5.random(255))


def key_pressed():
    py5.background("gray")


py5.run_sketch()
