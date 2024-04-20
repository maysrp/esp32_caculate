from machine import SoftI2C,Pin,UART,Timer,SPI
import time
from utils.drivers import SCREEN,KEYBOARD
from utils.fbconsole import FBConsole
import utils.settings as setting
import utils.color as color
import os
import st7789
import _thread

spi2=SPI(2,baudrate=20000000, sck=Pin(13), mosi=Pin(12), miso=Pin(14))
spi=SPI(1, baudrate=40000000,sck=Pin(1), mosi=Pin(2),miso=Pin(13))

set_dic=setting.load_setting()
NAME=set_dic['OWNER']
screen=SCREEN(spi,320,240)
kb=KEYBOARD()


theme=color.COLOR_CANDY
scr = FBConsole(screen,bg_color=theme['bg'],fg_color=theme['font'],bg=False)
os.dupterm(scr)

time.sleep(0.5)


def check_key(t):
    re=kb.get_key()
    if re!=None:
        if len(re)==1:
            scr._c=re
            scr._press()
        else:
            for b in re:
                scr._c=b.to_bytes(1,'big')
                scr._press()
    
tim=Timer(0)
tim.init(mode=Timer.PERIODIC, period=3, callback=check_key)


#_thread.start_new_thread(keyboard, (scr,))



