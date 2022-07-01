import tkinter
from PIL import ImageTk, Image
import urllib.request
import re
import os


imgs = []

def find_image_ext(full_url):
    found = ""
    m = re.search(r'[.](.[^/]+?)[?]', full_url)
    #print(m)
    if m:
        found = m.group(1)
    return found

def image_canvas_clicked(event, img_fn):
    #print("Data^", img_fn, event.x, event.y, event.widget)
    #img = Image.open(img_fn)
    #img.show()
    os.startfile(img_fn)

def show_giphy_image(urls_to_show):
    root = tkinter.Tk()
    for url_to_show in urls_to_show:
        pic_url, pic_height, pic_width = url_to_show
        canvas = tkinter.Canvas(root, height=pic_height, width=pic_width)
        canvas.pack(fill=tkinter.Y, side=tkinter.LEFT)
        image_fn = pic_url.split("/")[-2] +"."+find_image_ext(pic_url)

        if (not os.path.isdir(os.path.join(os.getcwd(),"pics"))):
            os.makedirs(os.path.join(os.getcwd(),"pics"))
        img_path = os.path.join(os.getcwd(),"pics", image_fn)
        urllib.request.urlretrieve(pic_url, img_path)

        img = ImageTk.PhotoImage(Image.open(img_path))
        imgs.append(img)
        canvas.create_image(1, 1, anchor=tkinter.NW, image=img, tags="canvas_image")
        image_id = canvas.create_text( (8, int(pic_height)-10), text=image_fn)

        canvas.tag_bind("canvas_image", "<Button-1>", lambda event,
                                                             img_fn=image_fn: image_canvas_clicked(event, img_fn))
        #Label(root, image=imgs[-1], width=pic_width, height=pic_height).grid()

    root.call('wm', 'attributes', '.', '-topmost', True)
    root.update()
    root.after_idle(root.attributes, '-topmost', False)
    #root.after(1, lambda: root.focus_force())
    root.mainloop()

    return
