import arcade
import bezier
import numpy as np
import math
import random
from enemy_bullet import enemy_bull


CHARACTER_SCALING = 2.5

PIXELS_PER_FRAME = 4

# Random True/False generator based on given probability


def decision(probability):
    return random.random() < probability

# Takes two points and returns the distance between them


def distance(point1, point2):
    vec = [(position[0]) - (self.pos[0]), (position[1]) - (self.pos[1])]
    return math.sqrt((vec[0]*vec[0]) + (vec[1]*vec[1]))

# Takes a vector and returns the unit vector


def unit_vector(position):
    length = math.sqrt((position[0]*position[0]) + (position[1]*position[1]))
    if length > 0:
        return [(position[0] / length), (position[1] / length)]
    else:
        return [0, 0]

# Represents an enemy in the game


class Enemy(arcade.Sprite):
    def __init__(self, enemy_img, starting_pos, path, delay, move_to_position, dive_path):
        super().__init__(enemy_img, CHARACTER_SCALING)
        self.starting_pos = starting_pos
        self.pos = starting_pos
        self.path = path
        self.delay = delay
        self.move_to_position = move_to_position
        self.dive_time = random.uniform(2.0, 4.0)
        self.dive_path = dive_path
        self.angle_rad = 0
        self.stationary = False
        self.go_to_formation_time = 1.0
        self.in_formation_time = 2.0
        self.player_been_hit = False

        # number of times the enemy will shoot in the ~3.5 max seconds it will be on screen
        self.shot_frequency = 0.0
        self.bullet_list = arcade.SpriteList()

        bullet = enemy_bull(0, 0, 1000, 1000)
        self.bullet_list.append(bullet)

    # Shoots a bullet by adding it to the enemy's bullet list
    def shoot(self, player_position):
        vec = unit_vector([player_position[0] - self.center_x,
                          player_position[1] - self.center_y])
        bullet = enemy_bull(self.center_x, self.center_y, vec[0], vec[1])
        self.bullet_list.append(bullet)

    # Controls enemies initial movement onto screen following the given path self.path
    def move_initial(self, time):
        self.pos = [(float)(self.starting_pos[0] + self.path.evaluate(time)[0]),
                    (float)(self.starting_pos[1] + self.path.evaluate(time)[1])]

        pos_before = [self.center_x, self.center_y]

        self.center_x = self.pos[0]
        self.center_y = 600 - self.pos[1]

        # Update sprite angle
        vec = [pos_before[0] - self.center_x, pos_before[1] - self.center_y]
        if vec[1] != 0.0:
            if vec[0] >= 0.0 and vec[1] < 0.0:
                self.angle = (math.degrees(np.arctan(vec[1] / vec[0]))-270)
            else:
                self.angle = (math.degrees(np.arctan(vec[1] / vec[0])) - 90)

    # Controls enemy movement to a specific point, used to move enemies into formation at top of screen
    def move_to(self, speed, position, time):
        time_left = self.in_formation_time - (time)
        if time_left > 0:
            vec = [(position[0]) - (self.pos[0]),
                   (position[1]) - (self.pos[1])]
            self.pos[0] += vec[0] * (1 - time_left)
            self.pos[1] += vec[1] * (1 - time_left)
            self.center_x = self.pos[0]
            self.center_y = 600 - self.pos[1]

            # Update sprite angle
            if vec[1] == 0.0:
                self.angle = 0
            else:
                self.angle = math.degrees(np.arctan(vec[0] / vec[1]))

            if time_left < .75:
                self.angle = 0

    # Controls enemy movement while diving
    def dive(self, time):
        pos_before = self.pos
        self.pos = [(float)(self.move_to_position[0] + self.dive_path.evaluate(time)[0]),
                    (float)(self.move_to_position[1] + self.dive_path.evaluate(time)[1])]
        self.center_x = self.pos[0]
        self.center_y = 600 - self.pos[1]

        vec = [self.pos[0] - pos_before[0], self.pos[1] - pos_before[1]]

        if vec[1] != 0.0:
            if vec[0] < 0.0 and vec[1] < 0.0:
                self.angle = (math.degrees(
                    np.arctan(vec[0] / vec[1])) + 180) % 360
            else:
                self.angle = (math.degrees(
                    np.arctan(vec[0] / vec[1])) + 180) % 360

    # General move function - called every frame, decides how to move enemy based on the current frame
    def move(self, speed, time, player_position):
        self.stationary = False
        time = time - self.delay
        # Initial pattern followed when entering screen

        if time < 0:
            self.center_x = -50
            self.center_y = -50

        elif time >= 0 and time < self.go_to_formation_time:
            self.move_initial(time)
            if decision(self.shot_frequency / 200) and self.center_y > 400:
                self.shoot(player_position)

        elif time < self.in_formation_time and time > self.go_to_formation_time:
            # Move to a specified position on the screen
            # Enemies will move to their position in armada after following initial pattern
            self.move_to(PIXELS_PER_FRAME, self.move_to_position, time)
            if decision(self.shot_frequency / 200):
                self.shoot(player_position)

        elif time == self.in_formation_time:
            self.center_x = self.move_to_position[0]
            self.center_y = 600 - self.move_to_position[1]

        elif time >= self.in_formation_time and time < self.dive_time:
            self.stationary = True
            # move_in_formation()
            if decision(self.shot_frequency / 200):
                self.shoot(player_position)

        elif time >= self.dive_time:
            # Enemy breaks off from armada at some point and dives towards player
            self.dive(time - self.dive_time)
            if decision(self.shot_frequency / 200) and self.center_y > 400:
                self.shoot(player_position)

    # Controls enemy movement after the player dies (similar to move_to but takes longer)
    def player_dead_animation(self, speed, position, time):
        time_left = 4.0 - (time)
        if time_left < 3.5:
            vec = [(position[0]) - (self.pos[0]),
                   (position[1]) - (self.pos[1])]
            self.pos[0] += vec[0] * (3.5 - time_left)
            self.pos[1] += vec[1] * (3.5 - time_left)
            self.center_x = self.pos[0]
            self.center_y = 600 - self.pos[1]

            # Update sprite angle
            if vec[1] == 0.0:
                self.angle = 0
            else:
                self.angle = math.degrees(np.arctan(vec[0] / vec[1]))

            if time_left < .75:
                self.angle = 0

    # Called when the player gets hit
    def player_hit(self, time):
        self.player_dead_animation(
            PIXELS_PER_FRAME, self.move_to_position, time)

    # Called when the enemy is hit - deletes the enemy and removes it from sprite lists
    def kill(self):
        self.remove_from_sprite_lists()
        del self

# Represents a model of a path that an enemy follows


class Path():
    def __init__(self, degree, nodes):
        self.nodes = nodes
        self.curve = bezier.Curve(nodes, degree=degree)

    # Given a value between 0 and 1, evaluates a point along the curve
    def evaluate(self, d):
        return self.curve.evaluate(d)


if __name__ == "__main__":
    main()
