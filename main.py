import pyautogui
import tkinter as tk
from tkinter.filedialog import *
import time

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def takeScreenshot():
    root.withdraw()
    time.sleep(1)
    myScreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myScreenshot.save(save_path+"_screenshot.png")

    root.update()
    root.deiconify()

myButton = tk.Button(text ="Take Screenshot", command = takeScreenshot, font = 10, bg = "black", fg = "white")
canvas1.create_window(150, 150, window=myButton)

root.mainloop()

