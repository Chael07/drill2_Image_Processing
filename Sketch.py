import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Create and configure the "Load New Image" button
        load_button = tk.Button(self.root, text="Load New Image", command=self.load_new_image)
        load_button.pack(pady=10)

        # Placeholder for displaying images
        self.image_label = tk.Label(self.root)
        self.image_label.pack(side="left", padx=10)

    def load_new_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if file_path:
            img = cv2.imread(file_path)
            img = cv2.resize(img, (640, 480))

            # Display the original image
            self.display_image(img, "Original Image")

            # Process and display the processed image
            processed_img = self.process_image(img)
            self.display_image(processed_img, "Processed Image")

    def process_image(self, img):
        # Your image processing code
        gray_img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
        invert_img = cv2.bitwise_not(src=gray_img)
        smooth_img = cv2.medianBlur(src=invert_img, ksize=27)
        ivt_smooth_img = cv2.bitwise_not(smooth_img)
        sketch_img = cv2.divide(gray_img, ivt_smooth_img, scale=250)
        return sketch_img

    def display_image(self, image, title):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)

        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        self.root.title(title)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
