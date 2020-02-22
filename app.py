import tkinter as tk
import random
import string


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Change the size of root.
        self.master.geometry("350x200")
        self.master.title("Generate a key")
        # Make root non-resizable, so its fixed in size.
        self.master.resizable(False, False)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """ Method to create the widgets."""
        self.passkeyArea = tk.Label(self, text="Your key here")
        # Make the key big and readable.
        self.passkeyArea.config(font=("Consolas", 25))
        # 'pady(topPadding, bottomPadding)' to add a little space between button and passkeyArea
        self.passkeyArea.pack(side="top", pady=(10, 100))

        # Call the generate method.
        self.gen = tk.Button(
            self, text="Generate and Copy", command=self.generate)
        # Pack this to the bottom.
        self.gen.pack(side="bottom")

    def generate(self, length=8):
        """ Method to generate a random string. """
        alpha = string.ascii_lowercase
        passer = ''.join(random.choice(alpha) for i in range(length))
        # Clear clipboard and copy generated string to clipboard.
        self.master.clipboard_clear()
        self.master.clipboard_append(passer)
        self.passkeyArea["text"] = passer


# 'root' object to be used for the Application class.
root = tk.Tk()
# This child is passed 'root' as a parent.
app = Application(master=root)
# A loop that runs until application is quit.
app.mainloop()
