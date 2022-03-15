from tkinter import *
from PIL import ImageTk,Image

root= Tk()
root.title('Viewer')
root.iconbitmap('sideicon.ico')

img_path = 'photo/'
imageList = []

for i in range(0, 5):
    img = img_path + 'download_' + str(i) + '.jfif'
    image = ImageTk.PhotoImage(Image.open(img))
    imageList.append(image)


label = Label(root, image=imageList[0])
label.grid(row=0, column=0, columnspan=3)

status = Label(root, text=f'Image 1 of 5')
status.grid(row=2, column=2, columnspan=3)

def back(number):
    global label
    global nextButton
    global backButton

    if number>0:
        label.grid_forget()
        label = Label(root, image=imageList[number-1])
        backButton = Button(root, text='<<', borderwidth=4, command=lambda: back(number-1))
        nextButton = Button(root, text='>>', borderwidth=4, command=lambda: next(number+1))

        label.grid(row=0, column=0, columnspan=3)
        backButton.grid(row=1, column=0)
        nextButton.grid(row=1, column=2)

        status = Label(root, text=f'Image {number} of 5')
        status.grid(row=2, column=2, columnspan=3)

    else: pass

def next(number):
    global label
    global nextButton
    global backButton

    if number==6:
        pass
    else:
        label.grid_forget()
        label = Label(root, image=imageList[number-1])
        nextButton = Button(root, text='>>', borderwidth=4, command=lambda: next(number+1))
        backButton = Button(root, text='<<', borderwidth=4, command=lambda: back(number-1))
        
        label.grid(row=0, column=0, columnspan=3)
        backButton.grid(row=1, column=0)
        nextButton.grid(row=1, column=2)

        status = Label(root, text=f'Image {number} of 5')
        status.grid(row=2, column=2, columnspan=3)


backButton = Button(root, text='<<', borderwidth=4, command=lambda: back())
exitButton = Button(root, text='EXIT', borderwidth=4, command=root.quit)
nextButton = Button(root, text='>>', borderwidth=4, command=lambda: next(2))

backButton.grid(row=1, column=0)
exitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2)

root.mainloop()
