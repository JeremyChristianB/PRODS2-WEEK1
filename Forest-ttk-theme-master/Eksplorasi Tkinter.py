import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def home_page():
    home_frame = tk.Frame(main_frame)
    

    # Load background image buat main frame
    background_image = Image.open("backgroundUtamaResized.jpg")  # Replace background image file
    background_photo = ImageTk.PhotoImage(background_image)


    # Create label dengan transparent background
    title_label = tk.Label(home_frame, text='Reforestation', font=('Bold', 36), fg='green', highlightthickness=0)
    title_label.pack()
    
    lb = tk.Label(home_frame, text='Home Page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    
    home_frame.pack(pady=20)
    
def about_page():
    about_frame = tk.Frame(main_frame)
    
    lb = tk.Label(about_frame, text='About Page\n\nPage: 3', font=('Bold', 30))
    lb.pack()
    
    about_frame.pack(pady=20)
    
def menu_page():
    menu_frame = tk.Frame(main_frame)
    
    lb = tk.Label(menu_frame, text='Menu Page\n\nPage: 2', font=('Bold', 30))
    lb.pack()
    
    menu_frame.pack(pady=20)
    

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    menu_indicate.config(bg='#c3c3c3')
    about_indicate.config(bg='#c3c3c3')
    
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

root = tk.Tk()
root.title("Dashboard Aplikasi")

# Import the tcl file
root.tk.call('source', 'forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

options_frame = tk.Frame(root, bg='#c3c3c3')

home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15), fg='green', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(home_indicate, home_page)
                     )

home_btn.place(x=10, y=50)

home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=50, width=5, height=40) 

menu_btn = tk.Button(options_frame, text='Menu', font=('Bold', 15), fg='green', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(menu_indicate, menu_page)
                     )

menu_btn.place(x=10, y=100)

menu_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
menu_indicate.place(x=3, y=100, width=5, height=40) 

about_btn = tk.Button(options_frame, text='About', font=('Bold', 15), fg='green', bd=0, bg='#c3c3c3',
                      command=lambda: indicate(about_indicate, about_page)
                      )

about_btn.place(x=10, y=150)

about_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
about_indicate.place(x=3, y=150, width=5, height=40) 

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

# Load background image buat main frame
background_image = Image.open("backgroundUtamaResized.jpg")  # Replace background image file
background_photo = ImageTk.PhotoImage(background_image)

# Create canvas untuk menaruh background image buat main frame
background_canvas = tk.Canvas(main_frame, width=background_image.width, height=background_image.height)
background_canvas.pack()

# Create label untuk display background image
background_label = tk.Label(background_canvas, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create label dengan transparent background
title_label = tk.Label(background_canvas, text='Reforestation', font=('Bold', 36), fg='green', highlightthickness=0)
title_label.place(x=20, y=20)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)

root.mainloop()  
