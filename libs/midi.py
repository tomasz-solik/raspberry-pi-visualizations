import pygame
import pygame.midi

vfx = None
midi_input = None


##
# Init midi module
#
# @param: vfx object
# @return: void
##
def init(vfx_obj):
    global vfx, midi_input
    vfx = vfx_obj

    pygame.midi.init()

    try:
        _set_device_info()

        if(vfx.default_input_id is None):
            vfx.default_input_id = pygame.midi.get_default_input_id()

        midi_input = pygame.midi.Input(vfx.default_input_id)

        vfx.usb_midi_connected = True
    except:
        vfx.usb_midi_connected = False


##
# Receive midi
#
# @return: void
##
def recv():
    global vfx, midi_input
    if (vfx.usb_midi_connected and vfx.usb_midi_trig):
        if midi_input.poll():
            try:
                _parse(midi_input.read(100))
            except:
                print('Midi error')


########################################################################################################
# private
########################################################################################################

##
# Set Midi device info
#
# @return: void
##
def _set_device_info():
    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        vfx.usb_midi_name = name

        print("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
              (i, interf, name, opened, in_out))


##
# Parse midi msg
#
#   Value(Hex) 	Command 	        Data bytes
#   0x80-0x8F 	Note off 	        2 (note, velocity)
#   0x90-0x9F 	Note on 	        2 (note, velocity)
#   0xA0-0xAF 	Key Pressure 	    2 (note, key pressure aftertouch)
#   0xB0-0xBF 	Control Change 	    2 (controller no., value)
#   0xC0-0xCF 	Program Change 	    1 (program no.)
#   0xD0-0xDF 	Channel Pressure 	1 (pressure)
#   0xE0-0xEF 	Pitch Bend 	        2 (least significant byte, most significant byte)
#
# @param: midi midi_event
# @return: void
##
def _parse(midi):
    global vfx

    for msg in midi:

        midi_msg = msg[0]
        msg_status = int(midi_msg[0])
        msg_channel = msg_status & 0xf
        msg_type = (msg_status >> 4) & 0xf

        # global message clock tick
        if (msg_status == 248):
            vfx.new_midi = True
            vfx.midi_clk += 1
            if (vfx.midi_clk >= 24):
                vfx.midi_clk = 0

        # global message clock start
        if (msg_status == 250):
            vfx.new_midi = True
            vfx.midi_clk = 0

        # channel messages
        if ((msg_channel == (vfx.midi_channel - 1)) or (vfx.midi_channel == 0)):

            # CC
            if (msg_type == 0xB):
                vfx.midi_new = True
                vfx.midi_cc[midi_msg[1]] = midi_msg[2]

            # note OFF
            if (msg_type == 0x8):
                vfx.midi_new = True
                vfx.midi_notes[midi_msg[1]] = 0

            # note ON
            if (msg_type == 0x9):
                vfx.midi_new = True
                vfx.midi_notes[midi_msg[1]] = midi_msg[2]

            # PGM
            if (msg_type == 0xC):
                vfx.midi_new = True
                vfx.midi_pgm = midi_msg[1]
