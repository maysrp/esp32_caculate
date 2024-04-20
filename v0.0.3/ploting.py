from spi2 import ssd  
import cmath
import math
import utime
import uos
from gui.core.writer import Writer, CWriter
from gui.core.fplot import PolarGraph, PolarCurve, CartesianGraph, Curve, TSequence
from gui.core.nanogui import refresh
from gui.widgets.label import Label


import gui.fonts.arial10 as arial10
import gui.fonts.font6 as font6
from gui.core.colors import *

CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
wri = CWriter(ssd, arial10, GREEN, BLACK, verbose=False)
wri.set_clip(True, True, False)



def cart(c=lambda x : x**2+1.2,a=-10,b=10,step=1,xd=False,yd=False,xorigin=False,yorigin=False,bx=False,by=False):
    wri = Writer(ssd, font6)
    if not(xd and yd):
        xd=b-a
        yd=b-a
    if not(xorigin and xorigin):
        xorigin=int(xd/2)
        yorigin=int(yd/2)
    if not(bx and by):
        bx=a
        by=b
    if abs(bx)>abs(by):
        bx=-1*abs(bx)
        by=abs(bx)
    else:
        bx=-1*abs(by)
        by=abs(by)
    def populate(func):
        x = a
        while x<=b:
            yield x, func(x)  # x, y
            x += step
    refresh(ssd, True)  # Clear any prior image
    g = CartesianGraph(wri, 5, 60, width=200,height=200,xdivs=xd,ydivs=yd,yorigin=yorigin,xorigin=xorigin, fgcolor=WHITE,bdcolor=WHITE, gridcolor=LIGHTGREEN) 
    curve1 = Curve(g, YELLOW, populate(c),excursion=(bx/-1, by/1)) # args demo
    one_div=int((by-bx)/xd)
    Writer.set_textpos(ssd, 40, 0)
    wri.printstring(" div="+str(one_div))
    Writer.set_textpos(ssd, 0, 0)
    wri.printstring("("+str(-1*one_div*xorigin)+","+str(1*one_div*(yd-yorigin))+")")
    Writer.set_textpos(ssd, 0, 270)
    wri.printstring("("+str(1*one_div*(xd-xorigin))+","+str(1*one_div*(yd-yorigin))+")")
    Writer.set_textpos(ssd, 194, 0)
    wri.printstring("("+str(-1*one_div*xorigin)+","+str(-1*one_div*yorigin)+")")
    Writer.set_textpos(ssd, 194, 270)
    wri.printstring("("+str(1*one_div*(xd-xorigin))+","+str(-1*one_div*yorigin)+")")
    refresh(ssd)
    return g

class HT(object):
    def __init__(self,c=lambda x : x**2+1.2,a=-10,b=10,step=1,xd=False,yd=False,xorigin=False,yorigin=False,bx=False,by=False):
        if not(xd and yd):
            xd=b-a
            yd=b-a
        if not(xorigin and xorigin):
            xorigin=int(xd/2)
            yorigin=int(yd/2)
        if not(bx and by):
            bx=a
            by=b 
        self.c=c
        self.a=a
        self.b=b
        self.step=step
        self.xd=xd
        self.yd=yd
        self.xorigin=xorigin
        self.yorigin=yorigin
        self.bx=bx
        self.by=by
        self.cart()
    def cart(self):
        cart(c=self.c,a=self.a,b=self.b,step=self.step,xd=self.xd,yd=self.yd,xorigin=self.xorigin,yorigin=self.yorigin,bx=self.bx,by=self.by)
    def up(self,move=1):
        self.yorigin=self.yorigin+move
        self.xorigin=int(self.xorigin)
        self.cart()
    def down(self,move=1):
        self.yorigin=self.yorigin-move
        self.xorigin=int(self.xorigin)
        self.cart()
    def left(self,move=1):
        self.xorigin=self.xorigin-move
        self.yorigin=int(self.yorigin)
        self.cart()
    def right(self,move=1):
        self.xorigin=self.xorigin+move
        self.yorigin=int(self.yorigin)
        self.cart()