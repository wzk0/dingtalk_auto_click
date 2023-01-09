import pyautogui as gui
import time
from os import listdir,system

# 可以在此按照嵌套列表的格式储存新的位置数据, 当前数据只适应1920*1080的屏幕
rgb_white = [[1137, 714], [779, 711], [789, 715], [1152, 716]]
rgb_black = [[565, 440], [794, 495], [1210, 444], [1191, 794]]
rgb_red = [[768, 698], [778, 735], [799, 714], [755, 712]]
rgb_green = [[1144, 693], [1113, 715], [1163, 713], [1136, 733]]

# 此函数通过传入的位置信息和目标颜色判断是否是目标颜色
def if_is_right_color(x, y, goal):
    r, g, b = gui.pixel(x, y)
    if goal == "white":
        if r == 255 and g == 255 and b == 255:
            return True
        else:
            return False
    if goal == "black":
        if r == 45 and g == 49 and b == 52:
            return True
        else:
            return False
    if goal == "red":
        if r == 255 and g == 85 and b == 33:
            return True
        else:
            return False
    if goal == "green":
        if r == 0 and g == 184 and b == 83:
            return True
        else:
            return False
    if goal == "test":
        if r == 217 and g == 218 and b == 219:
            return True
        else:
            return False
    # 可以在此定义新的颜色, 只需按上面的格式编写即可


# 主函数, 通过传入休眠时间, 接听按钮, 关闭摄像头按钮, 关闭麦克风按钮的位置信息执行相关操作
def main(sleep_time, final_x, final_y, camera_x, camera_y, microphone_x, microphone_y):
    while True:
        print('已启动!')
        # 此列表用于收集来自if_is_right_color函数的判断, 如果此列表元素全部为True, 则会执行点击等操作
        pass_list = []
        for rgb in rgb_white:
            pass_list.append(if_is_right_color(rgb[0], rgb[1], "white"))
        for rgb in rgb_black:
            pass_list.append(if_is_right_color(rgb[0], rgb[1], "black"))
        for rgb in rgb_red:
            pass_list.append(if_is_right_color(rgb[0], rgb[1], "red"))
        for rgb in rgb_green:
            pass_list.append(if_is_right_color(rgb[0], rgb[1], "green"))
        if False in pass_list:
            time.sleep(sleep_time)
        else:
            print("上课了!!!")
            gui.moveTo(final_x, final_y)
            gui.click()
            # 休眠这一秒钟是必要的, 需要等待整个视频会议界面加载出来
            time.sleep(1)
            gui.moveTo(camera_x, camera_y)
            gui.click()
            gui.moveTo(microphone_x, microphone_y)
            gui.click()


# 此函数用于更方便的收集符合目标颜色的位置信息
def picker(color):
    x, y = gui.position()
    r, g, b = gui.pixel(x, y)
    if if_is_right_color(x, y, color):
        print("[%s, %s]" % (x, y))

try:
    main(5, 1138, 716, 707, 872, 620, 870)
except KeyboardInterrupt:
    print('已退出!')
    [system('rm %s'%photo) for photo in listdir('.') if photo.startswith('.screenshot')]

# while True:
#    picker("black")
