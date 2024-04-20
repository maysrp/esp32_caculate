import st7789
from machine import SoftI2C,Pin,UART,Timer,SPI
import time
import network
import urequests
import utils.vga1_8x8 as font1
import utils.dos_font as font

class config(object):
    def __init__(self,start):
        self.start=start
        self.WLAN=network.WLAN()
        self.WLAN.active(True)
        self.tft=start.screen.tft
    def jpg(self,jpg):
        self.tft.init()      
        self.tft.jpg(jpg,0,0)
    def bg(self,bgx):
        self.start.scr.bg=bgx
        self.start.scr.cls()
    def bgcolor(self,color):
        self.start.scr.bgcolor=color
    def fgcolor(self,color):
        self.start.scr.fgcolor=color
    def windows(self):
        self.bg("windows.jpg")
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(986)
    def ubuntu(self):
        self.bg("ubuntu.jpg")
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(st7789.color565(123,10,40))
    def ys(self):
        self.bg("ys.jpg")
        self.fgcolor(st7789.color565(2, 2, 2))
        self.bgcolor(st7789.color565(255,255,255))
    def pao(self):
        self.bg("pao.jpg")
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(st7789.color565(32,86,174))
    def default(self):
        self.bg(False)
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(st7789.color565(0,0,0))
        self.start.scr.cls()
    def green(self):
        self.bg(False)
        self.bgcolor(st7789.color565(0,0,0))
        self.fgcolor(st7789.color565(166, 227, 45))
        self.start.scr.cls()
    def wifi(self,name,password):
        self.WLAN.connect(name,password)
    def ifconfig(self):
        return self.WLAN.ifconfig()
    def get(self,url):
        return urequests.get(url)
    def cls(self):
        self.start.scr.cls()
    def text(self,t="i"):
        self.tft.text(font1,t,4,4)
    def small(self):
        self.start.scr.typec=False
        self.start.scr.char_y=8
        self.start.scr.line_height(8)
        self.cls()
    def big(self):
        self.start.scr.typec=True
        self.start.scr.char_y=16
        self.start.scr.line_height(16)
        self.cls()
    def key(self):
        k=Pin(16,Pin.OUT)
        if k.value():
            k.value(0)
        else:
            k.value(1)

        

