# This module takes path to folder with images and 
# converts images to pdf.
# Images converts in pdf in order of the names.

import os
from tkinter import *
from PIL import Image
from pathlib import Path
from tkinter import filedialog as fd
from threading import Thread
from glob import glob
import time

w_folder = '.'

root = Tk()
root.geometry('400x150')

root.title('PNG and JPG to pdf')

def choose_folder():
    global w_folder
    w_folder = fd.askdirectory()
    lb.config(text=w_folder)

def run():
    t = Thread(target=main, args=())
    t.start()

def main():
    list_of_img = glob(w_folder + '/*.png') + glob(w_folder + '/*.jpg')
    list_of_img.sort(key=(lambda x: int(Path(x).stem)))
    print(list_of_img)

    img_objs = []

    for img in list_of_img:
        img_objs.append(Image.open(img))

    img_conv = []
    for obj in img_objs:
        img_conv.append(obj.convert('RGB'))
    
    ent_text = ent1.get()
    
    pdf_name = ent_text if ent_text else Path(os.path.dirname(list_of_img[0])).stem


    img_conv[0].save(w_folder + f'/{pdf_name}.pdf',
                     save_all=True,
                     append_images=img_conv[1:])


frm1 = Frame(master=root, height=300)
lb = Label(master=frm1, text='Choose folder')
btn = Button(master=frm1, text='Choose folder', command=choose_folder, width=15)
btn2 = Button(master=frm1, text='Run', command=run, width=15)

frm2 = Frame(master=root)
lb2 = Label(master=frm2, text="Enter pdf name: ")
ent1 = Entry(master=frm2, width=200)
lb2.pack(side=LEFT)
ent1.pack(side=LEFT, padx=5)
frm2.pack()
lb.pack()
btn.pack()
btn2.pack()
frm1.pack()

mainloop()
