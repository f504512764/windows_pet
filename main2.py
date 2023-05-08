# -*- coding: UTF-8 -*-
from tkinter import *
from random import randint
from PIL import Image
import os
# 版本2：实现4组gif随机切换

def getAllGifImage():
    gifList=[]
    for i in os.listdir():
        if i.endswith(".gif"):
            gifList.append(i)
    return gifList

def mergerGifImages(imgsList):
    mergerGifImagesList=[]
    for i in imgsList:
        tmpFrameNum,tmpFpsMs=getFramesNum(i)
        tmpPhotoImagesList=getGifList(i, tmpFrameNum)
        tmpPhotoImagesList.append(tmpFrameNum)
        tmpPhotoImagesList.append(tmpFpsMs)
        mergerGifImagesList.append(tmpPhotoImagesList)
    return mergerGifImagesList

def getGifList(gifName:str,frameNum:int)->list:
    tmpGifFrames=[]
    for i in range(frameNum):
        tmpFrame=PhotoImage(file=gifName, format='gif -index {}'.format(i))
        tmpGifFrames.append(tmpFrame)
    return tmpGifFrames

def getFramesNum(gifName):
    # 打开GIF文件
    with Image.open(gifName) as im:
        # 获取帧数
        frames = im.n_frames
        fpsMs = im.info['duration']
    return frames,fpsMs

# [[gif,framesNum,fpsMs],[],[],[]]
def updata(allGifFramesList,n,idx):
    global flag
    if idx==allGifFramesList[n][-2]:
        n=randint(0,3)
        idx=0
        label_gif['image'] = allGifFramesList[n][idx]
        flag=root.after(allGifFramesList[n][-1], updata, allGifFramesList,n,idx)
    else:
        label_gif['image']= allGifFramesList[n][idx]
        idx += 1
        flag=root.after(allGifFramesList[n][-1], updata, allGifFramesList,n,idx)

def start_move(event):
    global press_x,press_y
    # 相对于组件，x是width
    press_x = event.x
    press_y = event.y

def on_motion(event):
    global press_x,press_y
    # x_root是鼠标位置相对于屏幕，geometry窗体左上角的坐标
    root.geometry(f'+{event.x_root - press_x}+{event.y_root - press_y}')  # 窗体移动代码

def reset(event):
    if flag!='':
        root.after_cancel(flag)
        updata(mer, 0, 0)



flag=''
# step1:显示gif
root = Tk()
root_x = root.winfo_screenwidth()
root_y = root.winfo_screenheight()
win_width=randint(0,root_x)
win_height=randint(0,root_y)
root.geometry('+{}+{}'.format(win_width,win_height))
root.wm_attributes('-topmost', 1)
root.overrideredirect(True)  # 窗口无边框
TRANSCOLOUR = 'gray'
root.wm_attributes("-transparentcolor", TRANSCOLOUR)  # 设置'gray'为透明色

label_gif = Label(root)
label_gif = Label(root,background=TRANSCOLOUR)
label_gif.pack()
mer=mergerGifImages(getAllGifImage())

# 移动
root.bind("<ButtonPress-1>", start_move)
root.bind("<B1-Motion>", on_motion)
#双击重置
root.bind("<Double-Button-1>",reset)

updata(mer,0,0)
# print(mergerGifImages(getAllGifImage()))

root.mainloop()


