# esp32_caculate
ESP32 caculate plot  ST7789

![1](/img/1.jpg)
本项目来自于[MPY-CONSOLE](https://github.com/jd3096-mpy/MPY-CONSOLE) 在此基础上，改用了便宜的esp32s2 lolin mini，使用双st7789屏幕,一个用于显示micropython repl 一个用于绘图。键盘输入使用CH9350模块，直接使用USB无线键盘即可。

添加了模拟shell环境[micropython-shell](https://github.com/octopusengine/micropython-shell)，及绘图功能[micropython-nano-gui](https://github.com/peterhinch/micropython-nano-gui)，固件添加了ulab，可用使用numpy的基础计算功能，可用算得上是一个计算器了。

可以用面包板和杜邦线直接拼凑一个，也可以嘉立创PCB制作，免于排线。
## 烧录
请务必烧录 firmware中的固件 或者直接下其中的固件（无ulab）：https://github.com/russhughes/st7789_mpy
## 接线
|ESP32S2|drivers|
|-|-|
|*UART*|*ch9350*|
|18|rx|
|16|tx|
|*SPI_2*|*LCD_2*|
|sck  3|SCK|
|mosi  5|SDA|
|miso  14||
|cs  11|cs lcd2|
|9|dc|
|7|rst|
|12|bl|
|cs  15|tf cs|
|*SPI_1*|*LCD_1*|
|sck  1|SCK|
|mosi  2|SDA|
|miso  13||
|cs  8|cs lcd1|
|6|dc|
|4|rst|
|10|bl|

## 方法
### con 对象
+ help(con)查看全部con下的设置
#### 字体
+ con.small()  
+ con.big()
#### 主题
+ fcon.windows()
+ con.ubuntu()
+ con.green()
+ con.default()

### shell环境
shell() 进入
#### 命令
+ cat boot.py 2 10 #打印boot.py 每页10行 的第2页，直接 cat boot.py 显示第一页 默认一页14行
+ ls
+ edit a.py 行编辑器 相对于原来的编辑器多了个k参数
+ cd 
+ pwd
+ 等请查看

### 绘图
`a=HT(lambda x:x**2+1)  `
y=x**2+1

`a=HT(lambda x:x**2+1,a=-20,b=20,step=0.1)`
绘制[-20,20]区间内该函数的图像，每0.1步长取值（越小越慢曲线越光滑）

## 注意
+ CH9350 为5V工作电压，且若接有限键盘请在5v上独立供电，目前仅适用于2.4GHZ无线键盘
+ CH9350 模式1234下5上 如图
  ![ch9350设置](/img/3.jpg)

## 计划
+ 改用模组缩小体积
+ 增加充电管理模块
+ 将空余的IO模块化为SPI IIC UART GPIO
+ 整合mpy编辑器，便于长文本编辑
