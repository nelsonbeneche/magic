import random
import tkinter
import sqlite3
import customtkinter
from PIL import Image, ImageTk
import tkinter.ttk


class Magic8:
    def __init__(self):
        root = customtkinter.CTk()
        customtkinter.set_appearance_mode('Dark')
        customtkinter.set_default_color_theme('dark-blue')
        root.title('Magic8_Ball')  # titre de la fenetre
        # definir la hauteur et la largeur
        large = 500
        haut = 500
        largecran = root.winfo_screenwidth()
        hautecran = root.winfo_screenheight()
        x = (largecran/2)-(large/2)
        y = (hautecran/2)-(haut/2)
        root.geometry('%dx%d+%d+%d' % (large, haut, x, y))
        # definir une image
        magic_img = Image.open('Magic8ball.jpg')
        magicimage = ImageTk.PhotoImage(magic_img.resize((120, 120)))
        labelimag = tkinter.Label(root, image=magicimage, bd=0)
        labelimag.pack(pady=5)
        # configurer le resultat
        resultat = tkinter.Label(root, bg="#1a1a1a", text="cliquer sur le bouton Shake 8-ball", font=('Helvetica', 28), fg='white')
        resultat.pack(pady=30)
        # resultat.grid(colum)

        def shake():
            reponses = {'It is a certain': 'green',
                        'It is a decidedly so': 'aqua',
                        'without and doubt': 'red'}
            rep = list(reponses.items())
            random.shuffle(rep)
            resultat.config(text=rep[0][0], fg=rep[0][1])
            # tkinter.Message
        # creation de bouton
        bouton_ = customtkinter.CTkButton(root, text='Shake 8-Ball', width=190, height=40, compound='top', command=lambda: shake())
        bouton_.pack(pady=5)
        # creation de menu
        mainmenu = tkinter.Menu(root)
        menu1 = tkinter.Menu(mainmenu, tearoff=0)
        menu2 = tkinter.Menu(mainmenu, tearoff=0)
        menu1.add_command(label='Ouvrir', command='')
        mainmenu.add_cascade(label='Fichier', menu=menu1)
        # mainmenu.winfo_colormapfull('red')
        root.config(menu=mainmenu)
        progressbar = customtkinter.CTkProgressBar(master=root, width=160, height=20, border_width=5)
        progressbar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        progressbar.set(100)
        progres = tkinter.ttk.Progressbar(root, cursor='hand2', orient='vertical',   length=200, mode ='determinate')
        # progressbar.start('')
        progres.start(100)
        progres.pack()
        root.state('zoomed')
        root.mainloop()
        # list(orderdict)
        # def shak(s/)


if __name__ == '__main__':
    Magic8()


