#ST7789
from machine import Pin, SPI, freq,UART
import st7789
from utils import sdcard
import os
import time
# spi2=SPI(2,baudrate=20000000, sck=Pin(13), mosi=Pin(12), miso=Pin(14))
# spi=SPI(1, baudrate=40000000,sck=Pin(1), mosi=Pin(2),miso=Pin(13))
class SCREEN():
    def __init__(self,spi, width, height):
        self.spi=spi
        self.tft=st7789.ST7789(
        self.spi,
        height,
        width,
        cs=Pin(8, Pin.OUT),
        dc=Pin(6, Pin.OUT),
        backlight=Pin(10, Pin.OUT),
        reset=Pin(4, Pin.OUT),
        rotation=1,
        color_order=st7789.RGB,
        inversion=False)
        self.width = width
        self.height = height
        self.tft.init()
        self.tft.fill(220)


#CH9350
usage_id = ["NONE", "ERO", "PF", "ERR", b"a", b"b", b"c", b"d", b"e", b"f", b"g", b"h", b"i", b"j", b"k", b"l", b"m", b"n", b"o", b"p", b"q", b"r", b"s", b"t", b"u", b"v", b"w", b"x", b"y", b"z", b"1", b"2", b"3", b"4", b"5", b"6", b"7", b"8", b"9", b"0", b'\r\n', "ESC", b'\x08', b"\t", b" ", b"-", b"=", b"[", b"]", b"\\", b"`", b";", b"\'", b"`", b",", b".", b"/", "CAPS", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "PRTSCR", "SCRLK", "PAUSE", "INSERT", "HOME", "PGUP", "DEL", "END", "PGDN", "RIGHT", "LEFT", "DOWN", "UP", "NUMLK", "/", "*", "-", "+", "ENTER", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "\\", "APP", "POWER", "=", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24", "EXEC", "HELP", "SELECT", "STOP", "AGAIN", "UNDO", "CUT", "COPY", "PASTE", "FIND", "MUTE", "VOLUP", "VOLDN", "CAPSLK", "NUMLK", "SCKLK", ",", "NA", "\\", "HIRAGANA", "ROMAJI", "NA", "COVT", "NONCNVT", "NA", "NA", "NA", "KANA", "EISU", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "LCTRL", "LSHIFT", "LALT", "LWIN", "RCTRL", "RSHIFT", "RALT", "RWIN"]
usage_id_cap = ["NONE", "ERO", "PF", "ERR", b"A", b"B", b"C", b"D", b"E", b"F", b"G", b"H", b"I", b"J", b"K", b"L", b"M", b"N", b"O", b"P", b"Q", b"R", b"S", b"T", b"U", b"V", b"W", b"X", b"Y", b"Z", b"1", b"2", b"3", b"4", b"5", b"6", b"7", b"8", b"9", b"0", b'\r\n', "ESC", b'\x08', b"\t", b" ", b"-", b"=", b"[", b"]", b"\\", b"`", b";", b"\'", b"`", b",", b".", b"/", "CAPS", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "PRTSCR", "SCRLK", "PAUSE", "INSERT", "HOME", "PGUP", "DEL", "END", "PGDN", "RIGHT", "LEFT", "DOWN", "UP", "NUMLK", "/", "*", "-", "+", "ENTER", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "\\", "APP", "POWER", "=", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24", "EXEC", "HELP", "SELECT", "STOP", "AGAIN", "UNDO", "CUT", "COPY", "PASTE", "FIND", "MUTE", "VOLUP", "VOLDN", "CAPSLK", "NUMLK", "SCKLK", ",", "NA", "\\", "HIRAGANA", "ROMAJI", "NA", "COVT", "NONCNVT", "NA", "NA", "NA", "KANA", "EISU", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "LCTRL", "LSHIFT", "LALT", "LWIN", "RCTRL", "RSHIFT", "RALT", "RWIN"]
usage_id_shift = ["NONE", "ERO", "PF", "ERR", b"A", b"B", b"C", b"D", b"E", b"F", b"G", b"H", b"I", b"J", b"K", b"L", b"M", b"N", b"O", b"P", b"Q", b"R", b"S", b"T", b"U", b"V", b"W", b"X", b"Y", b"Z", b"!", b"@", b"#", b"$", b"%", b"^", b"&", b"*", b"(", b")", b'\r\n', "ESC", b'\x08', b"\t", b" ", b"-", b"+", b"{", b"}", b"|", b"~", b":", b"\"", b"~", b"<", b">", b"?", "CAPS", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "PRTSCR", "SCRLK", "PAUSE", "INSERT", "HOME", "PGUP", "DEL", "END", "PGDN", "RIGHT", "LEFT", "DOWN", "UP", "NUMLK", "/", "*", "-", "+", "ENTER", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "\\", "APP", "POWER", "=", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24", "EXEC", "HELP", "SELECT", "STOP", "AGAIN", "UNDO", "CUT", "COPY", "PASTE", "FIND", "MUTE", "VOLUP", "VOLDN", "CAPSLK", "NUMLK", "SCKLK", ",", "NA", "\\", "HIRAGANA", "ROMAJI", "NA", "COVT", "NONCNVT", "NA", "NA", "NA", "KANA", "EISU", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "LCTRL", "LSHIFT", "LALT", "LWIN", "RCTRL", "RSHIFT", "RALT", "RWIN"]


class KEYBOARD():
    def __init__(self):
        self.port=UART(1,baudrate=115200,tx=18,rx=16)
        self.port.flush()
    def get_key(self):
        cap=False
        while self.port.any():
            if self.port.read(1)==b'W':
                if self.port.read(1)==b'\xab':
                    hh=self.port.read(3)
                    if hh==b'\x01\x00\x00':
                        r=self.port.read(1)
                        try:
                            num=int.from_bytes(r, 'big')
                        except:
                            num=0
                        if num>0:
                            key=usage_id[num]
                            if str(key)=="CAPS":
                                cap=not cap
                            else:
                                if cap:
                                    key=usage_id_cap[num]
                            if type(key)==bytes:
                                return key
                    elif hh==b'\x01\x01\x00':
                        r=self.port.read(1)
                        try:
                            num=int.from_bytes(r, 'big')
                        except:
                            num=0
                        if num>0:
                            key=usage_id_shift[num]
                            if type(key)==bytes:
                                if key==b"A":
                                    return b'\x01'
                                elif key==b"B":
                                    return b'\x02'
                                elif key==b"C":
                                    return b'\x03'
                                elif key==b"D":
                                    return b'\x04'
                                elif key==b"E":
                                    return b'\x05'
#                             print("CTRL",usage_id_shift[num])
                            #CTRL 重新设置
                        else:
#                             print('CTRL')
                            pass
                    elif hh==b'\x01\x02\x00':
                        r=self.port.read(1)
                        try:
                            num=int.from_bytes(r, 'big')
                        except:
                            num=0
                        if num>0:
                            key=usage_id_shift[num]
                            if type(key)==bytes:
                                return key
                        else:
#                             print('SHIFT')
                            pass
                    elif hh==b'\x01\x04\x00':
#                         print('ALT')
#                         print("alt",self.port.read(1))
                        pass
            time.sleep(0.001)









 