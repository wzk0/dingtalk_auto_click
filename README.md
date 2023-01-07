# dingtalk_auto_click

一个自动进入钉钉视频会议并关闭摄像头和麦克风的小工具!

> 只适合`1920*1080`分辨率的屏幕, 不过也提供了一个方便的数据收集功能.

## 使用

需要确保电脑上有`python3`, 以及`pyautogui`模块.

```
sudo apt install python3-tk python3-dev -y && pip3 install pyautogui
```

下载并执行程序:

```sh
wget https://raw.githubusercontent.com/wzk0/dingtalk_auto_click/main/dingtalk.py && python3 dingtalk.py
```

随后就可以放心地做其他事情了!

## 开发

利用了`pyautogui`获取指定位置RGB色彩值的功能, 与已经收集好的数据进行判断是不是弹出了视频会议窗口, 是的话就进行点击等操作.

![](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202301071744118.png)

我的屏幕分辨率是`1920*1080`的, 所以收集的这组数据也只适合`1920*1080`的屏幕. 总共对白色, 绿色, 红色, 黑色四种颜色每种四个位点的数据进行了收集, 误判的概率应该是非常小的(这些颜色来自上图箭头指的地方).

如果你的屏幕分辨率不是`1920*1080`的, 可以使用picker函数获取相关颜色的位置信息. 收集好后可以发个issue!