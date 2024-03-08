import arcade
import Constants
from player_bullet import player_bull
import time
CHARACTER_SCALING = 0.05
STARTING_X = 400
STARTING_Y = 100
MOVEMENT_SPEED = 5

EXPLOSION_SCALING = 1.2

UPDATES_PER_FRAME = 10

# Represents an explosion when a player dies
class PlayerExplosion(arcade.Sprite):
        def __init__(self, xpos, ypos):
                super().__init__("sprites/player_explosion/1.png", EXPLOSION_SCALING)
                self.explosion_textures = [arcade.load_texture("sprites/player_explosion/1.png"), arcade.load_texture("sprites/player_explosion/2.png"), arcade.load_texture("sprites/player_explosion/3.png"), arcade.load_texture("sprites/player_explosion/4.png")]
                self.cur_texture = 0
                self.center_x = xpos
                self.center_y = ypos

        # Update the animation - switches the sprite every 10 frames and kills the sprite after 40 frames
        def update_animation(self, delta_time: float = 1 / 60):
            # Exploding animation
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.kill()
                return
            frame = self.cur_texture // UPDATES_PER_FRAME
            self.texture = self.explosion_textures[frame]

        def kill(self):
                self.remove_from_sprite_lists()
                del self
        
        