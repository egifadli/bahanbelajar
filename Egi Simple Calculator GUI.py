# Egi Calculator GUI (Simple)
# By : Egi Fadli Soerachman
# Youtube Channel : Egi Fadli Soerachman

import tkinter

nilai = ''
def tekan(nomer):
    global nilai
    nilai += str(nomer)
    persamaan.set(nilai)

def clear():
    global nilai
    nilai = ''
    persamaan.set('')

def funsamadeng():
    try:
        global nilai
        total = str(eval(nilai))
        persamaan.set(total)
        nilai = total
    except:
        persamaan.set('Error')
        nilai = ''

jendela = tkinter.Tk() #Object 
jendela.wm_iconbitmap('Logo Egi.ico') #icon
jendela.title('Egi Calculator GUI') #untuk judul aplikasi
jendela.geometry('400x250') #350 untuk panjang, 250 untuk tinggi
persamaan = tkinter.StringVar()
kotakangka = tkinter.Entry(jendela, textvariable=persamaan)
kotakangka.grid(columnspan=5, ipadx=70)
persamaan.set('Silahkan digunakan')

tombol1 = tkinter.Button(jendela, text='1', bg='deep sky blue', command=lambda: tekan(1), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol1.grid(row=2, column=0) # tombol angka 1

tombol2 = tkinter.Button(jendela, text='2', bg='deep sky blue', command=lambda: tekan(2), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol2.grid(row=2, column=1) # tombol angka 2

tombol3 = tkinter.Button(jendela, text='3', bg='deep sky blue', command=lambda: tekan(3), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol3.grid(row=2, column=2) # tombol angka 3

tombol4 = tkinter.Button(jendela, text='4', bg='deep sky blue', command=lambda: tekan(4), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol4.grid(row=3, column=0) # tombol angka 4

tombol5 = tkinter.Button(jendela, text='5', bg='deep sky blue', command=lambda: tekan(5), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol5.grid(row=3, column=1) # tombol angka 5

tombol6 = tkinter.Button(jendela, text='6', bg='deep sky blue', command=lambda: tekan(6), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol6.grid(row=3, column=2) # tombol angka 6

tombol7 = tkinter.Button(jendela, text='7', bg='deep sky blue', command=lambda: tekan(7), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol7.grid(row=4, column=0) # tombol angka 7

tombol8 = tkinter.Button(jendela, text='8', bg='deep sky blue', command=lambda: tekan(8), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol8.grid(row=4, column=1) # tombol angka 8

tombol9 = tkinter.Button(jendela, text='9', bg='deep sky blue', command=lambda: tekan(9), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol9.grid(row=4, column=2) # tombol angka 9

tombol0 = tkinter.Button(jendela, text='0', bg='deep sky blue', command=lambda: tekan(0), height=1, width=7) #berfungsi untuk mengetik angka 1
tombol0.grid(row=5, column=0) # tombol angka 9

tambah = tkinter.Button(jendela, text='+', bg='deep sky blue', command=lambda: tekan('+'), height=1, width=7) #berfungsi untuk mengetik angka 1
tambah.grid(row=2, column=3) # tombol tambah

kurang = tkinter.Button(jendela, text='-', bg='deep sky blue', command=lambda: tekan('-'), height=1, width=7) #berfungsi untuk mengetik angka 1
kurang.grid(row=3, column=3) # tombol kurang

kali = tkinter.Button(jendela, text='*', bg='deep sky blue', command=lambda: tekan('*'), height=1, width=7) #berfungsi untuk mengetik angka 1
kali.grid(row=4, column=3) # tombol kali

bagi = tkinter.Button(jendela, text='/', bg='deep sky blue', command=lambda: tekan('/'), height=1, width=7) #berfungsi untuk mengetik angka 1
bagi.grid(row=5, column=3) # tombol bagi

clear = tkinter.Button(jendela, text='clear', bg='deep sky blue', command=clear, height=1, width=7) #berfungsi untuk mengetik angka 1
clear.grid(row=5, column=1) # tombol clear

samadengan = tkinter.Button(jendela, text='=', bg='deep sky blue', command=funsamadeng, height=1, width=7) #berfungsi untuk mengetik angka 1
samadengan.grid(row=5, column=2) # tombol sama dengan

jendela.mainloop() #Untuk menampilkan object GUI




















"""
if __name__ == '__main__':
    jendela = tkinter.Tk() #Object 
    jendela.wm_iconbitmap('Logo Egi.ico') #icon
    jendela.title('Egi Calculator GUI') #untuk judul aplikasi
    jendela.geometry('400x250') #350 untuk panjang, 250 untuk tinggi
    persamaan = tkinter.StringVar()
    ekspresi = tkinter.Entry(jendela, textvariable=persamaan)
    ekspresi.grid(columnspan=4, ipadx=70)
    persamaan.set('Silahkan digunakan')
    button1 = tkinter.Button(jendela, text='1', bg='deep sky blue', command=lambda: tekan(1), heigh='1', width='7')
    button1.grid(row=2, column=0)
    button2 = tkinter.Button(jendela, text='2', bg='deep sky blue', command=lambda: tekan(2), heigh='1', width='7')
    button2.grid(row=2, column=1)
    button3 = tkinter.Button(jendela, text='3', bg='deep sky blue', command=lambda: tekan(3), heigh='1', width='7')
    button3.grid(row=2, column=2)
    button4 = tkinter.Button(jendela, text='4', bg='deep sky blue', command=lambda: tekan(4), heigh='1', width='7')
    button4.grid(row=3, column=0)
    button5 = tkinter.Button(jendela, text='5', bg='deep sky blue', command=lambda: tekan(5), heigh='1', width='7')
    button5.grid(row=3, column=1)
    button6 = tkinter.Button(jendela, text='6', bg='deep sky blue', command=lambda: tekan(6), heigh='1', width='7')
    button6.grid(row=3, column=2)
    button7 = tkinter.Button(jendela, text='7', bg='deep sky blue', command=lambda: tekan(7), heigh='1', width='7')
    button7.grid(row=4, column=0)
    button8 = tkinter.Button(jendela, text='8', bg='deep sky blue', command=lambda: tekan(8), heigh='1', width='7')
    button8.grid(row=4, column=1)
    button9 = tkinter.Button(jendela, text='9', bg='deep sky blue', command=lambda: tekan(9), heigh='1', width='7')
    button9.grid(row=4, column=2)
    jendela.mainloop() #Untuk menampilkan object GUI
"""