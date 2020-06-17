import pygame.gfxdraw
import pygame
import time
import math

count = 0

def setup(screen, vfx):
    pass

def draw(screen, vfx):

    global count

    size_x, size_y = screen.get_size()
    screen.fill((0, 0, 0))

    color = (0, 125, 250)

    radius = vfx.audio_peak #int(50 + math.sin(vfx.audio_peak / 1 + time.time()) * 50)

    pygame.gfxdraw.circle(
        screen,
        size_x/2,
        size_y/2,
        radius,
        color
    )

    rect1 = pygame.Rect(0, 0, radius, radius)

    rect1.centerx = size_x/2
    rect1.centery = size_y/2

    if(radius == 0):
        count += 1


    if(count > 10):
        pygame.draw.rect(screen, color, rect1, 1)

