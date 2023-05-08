import os
from tkinter import PhotoImage,Tk
from PIL import Image

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


def getAllGifImage():
    gifList=[]
    for i in os.listdir():
        if i.endswith(".gif"):
            gifList.append(i)
    return gifList


if __name__ == '__main__':
    # win=Tk()
    # print(len(getGifList("click.gif",10)))
    # a,b=getFramesNum("click.gif")
    # print(a,b)
    a=getAllGifImage()
    print(a)