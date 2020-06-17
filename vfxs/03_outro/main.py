import pygame.gfxdraw
import pygame
import time
import math

def setup(screen, vfx):
    pass

def draw(screen, vfx):
    size_x, size_y = screen.get_size()
    screen.fill((0, 0, 0))

    color = (0,255,255)

    radius = vfx.audio_peak #int(50 + math.sin(vfx.audio_peak / 1 + time.time()) * 50)

    pygame.gfxdraw.filled_circle(
        screen,
        size_x/2,
        size_y/2,
        radius + 1,
        color
    )