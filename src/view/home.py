import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

tk_home_screen = tk.Tk()
tk_home_screen.title("GA Product Control")
tk_home_screen.geometry("1280x600+30+20")
tk_home_screen.configure(bg="#FFFFFF")

img_searh_item = Image.open("../img/icons/search_white.png")
img_searh_item = img_searh_item.resize((30, 30))
img_searh_item_tk = ImageTk.PhotoImage(img_searh_item)

img_add_new_item = Image.open("../img/icons/add_white.png")
img_add_new_item = img_add_new_item.resize((30, 30))
img_add_new_item_tk = ImageTk.PhotoImage(img_add_new_item)

img_search_spreadsheet = Image.open("../img/icons/file-spreadsheet_white.png")
img_search_spreadsheet = img_search_spreadsheet.resize((30, 30))
img_search_spreadsheet_tk = ImageTk.PhotoImage(img_search_spreadsheet)

tk_tab_bar = tk.Frame(tk_home_screen, bg="#000000", height=50)
tk_tab_bar.pack(side="bottom", fill="x")

btn_search_item = tk.Button(tk_tab_bar, cursor="hand2", bg="#000000", border=0, image=img_searh_item_tk)
btn_search_item.place(x=520, y=10)

btn_add_new_item = tk.Button(tk_tab_bar, cursor="hand2", bg="#000000", border=0, image=img_add_new_item_tk)
btn_add_new_item.place(x=640, y=10)

btn_search_spreadsheet = tk.Button(tk_tab_bar, cursor="hand2", bg="#000000", border=0, anchor="center", image=img_search_spreadsheet_tk)
btn_search_spreadsheet.place(x=760, y=10)

tk_canvas_tab_bar = tk.Canvas(tk_home_screen, bg="#FFFFFF", width=1280, height=50)
tk_canvas_tab_bar.pack(fill="both", expand=True)

tk_home_screen.mainloop()