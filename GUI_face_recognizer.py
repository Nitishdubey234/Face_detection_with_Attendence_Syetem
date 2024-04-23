import tkinter as tk
from tkinter import messagebox
import cv2
import os
from PIL import Image
import numpy as np


window=tk.Tk()
window.title("Face Recognition System")

l1=tk.Label(window,text="Name",font=("Algerian",20))
l1.grid(column=0,row=0)

window.geometry("1530x790+0+0")
window.mainloop()

