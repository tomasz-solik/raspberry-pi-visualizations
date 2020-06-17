vfx = None

##
# Init gpio module
#
# @param: vfx object
# @return: void
##
def init(vfx_obj):
    global vfx
    vfx = vfx_obj


def debug():
    global vfx

    if(vfx.gpio_connected == False):
        print('GPIO not connected')
        pass

    print("Btn prev: %s | next: %s | audio trig: %s | midi trig: %s | osd menu: %s" %
        (str(vfx.gpio_btn_prev),
         str(vfx.gpio_btn_next),
         str(vfx.gpio_btn_audio_trig),
         str(vfx.gpio_btn_midi_trig),
         str(vfx.gpio_btn_osd_menu)
         )
    )