import pygame

vfx = None

def init(vfx_obj):
    global vfx
    vfx = vfx_obj


def info_box(screen, txt):
    global vfx
    screen.fill((0, 0, 0))

    font = pygame.font.SysFont("monospace", 20)
    text = font.render(txt, True, (255, 255, 255), (0, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = screen.get_width() / 2
    textpos.centery = screen.get_height() / 2
    screen.blit(text, textpos)
    pygame.display.update()


def menu(screen):
    global vfx

    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("monospace", 20)

    # -------------------------------------------------------------------------
    # vfxs
    _text_bracket(screen, font, 0)
    txt = ("Vfx's loaded: %s " %
           (str(vfx.vfx_names)))
    text = font.render(txt, True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.centery = 20
    screen.blit(text, text_rect)

    # -------------------------------------------------------------------------
    # audio input
    _text_bracket(screen, font, 40)
    txt = ("Audio trig: %s | audio connected: %s | lvl: %s" %
           (str(vfx.audio_trig),
            str(vfx.audio_connected),
            str(vfx.audio_peak)))
    text = font.render(txt, True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.centery = 60
    screen.blit(text, text_rect)
    _draw_vu(screen, vfx, 240, 484)

    # -------------------------------------------------------------------------
    # midi input
    _text_bracket(screen, font, 80)
    txt = ("Midi trig: %s | connected: %s | name: %s | active ch: %s " %
           (str(vfx.usb_midi_trig),
            str(vfx.usb_midi_connected),
            str(vfx.usb_midi_name),
            str(vfx.midi_channel)))

    text = font.render(txt, True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.centery = 100
    screen.blit(text, text_rect)

    font_min = pygame.font.SysFont("monospace", 20)
    txt = ("Midi new: %s | clock: %s | pgm: %s | cc: %s | note: %s " %
           (str(vfx.midi_new),
            str(vfx.midi_clk),
            str(vfx.midi_pgm),
            str(vfx.midi_cc),
            str(vfx.midi_notes)))

    text = font_min.render(txt, True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.centery = 120
    screen.blit(text, text_rect)

    # -------------------------------------------------------------------------
    # gpio input
    _text_bracket(screen, font, 140)
    txt = ("GPIO Connected: %s | btns: prev: %s | next: %s | audio trig: %s | midi trig: %s | osd: %s" %
           (str(vfx.gpio_connected),
            str(vfx.gpio_btn_prev),
            str(vfx.gpio_btn_next),
            str(vfx.gpio_btn_audio_trig),
            str(vfx.gpio_btn_midi_trig),
            str(vfx.gpio_btn_osd_menu)))
    text = font.render(txt, True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.centery = 160
    screen.blit(text, text_rect)

    # -------------------------------------------------------------------------
    # system utils
    _text_bracket(screen, font, 180)
    txt = ("Utils memory used: %s | cpu's used: %s " %
           (str(vfx.utils_memory_used)+"%",
            str(vfx.utils_cpu_used)+"%"))
    text = font.render(txt, True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.centery = 200
    screen.blit(text, text_rect)

    pygame.display.update()


########################################################################################################
# private
########################################################################################################

def _draw_vu(screen, vfx, offx, offy):
    color = (255, 255, 255)
    for i in range(0, 15):
        x = offx + 14 * i
        pygame.draw.line(screen, color, [x, offy], [x + 10, offy], 1)
        pygame.draw.line(screen, color, [x, offy], [x, offy + 30], 1)
        pygame.draw.line(screen, color, [x + 10, offy], [x + 10, offy + 30], 1)
        pygame.draw.line(screen, color, [x, offy + 30], [x + 10, offy + 30], 1)
    color = (0, 255, 0)
    for i in range(0, vfx.audio_peak / 2048):
        if i > 8: color = (255, 255, 0)
        if i == 14: color = (255, 0, 0)
        x = offx + 14 * i
        pygame.draw.rect(screen, color, (x + 1, offy + 1, 9, 29))

def _text_bracket(screen, font, centery):
    txt = ("------------------------------------------------------------------------------------------")
    text = font.render(txt, True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 5
    text_rect.centery = centery
    screen.blit(text, text_rect)