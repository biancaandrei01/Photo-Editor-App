from tkinter import filedialog, colorchooser
from tkinter.messagebox import showerror, showinfo

import ttkbootstrap as ttk
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab

INITIAL_WIDTH = 400
INITIAL_HEIGHT = 520


class ImageEditor:
    def __init__(self, master):
        """Initialize the Image Editor application."""
        self.master = master
        self.master.title("Photo Editor App")

        # --- State Attributes (replaces global variables) ---
        self.file_path = None
        self.original_image = None  # The image as loaded from the file
        self.display_image = None  # The image currently being manipulated
        self.tk_image = None  # The PhotoImage to display on the canvas

        self.pen_size = 3
        self.pen_color = "black"
        self.is_pen_active = False

        # --- Load Resources ---
        self._load_icons()

        # --- Create Widgets ---
        self._create_widgets()

    def _load_icons(self):
        """Load all icons used in the UI."""
        try:
            self.icons = {
                'app': ttk.PhotoImage(file='icons/icon.png'),
                'open': ttk.PhotoImage(file='icons/add.png').subsample(2, 2),
                'flip': ttk.PhotoImage(file='icons/flip.png').subsample(2, 2),
                'rotate_left': ttk.PhotoImage(file='icons/rotate_left.png').subsample(2, 2),
                'rotate_right': ttk.PhotoImage(file='icons/rotate_right.png').subsample(2, 2),
                'pen': ttk.PhotoImage(file='icons/edit.png').subsample(2, 2),
                'color': ttk.PhotoImage(file='icons/color.png').subsample(2, 2),
                'erase': ttk.PhotoImage(file='icons/erase.png').subsample(2, 2),
                'save': ttk.PhotoImage(file='icons/save.png').subsample(2, 2),
                'revert': ttk.PhotoImage(file='icons/return.png').subsample(2, 2)
            }
            self.master.iconphoto(False, self.icons['app'])
        except Exception as e:
            print(f"Error loading icons: {e}\nUsing text buttons as fallback.")
            self.icons = {}  # Clear icons so we can fallback to text

    def _create_widgets(self):
        """Create and layout all the GUI widgets."""
        # --- Left Frame for Controls ---
        left_frame = ttk.Frame(self.master)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)

        # --- Right Canvas for Image ---
        self.canvas = ttk.Canvas(self.master, width=INITIAL_WIDTH, height=INITIAL_HEIGHT)
        self.canvas.pack(fill="both", expand=True)

        # --- Control Widgets ---
        # Helper to create buttons, handles icon/text fallback
        def create_button(parent, text, icon_key, command):
            return ttk.Button(
                parent,
                text=text if not self.icons else "",
                image=self.icons.get(icon_key),
                compound="left",
                style="light",
                command=command
            )

        filter_label = ttk.Label(left_frame, text="Select Filter:")
        filter_label.pack(pady=5)

        image_filters = ["Contour", "Black and White", "Blur", "Detail", "Emboss", "Edge Enhance", "Sharpen", "Smooth"]
        self.filter_combobox = ttk.Combobox(left_frame, values=image_filters, state='readonly')
        self.filter_combobox.pack(pady=5, fill='x')
        self.filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.apply_filter())

        ttk.Separator(left_frame, orient='horizontal').pack(pady=10, fill='x')

        open_button = create_button(left_frame, "Open", 'open', self.open_image)
        open_button.pack(pady=5, fill="x")

        revert_button = create_button(left_frame, "Revert", 'revert', self.revert_to_original)
        revert_button.pack(pady=5, fill="x")

        ttk.Separator(left_frame, orient='horizontal').pack(pady=10, fill='x')

        flip_button = create_button(left_frame, "Flip", 'flip', self.flip_image)
        flip_button.pack(pady=5, fill="x")

        rotate_left_button = create_button(left_frame, "Rotate L", 'rotate_left', self.rotate_left_image)
        rotate_left_button.pack(pady=5, fill="x")

        rotate_right_button = create_button(left_frame, "Rotate R", 'rotate_right', self.rotate_right_image)
        rotate_right_button.pack(pady=5, fill="x")

        ttk.Separator(left_frame, orient='horizontal').pack(pady=10, fill='x')

        pen_button = create_button(left_frame, "Toggle Pen", 'pen', self.toggle_pen)
        pen_button.pack(pady=5, fill="x")

        color_button = create_button(left_frame, "Pen Color", 'color', self.change_pen_color)
        color_button.pack(pady=5, fill="x")

        erase_button = create_button(left_frame, "Erase Lines", 'erase', self.erase_lines)
        erase_button.pack(pady=5, fill="x")

        ttk.Separator(left_frame, orient='horizontal').pack(pady=10, fill='x')

        save_button = create_button(left_frame, "Save", 'save', self.save_image)
        save_button.pack(pady=5, fill="x")

    def _image_loaded(self, show_msg=True):
        """Check if an image is loaded, optionally show an error message."""
        if not self.display_image:
            if show_msg:
                showerror(title='No Image', message='Please open an image first.')
            return False
        return True

    def _update_canvas(self):
        """Convert the PIL image to a Tkinter PhotoImage and display it."""
        if not self._image_loaded(show_msg=False):
            return

        # Prevent garbage collection of the image
        self.tk_image = ImageTk.PhotoImage(self.display_image)

        self.canvas.config(width=self.display_image.width, height=self.display_image.height)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def open_image(self):
        """Open an image file and display it."""
        self.file_path = filedialog.askopenfilename(
            title="Open Image File",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if self.file_path:
            # Store both original and display versions
            self.original_image = Image.open(self.file_path)
            self.display_image = self.original_image.copy()
            self.display_image.thumbnail((self.master.winfo_width() - 150, self.master.winfo_height() - 50))

            # Reset any drawing
            self.erase_lines()
            self.toggle_pen(force_off=True)

            self._update_canvas()

    def revert_to_original(self):
        """Revert all changes back to the originally opened image."""
        if not self._image_loaded():
            return
        self.display_image = self.original_image.copy()
        self.display_image.thumbnail((self.master.winfo_width() - 150, self.master.winfo_height() - 50))
        self.erase_lines()
        self._update_canvas()

    def flip_image(self):
        """Flip the image horizontally."""
        if not self._image_loaded():
            return
        self.display_image = self.display_image.transpose(Image.FLIP_LEFT_RIGHT)
        self._update_canvas()

    def rotate_left_image(self):
        """Rotate the image 90 degrees to the left."""
        if not self._image_loaded():
            return
        self.display_image = self.display_image.rotate(90, expand=True)
        self._update_canvas()

    def rotate_right_image(self):
        """Rotate the image 90 degrees to the right."""
        if not self._image_loaded():
            return
        self.display_image = self.display_image.rotate(-90, expand=True)
        self._update_canvas()

    def apply_filter(self):
        """Apply the selected filter to the image."""
        if not self._image_loaded():
            # Reset combobox if no image is loaded
            self.filter_combobox.set('')
            return

        filter_name = self.filter_combobox.get()
        filter_map = {
            "Black and White": lambda img: ImageOps.grayscale(img),
            "Blur": lambda img: img.filter(ImageFilter.BLUR),
            "Sharpen": lambda img: img.filter(ImageFilter.SHARPEN),
            "Smooth": lambda img: img.filter(ImageFilter.SMOOTH),
            "Emboss": lambda img: img.filter(ImageFilter.EMBOSS),
            "Detail": lambda img: img.filter(ImageFilter.DETAIL),
            "Edge Enhance": lambda img: img.filter(ImageFilter.EDGE_ENHANCE),
            "Contour": lambda img: img.filter(ImageFilter.CONTOUR),
        }

        filter_function = filter_map.get(filter_name)
        if filter_function:
            # Grayscale returns a different mode, handle it
            if filter_name == "Black and White":
                self.display_image = filter_function(self.display_image)
            else:  # Other filters might not work on 'L' mode images
                try:
                    self.display_image = filter_function(self.display_image.convert("RGB"))
                except ValueError:
                    showerror(title="Filter Error", message=f"Cannot apply '{filter_name}' filter after grayscale.")
            self._update_canvas()
        self.filter_combobox.set('')  # Clear selection after applying

    def toggle_pen(self, force_off=False):
        """Activate or deactivate the drawing pen."""
        if force_off:
            self.is_pen_active = True  # To enter the `if` block below

        if self.is_pen_active:
            self.canvas.unbind("<B1-Motion>")
            self.is_pen_active = False
            self.master.config(cursor="")
        else:
            if not self._image_loaded():
                return
            self.canvas.bind("<B1-Motion>", self.draw)
            self.is_pen_active = True
            self.master.config(cursor="crosshair")

    def change_pen_color(self):
        """Open a color chooser to select the pen color."""
        color = colorchooser.askcolor(title="Select Pen Color")[1]
        if color:
            self.pen_color = color

    def draw(self, event):
        """Draw a small oval on the canvas at the mouse position."""
        if self.is_pen_active:
            x1, y1 = (event.x - self.pen_size), (event.y - self.pen_size)
            x2, y2 = (event.x + self.pen_size), (event.y + self.pen_size)
            self.canvas.create_oval(
                x1, y1, x2, y2,
                fill=self.pen_color,
                outline="",
                tags="drawing"
            )

    def erase_lines(self):
        """Erase all lines drawn on the canvas."""
        self.canvas.delete("drawing")

    def save_image(self):
        """Capture the canvas content and save it to a file."""
        if not self._image_loaded():
            return

        new_file_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Bitmap", "*.bmp")]
        )
        if new_file_path:
            # Get coordinates of the canvas
            x = self.canvas.winfo_rootx()
            y = self.canvas.winfo_rooty()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            # Grab the image from the canvas area and save it
            ImageGrab.grab(bbox=(x, y, x1, y1)).save(new_file_path)
            showinfo("Success", "Image saved successfully!")


if __name__ == "__main__":
    root = ttk.Window()
    app = ImageEditor(root)
    root.mainloop()
