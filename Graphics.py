import arcade
import arcade.gui
from player_bullet import player_bull
from enemy_bullet import enemy_bull
from Player import Player
from Constants import *
import random
import copy
from PlayerExplosion import PlayerExplosion
from EnemyExplosion import EnemyExplosion
from admin import get_top_scores
import subprocess
import audio

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Galaga"

CHARACTER_SCALING = 0.05
global score, intro_sound, hit_sound, death_sound
intro_sound = audio.intro_sound
hit_sound = audio.hit_sound
death_sound = audio.death_sound

# Start Menu View


class InstructionView(arcade.View):
    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.logo = arcade.load_texture(LOGO_IMG)
        self.points_list = []
        self.tick = 0
        self.logo_blink = False
        "UIManager Init"
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        "Button Init"
        start_game_button = arcade.gui.UIFlatButton(
            text="Start Game", width=150)
        high_score_button = arcade.gui.UIFlatButton(
            text="Check High Scores", width=150)
        instructions_button = arcade.gui.UIFlatButton(
            text="Instructions", width=150)
        exit_button = arcade.gui.UIFlatButton(text="Exit", width=150)
        "Init Grid Layout"
        self.grid = arcade.gui.UIBoxLayout(space_between=15)
        "Adding the buttons to the layout"
        self.grid.add(start_game_button)
        self.grid.add(instructions_button)
        self.grid.add(high_score_button)
        self.grid.add(exit_button)
        "Use the anchor to position the button on the screen"
        self.anchor = self.manager.add(
            arcade.gui.UIAnchorWidget(child=self.grid, align_y=-130))

        "Setting up events"
        @start_game_button.event("on_click")
        def on_click_start_button(event):
            "Passing the main game view"
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

        @instructions_button.event("on_click")
        def on_click_instructions_button(event):
            "Passing the instructions messagebox"
            self.inner_grid = arcade.gui.UIBoxLayout()
            message_box = arcade.gui.UIMessageBox(
                width=300,
                height=200,
                message_text=(
                    "Welcome to Galaga!\n"
                    "Press and hold the right arrow key to move right, left arrow key to move left.\n"
                    "Press space bar to shoot. Esc key to pause"
                ),
                buttons=["Ok"]
            )
            self.inner_grid.add(message_box)
            self.anchor = self.manager.add(
                arcade.gui.UIAnchorWidget(child=self.inner_grid, align_y=-60))

        @high_score_button.event("on_click")
        def on_click_high_score_button(event):
            "Passing the high score messagebox"
            high_score = get_top_scores()
            score1 = high_score[0]
            score2 = high_score[1]
            score3 = high_score[2]
            score4 = high_score[3]
            score5 = high_score[4]
            self.inner_grid = arcade.gui.UIBoxLayout()
            message_box_score = arcade.gui.UIMessageBox(
                width=300,
                height=200,
                message_text=(
                    "High Scores:\n"
                    "#1: " + str(score1) + "\n"
                    "#2: " + str(score2) + "\n"
                    "#3: " + str(score3) + "\n"
                    "#4: " + str(score4) + "\n"
                    "#5: " + str(score5) + "\n"
                ),
                buttons=["Ok"]
            )
            self.inner_grid.add(message_box_score)
            self.anchor = self.manager.add(
                arcade.gui.UIAnchorWidget(child=self.inner_grid, align_y=-60))

        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        "Enabing UI manager in this view"
        self.manager.enable()
        "Add Stars"
        for i in range(15):
            point = (random.randint(0, 800), random.randint(0, 600))
            self.points_list.append(point)

    def on_draw(self):
        "Rendering the view"
        self.clear()

        "Drawing the manager"
        self.manager.draw()

        "Checking the boolean for drawing"
        if self.logo_blink:
            self.logo.draw_sized(
                SCREEN_WIDTH/2, SCREEN_HEIGHT/1.3, SCREEN_WIDTH/2.5, SCREEN_HEIGHT/2.5)

        arcade.draw_points(self.points_list, (105, 105, 105), 4.0)

    def on_update(self, delta_time):
        "Frame updating"
        self.tick += 1

        "Updating the logo boolean"
        if self.tick % 90 == 1:
            self.logo_blink = not self.logo_blink
        "Updating Stars"
        if self.tick % 1 == 0:
            newpointslist = []
            for point in self.points_list:
                if point[1] < 0:
                    newpoint = (random.randint(0, 800), 600)
                else:
                    newpoint = (point[0], point[1]-3)
                newpointslist.append(newpoint)
        self.points_list = newpointslist

    def on_hide_view(self):
        "Disabling UI manager when the view dissapears"
        self.manager.disable()

# View when game is paused


class PauseView(arcade.View):
    """ View to show when game is paused"""

    def __init__(self, game_view):
        """ This is run once when we switch to this view """
        super().__init__()
        self.window.set_mouse_visible(True)
        self.game_view = game_view
        self.points_list = []
        self.tick = 0
        self.logo_blink = False
        "Init manager"
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        "Init buttons"
        resume_game_button = arcade.gui.UIFlatButton(
            text="Resume Game", width=150)
        exit_button = arcade.gui.UIFlatButton(text="Exit Game", width=150)
        "Init Grid Layout"
        self.grid = arcade.gui.UIBoxLayout(space_between=15)
        "Adding the buttons to the layout"
        self.grid.add(resume_game_button)
        self.grid.add(exit_button)
        "Use the anchor to position the button on the screen"
        self.anchor = self.manager.add(
            arcade.gui.UIAnchorWidget(child=self.grid, align_y=-130))
        "Button Events and Functionality"
        @resume_game_button.event("on_click")
        def on_click_resume_game_button(event):
            self.window.set_mouse_visible(False)
            self.window.show_view(self.game_view)

        @exit_button.event("on_click")
        def on_click_exit_button(event):
            try:
                arcade.exit()
            except:
                None
        "Add Stars"
        for i in range(15):
            point = (random.randint(0, 800), random.randint(0, 600))
            self.points_list.append(point)

    def on_draw(self):
        """ Draw this view """
        self.clear()

        "Drawing the manager"
        self.manager.draw()

        "Draw Stars"
        arcade.draw_points(self.points_list, (105, 105, 105), 4.0)

        "Blinking Logo"
        if self.logo_blink:
            arcade.draw_text("GAME PAUSED", self.window.width / 2, self.window.height / 2,
                             arcade.color.WHITE, font_size=50, anchor_x="center", font_name=("Public Pixel"))

    def on_update(self, delta_time):
        "Frame updating"
        self.tick += 1

        "Updating the logo boolean"
        if self.tick % 90 == 1:
            self.logo_blink = not self.logo_blink
        "Updating Stars"
        if self.tick % 1 == 0:
            newpointslist = []
            for point in self.points_list:
                if point[1] < 0:
                    newpoint = (random.randint(0, 800), 600)
                else:
                    newpoint = (point[0], point[1]-3)
                newpointslist.append(newpoint)
        self.points_list = newpointslist

    def on_hide_view(self):
        "Disabling UI manager when the view dissapears"
        self.manager.disable()

# View when game is over


class GameOverView(arcade.View):
    """ View to show when game is over """
    global score

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.window.set_mouse_visible(True)
        self.points_list = []
        self.tick = 0
        self.logo_blink = False
        "Init manager"
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        "Init buttons"
        exit_button = arcade.gui.UIFlatButton(text="Exit Game", width=150)
        "Init Grid Layout"
        self.grid = arcade.gui.UIBoxLayout(space_between=15)
        "Adding the buttons to the layout"
        self.grid.add(exit_button)
        "Use the anchor to position the button on the screen"
        self.anchor = self.manager.add(
            arcade.gui.UIAnchorWidget(child=self.grid, align_y=-130))
        "Button Events and Functionality"
        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()
        "Init Stars"
        for _ in range(15):
            point = (random.randint(0, 800), random.randint(0, 600))
            self.points_list.append(point)

    def on_draw(self):
        """ Draw this view """
        self.clear()

        "Drawing the manager"
        self.manager.draw()

        arcade.draw_points(self.points_list, (105, 105, 105), 4.0)

        scoretext = "Score: " + str(score)
        arcade.draw_text(scoretext, self.window.width / 2, self.window.height / 2-100,
                         arcade.color.WHITE, font_size=20, anchor_x="center", font_name=("Public Pixel"))

        if self.logo_blink:
            arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2,
                             arcade.color.WHITE, font_size=50, anchor_x="center", font_name=("Public Pixel"))

    def on_update(self, delta_time):
        "Frame updating"
        self.tick += 1

        "Updating the logo boolean"
        if self.tick % 90 == 1:
            self.logo_blink = not self.logo_blink

        "Updating Stars"
        if self.tick % 1 == 0:
            newpointslist = []
            for point in self.points_list:
                if point[1] < 0:
                    newpoint = (random.randint(0, 800), 600)
                else:
                    newpoint = (point[0], point[1]-3)
                newpointslist.append(newpoint)
        self.points_list = newpointslist

    def on_hide_view(self):
        "Disabling UI manager when the view dissapears"
        self.manager.disable()

# Main Game view


class GameView(arcade.View):
    global score
    global high_score
    high_score = get_top_scores()
    high_score = high_score[0]

    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.BLACK)

        self.tick = 0
        self.points_list = []
        self.enemy_list = None
        self.player_bullet_list = None
        # Will hold enemy bullets whose parent enemy got killed (other bullets exist inside the enemy class, but we want them to still be on the screen when the enemy gets killed)
        self.estranged_enemy_bullet_list = None

        # Movement variables
        self.last_press = "NONE"
        self.is_right_press = False
        self.is_left_press = False

        # Make the mouse invisible when hovering the screen
        self.window.set_mouse_visible(False)

        self.explosion_list = arcade.SpriteList()

        self.extra_frames = 0.0

        self.loops = 0
        self.tick_amount = 1.0

    def setup(self):
        # Call to restart game
        # Setup base sprites
        arcade.play_sound(intro_sound, 0.5, 0, False, 1)
        self.user = Player(PLAYER_IMG)

        # Spawn a bullet off screen during setup so that the game
        # Does not slow down upon the player shooting a bullet for
        # the first time
        bullet = player_bull(self.user.sprite.center_x, 600)
        self.user.player_bullet_list.append(bullet)

        # Do the same for the enemy bullet as you did above for
        # Player bullet
        self.estranged_enemy_bullet_list = arcade.SpriteList()
        e_bullet = enemy_bull(-100, -100, 0, 0)
        self.estranged_enemy_bullet_list.append(e_bullet)

        # Spawn in the explosion textures as the game starts
        self.explosion_list.append(PlayerExplosion(-100, -100))
        self.explosion_list.append(EnemyExplosion(-100, -100))

        # Add Stars:
        for i in range(15):
            point = (random.randint(0, 800), random.randint(0, 600))
            self.points_list.append(point)

        # Add Enemies
        self.enemy_list = []
        for flock in FLOCK_LIST:
            for enemy in flock.enemy_list:
                self.enemy_list.append(copy.deepcopy(enemy))

    def on_draw(self):
        global high_score, score
        # Call before drawing to erase last frame
        self.clear()

        arcade.start_render()

        # Draw all explosions
        for explosion in self.explosion_list:
            explosion.draw()

        # Draw the player sprite
        self.user.sprite.draw()
        # Draw the bullet sprites
        self.user.player_bullet_list.draw()

        # Drawing Backround
        arcade.draw_points(self.points_list, (105, 105, 105), 4.0)

        ### Testing enemy draw ###
        for enemy in self.enemy_list:
            # draw each bullet in the list individually breaks on windows otherwise
            for bullet in enemy.bullet_list:
                bullet.draw()
            if enemy.center_y < 625 and enemy.center_y > -25:
                enemy.draw()

        # Draw the bullets for each enemy who died
        # Before its bullet could finish traveling
        self.estranged_enemy_bullet_list.draw()

        # Draw score and live text
        arcade.draw_text("Score: " + str(self.user.score), 50, 580.0,
                         arcade.color.WHITE, 10, 20, 'left', font_name=("Public Pixel"))

        arcade.draw_text("High Score: " + str(high_score), 560, 580.0,
                         arcade.color.WHITE, 10, 20, 'left', font_name=("Public Pixel"))

        arcade.draw_text("Lives: " + str(self.user.player_lives), 50, 50.0,
                         arcade.color.WHITE, 10, 20, 'left', font_name=("Public Pixel"))

        # Draw Level Titles
        if not self.user.hit:
            if self.tick > 20 + self.extra_frames and self.tick < 120.0 + self.extra_frames:
                arcade.draw_text("Level " + str((1 + (self.loops * 3))), 230, 300,
                                 arcade.color.WHITE, 40, 200, font_name=("Public Pixel"))
            elif self.tick > 1260.0 + self.extra_frames and self.tick < 1380.0 + self.extra_frames:
                arcade.draw_text("Level " + str((2 + (self.loops * 3))), 230, 300,
                                 arcade.color.WHITE, 40, 200, font_name=("Public Pixel"))
            elif self.tick > 2880.0 + self.extra_frames and self.tick < 3000.0 + self.extra_frames:
                arcade.draw_text("Level " + str((3 + (self.loops * 3))), 230, 300,
                                 arcade.color.WHITE, 40, 200, font_name=("Public Pixel"))

    def on_update(self, delta_time):
        global score
        score = self.user.score
        # Update the explosion animation to the next frame
        for explosion in self.explosion_list:
            explosion.update_animation()

        # Update games frame counter
        self.tick += self.tick_amount

        # Reset tick when levels end so levels loop
        if self.tick >= 4800 + self.extra_frames:
            self.tick = 0
            self.extra_frames = 0.0
            self.loops += 1
            # Increase speed
            self.tick_amount += 0.1
            self.enemy_list.clear()
            self.user.time_of_death = -1000
            flock_deep_copy_2 = FLOCK_LIST.copy()
            # Reset enemies
            for flock in flock_deep_copy_2:
                for enemy in flock.enemy_list:
                    self.enemy_list.append(copy.deepcopy(enemy))

        self.user.update_state(self.tick)
        # update the player
        self.user.sprite.update()

        # Update Background
        if True:
            newpointslist = []
            for point in self.points_list:
                if point[1] < 0:
                    newpoint = (random.randint(0, 800), 600)
                else:
                    newpoint = (point[0], point[1]-3)
                newpointslist.append(newpoint)
        self.points_list = newpointslist

        if self.user.hit:
            for enemy in self.enemy_list:
                if enemy.center_x > 0 and enemy.center_y > 0:
                    enemy.player_hit(
                        (self.tick - self.user.time_of_death) / 120.0)
                    if self.tick >= self.user.time_of_death + 480:
                        enemy.delay = self.tick / 120.0 - 2.0
            if self.tick >= self.user.time_of_death + 480:
                self.user.hit = False
                for enemy in self.enemy_list:
                    if enemy.center_x < 0 or enemy.center_y < 0:
                        enemy.delay = enemy.delay + 4.0

        else:
            # move player bullets if still on screen and check for collisions
            for bullet in self.user.player_bullet_list:
                # if offscreen kill the bullet
                if bullet.center_y > 600 or bullet.center_y < 0:
                    bullet.kill()
                # otherwise move
                else:
                    bullet.move()
                # Check if that bullet is colliding with any of the enemies
                for enemy in self.enemy_list:
                    colliding = arcade.check_for_collision(bullet, enemy)
                    # if colliding kill enemy,bullet and increase score
                    if colliding:
                        arcade.play_sound(hit_sound, .5)
                        if enemy.stationary:
                            self.user.increase_score(40)
                        else:
                            self.user.increase_score(80)
                        enemy.remove_from_sprite_lists()
                        for bullet2 in enemy.bullet_list:
                            self.estranged_enemy_bullet_list.append(bullet2)
                        self.explosion_list.append(
                            EnemyExplosion(enemy.center_x, enemy.center_y))
                        self.enemy_list.remove(enemy)
                        bullet.kill()
                        enemy.kill()

            # Check each bullet whos original enemy fired it has died
            for bullet in self.estranged_enemy_bullet_list:
                # if offscreen kill bullet
                if bullet.center_y > 600 or bullet.center_y < 0:
                    bullet.kill()
                # otherwise move
                else:
                    bullet.move()
                # if hitting the player kill the bullet and the player
                colliding = arcade.check_for_collision(
                    bullet, self.user.sprite)
                if colliding:
                    self.explosion_list.append(PlayerExplosion(
                        self.user.sprite.center_x, self.user.sprite.center_y))
                    arcade.play_sound(death_sound, .5)
                    # If out of lives switch view
                    if not self.user.kill(self.tick):
                        view = GameOverView()
                        self.window.show_view(view)
                    self.delete_bullets()
                    bullet.kill()
                    self.extra_frames += 480

            # move enemies and enemy bullets if still on screen and check collisions
            for enemy in self.enemy_list:
                enemy.move(5.0, self.tick / 120.0,
                           (self.user.sprite.center_x, self.user.sprite.center_y))
                if enemy.center_y < -50:
                    enemy.kill()

                colliding = arcade.check_for_collision(enemy, self.user.sprite)
                if colliding:
                    arcade.play_sound(death_sound, .5)
                    self.explosion_list.append(PlayerExplosion(
                        self.user.sprite.center_x, self.user.sprite.center_y))
                    # If out of lives switch view
                    if not self.user.kill(self.tick):
                        view = GameOverView()
                        self.window.show_view(view)
                    # clear bullets
                    self.delete_bullets()
                    enemy.kill()
                    self.extra_frames += 480

                # Check enemy bullets
                for bullet in enemy.bullet_list:
                    if bullet.center_y > 600 or bullet.center_y < 0:
                        bullet.kill()
                    else:
                        bullet.move()
                        colliding = arcade.check_for_collision(
                            bullet, self.user.sprite)
                        if colliding:
                            arcade.play_sound(death_sound, .5)
                            self.explosion_list.append(PlayerExplosion(
                                self.user.sprite.center_x, self.user.sprite.center_y))
                            # If out of lives switch view
                            if not self.user.kill(self.tick):
                                view = GameOverView()
                                self.window.show_view(view)
                            # clear bullets
                            self.delete_bullets()
                            bullet.kill()
                            self.extra_frames += 480
                # At the end of update check if the player has gained
                # a life for their point total
                self.user.gain_life()

    def on_key_press(self, key, key_modifiers):
        # if you press the left key set the variable to true and
        # the last pressed key to LEFT
        self.user.inputs(key)
        # Pause Game
        if key == arcade.key.ESCAPE:
            pause = PauseView(self)
            self.window.show_view(pause)

    def on_key_release(self, key, key_modifiers):
        # if the key released is left update the bool
        # and check if other key is pressed
        if not self.user.hit:
            self.user.release(key)

    # Clear all enemy and player bullets
    def delete_bullets(self):
        self.user.player_bullet_list.clear()
        self.estranged_enemy_bullet_list.clear()
        for enemy in self.enemy_list:
            enemy.bullet_list.clear()


def main():
    """ Main function """
    # Connect to firebase
    subprocess.run(["python", "admin.py"])
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    """Running game"""
    arcade.run()


if __name__ == "__main__":
    main()
