vfx = None

##
# Init sound module
#
# @param: vfx object
# @return: void
##
def init(vfx_obj):
    global vfx
    vfx = vfx_obj


def debug():
    global vfx

    if(vfx.audio_connected == False):
        print('Audio not connected')
        pass

    print("Audio trig: %s | device index: %s | peak: %s" %
        (str(vfx.audio_trig),
         str(vfx.audio_input_device_index),
         str(vfx.audio_peak)
         )
    )