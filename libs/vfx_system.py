import os
import imp
import pygame

from libs import config


class System:

    osd_menu = False
    quit = False

    # screen
    screen = None
    vfx_names = []
    vfx_mod_number = 0

    # audio
    audio_connected = False
    audio_input_device_index = config.AUDIO_INPUT_DEVICE_INDEX
    audio_trig = config.AUDIO_DEFAULT_TRIGGER
    audio_peak = 0

    # midi
    usb_midi_connected = False
    usb_midi_trig = config.MIDI_DEFAULT_TRIGGER
    default_input_id = config.MIDI_DEFAULT_INPUT_ID
    usb_midi_name = ''
    midi_channel = config.MIDI_CHANNEL % 17
    midi_new = False
    midi_clk = 0
    midi_pgm = 0
    midi_cc = {}  # [0] * 128
    midi_notes = {} #[0] * 128

    # GPIO
    gpio_connected = False
    gpio_btn_prev = False
    gpio_btn_next = False
    gpio_btn_audio_trig = False
    gpio_btn_midi_trig = False
    gpio_btn_osd_menu = False

    # utils
    utils_memory_used = 0
    utils_cpu_used = 0

    ##
    # Init
    #
    # @param: self
    # @return: void
    ##
    def __init__(self):
        pass

    ##
    # Load all vfx
    #
    # @param: self
    # @return: bool
    ##
    def load_vfxs(self):
        result = False
        try:
            folders = sorted(os.listdir("vfxs"))
            for folder in folders:
                path = os.path.abspath("vfxs") + os.sep + folder + os.sep + "main.py"
                if os.path.exists(path):
                    name = str(folder)
                    imp.load_source(name, path)
                    self.vfx_names.append(name)

            if (len(self.vfx_names) > 0):
                result = True
        except Exception:
            print('Except')
        return result

    ##
    # Keydown, keyboard or gpio
    #
    # @param: self
    # @return: void
    ##
    def keydown(self):
        self._keyboard()

    def clear(self):
        self.midi_new = False

########################################################################################################
# private
########################################################################################################

    ##
    # Keydown keyboard
    #
    # @param: self
    # @return: void
    ##
    def _keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
                elif event.key == pygame.K_m:
                    if(self.osd_menu == False):
                        self.osd_menu = True
                    else:
                        self.osd_menu = False
                elif event.key == pygame.K_RIGHT:
                    if (self.vfx_mod_number < len(self.vfx_names) - 1):
                        self.vfx_mod_number += 1
                elif event.key == pygame.K_LEFT:
                    if (self.vfx_mod_number > 0):
                        self.vfx_mod_number -= 1

                elif event.key == pygame.K_BACKSPACE:  # return to main scene
                    self.osd_menu = False