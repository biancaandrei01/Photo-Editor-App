# Photo Editor Application

The main window of the Photo Editor application features a simple and intuitive graphical user interface (GUI) built with Python using the **Tkinter** and **ttkbootstrap** libraries. The interface is divided into two main sections: a **control panel** on the left and a **canvas** for image viewing and editing on the right.

<img src="https://github.com/user-attachments/assets/f187e4fb-5265-4b09-a201-a24d663cd446" alt="Application Main Interface" width="50%"/>

## Control Panel

The control panel contains buttons for the application's key functionalities. These controls include:

*   **Load Image:** Using the "Open" button, the user can select and load an image from their local file system.
*   **Flip Image:** The "Flip" button allows the user to mirror the image horizontally.
*   **Rotate Image:** The "Rotate Left" and "Rotate Right" buttons rotate the image 90 degrees counter-clockwise or clockwise.
*   **Pen Color Selection:** The user can choose a color for the drawing tool using the "Pen Color" button.
*   **Drawing Tools:** The "Toggle Pen" and "Erase" buttons activate and deactivate the drawing tool, allowing users to add or remove freehand lines on the image.
*   **Revert to Original:** This button cancels all edits and restores the image to its original state, without needing to reload it.
*   **Save Image:** The "Save" button provides the option to save the edited image to a new file.

## Filters and Effects

The application also offers a range of filters and effects that users can apply to their images from a dropdown menu:

*   **Black and White:** Converts the color image to grayscale, preserving only the light intensities.
*   **Blur:** Creates a blurring effect, reducing detail and giving the image a smoother appearance.
*   **Detail:** Accentuates the details in the image, highlighting textures and object edges.
*   **Smooth:** Applies a subtle blur effect that reduces contrast and softens the image.
*   **Emboss:** Adds a relief effect to the image, giving it a three-dimensional look.
*   **Edge Enhance:** Sharpens the edges within the image, increasing their clarity.
*   **Contour:** Highlights the contours of objects, giving the image a distinct graphic style.
*   **Sharpen:** Increases the contrast between pixels, making the image appear crisper.

## Image Canvas

The image canvas is the main area on the right side of the window. This is where the loaded image is displayed, and users can see the results of their edits in **real-time**. This interactive space allows users to work directly with the image as they explore the application's various features.

<table>
<tr>
<td><b>Original Image</b></td>
<td><b>Edited Image (rotated, with black and white and detail filters and drawing)</b></td>
</tr>
<tr>
<td><img src="https://github.com/user-attachments/assets/82e24491-b149-46be-bb8f-3f60b0898781" alt="Original Image"></td>
<td><img src="https://github.com/user-attachments/assets/bf6c0089-38d0-49c4-92e4-4946b24555cc" alt="Edited Image"></td>
</tr>
</table>

Overall, the application's interface combines utility with accessibility, providing an efficient and user-friendly way to edit and view images.
