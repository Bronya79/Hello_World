# microbit

## Hello World

```python
from microbit import *

diplay.scroll("Hello World")
display.show("Hello World")
```

- display 显示屏
	- scroll 滚动显示
	- show 每次只显示一个字符

## 常见报错

## 图像Image

- 5*5 的坐标显示
- 无颜色区分，亮度为0-9
- display.show 显示Image对象
- Image有一些内置对象
	- 表情类
	- 时钟类
	- 方向类
	- 形状类
	- 动物类
	- 杂物类
```python
from microbit import *

diplay.show(Image.RABBIT)
```
## 显示动画

- 用图像序列来显示动画

 ```python
display.show(seq, delay=400,wait=True,loop=False,clear=False)
```

## LED点阵屏控制display

- 开关显示屏
	- display.on(),of()
- 显示字符串或者图像
	- display.show(s)
- 滚动显示字符串
	- display.scroll(s)
- 清除显示
	- display.clesr()
- 点亮一个像素（b=0~9）
	- display.set_pixel(x, y, b)
