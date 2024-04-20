# esp32_caculate
ESP32 caculate plot  ST7789


本项目来自于[MPY-CONSOLE](https://github.com/jd3096-mpy/MPY-CONSOLE) 在此基础上，改用了便宜的esp32s2 lolin mini，使用双st7789屏幕,一个用于显示micropython repl 一个用于绘图。键盘输入使用CH9350模块，直接使用USB无线键盘即可。

添加了模拟shell环境，及绘图功能，固件添加了ulab，可用使用numpy的基础计算功能，可用算得上是一个计算器了。

可以用面包板和杜邦线直接拼凑一个，也可以嘉立创PCB制作，免于排线。


