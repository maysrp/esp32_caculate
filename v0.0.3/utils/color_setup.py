# color_setup.py Customise for your hardware config

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2021 Peter Hinch

# As written, supports:
# Adafruit 1.3" and 1.54" 240x240 Wide Angle TFT LCD Display with MicroSD - ST7789
# https://www.adafruit.com/product/4313
# https://www.adafruit.com/product/3787

# Demo of initialisation procedure designed to minimise risk of memory fail
# when instantiating the frame buffer. The aim is to do this as early as
# possible before importing other modules.

# WIRING (Adafruit pin nos and names).
# Pico  SSD
# VBUS  Vin
# Gnd   Gnd
# 13    D/C
# 14    TCS
# 15    RST
# 10    SCK
# 11    SI MOSI

# No connect: Lite, CCS, SO (MISO)
from machine import Pin, SPI
import gc

from drivers.st7789.st7789_4bit import *
# from start import screen
SSD = ST7789

pdc = Pin(9, Pin.OUT, value=1)  # Arbitrary pins
pcs = Pin(11, Pin.OUT, value=1)
prst = Pin(7, Pin.OUT, value=1)

gc.collect()  # Precaution before instantiating framebuf
# Conservative low baudrate. Can go to 62.5MHz. Depending on wiring.
# spi = SPI(1, baudrate=40000000,sck=Pin(4), mosi=Pin(5),miso=Pin(17))
spi =SPI(2,baudrate=40000000, sck=Pin(3), mosi=Pin(5), miso=Pin(14))
# spi=screen.spi
# ssd = SSD(spi, dc=pdc, cs=pcs, rst=prst)
ssd = SSD(spi, height=240, width=320, disp_mode=4, dc=pdc, cs=pcs, rst=prst)