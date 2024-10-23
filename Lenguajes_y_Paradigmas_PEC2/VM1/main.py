from src.vm_interface import VMInterface
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    app = VMInterface(root)
    root.mainloop()
