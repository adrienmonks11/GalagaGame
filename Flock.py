import arcade
import bezier
import numpy as np
import math
import random

# Represents a flock of enemies
class Flock():
    def __init__(self, enemy_list, path, flock_delay, shot_frequency):
        self.enemy_list = enemy_list
        self.path = path
        self.flock_delay = flock_delay
        # Adds the general delay for the flock to each enemy and changes the shot_frequency of each enemy to the shot_frequency of the flock
        for enemy in self.enemy_list:
            enemy.delay += flock_delay
            enemy.shot_frequency = shot_frequency

