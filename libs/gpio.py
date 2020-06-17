from libs import config

try:
    if(config.GPIO):
        import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")



vfx = None

##
# Init gpio module
#
# @param: vfx object
# @return: void
##
def init(vfx_obj):
    if(not config.GPIO):
        pass

    global vfx
    vfx = vfx_obj

    try:
        # set gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(config.GPIO_IN_BTN_PREV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_IN_BTN_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_IN_BTN_AUDIO_TRIG, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_IN_BTN_MIDI_TRIG, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(config.GPIO_IN_BTN_OSD_MENU, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(config.GPIO_OUT_LED_AUDIO_TRIG, GPIO.OUT)
        GPIO.setup(config.GPIO_OUT_LED_MIDI_TRIG, GPIO.OUT)

        vfx.gpio_connected = True
    except:
        vfx.gpio_connected = False

##
# Receive gpio
#
# @return: void
##
def recv():
    global vfx
    if(vfx.gpio_connected):

        # ---------------------------------------------------------------
        # BTN PREV
        if (GPIO.input(config.GPIO_IN_BTN_PREV) == GPIO.HIGH):
            vfx.gpio_btn_prev = True
            if (vfx.vfx_mod_number > 0):
                vfx.vfx_mod_number -= 1
        else:
            vfx.gpio_btn_prev = False

        # ---------------------------------------------------------------
        # BTN NEXT
        if (GPIO.input(config.GPIO_IN_BTN_NEXT) == GPIO.HIGH):
            vfx.gpio_btn_next = True
            if (vfx.vfx_mod_number < len(vfx.vfx_names) - 1):
                vfx.vfx_mod_number += 1
        else:
            vfx.gpio_btn_next = False

        # ---------------------------------------------------------------
        # AUDIO TRIG
        if(vfx.audio_connected):
            if(GPIO.input(config.GPIO_IN_BTN_AUDIO_TRIG) == GPIO.HIGH):
                vfx.gpio_btn_audio_trig = True
                if (vfx.audio_trig == False):
                    vfx.audio_trig = True
                    GPIO.output(config.GPIO_OUT_LED_AUDIO_TRIG, GPIO.HIGH)
                else:
                    vfx.audio_trig = False
                    GPIO.output(config.GPIO_OUT_LED_AUDIO_TRIG, GPIO.LOW)
            else:
                vfx.gpio_btn_audio_trig = False

            if(vfx.audio_trig):
                if(vfx.audio_peak > 0):
                    GPIO.output(config.GPIO_OUT_LED_AUDIO_TRIG, GPIO.HIGH)
                else:
                    GPIO.output(config.GPIO_OUT_LED_AUDIO_TRIG, GPIO.LOW)

        # ---------------------------------------------------------------
        # MIDI TRIG
        if(vfx.usb_midi_connected):
            if(GPIO.input(config.GPIO_IN_BTN_MIDI_TRIG) == GPIO.HIGH):
                vfx.gpio_btn_midi_trig = True
                if(vfx.usb_midi_trig == False):
                    vfx.usb_midi_trig = True
                    GPIO.output(config.GPIO_OUT_LED_MIDI_TRIG, GPIO.HIGH)
                else:
                    vfx.usb_midi_trig = False
                    GPIO.output(config.GPIO_OUT_LED_MIDI_TRIG, GPIO.LOW)
            else:
                vfx.gpio_btn_midi_trig = False

            if(vfx.usb_midi_trig):
                if(vfx.midi_new):
                    GPIO.output(config.GPIO_OUT_LED_MIDI_TRIG, GPIO.HIGH)
                else:
                    GPIO.output(config.GPIO_OUT_LED_MIDI_TRIG, GPIO.LOW)

        # ---------------------------------------------------------------
        # BTN MENU
        if (GPIO.input(config.GPIO_IN_BTN_OSD_MENU) == GPIO.HIGH):
            vfx.gpio_btn_osd_menu = True
            if (vfx.osd_menu == False):
                vfx.osd_menu = True
            else:
                vfx.osd_menu = False
        else:
            vfx.gpio_btn_osd_menu = False
