from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def klasifikasi_page():
    klasifikasi_frame = tk.Frame(main_frame)

    # Frame untuk daftar model (frame atas)
    daftar_model_frame = tk.Frame(klasifikasi_frame, bg='white')
    daftar_model_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Label "Daftar Model"
    daftar_model_label = tk.Label(daftar_model_frame, text='Daftar Model:', font=('Helvetica', 16))
    daftar_model_label.pack(pady=10)

    # Frame untuk "Model Pixel" (frame kiri)
    model_pixel_frame = tk.Frame(daftar_model_frame, bg='white')
    model_pixel_frame.pack(side=tk.LEFT, padx=20, anchor='n')

    # Label untuk "Model Pixel" (tombol gambar)
    model_pixel_image = Image.open("modelPixel.png")  # Ganti dengan path gambar model pixel
    model_pixel_image = model_pixel_image.resize((150, 150), Image.ANTIALIAS)
    model_pixel_image = ImageTk.PhotoImage(model_pixel_image)
    model_pixel_label = tk.Label(model_pixel_frame, image=model_pixel_image)
    model_pixel_label.image = model_pixel_image
    model_pixel_label.bind("<Button-1>", lambda event, page=modelPixel_page: switch_page(event, page))
    model_pixel_label.pack(pady=10,padx=20)

    # Frame untuk "Model Grid" (frame kanan)
    model_grid_frame = tk.Frame(daftar_model_frame, bg='white')
    model_grid_frame.pack(side=tk.RIGHT, padx=20, anchor='n')

    # Label untuk "Model Grid" (tombol gambar)
    model_grid_image = Image.open("modelGrid.png")  # Ganti dengan path gambar model grid
    model_grid_image = model_grid_image.resize((150, 150), Image.ANTIALIAS)
    model_grid_image = ImageTk.PhotoImage(model_grid_image)
    model_grid_label = tk.Label(model_grid_frame, image=model_grid_image)
    model_grid_label.image = model_grid_image
    model_grid_label.bind("<Button-1>", lambda event, page=modelGrid_page: switch_page(event, page))
    model_grid_label.pack(pady=10,padx=30)

    klasifikasi_frame.pack(pady=20, side=tk.RIGHT)  # Frame untuk elemen-elemen baru diletakkan di sebelah kanan

def modelGrid_page():
    # Frame atas (bagian kiri)
    atas_frame = tk.Frame(main_frame, bg='white')
    atas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Label "Daftar Sentinel" di atas kiri
    daftar_sentinel_label = tk.Label(atas_frame, text='Daftar Sentinel', font=('Helvetica', 16))
    daftar_sentinel_label.pack(side=tk.LEFT, padx=20, pady=10)

    # Frame atas (bagian kanan)
    dropdown_frame = tk.Frame(atas_frame, bg='white')
    dropdown_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Dropdown "Pilih Daerah"
    pilih_daerah_label = tk.Label(dropdown_frame, text='Pilih Daerah:', font=('Helvetica', 12))
    pilih_daerah_label.pack(pady=10)

    daerah_var = tk.StringVar()
    daerah_dropdown = ttk.Combobox(dropdown_frame, textvariable=daerah_var,
                                   values=['Jawa Barat', 'Jawa Timur', 'Jawa Tengah', 'Sumatera Barat', 'Sumatera Timur'])
    daerah_dropdown.pack(pady=5)

    # Dropdown "Pilih Tanggal"
    pilih_tanggal_label = tk.Label(dropdown_frame, text='Pilih Tanggal:', font=('Helvetica', 12))
    pilih_tanggal_label.pack(pady=10)

    tanggal_var = tk.StringVar()
    tanggal_dropdown = ttk.Combobox(dropdown_frame, textvariable=tanggal_var,
                                    values=['Tanggal 1', 'Tanggal 2', 'Tanggal 3', 'Tanggal 4', 'Tanggal 5'])
    tanggal_dropdown.pack(pady=5)

    # Tombol "Cari Sentinel"
    cari_sentinel_btn = tk.Button(dropdown_frame, text='Cari Sentinel', font=('Helvetica', 14), command=cari_sentinel)
    cari_sentinel_btn.pack(pady=10)

    # Frame bawah
    bawah_frame = tk.Frame(main_frame, bg='white')
    bawah_frame.pack(fill=tk.BOTH, expand=True)

    # Tabel daftar sentinel dengan 5 kolom
    tabel = ttk.Treeview(bawah_frame, columns=("No", "Nama Sentinel", "Nama Daerah", "Deskripsi", "Tanggal"))

    # Set the column headings
    tabel.heading("#1", text="No")
    tabel.heading("#2", text="Nama Sentinel")
    tabel.heading("#3", text="Nama Daerah")
    tabel.heading("#4", text="Deskripsi")
    tabel.heading("#5", text="Tanggal")

    # Define column widths
    tabel.column("#1", width=50)
    tabel.column("#2", width=150)
    tabel.column("#3", width=150)
    tabel.column("#4", width=200)
    tabel.column("#5", width=100)

    # Insert sample data (you can replace this with your data)
    for i in range(1, 11):
        tabel.insert("", "end", values=(i, f"Sentinel-{i}", f"Daerah-{i}", f"Deskripsi-{i}", f"Tanggal-{i}"))

    tabel.pack(fill=tk.BOTH, expand=True)
    
def modelPixel_page():
    # Frame atas (bagian kiri)
    atas_frame = tk.Frame(main_frame, bg='white')
    atas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Label "Daftar Sentinel" di atas kiri
    daftar_sentinel_label = tk.Label(atas_frame, text='Daftar Sentinel', font=('Helvetica', 16))
    daftar_sentinel_label.pack(side=tk.LEFT, padx=20, pady=10)

    # Frame atas (bagian kanan)
    dropdown_frame = tk.Frame(atas_frame, bg='white')
    dropdown_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Dropdown "Pilih Daerah"
    pilih_daerah_label = tk.Label(dropdown_frame, text='Pilih Daerah:', font=('Helvetica', 12))
    pilih_daerah_label.pack(pady=10)

    daerah_var = tk.StringVar()
    daerah_dropdown = ttk.Combobox(dropdown_frame, textvariable=daerah_var,
                                   values=['Jawa Barat', 'Jawa Timur', 'Jawa Tengah', 'Sumatera Barat', 'Sumatera Timur'])
    daerah_dropdown.pack(pady=5)

    # Dropdown "Pilih Tanggal"
    pilih_tanggal_label = tk.Label(dropdown_frame, text='Pilih Tanggal:', font=('Helvetica', 12))
    pilih_tanggal_label.pack(pady=10)

    tanggal_var = tk.StringVar()
    tanggal_dropdown = ttk.Combobox(dropdown_frame, textvariable=tanggal_var,
                                    values=['Tanggal 1', 'Tanggal 2', 'Tanggal 3', 'Tanggal 4', 'Tanggal 5'])
    tanggal_dropdown.pack(pady=5)

    # Tombol "Cari Sentinel"
    cari_sentinel_btn = tk.Button(dropdown_frame, text='Cari Sentinel', font=('Helvetica', 14), command=cari_sentinel)
    cari_sentinel_btn.pack(pady=10)

    # Frame bawah
    bawah_frame = tk.Frame(main_frame, bg='white')
    bawah_frame.pack(fill=tk.BOTH, expand=True)

    # Tabel daftar sentinel dengan 5 kolom
    tabel = ttk.Treeview(bawah_frame, columns=("No", "Nama Sentinel", "Nama Daerah", "Deskripsi", "Tanggal"))

    # Set the column headings
    tabel.heading("#1", text="No")
    tabel.heading("#2", text="Nama Sentinel")
    tabel.heading("#3", text="Nama Daerah")
    tabel.heading("#4", text="Deskripsi")
    tabel.heading("#5", text="Tanggal")

    # Define column widths
    tabel.column("#1", width=50)
    tabel.column("#2", width=150)
    tabel.column("#3", width=150)
    tabel.column("#4", width=200)
    tabel.column("#5", width=100)

    # Insert sample data (you can replace this with your data)
    for i in range(1, 11):
        tabel.insert("", "end", values=(i, f"Sentinel-{i}", f"Daerah-{i}", f"Deskripsi-{i}", f"Tanggal-{i}"))

    tabel.pack(fill=tk.BOTH, expand=True)

    
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


def cari_sentinel():
    # Fungsi yang akan dijalankan ketika tombol "Cari Sentinel" ditekan
    # Anda dapat menambahkan kode untuk mencari sentinel di sini
    pass

def switch_page(event, new_page):
    delete_pages()
    new_page()    

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
