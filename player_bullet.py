import arcade
BULLET_SCALING = 0.08
bullet_img = "sprites/player_bullet.png"


class player_bull(arcade.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__(bullet_img, BULLET_SCALING)
        self.center_x = xpos
        self.center_y = ypos

    def move(self):
        self.center_y += 15

    def kill(self):
        self.remove_from_sprite_lists()
        del self
