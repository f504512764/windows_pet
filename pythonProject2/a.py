import os
import io
from PIL import Image, ImageSequence

all_file = os.listdir()
for file in all_file:
    if file.endswith('.gif'):
        real_name = file[:-4]
        gif_frames = Image.open(file)
        write_data = "{}=[".format(real_name)
        tmp=999999
        for idx,frame in enumerate(ImageSequence.Iterator(gif_frames)):
            tmp=min(tmp,frame.info['duration'])
            imgByteArr = io.BytesIO()
            frame.save(imgByteArr, format='PNG')
            imgByteArr = imgByteArr.getvalue()
            write_data = write_data + "%s," % (imgByteArr)
        write_data = write_data + '{},{}]\n'.format(gif_frames.n_frames,tmp)
        print(gif_frames.n_frames,tmp)
        f = open("all_image.py","a+")
        f.write(write_data)
        f.close()
