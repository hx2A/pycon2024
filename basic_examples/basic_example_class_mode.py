from py5 import Sketch


class BasicExample(Sketch):

    def settings(self):
        self.size(500, 500, self.P2D)

    def setup(self):
        self.stroke_weight(2)
        self.rect_mode(self.CENTER)
        self.background("gray")

    def draw(self):
        self.rect(self.mouse_x, self.mouse_y, 50, 50)

    def mouse_pressed(self):
        self.fill(self.random(255), self.random(255), self.random(255))

    def key_pressed(self):
        self.background("gray")


if __name__ == "__main__":
    BasicExample().run_sketch()
