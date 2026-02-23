import time
import sys
from gfx_pack import GfxPack, SWITCH_A, SWITCH_B, SWITCH_C, SWITCH_D

# setup
board = GfxPack()
display = board.display
WIDTH, HEIGHT = display.get_bounds()

# player data
playerx = [14, 24, 34, 52, 68, 86, 96, 106]
playery = [46, 34, 23]
xcoordPlayer = 1
ycoordPlayer = 2

# platform data
platfromy = [9, 21, 31, 42, 54, 64]
platfromx = 66
platformxLeft = 50
ycoordPlat = 0
ycoordPlat_left = 4

# stage data
lower_death_zone = 64

# score
score = 0


# object values
player_values = {
    "x": 14,
    "y": 23,
    "width": 8,
    "height": 8,
    "lives" : 3
}

plat_values = {
    "x": platfromx,
    "y": 11,
    "width": 14,
    "height": 2,
    "speed": 1,
}

plat_values_left = {
    "x": platformxLeft,
    "y": 64,
    "width": 14,
    "height": 2,
    "speed": 1,
}

stage_values = {
    "x": 0,
    "y": 0,
    "width": 64,
    "height": 64
}

stage_values2 = {
    "x": 64,
    "y": 0,
    "width": 64,
    "height": 64
}

lives_sprite_values_one = {
    "x": 120,
    "y": 2,
    "width": 5,
    "height": 4
}

lives_sprite_values_two = {
    "x": 114,
    "y": 2,
    "width": 5,
    "height": 4
}

lives_sprite_values_three = {
    "x": 108,
    "y": 2,
    "width": 5,
    "height": 4
}

hopper_sprite_right1_values = {
    "x": 113,
    "y": 25,
    "width": 16,
    "height": 7
}

hopper_sprite_left1_values = {
    "x": 0,
    "y": 25,
    "width": 16,
    "height": 7
}

hopper_sprite_right2_values = {
    "x": 113,
    "y": 36,
    "width": 16,
    "height": 7
}

hopper_sprite_left2_values = {
    "x": 0,
    "y": 36,
    "width": 16,
    "height": 7
}

reciever_sprite_left_values = {
    "x": 1,
    "y": 51,
    "width": 12,
    "height": 13
}

reciever_sprite_right_values = {
    "x": 115,
    "y": 51,
    "width": 12,
    "height": 13
}

dispenser_sprite_left_values = {
    "x": 3,     
    "y": 14,
    "width": 9,
    "height": 6
}
dispenser_sprite_right_values = {
    "x": 117,
    "y": 14,
    "width": 9,
    "height": 6
}

sand_sprite_values = {
    "x": 50,
    "y": 64,
    "width": 14,
    "height": 2
}

# sprite data
player_sprite = [
[0, 1, 1, 1, 1, 1, 0, 0], 
[0, 1, 0, 1, 0, 1, 0, 1], 
[0, 1, 1, 1, 1, 1, 0, 1], 
[1, 0, 0, 1, 1, 1, 1, 0], 
[0, 1, 1, 1, 1, 1, 0, 0], 
[0, 0, 0, 1, 1, 1, 1, 0], 
[0, 0, 1, 1, 0, 0, 1, 0], 
[0, 1, 0, 0, 0, 0, 0, 1]]


plat_sprite = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

stage_sprite = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]							

stage_sprite2 = [
[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]						

hopper_sprite_left1 = [
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]
hopper_sprite_left2 = [
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]
hopper_sprite_right1 = [
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
hopper_sprite_right2 = [
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

reciever_sprite_left = [
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
reciever_sprite_right = [
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

dispenser_sprite_left = [
[1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1, 0]]
dispenser_sprite_right = [
[1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1, 0]]
sand_sprite = [
[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

lives_sprite_one = [
[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]]

lives_sprite_two = [
[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]]

lives_sprite_three = [
[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]]

#sands
active_sand = []
sand_spawn_timer = 0
sand_spawn_rate = 50

hopper_left_open = True
hopper_right_open = True

sand_in_top_left = []
sand_in_top_right = []
sand_in_bot_left = []
sand_in_bot_right = []

def DrawPlayer():
    display.set_pen(15)
    for row in range(player_values["height"]):
        for col in range(player_values["width"]):
            if player_sprite[row][col]: #checks for a pixel to be drawn
                display.pixel(player_values["x"] + col, player_values["y"] + row)

def DrawPlatform():
    display.set_pen(15)
    for row in range(plat_values["height"]):
        for col in range(plat_values["width"]):
            if plat_sprite[row][col]: #checks for a pixel to be drawn
                display.pixel(plat_values["x"] + col, plat_values["y"] + row)

def DrawPlatform2():
    display.set_pen(15)
    for row in range(plat_values_left["height"]):
        for col in range(plat_values_left["width"]):
            if plat_sprite[row][col]: #checks for a pixel to be drawn
                display.pixel(plat_values_left["x"] + col, plat_values_left["y"] + row)

    
def DrawStage():
    display.set_pen(15)
    for row in range(stage_values["height"]):
        for col in range(stage_values["width"]):
            if stage_sprite[row][col]: #checks for a pixel to be drawn
                display.pixel(stage_values["x"] + col, stage_values["y"] + row)

def DrawStage2():
    display.set_pen(15)
    for row in range(stage_values2["height"]):
        for col in range(stage_values2["width"]):
            if stage_sprite2[row][col]: #checks for a pixel to be drawn
                display.pixel(stage_values2["x"] + col, stage_values2["y"] + row)

def DrawHopperLeft():
    display.set_pen(15)
    for row in range(hopper_sprite_left1_values["height"]):
        for col in range(hopper_sprite_left1_values["width"]):
            if hopper_sprite_left1[row][col]: #checks for a pixel to be drawn
                display.pixel(hopper_sprite_left1_values["x"] + col, hopper_sprite_left1_values["y"] + row)
def DrawHopperRight():
    display.set_pen(15)
    for row in range(hopper_sprite_right1_values["height"]):
        for col in range(hopper_sprite_right1_values["width"]):
            if hopper_sprite_right1[row][col]: #checks for a pixel to be drawn
                display.pixel(hopper_sprite_right1_values["x"] + col, hopper_sprite_right1_values["y"] + row)
def DrawHopperLeft2():
    display.set_pen(15)
    for row in range(hopper_sprite_left2_values["height"]):
        for col in range(hopper_sprite_left2_values["width"]):
            if hopper_sprite_left2[row][col]: #checks for a pixel to be drawn
                display.pixel(hopper_sprite_left2_values["x"] + col, hopper_sprite_left2_values["y"] + row)
def DrawHopperRight2():
    display.set_pen(15)
    for row in range(hopper_sprite_right2_values["height"]):
        for col in range(hopper_sprite_right2_values["width"]):
            if hopper_sprite_right2[row][col]: #checks for a pixel to be drawn
                display.pixel(hopper_sprite_right2_values["x"] + col, hopper_sprite_right2_values["y"] + row)

def DrawRecieverLeft():
    display.set_pen(15)
    for row in range(reciever_sprite_left_values["height"]):
        for col in range(reciever_sprite_left_values["width"]):
            if reciever_sprite_left[row][col]: #checks for a pixel to be drawn
                display.pixel(reciever_sprite_left_values["x"] + col, reciever_sprite_left_values["y"] + row)
def DrawRecieverRight():
    display.set_pen(15)
    for row in range(reciever_sprite_right_values["height"]):
        for col in range(reciever_sprite_right_values["width"]):
            if reciever_sprite_right[row][col]: #checks for a pixel to be drawn
                display.pixel(reciever_sprite_right_values["x"] + col, reciever_sprite_right_values["y"] + row)

def DrawDispenserLeft():
    display.set_pen(15)
    for row in range(dispenser_sprite_left_values["height"]):
        for col in range(dispenser_sprite_left_values["width"]):
            if dispenser_sprite_left[row][col]: #checks for a pixel to be drawn
                display.pixel(dispenser_sprite_left_values["x"] + col, dispenser_sprite_left_values["y"] + row)
def DrawDispenserRight():
    display.set_pen(15)
    for row in range(dispenser_sprite_right_values["height"]):
        for col in range(dispenser_sprite_right_values["width"]):
            if dispenser_sprite_right[row][col]: #checks for a pixel to be drawn
                display.pixel(dispenser_sprite_right_values["x"] + col, dispenser_sprite_right_values["y"] + row)

def DrawSand():
    display.set_pen(15)
    for row in range(sand_sprite_values["height"]):
        for col in range(sand_sprite_values["width"]):
            if sand_sprite[row][col]: #checks for a pixel to be drawn
                display.pixel(sand_sprite_values["x"] + col, sand_sprite_values["y"] + row)

def DrawLivesOne():
    display.set_pen(15)
    for row in range(lives_sprite_values_one["height"]):
        for col in range(lives_sprite_values_one["width"]):
            if lives_sprite_one[row][col]: #checks for a pixel to be drawn
                display.pixel(lives_sprite_values_one["x"] + col, lives_sprite_values_one["y"] + row)

def DrawLivesTwo():
    display.set_pen(15)
    for row in range(lives_sprite_values_two["height"]):
        for col in range(lives_sprite_values_two["width"]):
            if lives_sprite_two[row][col]: #checks for a pixel to be drawn
                display.pixel(lives_sprite_values_two["x"] + col, lives_sprite_values_two["y"] + row)

def DrawLivesThree():
    display.set_pen(15)
    for row in range(lives_sprite_values_three["height"]):
        for col in range(lives_sprite_values_three["width"]):
            if lives_sprite_three[row][col]: #checks for a pixel to be drawn
                display.pixel(lives_sprite_values_three["x"] + col, lives_sprite_values_three["y"] + row)

def is_on_ground():
    player_x = player_values["x"]
    player_y = player_values["y"]
    player_w = player_values["width"]
    player_h = player_values["height"]
    
    check_y = player_y + player_h 
    
    if check_y >= 64: #death zone
        return False 

    for col in range(player_w):
        check_x = player_x + col
        if 0 <= check_x < 64:
            if stage_sprite[check_y][check_x] == 1:
                return True
        elif 64 <= check_x < 128:
            if stage_sprite2[check_y][check_x - 64] == 1: 
                return True
    return False

def DrawSands():
    display.set_pen(15)
    for sand in active_sand:
        for row in range(2):
            for col in range(9):
                if sand_sprite[row][col]:
                    display.pixel(sand["x"] + col, sand["y"] + row)

def update_sand():
    global sand_spawn_timer
    global score

    # Spawn sand at intervals
    sand_spawn_timer += 1
    if sand_spawn_timer >= 60:
        active_sand.append({"x": 3, "y": 14, "state": "falling"})      # Left
        active_sand.append({"x": 117, "y": 14, "state": "falling"})    # Right
        sand_spawn_timer = 0



    for sand in active_sand[:]:
	# Falling state
        sand["y"] += 1
        
        # Check for Hopper cathing it
	# If it hits the hopper Y and the hopper is in a closed state, it stops.
        if 25 <= sand["y"] <= 26:
            if sand["x"] < 64 and not hopper_left_open:
                if len(sand_in_top_left) < 3:
                    sand_in_top_left.append(sand)
                    active_sand.remove(sand)
                else:
                    player_values["lives"] -= 1 # Overflow
                    active_sand.remove(sand)
            elif sand["x"] > 64 and not hopper_right_open:
                if len(sand_in_top_right) < 3:
                    sand_in_top_right.append(sand)
                    active_sand.remove(sand)
                else:
                    player_values["lives"] -= 1 # Overflow
                    active_sand.remove(sand)

        
        elif 36 <= sand["y"] <= 37:
            if sand["x"] < 64 and not hopper_left2_open:
                if len(sand_in_bot_left) < 3:
                    sand_in_bot_left.append(sand)
                    active_sand.remove(sand)
                else:
                    player_values["lives"] -= 1 # Overflow
                    active_sand.remove(sand)
            elif sand["x"] > 64 and not hopper_right2_open:
                if len(sand_in_bot_right) < 3:
                    sand_in_bot_right.append(sand)
                    active_sand.remove(sand)
                else:
                    player_values["lives"] -= 1 # Overflow
                    active_sand.remove(sand)

        
        elif sand["y"] > 58:
            if (1 <= sand["x"] <= 13) or (115 <= sand["x"] <= 127):
                score += 1
            active_sand.remove(sand)

    # Releasing Sand when Hopper Opens
    release_hopper(sand_in_top_left, hopper_left_open)
    release_hopper(sand_in_top_right, hopper_right_open)
    release_hopper(sand_in_bot_left, hopper_left2_open)
    release_hopper(sand_in_bot_right, hopper_right2_open)

def release_hopper(hopper_list, is_open):
    if is_open and len(hopper_list) > 0:
        sand = hopper_list.pop(0) # Take the bottom-most sand
        sand["y"] += 2            
        active_sand.append(sand)

def DrawStackedSand():
    display.set_pen(15)
    # each hopper's base coords
    hopper_coords = [
        (sand_in_top_left, 3, 30), 
        (sand_in_top_right, 116, 30),
        (sand_in_bot_left, 3, 40),
        (sand_in_bot_right, 116, 40)
    ]
    
    for sand_list, x, base_y in hopper_coords:
        for i, sand in enumerate(sand_list):            
            draw_single_sand(x, base_y - (i * 2)) # i*2 to stacks sand 

def draw_single_sand(x, y):
    for row in range(2):
        for col in range(9):
            if sand_sprite[row][col]:
                display.pixel(x + col, y + row)

def DrawScore():
    display.set_pen(15)
    display.text(f"SC: {score}", 2, 2, 128, 1)

SPEED = 1

# Timer variables for moving platform
wait = [0, 1, 2, 3, 4, 5]
currentWait = 0

player_direction = 1  # 1 for down, -1 for up


plat_direction = 1  # 1 for up, -1 for down
plat_direction_left = 1  # 1 for up, -1 for down

game_running = True

# main loop
while True:
    if game_running:
        # Check if player is on platforms
        on_right_plat = (abs(player_values["x"] - plat_values["x"]) < 12) and (abs((plat_values["y"] - 8) - player_values["y"]) < 5)

        on_left_plat = (abs(player_values["x"] - plat_values_left["x"]) < 12) and (abs((plat_values_left["y"] - 8) - player_values["y"]) < 5)

        old_plat_y = plat_values["y"]
        old_plat_left_y = plat_values_left["y"]

        # Check if player is at the Left Hopper trigger
        if abs(player_values["x"] - hopper_sprite_left1_values["x"]) < 15 and abs(player_values["y"] - hopper_sprite_left1_values["y"]) < 8:
            hopper_left_open = True
        else:
            hopper_left_open = False

        # Check if player is at the Right Hopper trigger
        if abs(player_values["x"] - hopper_sprite_right1_values["x"]) < 15 and abs(player_values["y"] - hopper_sprite_right1_values["y"]) < 8:
            hopper_right_open = True
        else:
            hopper_right_open = False

        # Check if player is at the Left Hopper 2 trigger
        if abs(player_values["x"] - hopper_sprite_left2_values["x"]) < 15 and abs(player_values["y"] - hopper_sprite_left2_values["y"]) < 8:
            hopper_left2_open = True
        else:
            hopper_left2_open = False

        # Check if player is at the Right Hopper 2 trigger
        if abs(player_values["x"] - hopper_sprite_right2_values["x"]) < 15 and abs(player_values["y"] - hopper_sprite_right2_values["y"]) < 8:
            hopper_right2_open = True
        else:
            hopper_right2_open = False


        # Moving Right_side platform logic 
        if wait[currentWait] == 0:
            if plat_direction == 1:
                ycoordPlat += 1 
            else:
                ycoordPlat -= 1
            
            plat_values["y"] = platfromy[ycoordPlat]

            # If player was on the platform move them by the same distance it just moved
            if on_right_plat:
                player_values["y"] += (plat_values["y"] - old_plat_y)

        if ycoordPlat == 5:
            plat_direction = -1
        elif ycoordPlat == 0:
            plat_direction = 1


        # Moving Left side Platform logic
        if wait[currentWait] == 0:
            if plat_direction_left == 1:
                ycoordPlat_left += 1
            else:
                ycoordPlat_left -= 1
                
            plat_values_left["y"] = platfromy[ycoordPlat_left]

            # If player was on the platform move them by the same distance it just moved
            if on_left_plat:
                player_values["y"] += (plat_values_left["y"] - old_plat_left_y)

        if ycoordPlat_left == 5:
            plat_direction_left = -1
        elif ycoordPlat_left == 0:
            plat_direction_left = 1
        
        
        # Keeps the player locked to the platfomr
        if on_right_plat:
            player_values["y"] = plat_values["y"] - 8
        elif on_left_plat:
            player_values["y"] = plat_values_left["y"] - 8


        # Movement restrictions
        can_move_horizontally = True
        restricted_elevations = [9, 21, 64] 

        if on_right_plat:
            if plat_values["y"] in restricted_elevations:
                can_move_horizontally = False
        elif on_left_plat:
            if plat_values_left["y"] in restricted_elevations:
                can_move_horizontally = False


        # Horizontal movement logic
        if board.switch_pressed(SWITCH_A) and can_move_horizontally:
            if xcoordPlayer > 0:
                xcoordPlayer -= 1
                player_values["x"] = playerx[xcoordPlayer]
                time.sleep(0.1) 

        if board.switch_pressed(SWITCH_B) and can_move_horizontally:
            if xcoordPlayer < 7:
                xcoordPlayer += 1
                player_values["x"] = playerx[xcoordPlayer]
                time.sleep(0.1)

        # Gravity and ground Check
        if not on_right_plat and not on_left_plat:
            if not is_on_ground():
                player_values["y"] += 5


        #increment wait timer
        if currentWait < 5: 
            currentWait += 1
        else:
            currentWait = 0


        # player death
        # if player goes off top or bottom of screen
        if player_values["y"] > 60 or player_values["y"] < 0:
            print("Player death")
            player_values["lives"] -= 1
            player_values["x"] = 14
            player_values["y"] = 23
            time.sleep(0.5) 

        update_sand()

        if player_values["lives"] <= 0:
            game_running = False


        # draw everything
        display.set_pen(0)
        display.clear()      

        DrawPlatform()
        DrawPlatform2()
        DrawPlayer()
        DrawStage()
        DrawStage2()
        DrawHopperLeft()
        DrawHopperRight() 
        DrawHopperLeft2()
        DrawHopperRight2()
        DrawRecieverLeft()
        DrawRecieverRight()  
        DrawDispenserLeft()
        DrawDispenserRight()  
        DrawSands()  
        DrawScore()  
        DrawStackedSand()  

        if player_values["lives"] >= 1:
            DrawLivesOne()
        if player_values["lives"] >= 2:
            DrawLivesTwo()
        if player_values["lives"] >= 3:
            DrawLivesThree()
    
    else: # Game Over Screen
        display.set_pen(0)
        display.clear()
        display.set_pen(15)
        display.text("GAME OVER", 15, 20, 128, 2)
        display.text(f"SCORE: {score}", 45, 40, 128, 1)
        display.text("Press A to Restart", 17, 55, 128, 1)

        if board.switch_pressed(SWITCH_A):
            player_values["lives"] = 3
            score = 0
            active_sand = [] # Clear old sand
            game_running = True
            time.sleep(0.5)

    display.update()      
    time.sleep(0.05)

