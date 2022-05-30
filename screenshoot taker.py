#RO:vezi ca nu o sa mearga daca nu ii pui "pip install pyautogui" in terminal,+tkinter
#ENG:you need to run the command "pip install pyautogui" for this script to work
#that and tkinter too....
import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()

canvas1 = tk.Canvas(root, witdh = 300, height= 300)
canvas1.pack()

def Screenshoot():
  SS= pyautogui.screenshot()
  save_path = asksaveasfilename()
  SS.save(save_path+"_screenshot.png")

myButton= tk.button(text="why dont you press me?", command=screenshot,font=10)
canvas1.create_windows(150,150,window=myButton)

root.mainloop()