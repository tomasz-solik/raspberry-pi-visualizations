import pygame
import traceback
import time
import sys
import psutil
########################################################################################################
# custom
from libs import gpio, midi, osd, config, sound, vfx_system

########################################################################################################
# start & init
########################################################################################################
vfx = vfx_system.System()
########################################################################################################
osd.init(vfx)
sound.init(vfx)
midi.init(vfx)
gpio.init(vfx)
pygame.init()

clock = pygame.time.Clock()

if(config.FULL_SCREEN):
    pygame.mouse.set_visible(False)
    screensize = pygame.display.set_mode(config.VIDEO_SCREEN_SIZE,  pygame.FULLSCREEN | pygame.DOUBLEBUF, 32)
    screen = pygame.Surface(screensize.get_size())
else:
    pygame.mouse.set_visible(True)
    screensize = config.VIDEO_SCREEN_SIZE
    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption(config.VIDEO_WINDOW_NAME)

screen.fill((0,0,0))
pygame.display.flip()

vfx.screen = screen

########################################################################################################
# Load vfxs
########################################################################################################
if not (vfx.load_vfxs()):
    osd.info_box(screen, "No vfxs found")
    while True:
        vfx.keydown()

        # quit
        if (vfx.quit):
            exit()

        time.sleep(1)

vfx.utils_memory_used = psutil.virtual_memory()[2]
vfx.utils_cpu_used = psutil.cpu_percent(interval=None, percpu=True)

########################################################################################################
# main loop
########################################################################################################
while True:

    # recv
    sound.recv()
    midi.recv()
    gpio.recv()

    # keydown
    vfx.keydown()

    try:
        if(vfx.osd_menu):
            osd.menu(screen)
        else:
            mode = sys.modules[vfx.vfx_names[vfx.vfx_mod_number]]
            mode.draw(screen, vfx)
    except Exception:
        print(traceback.format_exc())

    # limit fps 30 for cpu usage
    clock.tick(30)
    if (config.FULL_SCREEN):
        screensize.blit(screen, (0, 0))

    pygame.display.update()

    #quit
    if(vfx.quit):
        exit()

    vfx.clear()
