import tkinter
from PIL import ImageTk, Image
import urllib.request
import re

imgs = []
frame_Cnt=[]

def find_image_ext(full_url):
    found = ""
    m = re.search(r'[.](.[^/]+?)[?]', full_url)
    #print(m)
    if m:
        found = m.group(1)
    return found

def show_giphy_image(urls_to_show):
    root = tkinter.Tk()
    for url_to_show in urls_to_show:
        pic_url, pic_height, pic_width = url_to_show
        #print(pic_url)
        canvas = tkinter.Canvas(root, height=pic_height, width=pic_width)
        canvas.pack(fill=tkinter.Y, side=tkinter.LEFT)
        image_fn = pic_url.split("/")[-2] +"."+find_image_ext(pic_url)
        #print(image_fn)
        #print(pic_url)
        #break
        urllib.request.urlretrieve(pic_url, image_fn)

        img = ImageTk.PhotoImage(Image.open(image_fn))
        frameCnt.append(img.n_frames)
        imgs.append(img)
        canvas.create_image(1, 1, anchor=tkinter.NW, image=img)
        id = canvas.create_text( (8, int(pic_height)-10), text=image_fn)
        #Label(root, image=imgs[-1], width=pic_width, height=pic_height).grid()

    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after(1, lambda: root.focus_force())
    root.mainloop()

    return
