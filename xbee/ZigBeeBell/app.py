#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import serial
from xbee import ZigBee

from mywinsound import winsound

import config

def playsound():
    snd_flags = winsound.SND_ASYNC|winsound.SND_NOWAIT
    winsound.PlaySound('se_maoudamashii_chime10.wav', snd_flags)

def main():
    ser = serial.Serial(port=config.PORT, baudrate=9600)
    xbee = ZigBee(ser)


    while True:
        try:
            response = xbee.wait_read_frame()
            if response['samples'][0]['dio-1'] == False:
                playsound()
            print response
        except KeyboardInterrupt:
            break

    ser.close()

if __name__ == '__main__':
    main()
