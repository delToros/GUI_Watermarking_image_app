import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Create a window
window = tk.Tk()
window.title('Watermarking')
window.config(pady=50, padx=50)
window['bg'] = '#B3CFF2'


filename = ''

# ---- Functions ---- #

def select_file():
    filetypes = [('Image files', '*.jpg'), ('Image files', '*.png'), ('Image files', '*.jpeg')]
    global filename
    filename = fd.askopenfilename(title='open a file', initialdir='/', filetypes=filetypes)
    # print(filename)
    # messagebox.showinfo(
    #     title='Selected File',
    #     message=filename
    # )
    img_new = Image.open(filename)
    r_image = img_new.resize((200, 200))
    n_image = ImageTk.PhotoImage(r_image)
    # img_n = tk.PhotoImage(file='C:/Users/Nikita/Learning/WEB Dev/day-03/images/angela.png')
    canvas.itemconfig(image_container, image=n_image)
    canvas.img = n_image #  <- !!!!!! WITHOUT IT WOULD NOT WORK !!!!!! EXTREMELY IMPORTANT


def add_text():
    if filename == '':
        messagebox.showinfo(
            title='Select File First',
            message='You must select your file first'
        )
    elif txt_box.get() == '':
        messagebox.showinfo(
            title='Text needed',
            message="First put your text in the field text.\nWe can't read your mind"
        )
    working_image = Image.open(filename)
    width, height = working_image.size

    draw = ImageDraw.Draw(working_image)
    text = txt_box.get()

    font = ImageFont.truetype('arial.ttf', 45)

    textwidth, textheight = draw.textsize(text, font)

    x = width - textwidth - 10
    y = height - textheight - 15

    draw.text((x, y), text, font=font)

    # Saving the image
    working_image.save('watermarked.jpg')
    r_image = working_image.resize((200, 200))
    update_canvas_img = ImageTk.PhotoImage(r_image)
    canvas.itemconfig(image_container, image=update_canvas_img)
    canvas.img = update_canvas_img

def add_logo():
    # Open base file
    baseimg = Image.open(filename)

    # Open logo file
    filetypes = [('Image files', '*.jpg'), ('Image files', '*.png'), ('Image files', '*.jpeg')]
    logoimg = fd.askopenfilename(title='open a file', initialdir='/', filetypes=filetypes)
    logo_img_pil = Image.open(logoimg)

    # Getting the height and width of the image
    width, height = baseimg.size

    size = (100, 100)

    # You can use resize method here instead of
    # thumbnail method
    logo_img_pil.thumbnail(size)

    # Location where we want to paste it on the
    # main image
    x = width - 100 - 10
    y = height - 100 - 15

    baseimg.paste(logo_img_pil, (x, y))
    # Save the image
    baseimg.save('image_with_logo.jpg')

    # Updating preview
    r_image = baseimg.resize((200, 200))
    update_canvas_img = ImageTk.PhotoImage(r_image)
    canvas.itemconfig(image_container, image=update_canvas_img)
    canvas.img = update_canvas_img


# ----- UI ------ #
# Create Canvas
canvas = tk.Canvas(window, height=200, width=200, bg='skyblue')
canvas.grid(column=1, row=0)
img = tk.PhotoImage(file='C:/Users/Nikita/Learning/WEB Dev/day-03/images/computer.png')
image_container = canvas.create_image(100, 100, image=img)

# Create Buttons
add_img = tk.PhotoImage(file='assests/button_choose-image.png')
# add_img_button = Button(text='Choose image', bg='#4B94F2', fg='#B3CFF2')
add_img_button = tk.Button(image=add_img, borderwidth=0, bg='#B3CFF2',
                           activebackground="#B3CFF2", command=lambda:select_file())
add_img_button.grid(column=0, row=0, pady=50)

txt_label = tk.Label(text='Enter your text below', font=("Open Sans", 26), fg='white', bg='#B3CFF2')
txt_label.grid(column=0, row=1)

txt_box = tk.Entry(width=20, font=('Open Sans', 22), fg='#4B94F2', bg='#B3CFF2', borderwidth=0)
txt_box.grid(column=0, row=2, pady=(0, 15))
txt_box.focus()
# separator = ttk.Separator(orient="horizontal")
# separator.place(x=0, y=-100, rely=1.0, height=2, width=-210, relwidth=1.0)

add_text_button_img = tk.PhotoImage(file='assests/button_add-text-to-photo.png')
add_text_button = tk.Button(image=add_text_button_img, borderwidth=0, bg='#B3CFF2',
                            activebackground="#B3CFF2",  command=add_text)
add_text_button.grid(column=0, row=3, pady=(0, 25))

wm_img = tk.PhotoImage(file='assests/button_add-logo-to-photo.png')
wm_img_button = tk.Button(image=wm_img, borderwidth=0, bg='#B3CFF2', activebackground="#B3CFF2", command=add_logo)
wm_img_button.grid(column=0, row=4)

# test_button = tk.Button(text='Test button', command=add_text)
# test_button.grid(column=0, row=5)



window.mainloop()





