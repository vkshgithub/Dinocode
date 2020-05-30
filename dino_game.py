import pyautogui
from PIL import Image,ImageGrab
import time


# def day(data):
#     for i in range(570, 585):
#         for j in range(100, 130):
#             if(data[i,j]<40):
#                 return False
#     return True
#


def hit():
    pyautogui.keyDown("up")
    return

def isCollide_night(data):
    for i in range(740,775):
        for j in range(245,280):
            if(data[i,j]>160 and data[i,j]<185):
                hit()
                return


# def isCollide_day(data):
#     for i in range(570, 615):
#         for j in range(300, 350):
#             if (data[i, j] < 40):
#                 hit()
#

time.sleep(3)

# image = ImageGrab.grab().convert("L")
# data=image.load()

while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    isCollide_night(data)


# for i in range(705,755):   #Lower Bar
#     for j in range(240,280):
#         data[i,j]=185
#
# for i in range(570,585):  #Upper bar
#     for j in range(100,130):
#         data[i,j]=240
#
# image.show()




