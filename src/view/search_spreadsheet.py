import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

str_path_file = ""

tk_search_spreadsheet_screen = tk.Tk()
tk_search_spreadsheet_screen.title("GA Product Control")
tk_search_spreadsheet_screen.geometry("600x200+30+20")
tk_search_spreadsheet_screen.configure(bg="#FFFFFF")

def search_spreadsheet():
    global str_path_file
    str_path_file = filedialog.askopenfilename(
        title="Select a .xlsx file",
        filetypes=[("Files", "*.xlsx")]
    )
    
    if str_path_file:
        label_path_file_user = tk.Label(tk_search_spreadsheet_screen, text= f"{str_path_file}", font=("Arial", 8, "bold"), bg="#D9D9D9", fg="#000000")
        label_path_file_user.place(x=10, y=90)

img_add_new_spreadsheet= Image.open(".../src/img/buttons/img_button_add.png")
img_add_new_spreadsheet = img_add_new_spreadsheet.resize((40, 40))
img_add_new_spreadsheet_tk = ImageTk.PhotoImage(img_add_new_spreadsheet)

img_confirm_spreadsheet = Image.open(".../src/img/buttons/img_button_confirm.png")
img_confirm_spreadsheet = img_confirm_spreadsheet.resize((140, 33))
img_confirm_spreadsheet_tk = ImageTk.PhotoImage(img_confirm_spreadsheet)

label_title = tk.Label(tk_search_spreadsheet_screen, text= "New Spreadsheet", font=("Arial", 16, "bold"), fg="#000000", bg="#FFFFFF")
label_title.place(x=10, y=10)

label_path_file = tk.Label(tk_search_spreadsheet_screen, text= "Path", font=("Inter", 12), fg="#000000", bg="#FFFFFF")
label_path_file.place(x=10, y=50)

btn_search_item = tk.Button(tk_search_spreadsheet_screen,
                            cursor="hand2",
                            bg="#FFFFFF",
                            border=0,
                            image=img_add_new_spreadsheet_tk,
                            command=search_spreadsheet,
                            )

btn_search_item.place(x=530, y=80)

btn_confirm = tk.Button(tk_search_spreadsheet_screen,
                        cursor="hand2",
                        bg="#FFFFFF",
                        border=0,
                        image=img_confirm_spreadsheet_tk,
                        )

btn_confirm.place(x=9, y=150)

tk_search_spreadsheet_screen.mainloop()

print(str_path_file)