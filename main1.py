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
    if idx==allGifFramesList[n][-2]:
        n=randint(0,3)
        idx=0
        label_gif['image'] = allGifFramesList[n][idx]
        label_gif.after(allGifFramesList[n][-1], updata, allGifFramesList,n,idx)
    else:
        label_gif['image']= allGifFramesList[n][idx]
        idx += 1
        label_gif.after(allGifFramesList[n][-1], updata, allGifFramesList,n,idx)

# step1:显示gif
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('+{}+{}'.format(randint(0,screen_width),randint(0,screen_height)))
root.wm_attributes('-topmost', 1)
root.overrideredirect(True)  # 窗口无边框
TRANSCOLOUR = 'gray'
root.wm_attributes("-transparentcolor", TRANSCOLOUR)  # 设置'gray'为透明色

label_gif = Label(root)
label_gif = Label(root,background=TRANSCOLOUR)
label_gif.pack()
mer=mergerGifImages(getAllGifImage())
updata(mer,0,0)
# print(mergerGifImages(getAllGifImage()))


root.mainloop()


