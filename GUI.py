import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab

# defining global variables
WIDTH = 500
HEIGHT = 650
file_path = ""
pen_size = 3
pen_color = "black"
pen_active = False
is_flipped = False
rotation_angle = 0
image = NotImplemented
photo_image = NotImplemented


# function to open the image file
def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Open Image File",
                                           filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        global image, photo_image
        image = Image.open(file_path)
        image = image.resize((WIDTH, HEIGHT))

        photo_image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 20, anchor="nw", image=photo_image)


def flip_image():
    try:
        global image, photo_image, is_flipped
        # flip the image left and right
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        photo_image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 20, anchor="nw", image=photo_image)
    except:
        showerror(title='Flip Image Error', message='Please select an image to flip!')

# function for rotating left the image
def rotate_left_image():
    try:
        global image, photo_image, rotation_angle
        # rotate left the image
        rotated_image = image.rotate(rotation_angle + 90)
        rotation_angle += 90
        # reset image if angle is a multiple of 360 degrees
        if rotation_angle % 360 == 0:
            rotation_angle = 0
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas.create_image(0, 20, anchor="nw", image=photo_image)
    # catches errors
    except:
        showerror(title='Rotate Image Error', message='Please select an image to rotate!')


# function for rotating left the image
def rotate_right_image():
    try:
        global image, photo_image, rotation_angle
        # rotate right the image
        rotated_image = image.rotate(rotation_angle - 90)
        rotation_angle -= 90
        # reset image if angle is a multiple of 360 degrees
        if rotation_angle % 360 == 0:
            rotation_angle = 0
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        photo_image = ImageTk.PhotoImage(rotated_image)
        canvas.create_image(0, 20, anchor="nw", image=photo_image)
    # catches errors
    except:
        showerror(title='Rotate Image Error', message='Please select an image to rotate!')


# function for applying filters to the opened image file
def apply_filter(filter):
    global image, photo_image
    try:
        # apply the filter to the image
        if filter == "Black and White":
            image = ImageOps.grayscale(image)
        elif filter == "Blur":
            image = image.filter(ImageFilter.BLUR)
        elif filter == "Sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif filter == "Smooth":
            image = image.filter(ImageFilter.SMOOTH)
        elif filter == "Emboss":
            image = image.filter(ImageFilter.EMBOSS)
        elif filter == "Detail":
            image = image.filter(ImageFilter.DETAIL)
        elif filter == "Edge Enhance":
            image = image.filter(ImageFilter.EDGE_ENHANCE)
        elif filter == "Contour":
            image = image.filter(ImageFilter.CONTOUR)
        # convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        photo_image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 20, anchor="nw", image=photo_image)
    except:
        showerror(title='Error', message='Please select an image first!')


# function for drawing lines on the opened image
def draw(event):
    global file_path, image
    if file_path:
        x1, y1 = (event.x - pen_size), (event.y - pen_size)
        x2, y2 = (event.x + pen_size), (event.y + pen_size)
        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline="", width=pen_size, tags="oval")
        # add the drawing on image
        image = ImageGrab.grab(bbox=(
            canvas.winfo_rootx(), canvas.winfo_rooty() + 20, canvas.winfo_rootx() + canvas.winfo_width(),
            canvas.winfo_rooty() + canvas.winfo_height()))


# function for activate pen
def set_pen():
    global pen_active
    if not pen_active:
        # binding the Canvas to the B1-Motion event
        canvas.bind("<B1-Motion>", draw)
        pen_active = True
    else:
        # binding the Canvas to the B1-Motion event
        canvas.unbind("<B1-Motion>")
        pen_active = False


# function for changing the pen color
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


# function for erasing lines on the opened image
def erase_lines():
    global file_path
    if file_path:
        canvas.delete("oval")


# the function for saving an image
def save_image():
    # create a new PIL Image object from the canvas
    new_image = ImageGrab.grab(bbox=(
        canvas.winfo_rootx(), canvas.winfo_rooty() + 20, canvas.winfo_rootx() + canvas.winfo_width(),
        canvas.winfo_rooty() + canvas.winfo_height()))

    # open file dialog to select save location and file type
    new_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if new_file_path:
        if askyesno(title='Save Image', message='Do you want to save this image?'):
            # save the image to a file
            new_image.save(new_file_path)


root = ttk.Window()
root.title("Image Editor")
root.geometry("720x670+300+100")
root.resizable(width=True, height=True)
icon = ttk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)

# the left frame to contain the 4 buttons
left_frame = ttk.Frame(root)
left_frame.pack(side="left", fill="y")

# the right canvas for displaying the image
canvas = ttk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# label
filter_label = ttk.Label(left_frame, text="Select Filter:")
filter_label.pack(padx=0, pady=5)

# a list of filters
image_filters = ["Contour", "Black and White", "Blur", "Detail", "Emboss", "Edge Enhance", "Sharpen", "Smooth"]

# combobox for the filters
filter_combobox = ttk.Combobox(left_frame, values=image_filters, width=15)
filter_combobox.pack(padx=10, pady=5)
filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))

# loading the icons for the 4 buttons
image_icon = ttk.PhotoImage(file='add.png').subsample(2, 2)
flip_icon = ttk.PhotoImage(file='flip.png').subsample(2, 2)
rotate_left_icon = ttk.PhotoImage(file='rotate_left.png').subsample(2, 2)
rotate_right_icon = ttk.PhotoImage(file='rotate_right.png').subsample(2, 2)
pen_icon = ttk.PhotoImage(file='edit.png').subsample(2, 2)
color_icon = ttk.PhotoImage(file='color.png').subsample(2, 2)
erase_icon = ttk.PhotoImage(file='erase.png').subsample(2, 2)
save_icon = ttk.PhotoImage(file='save.png').subsample(2, 2)

# button for adding/opening the image file
image_button = ttk.Button(left_frame, image=image_icon, style="light", command=open_image)
image_button.pack(padx=0, pady=5)

# button for flipping the image file
flip_button = ttk.Button(left_frame, image=flip_icon, style="light", command=flip_image)
flip_button.pack(padx=0, pady=5)

# button for rotating left the image file
rotate_left_button = ttk.Button(left_frame, image=rotate_left_icon, style="light", command=rotate_left_image)
rotate_left_button.pack(padx=0, pady=5)

# button for rotating rigt the image file
rotate_right_button = ttk.Button(left_frame, image=rotate_right_icon, style="light", command=rotate_right_image)
rotate_right_button.pack(padx=0, pady=5)

# button for choosing pen color
pen_button = ttk.Button(left_frame, image=pen_icon, style="light", command=set_pen)
pen_button.pack(padx=0, pady=5)

# button for choosing pen color
color_button = ttk.Button(left_frame, image=color_icon, style="light", command=change_color)
color_button.pack(padx=0, pady=5)

# button for erasing the lines drawn over the image file
erase_button = ttk.Button(left_frame, image=erase_icon, style="light", command=erase_lines)
erase_button.pack(padx=0, pady=5)

# button for saving the image file
save_button = ttk.Button(left_frame, image=save_icon, style="light", command=save_image)
save_button.pack(padx=0, pady=5)

root.mainloop()
