import pyaudio
import numpy
import math
import traceback

from libs import config

vfx = None
stream = None
sin = [0] * 100
peak = 0


##
# Init sound module
#
# @param: vfx object
# @return: void
##
def init(vfx_obj):
    global vfx, stream, sin
    vfx = vfx_obj

    try:

        audio = pyaudio.PyAudio()

        if(vfx.audio_input_device_index is None):
            vfx.audio_input_device_index = audio.get_default_input_device_info()

        stream = audio.open(
            format=pyaudio.paInt16,
            channels=config.AUDIO_CHANNELS,
            rate=config.AUDIO_RATE,
            input_device_index=0,
            input=config.AUDIO_INPUT,
            frames_per_buffer=config.AUDIO_CHUNK
        )
        vfx.audio_connected = True
    except:
        vfx.audio_connected = False

    for i in range(0, 100):
        sin[i] = int(math.sin(2 * 3.1459 * i / 100) * 327) + 326

    # a = 1
    # for i in range(0, 100):
    #     if(i > 50):
    #         a += 2
    #         sin[i] = i - a
    #     else:
    #         sin[i] = i

##
# Stream audio
#
# @return: void
##
def recv():
    global vfx, stream, sin, peak

    if (vfx.audio_trig):
        if (vfx.audio_connected):
            try:
                data = numpy.fromstring(
                    stream.read(
                        config.AUDIO_CHUNK,
                        exception_on_overflow=False
                    ),
                    dtype=numpy.int16
                )

                peak = numpy.average(numpy.abs(data)) * 10
                vfx.audio_peak = int(100 * peak / 10000)
                vfx.audio_connected = True
            except:
                vfx.audio_connected = False
                vfx.audio_peak = 0
    else:
        peak += 1
        if (peak >= 100):
            peak = 0
        vfx.audio_peak = sin[peak]
