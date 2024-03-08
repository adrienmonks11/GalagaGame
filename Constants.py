from Enemy import Enemy, Path
from Flock import Flock
import numpy as np
import bezier
import random

LOGO_IMG = "sprites/logo_galaga.png"

# Enemy sprites
ENEMY_IMG_0_1 = "sprites/enemies/enemy0-1.png"
ENEMY_IMG_0_2 = "sprites/enemies/enemy0-2.png"
ENEMY_IMG_1_1 = "sprites/enemies/enemy1-1.png"
ENEMY_IMG_1_2 = "sprites/enemies/enemy1-2.png"
ENEMY_IMG_3 = "sprites/enemies/enemy3.png"
ENEMY_IMG_4 = "sprites/enemies/enemy4.png"
ENEMY_IMG_5 = "sprites/enemies/enemy5.png"
ENEMY_IMG_6 = "sprites/enemies/enemy6.png"
ENEMY_IMG_7 = "sprites/enemies/enemy7.png"

# Player sprite
PLAYER_IMG = "sprites/player_sprite.png"
PLAYER_IMG_EMPTY = "sprites/player_sprite_empty.png"

# Defining constants to represent enemy paths
PATH_1 = Path(10, np.asfortranarray([
    [0.0, -122, -189, -85.0, 89.0, 201.0, 172.0, -20, -124.0, 0.0, 17.0],
    [0.0, 50, 176, 296, 326, 425.0, 542.0, 489.0, 367.0, 266.0, 228.0]
]))

PATH_2 = Path(10, np.asfortranarray([
    [0.0, 122, 189, 85.0, -89.0, -201.0, -172.0, 20, 124.0, 0.0, -17.0],
    [0.0, 50, 176, 296, 326, 425.0, 542.0, 489.0, 367.0, 266.0, 228.0]
]))

PATH_3 = Path(7, np.asfortranarray([
    [0.0, 10, 15, 35, 128, 282, 328, 264],
    [0.0, 118, 23, 381, 478, 480, 393, 325],
]))

DIVE_PATH_1 = Path(10, np.asfortranarray([
    [0.0, -25.0, -100.0, -68.0, 14.0, 93.0, 118.0, 88.0, 33.0, -23.0, 0.0],
    [0.0, -63.0, -23.0, 62.0, 111.0, 160.0,
     244.0, 325.0, 396.0, 458.0, 800]
]))

DIVE_PATH_2 = Path(11, np.asfortranarray([
    [0.0, 19.0, 74.0, 5.0, -54.0, -98.0, -127.0, -156.0, -145.0, -91.0, -57.0, -37.0],
    [0.0, -50.0, 3.0, 33.0, 64.0, 103.0, 155.0, 222.0, 289.0, 344.0, 398.0, 480.0]
]))

DIVE_PATH_3 = Path(15, np.asfortranarray([
    [0.0, 19.0, 64.0, 5.0, -71.0, -145.0, -192.0, -184.0, -110.0, -25.0, 49.0, 116.0, 168.0, 154.0, 104.0, 0.0],
    [0.0, -52.0, 1.0, 31.0, 49.0, 81.0, 132.0, 196.0, 218.0, 227.0, 255.0, 298.0, 348.0, 416.0, 471.0, 700.0]
]))

DIVE_PATHS = [DIVE_PATH_1, DIVE_PATH_2, DIVE_PATH_3]

# Defining constants to represent enemies and flocks of enemies

# LEVEL 1

ENEMY_1 = Enemy(ENEMY_IMG_0_1, [300, -50], PATH_1, 0, [300, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_2 = Enemy(ENEMY_IMG_0_1, [300, -50], PATH_1, 0.1, [340, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_3 = Enemy(ENEMY_IMG_0_1, [300, -50], PATH_1, 0.2, [380, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_4 = Enemy(ENEMY_IMG_0_1, [300, -50], PATH_1, 0.3, [420, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_5 = Enemy(ENEMY_IMG_0_1, [300, -50], PATH_1, 0.4, [460, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_6 = Enemy(ENEMY_IMG_0_1, [300, -50], PATH_1, 0.5, [500, 100], DIVE_PATHS[random.randint(0,2)])

FLOCK_1 = Flock([ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_4, ENEMY_5, ENEMY_6], PATH_1, 1.5, 0.0)

ENEMY_7 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.1, [260, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_8 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.2, [220, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_9 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.3, [260, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_10 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.4, [220, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_2 = Flock([ENEMY_7, ENEMY_8, ENEMY_9, ENEMY_10], PATH_3, 2.5, 0.0)

ENEMY_11 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0, [300, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_12 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.1, [340, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_13 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.2, [380, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_14 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.3, [340, 180], DIVE_PATHS[random.randint(0,2)])
ENEMY_15 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.4, [380, 180], DIVE_PATHS[random.randint(0,2)])

FLOCK_3 = Flock([ENEMY_11, ENEMY_12, ENEMY_13,
                ENEMY_14, ENEMY_15], PATH_1, 3.5, 0.5)

ENEMY_16 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0, [420, 60], DIVE_PATHS[random.randint(0,2)])
ENEMY_17 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.1, [460, 60], DIVE_PATHS[random.randint(0,2)])
ENEMY_18 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.2, [500, 60], DIVE_PATHS[random.randint(0,2)])
ENEMY_19 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.3, [420, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_20 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.4, [460, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_4 = Flock([ENEMY_16, ENEMY_17, ENEMY_18,
                ENEMY_19, ENEMY_20], PATH_2, 3.5, 0.5)

ENEMY_21 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0, [540, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_22 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.1, [580, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_23 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.2, [620, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_24 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.3, [540, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_25 = Enemy(ENEMY_IMG_0_1, [50, 0], PATH_3, 0.4, [580, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_5 = Flock([ENEMY_21, ENEMY_22, ENEMY_23,
                ENEMY_24, ENEMY_25], PATH_1, 6.5, 0.5)

#LEVEL 2

ENEMY_26 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0, [220, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_27 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.1, [260, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_28 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.2, [300, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_29 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.3, [340, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_30 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.4, [380, 100], DIVE_PATHS[random.randint(0,2)])

FLOCK_6 = Flock([ENEMY_26, ENEMY_27, ENEMY_28, ENEMY_29, ENEMY_30], PATH_2, 11.5, 1.0)

ENEMY_31 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0, [420, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_32 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.1, [460, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_33 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.2, [500, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_34 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.3, [540, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_35 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.4, [580, 100], DIVE_PATHS[random.randint(0,2)])

FLOCK_7 = Flock([ENEMY_31, ENEMY_32, ENEMY_33, ENEMY_34, ENEMY_35], PATH_1, 13.0, 1.0)

ENEMY_36 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0, [220, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_37 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.1, [260, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_38 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.2, [300, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_39 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.3, [340, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_40 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.4, [380, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_8 = Flock([ENEMY_36, ENEMY_37, ENEMY_38, ENEMY_39, ENEMY_40], PATH_2, 15.5, 1.0)

ENEMY_41 = Enemy(ENEMY_IMG_3, [50, 0], PATH_3, 0, [420, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_42 = Enemy(ENEMY_IMG_3, [50, 0], PATH_3, 0.1, [460, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_43 = Enemy(ENEMY_IMG_3, [50, 0], PATH_3, 0.2, [500, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_44 = Enemy(ENEMY_IMG_3, [50, 0], PATH_3, 0.3, [540, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_45 = Enemy(ENEMY_IMG_3, [50, 0], PATH_3, 0.4, [580, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_9 = Flock([ENEMY_41, ENEMY_42, ENEMY_43, ENEMY_44, ENEMY_45], PATH_1, 18.5, 1.0)

ENEMY_46 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0, [300, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_47 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.1, [340, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_48 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.2, [380, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_49 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.3, [340, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_50 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.4, [380, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_10 = Flock([ENEMY_46, ENEMY_47, ENEMY_48, ENEMY_49, ENEMY_50], PATH_1, 21.5, 2.0)

ENEMY_51 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0, [420, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_52 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.1, [460, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_53 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.2, [500, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_54 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.3, [420, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_55 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.4, [460, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_11 = Flock([ENEMY_51, ENEMY_52, ENEMY_53, ENEMY_54, ENEMY_55], PATH_2, 21.5, 2.0)

#LEVEL 3

ENEMY_56 = Enemy(ENEMY_IMG_4, [300, -50], PATH_3, 0, [220, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_57 = Enemy(ENEMY_IMG_4, [300, -50], PATH_3, 0.1, [260, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_58 = Enemy(ENEMY_IMG_4, [300, -50], PATH_3, 0.2, [300, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_59 = Enemy(ENEMY_IMG_4, [300, -50], PATH_3, 0.3, [340, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_60 = Enemy(ENEMY_IMG_4, [300, -50], PATH_3, 0.4, [380, 100], DIVE_PATHS[random.randint(0,2)])

FLOCK_12 = Flock([ENEMY_56, ENEMY_57, ENEMY_58, ENEMY_59, ENEMY_60], PATH_2, 25.0, 2.0)

ENEMY_61 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0, [420, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_62 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.1, [460, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_63 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.2, [500, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_64 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.3, [540, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_65 = Enemy(ENEMY_IMG_1_1, [50, 0], PATH_3, 0.4, [580, 100], DIVE_PATHS[random.randint(0,2)])

FLOCK_13 = Flock([ENEMY_61, ENEMY_62, ENEMY_63, ENEMY_64, ENEMY_65], PATH_1, 27.5, 2.0)

ENEMY_66 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0, [220, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_67 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.1, [260, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_68 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.2, [300, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_69 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.3, [340, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_70 = Enemy(ENEMY_IMG_3, [300, -50], PATH_2, 0.4, [380, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_14 = Flock([ENEMY_66, ENEMY_67, ENEMY_68, ENEMY_69, ENEMY_70], PATH_2, 27.5, 2.0)

ENEMY_71 = Enemy(ENEMY_IMG_5, [50, 0], PATH_3, 0, [420, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_72 = Enemy(ENEMY_IMG_5, [50, 0], PATH_3, 0.1, [460, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_73 = Enemy(ENEMY_IMG_5, [50, 0], PATH_3, 0.2, [500, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_74 = Enemy(ENEMY_IMG_5, [50, 0], PATH_3, 0.3, [540, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_75 = Enemy(ENEMY_IMG_5, [50, 0], PATH_3, 0.4, [580, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_15 = Flock([ENEMY_71, ENEMY_72, ENEMY_73, ENEMY_74, ENEMY_75], PATH_1, 31.5, 2.0)

ENEMY_76 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0, [300, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_77 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.1, [340, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_78 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.2, [380, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_79 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.3, [340, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_80 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_1, 0.4, [380, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_16 = Flock([ENEMY_76, ENEMY_77, ENEMY_78, ENEMY_79, ENEMY_80], PATH_1, 33.5, 3.0)

ENEMY_81 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0, [420, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_82 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.1, [460, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_83 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.2, [500, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_84 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.3, [420, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_85 = Enemy(ENEMY_IMG_1_1, [300, -50], PATH_2, 0.4, [460, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_17 = Flock([ENEMY_81, ENEMY_82, ENEMY_83, ENEMY_84, ENEMY_85], PATH_2, 33.5, 3.0)

ENEMY_86 = Enemy(ENEMY_IMG_3, [300, -50], PATH_3, 0, [300, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_87 = Enemy(ENEMY_IMG_3, [300, -50], PATH_3, 0.1, [340, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_88 = Enemy(ENEMY_IMG_3, [300, -50], PATH_3, 0.2, [380, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_89 = Enemy(ENEMY_IMG_3, [300, -50], PATH_3, 0.3, [340, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_90 = Enemy(ENEMY_IMG_3, [300, -50], PATH_3, 0.4, [380, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_18 = Flock([ENEMY_46, ENEMY_47, ENEMY_48, ENEMY_49, ENEMY_50], PATH_1, 36.5, 3.0)

ENEMY_91 = Enemy(ENEMY_IMG_4, [300, -50], PATH_2, 0, [420, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_92 = Enemy(ENEMY_IMG_4, [300, -50], PATH_2, 0.1, [460, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_93 = Enemy(ENEMY_IMG_4, [300, -50], PATH_2, 0.2, [500, 100], DIVE_PATHS[random.randint(0,2)])
ENEMY_94 = Enemy(ENEMY_IMG_4, [300, -50], PATH_2, 0.3, [420, 140], DIVE_PATHS[random.randint(0,2)])
ENEMY_95 = Enemy(ENEMY_IMG_4, [300, -50], PATH_2, 0.4, [460, 140], DIVE_PATHS[random.randint(0,2)])

FLOCK_19 = Flock([ENEMY_51, ENEMY_52, ENEMY_53, ENEMY_54, ENEMY_55], PATH_2, 39.5, 3.0)

# All enemies in one list of flocks
FLOCK_LIST = [FLOCK_1, FLOCK_2, FLOCK_3, FLOCK_4, FLOCK_5, FLOCK_6, FLOCK_7, FLOCK_8, FLOCK_9, FLOCK_10, FLOCK_11, FLOCK_12, FLOCK_13, FLOCK_14, FLOCK_15, FLOCK_16, FLOCK_17, FLOCK_18, FLOCK_19]

