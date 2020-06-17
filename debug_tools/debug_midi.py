vfx = None

##
# Init midi module
#
# @param: vfx object
# @return: void
##
def init(vfx_obj):
    global vfx
    vfx = vfx_obj


def debug():
    global vfx

    if(vfx.usb_midi_connected == False):
        print('Midi not connected')
        pass

    print("Midi trig: %s | id: %s | name: %s |active ch: %s | midi new: %s | clock: %s | pgm: %s | cc: %s | note: %s " %
        (str(vfx.usb_midi_trig),
         str(vfx.default_input_id),
         str(vfx.usb_midi_name),
         str(vfx.midi_channel),
         str(vfx.midi_new),
         str(vfx.midi_clk),
         str(vfx.midi_pgm),
         str(vfx.midi_cc),
         str(vfx.midi_notes)
         )
    )