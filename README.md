# dingtalk_auto_click

一个自动进入钉钉视频会议并关闭摄像头和麦克风的小工具!

> 只适合Gnome桌面. 且程序内置的数据只适用于无顶栏的Gnome桌面...是的, 很刁钻的条件. 不过下方提供了Gnome原生桌面的数据.

> 只适合`1920*1080`分辨率的屏幕, 不过也提供了一个方便的数据收集功能.

## 使用

需要确保电脑上有`python3`, 以及`pyautogui`模块.

```
sudo apt install python3-tk python3-dev scrot -y && pip3 install pyautogui
```

下载并执行程序:

```sh
wget https://raw.githubusercontent.com/wzk0/dingtalk_auto_click/main/dingtalk.py && python3 dingtalk.py
```

随后就可以放心地做其他事情了!

> 不过有大概率你无法使用, 此时请自行调用picker函数功能进行数据更新.

## 开发

利用了`pyautogui`获取指定位置RGB色彩值的功能, 与已经收集好的数据进行判断是不是弹出了视频会议窗口, 是的话就进行点击等操作.

![](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202301071744118.png)

我的屏幕分辨率是`1920*1080`的, 所以收集的这组数据也只适合`1920*1080`的屏幕. 总共对白色, 绿色, 红色, 黑色四种颜色每种四个位点的数据进行了收集, 误判的概率应该是非常小的(这些颜色来自上图箭头指的地方).

如果你的屏幕分辨率不是`1920*1080`的, 可以使用picker函数获取相关颜色的位置信息. 收集好后可以发个issue!

以下是已知的桌面可用的数据:

> 用法: rgb_开头的四行列表变量替换`dingtalk.py`第五行的内容, main函数替换原本的main函数即可.

适用于Gnome桌面的数据(有顶栏):

```
rgb_white = [[757, 436], [770, 670], [1138, 669], [1151, 139]]
rgb_black = [[561, 239], [616, 683], [1222, 630], [1321, 325]]
rgb_red = [[785, 646], [781, 687], [758, 671], [802, 669]]
rgb_green = [[1144, 644], [1113, 673], [1166, 667], [1139, 686]]
```

main(5, 1137, 646, 703, 826, 617, 822, empty_func)

适用于Gnome桌面的数据(无顶栏):

此程序的内置数据.