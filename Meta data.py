import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageMetadataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Metadata Viewer")

        self.image_path = tk.StringVar()

        tk.Label(self.root, text="Image Path:").grid(row=0, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.image_path, width=50).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_image).grid(row=0, column=2)

        tk.Button(self.root, text="Show Metadata", command=self.show_metadata).grid(row=1, column=0, columnspan=3, pady=10)

    def browse_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if filename:
            self.image_path.set(filename)

    def show_metadata(self):
        image_path = self.image_path.get()
        if not image_path:
            messagebox.showerror("Error", "Please select an image.")
            return

        try:
            img = Image.open(image_path)
            metadata = img.info
            metadata_str = "\n".join(f"{key}: {value}" for key, value in metadata.items())

            # Show metadata in a pop-up window
            metadata_window = tk.Toplevel(self.root)
            metadata_window.title("Image Metadata")
            metadata_text = tk.Text(metadata_window)
            metadata_text.insert(tk.END, metadata_str)
            metadata_text.config(state="disabled")
            metadata_text.pack()

        except Exception as e:
            messagebox.showerror("Error", "Failed to read metadata: {}".format(str(e)))
            print("Error reading metadata:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageMetadataApp(root)
    root.mainloop()
