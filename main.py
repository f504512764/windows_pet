# -*- coding: UTF-8 -*-
from tkinter import *
from random import randint
from PIL import Image

# 版本1：实现gif的随机位置的显示

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

'''
after(self, ms, func=None， *args)

在给定时间后调用函数一次。
MS以毫秒为单位指定时间。函数给出了
要调用的函数。额外的参数
作为函数调用的参数。返回
使用after_cancel取消调度的标识符。
'''
def updata(frames,idx,allIdx,ms):
    global flag
    label_gif['image']=frames[idx]
    idx += 1
    if idx<allIdx:
        # print("start flag1:",flag,type(flag))
        # flag1->after#0
        flag=root.after(ms,updata,frames,idx,allIdx,ms)
        # print("end flag1:", flag)
    else:
        idx=0
        # print("start flag2:", flag)
        flag=root.after(ms, updata, frames,idx, allIdx,ms)
        # print("end flag2:", flag)
    # label_gif.after(ms,updata,frames,idx%allIdx,allIdx,ms)

# def stop():
# 	'''停止计数'''
#     global flag
# 	root.after_cancel(flag)

# step1:显示gif
flag=-22

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

# button = Button(root, text='Stop', width=25, command=stop,relief=GROOVE)
# button.pack()
frames=getGifList('click.gif',10)
a,b=getFramesNum('click.gif')
# print("+++++++++++++++++")
updata(frames,0,a,b)
# print("-----------------")
root.mainloop()
