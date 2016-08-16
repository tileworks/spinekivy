from kivy.graphics import Canvas, Color, Mesh

MODE_TRIANGLE_FAN = 'triangle_fan'
MODE_TRIANGLES = 'triangles'


class Sprite(Canvas):

    color = None
    mesh = None

    def __init__(self):
        super(Sprite, self).__init__()
        with self:
            self.color = Color()
            self.mesh = Mesh(vertices=[0.0] * 16,
                             indices=range(4),
                             mode=MODE_TRIANGLE_FAN)
