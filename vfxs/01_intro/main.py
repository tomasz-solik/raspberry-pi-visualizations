import pygame.gfxdraw
import pygame
import time
import math

def setup(screen, vfx):
    pass

def draw(screen, vfx):
    size_x, size_y = screen.get_size()
    screen.fill((0, 0, 0))

    color = (0,0,255)

    radius = vfx.audio_peak

    pygame.gfxdraw.filled_circle(
        screen,
        size_x/2,
        size_y/2,
        radius + 1,
        color
    )