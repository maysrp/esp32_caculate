# esp32_caculate
ESP32 caculate plot  ST7789


本项目来自于[MPY-CONSOLE](https://github.com/jd3096-mpy/MPY-CONSOLE) 在此基础上，改用了便宜的esp32s2 lolin mini，使用双st7789屏幕,一个用于显示micropython repl 一个用于绘图。键盘输入使用CH9350模块，直接使用USB无线键盘即可。

添加了模拟shell环境[micropython-shell](https://github.com/octopusengine/micropython-shell)，及绘图功能[micropython-nano-gui](https://github.com/peterhinch/micropython-nano-gui)，固件添加了ulab，可用使用numpy的基础计算功能，可用算得上是一个计算器了。

可以用面包板和杜邦线直接拼凑一个，也可以嘉立创PCB制作，免于排线。


pdc = Pin(9, Pin.OUT, value=1)  
pcs = Pin(11, Pin.OUT, value=1)
prst = Pin(7, Pin.OUT, value=1)
12 bl
gc.collect()  

spi =SPI(2,baudrate=40000000, sck=Pin(3), mosi=Pin(5), miso=Pin(14))

TF卡CS 15

self.port=UART(1,baudrate=115200,tx=18,rx=16)


spi=SPI(1, baudrate=40000000,sck=Pin(1), mosi=Pin(2),miso=Pin(13))
        cs=Pin(8, Pin.OUT),
        dc=Pin(6, Pin.OUT),
        backlight=Pin(10, Pin.OUT),
        reset=Pin(4, Pin.OUT),

|||
