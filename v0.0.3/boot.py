from machine import Pin,freq
from config import config
import shell as sh
import math
import time

time.sleep(3)

freq(240000000)
def shell():
    con.small()
    con.cls()
    sh.shell()
    

import start
con=config(start)
from spi2 import ssd,mount
from ploting import HT