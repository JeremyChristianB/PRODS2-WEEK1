from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def klasifikasi_page():
    klasifikasi_frame = tk.Frame(main_frame)
    
    klasifikasi_frame.pack(pady=20, side=tk.RIGHT)  # Frame untuk elemen-elemen baru diletakkan di sebelah kanan
    
    # Dropdown dengan judul "Daftar Daerah"
    daftar_daerah_label = tk.Label(klasifikasi_frame, text='Daftar Daerah', font=('Helvetica', 16))
    daftar_daerah_label.pack(pady=10)
    
    daerah_var = tk.StringVar()
    daerah_dropdown = ttk.Combobox(klasifikasi_frame, textvariable=daerah_var,
                                   values=['Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Sumatera Barat', 'Sumatera Utara'])
    daerah_dropdown.pack(pady=10)
    
    # Tombol "Choose Files"
    choose_files_btn = tk.Button(klasifikasi_frame, text='Choose Files', font=('Helvetica', 14), command=choose_files)
    choose_files_btn.pack(pady=10)
    
    # Tombol "Mulai Klasifikasi"
    mulai_klasifikasi_btn = tk.Button(klasifikasi_frame, text='Mulai Klasifikasi', font=('Helvetica', 16), command=start_classification)
    mulai_klasifikasi_btn.pack(pady=20)
    
def about_page():
    about_frame = tk.Frame(main_frame)
    
    lb = tk.Label(about_frame, text='About Page\n\nPage: 3', font=('Bold', 30))
    lb.pack()
    
    about_frame.pack(pady=20)
    
def hitung_page():
    hitung_frame = tk.Frame(main_frame)

    # Frame untuk elemen-elemen baru diletakkan di sebelah kanan
    hitung_frame.pack(padx=20, pady=20, side=tk.RIGHT)

    # Frame untuk gambar (di sebelah kiri)
    gambar_frame = tk.Frame(hitung_frame)
    gambar_frame.pack(side=tk.LEFT)

    # Isi frame gambar (contoh gambar)
    contoh_gambar = Image.open("backgroundUtamaResized.png")  # Ganti dengan path ke gambar Anda
    contoh_gambar = contoh_gambar.resize((200, 200), Image.ANTIALIAS)
    contoh_gambar = ImageTk.PhotoImage(contoh_gambar)
    gambar_label = tk.Label(gambar_frame, image=contoh_gambar)
    gambar_label.image = contoh_gambar
    gambar_label.pack(pady=10)

    # Frame untuk deskripsi (di sebelah kanan)
    deskripsi_frame = tk.Frame(hitung_frame, bg='white')
    deskripsi_frame.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Judul "Deskripsi"
    judul_label = tk.Label(deskripsi_frame, text='Deskripsi',bg='green', font=('Helvetica', 12))
    judul_label.pack(pady=10)

    # Isi deskripsi
    deskripsi_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Nullam non metus eget nunc facilisis varius. Proin bibendum,
    justo in varius bibendum, neque justo consequat justo, id
    pellentesque justo orci id mi.
    """
    deskripsi_label = tk.Label(deskripsi_frame,bg='green', text=deskripsi_text)
    deskripsi_label.pack(pady=10)

# ...


    

def hide_indicators():
    klasifikasi_indicate.config(bg='#c3c3c3')
    hitung_indicate.config(bg='#c3c3c3')
    about_indicate.config(bg='#c3c3c3')
    
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

def choose_files():
    # Fungsi yang akan dijalankan ketika tombol "Choose Files" ditekan
    # Anda dapat menambahkan kode untuk memilih file di sini
    pass

def start_classification():
    # Fungsi yang akan dijalankan ketika tombol "Mulai Klasifikasi" ditekan
    # Anda dapat menambahkan kode untuk memulai klasifikasi di sini
    pass

root = tk.Tk()
root.title("Dashboard Aplikasi")

# Import the tcl file
root.tk.call('source', 'forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

options_frame = tk.Frame(root, bg='#c3c3c3')

klasifikasi_btn = tk.Button(options_frame, text='Klasifikasi', font=('Bold', 15), fg='green', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(klasifikasi_indicate, klasifikasi_page)
                     )

klasifikasi_btn.place(x=2, y=50)

klasifikasi_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
klasifikasi_indicate.place(x=3, y=50, width=5, height=40) 

hitung_btn = tk.Button(options_frame, text='Hitung', font=('Bold', 15), fg='green', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(hitung_indicate, hitung_page)
                     )

hitung_btn.place(x=10, y=100)

hitung_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
hitung_indicate.place(x=3, y=100, width=5, height=40) 

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
background_image = PhotoImage(file="backgroundUtamaResized.png")  # Replace background image file

# Create canvas untuk menaruh background image buat main frame
background_canvas = tk.Canvas(main_frame, width=400, height=500)
background_canvas.pack(fill='both',expand=True)

background_canvas.create_image(0,0, image=background_image,anchor = 'nw')

background_canvas.create_text(130,40,text='Reforestation',font=('Helvetica',30))

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)

root.mainloop()  
