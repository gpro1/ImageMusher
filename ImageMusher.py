import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
root = tk.Tk()
image1 = Image.Image()

canvas = tk.Canvas(root, width = 400, height=600, bg="#94b573")
canvas.grid(columnspan=3, rowspan = 7)

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
browse_img1_button = tk.Button(root, textvariable = browse_img1_text, bg="#20bebe", fg="white", height=2, width=10, command=lambda:open_file())
browse_img1_text.set('Browse')

#Section for Image 2
image2_text = tk.StringVar()
image2Prompt = tk.Label(root, text='Please select image 2: ' ,bg="#94b573", fg="White", font=("Freestyle Script", 28))
image2_label = tk.Label(root, textvariable=image1_text, bg="#94b573",fg="White", font=("Arial", 12))
image2_text.set('None')
browse_img2_text = tk.StringVar()
browse_img2_button = tk.Button(root, textvariable = browse_img2_text, bg="#20bebe", fg="white", height=2, width=10, command=lambda:open_file())
browse_img2_text.set('Browse')

#Section for "Mush" image
image3_text = tk.StringVar()
image3Prompt = tk.Label(root, text='Please select the mush image: ' ,bg="#94b573", fg="White", font=("Freestyle Script", 25))
image3_label = tk.Label(root, textvariable=image1_text, bg="#94b573",fg="White", font=("Arial", 12))
image3_text.set('None')
browse_img3_text = tk.StringVar()
browse_img3_button = tk.Button(root, textvariable = browse_img3_text, bg="#20bebe", fg="white", height=2, width=10, command=lambda:open_file())
browse_img3_text.set('Browse')



def open_file():
        global image1
        #file = askopenfile(parent=root, mode='rb', title="Choose a file...", filetype=[("JPEG Image","*.jpg")])
        file = askopenfilename(parent=root, title="Choose a file...", filetype=[("JPEG Image", "*.jpg")])
        if file:

            image1 = Image.open(file)
            edit = file.split("/")
            image1_text.set(edit.pop())
#set up GUI
logo_label.grid(columnspan=3, column=0, row=0)
image1Prompt.grid(columnspan=1, column=0, row=1)
browse_img1_button.grid(columnspan=1, column=2, row=1)
image1_label.grid(columnspan=3, row=2)



root.mainloop()

