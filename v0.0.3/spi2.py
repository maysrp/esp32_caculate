from machine import Pin, SPI
import gc,os
from utils import sdcard
from drivers.st7789.st7789_4bit import *
SSD = ST7789

pdc = Pin(9, Pin.OUT, value=1)  
pcs = Pin(11, Pin.OUT, value=1)
prst = Pin(7, Pin.OUT, value=1)

gc.collect()  

spi =SPI(2,baudrate=40000000, sck=Pin(3), mosi=Pin(5), miso=Pin(14))

ssd = SSD(spi, height=240, width=320, disp_mode=4, dc=pdc, cs=pcs, rst=prst)

#disp_mode=5 调节这个来调节画面的方位


def mount():
    sd = sdcard.SDCard(spi,Pin(15))
    os.mount(sd, '/sd')
    print("sdcard is wrong")

try:
    mount()
except:
    print("ERROR TFCard")