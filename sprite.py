from kivy.graphics import Canvas, Color, Mesh


class Sprite(Canvas):

    color = None
    mesh = None

    def __init__(self):
        super(Sprite, self).__init__()
        with self:
            self.color = Color(0, 0, 0, 0)
            self.mesh = Mesh(vertices=[0.0] * 16,
                             indices=range(4),
                             mode='triangle_fan')
