import tkinter as tk
import random
import time
from PIL import Image, ImageTk, ImageChops
from tkinter.filedialog import askopenfilename
root = tk.Tk()
image1 = Image.Image()
image2 = Image.Image()
gradient = Image.Image()
random.seed(time.time())

def open_file():

        file = askopenfilename(parent=root, title="Choose a file...", filetype=[("PNG Image", "*.png")])
        if file:
            image = Image.open(file)
            edit = file.split("/")
            text = edit.pop()
            return image, text
        return


def btn1_handler():
    global image1
    image1, text = open_file()
    image1_text.set(text)


def btn2_handler():
    global image2
    image2, text = open_file()
    image2_text.set(text)


def btn3_handler():
    global gradient
    gradient, text = open_file()
    image3_text.set(text)

def do_mush():
    print('doing the mush')
    input1 = image1.load()
    input2 = image2.load()
    output = gradient.load()
    xsize, ysize = gradient.size

    if image1.size[0] > image2.size[0]:
        inputx = image2.size[0]
    else :
        inputx = image1.size[0]

    if image1.size[1] > image2.size[1]:
        inputy = image2.size[1]
    else :
        inputy = image1.size[1]

    #Use gradient as a probability matrix to select which image to take a pixel from
    for x in range(xsize):
        for y in range(ysize):
            if y >= inputy or x >= inputx :
                output[x, y] = 255
                break;

            rando = random.randint(0,255)
            if rando > output[x,y]:
                output[x,y] = input1[x,y]
            else:
                output[x,y] = input2[x,y]

    gradient.save('output.jpg')


canvas = tk.Canvas(root, width = 400, height=700, bg="#94b573")
canvas.grid(columnspan=3, rowspan = 11)

#Set up the logo
logo = Image.open('shroom.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg="#94b573")
logo_label.image = logo

#Section for Image 1
image1_text = tk.StringVar()
image1Prompt = tk.Label(root, text='Please select image 1: ' ,bg="#94b573", fg="White", font=("Freestyle Script", 28))
image1_label = tk.Label(root, textvariable=image1_text, bg="#94b573",fg="White", font=("Arial", 12))
image1_text.set('None')
browse_img1_text = tk.StringVar()
browse_img1_button = tk.Button(root, textvariable = browse_img1_text, bg="#20bebe", fg="white", height=2, width=10, command=lambda: btn1_handler())
browse_img1_text.set('Browse')

#Section for Image 2
image2_text = tk.StringVar()
image2Prompt = tk.Label(root, text='Please select image 2: ' ,bg="#94b573", fg="White", font=("Freestyle Script", 28))
image2_label = tk.Label(root, textvariable=image2_text, bg="#94b573",fg="White", font=("Arial", 12))
image2_text.set('None')
browse_img2_text = tk.StringVar()
browse_img2_button = tk.Button(root, textvariable = browse_img2_text, bg="#20bebe", fg="white", height=2, width=10, command=lambda:btn2_handler())
browse_img2_text.set('Browse')

#Section for "Mush" image
image3_text = tk.StringVar()
image3Prompt = tk.Label(root, text='Please select the mush image: ' ,bg="#94b573", fg="White", font=("Freestyle Script", 25))
image3_label = tk.Label(root, textvariable=image3_text, bg="#94b573",fg="White", font=("Arial", 12))
image3_text.set('None')
browse_img3_text = tk.StringVar()
browse_img3_button = tk.Button(root, textvariable = browse_img3_text, bg="#20bebe", fg="white", height=2, width=10, command=lambda: btn3_handler())
browse_img3_text.set('Browse')

#MUSH BUTTON

doMush_text = tk.StringVar()
doMush_button = tk.Button(root, textvariable = doMush_text, bg = 'red', fg = "white", height = 10, width = 20, command = lambda: do_mush())
doMush_text.set('MUSH!')

#set up GUI
logo_label.grid(columnspan=3, column=0, row=0)
image1Prompt.grid(columnspan=1, column=0, row=1)
browse_img1_button.grid(columnspan=1, column=2, row=1)
image1_label.grid(columnspan=3, row=2)

image2Prompt.grid(columnspan=1, column=0, row=4)
browse_img2_button.grid(columnspan=1, column=2, row=4)
image2_label.grid(columnspan=3, row=5)

image3Prompt.grid(columnspan=1, column=0, row=7)
browse_img3_button.grid(columnspan=1, column=2, row=7)
image3_label.grid(columnspan=3, row=8)

doMush_button.grid(columnspan = 3, rowspan = 2, row = 10)



root.mainloop()

