from tkinter import *
from random import randint
from PIL import Image,ImageTk
import io
from all_image import *

def get_tk_image(gifBytesList):
    # 从字节流获取图像和duration
    gif_frames = []
    i=0
    for temp_gif in gifBytesList:
        temp_png_photos=[]
        for temp_png in temp_gif[:-2]:
            bytes_stream = io.BytesIO(temp_png)
            gifimg = Image.open(bytes_stream)
            roiimg = ImageTk.PhotoImage(gifimg)
            temp_png_photos.append(roiimg)
        temp_png_photos.append(temp_gif[-2])
        temp_png_photos.append(temp_gif[-1])
        gif_frames.append(temp_png_photos)
    return gif_frames

def meu(event):
    menuBar.post(event.x_root,event.y_root)

def quit():
    root.destroy()
# [[gif,framesNum,fpsMs],[],[],[]]
# def updata(allGifFramesList,n,idx):
#     global flag
#     if idx<allGifFramesList[0][-2]:
#         label_gif['image']= allGifFramesList[0][idx]
#         idx += 1
#         flag=root.after(allGifFramesList[0][-1], updata, allGifFramesList,n,idx)
#     else:
#         idx=0
#         flag = root.after(allGifFramesList[0][-1], updata, allGifFramesList, n, idx)

def updata(allGifFramesList,n,idx):
    global flag
    if idx==allGifFramesList[n][-2]:
        n=randint(0,1)
        idx=0
        flag=root.after(allGifFramesList[n][-1], updata, allGifFramesList,n,idx)
    else:
        label_gif['image']= allGifFramesList[n][idx]
        idx += 1
        flag=root.after(allGifFramesList[n][-1], updata, allGifFramesList,n,idx)

def reset(event):
    if flag!='':
        root.after_cancel(flag)
        updata(mer, 0, 0)

def start_move(event):
    global press_x,press_y
    # 相对于组件，x是width
    press_x = event.x
    press_y = event.y

def on_motion(event):
    global press_x,press_y
    # x_root是鼠标位置相对于屏幕，geometry窗体左上角的坐标
    root.geometry(f'+{event.x_root - press_x}+{event.y_root - press_y}')  # 窗体移动代码

flag=''
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

#右键打开程序
menuBar=Menu(root)
#右键打开程序和关闭
menuBar.add_command(label="python",command=None)
menuBar.add_command(label="退出",command=quit)
root.bind("<ButtonPress-3>", meu)
gifNames=[click,normal1,normal2,normal3]
mer=get_tk_image(gifNames)
print(mer)
updata(mer,0,0)

root.bind("<ButtonPress-1>", start_move)
root.bind("<B1-Motion>", on_motion)
#双击重置
root.bind("<Double-Button-1>",reset)

root.mainloop()
