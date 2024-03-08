import arcade
BULLET_SCALING = 0.015
bullet_img = "sprites/enemy_bullet.png"


class enemy_bull(arcade.Sprite):
    def __init__(self, xpos, ypos, delta_x, delta_y):
        super().__init__(bullet_img, BULLET_SCALING)
        self.center_x = xpos
        self.center_y = ypos
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.velocity = 4.5

    def move(self):
        self.center_x += self.velocity * self.delta_x
        self.center_y += self.velocity * self.delta_y

    def kill(self):
        self.remove_from_sprite_lists()
        del self
