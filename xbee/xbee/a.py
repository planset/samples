#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xbee import XBee
import serial


def main():
    ser = serial.Serial('', 9600)
    xbee = XBee(ser)
    while True:
        try:
            response = xbee.wait_read_frame()
            print response
        except KeyboardInterrupt:
            break
    ser.close()


if __name__ == '__main__':
    main()


