import audio
import arcade
from player_bullet import player_bull
from Constants import PLAYER_IMG, PLAYER_IMG_EMPTY
from admin import put_score
from datetime import datetime
CHARACTER_SCALING = 0.05
STARTING_X = 400
STARTING_Y = 100
MOVEMENT_SPEED = 5
STARTING_LIVES = 3
global shoot_sound
shoot_sound = audio.shoot_sound


class Player:
    def __init__(self, player_img):
        # Load the player sprite
        self.sprite = arcade.Sprite(player_img, CHARACTER_SCALING)
        # Set the positions to the X and Y value
        self.sprite.center_x = STARTING_X
        self.sprite.center_y = STARTING_Y
        self.score = 0

        # Set the lives
        self.player_lives = STARTING_LIVES
        self.time_of_death = -480

        # Define the inputs for movement
        self.is_left_press = False
        self.is_right_press = False
        self.last_press = "NONE"

        # Create a spritelist of bullets
        self.player_bullet_list = arcade.SpriteList()

        # Score and life gaining variables
        self.delta_score = 0
        self.lives_gained = 0
        self.hit = False

    def kill(self, time_of_death):
        # Lower the lift counter by 1
        self.player_lives -= 1
        self.time_of_death = time_of_death
        self.hit = True
        # Exit the game if you have no lives
        if self.player_lives == 0:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            put_score(self.score, time)
            return False

        self.is_right_press = False
        self.is_left_press = False

        self.change_vel(0)

        # Move the shit back to the center
        self.sprite.center_x = STARTING_X
        self.sprite.center_y = STARTING_Y

        # Make the player blink
        self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        return True

    # Change the velocity of the ship
    def change_vel(self, velocity):
        self.sprite.change_x = velocity

    # increment the score and delta score
    def increase_score(self, points):
        self.score += points
        self.delta_score = points
    
    # defines the inputs that the ship can be given
    def inputs(self, key):
        if key == arcade.key.LEFT and self.hit == False:
            self.is_left_press = True
            self.last_press = "LEFT"

        # if you press the right key set the variable to true and
        # the last pressed key to RIGHT
        if key == arcade.key.RIGHT and self.hit == False:
            self.is_right_press = True
            self.last_press = "RIGHT"

        # player shoots a bullet by pressing space
        if key == arcade.key.SPACE and self.hit == False:
            if len(self.player_bullet_list) < 2:
                arcade.play_sound(shoot_sound,.5)
                bullet = player_bull(self.sprite.center_x, 120)
                self.player_bullet_list.append(bullet)
        # Used in graphics to pause game now
        # elif key == arcade.key.ESCAPE:
        #     arcade.exit()

    # Logic for the ship to move correctly
    def release(self, key):
        if key == arcade.key.LEFT:
            self.is_left_press = False
            if self.is_right_press == True:
                self.last_press = "RIGHT"
            else:
                self.last_press = "NONE"

        # if the key released is right update the bool
        # and check if other key is pressed
        if key == arcade.key.RIGHT:
            self.is_right_press = False
            if self.is_left_press == True:
                self.last_press = "LEFT"
            else:
                self.last_press = "NONE"

    # if statements to decide if the player gained a life
    def gain_life(self):
        if(self.delta_score >= 20000 and self.lives_gained == 0):
            self.player_lives += 1
            self.lives_gained += 1
            self.delta_score -= 20000
        elif(self.delta_score >= 40000 and self.lives_gained == 1):
            self.player_lives += 1
            self.lives_gained += 1
            self.delta_score -= 40000
        elif(self.delta_score >= 60000):
            self.player_lives += 1
            self.lives_gained += 1
            self.delta_score -= 60000

    # Update the sprite each frame and define borders
    def update_state(self, time):
        # logic for making the player blink
        if time < self.time_of_death + 240:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        elif time > self.time_of_death + 240 and time < self.time_of_death + 270:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG)
        elif time > self.time_of_death + 270 and time < self.time_of_death + 300:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        elif time > self.time_of_death + 300 and time < self.time_of_death + 330:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG)
        elif time > self.time_of_death + 330 and time < self.time_of_death + 360:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        elif time > self.time_of_death + 360 and time < self.time_of_death + 375:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG)
        elif time > self.time_of_death + 375 and time < self.time_of_death + 390:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        elif time > self.time_of_death + 390 and time < self.time_of_death + 405:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG)
        elif time > self.time_of_death + 405 and time < self.time_of_death + 420:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        elif time > self.time_of_death + 420 and time < self.time_of_death + 435:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG)
        elif time > self.time_of_death + 435 and time < self.time_of_death + 450:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        elif time > self.time_of_death + 450 and time < self.time_of_death + 465:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG)
        elif time > self.time_of_death + 465 and time < self.time_of_death + 480:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG_EMPTY)
        else:
            self.sprite.texture = arcade.load_texture(PLAYER_IMG)
            if not self.hit:
                # if right key is pressed and the last key is right move right
                if self.is_right_press == True and self.last_press == "RIGHT":
                    self.change_vel(MOVEMENT_SPEED)

                # if left key is pressed and the last key is left move left
                if self.is_left_press == True and self.last_press == "LEFT":
                    self.change_vel(-MOVEMENT_SPEED)

                # if at any point the last pressed key is none do not move
                if self.last_press == "NONE":
                    self.change_vel(0)

                # Update the sprites and check for collisions
                if self.sprite.center_x > 780:
                    if self.sprite.change_x > 0:
                        self.sprite.change_x = 0
                # check is the player will hit the left side of the screen
                elif self.sprite.center_x < 20:
                    if self.sprite.change_x < 0:
                        self.sprite.change_x = 0
