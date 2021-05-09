import tkinter
from tkinter import *
import tkinter.messagebox as box
import random
import time
import tkinter as tk
import tkinter.scrolledtext as st
import os
from tapayta import run_old
from PIL import ImageTk,Image
from time import sleep
import threading
import random

class Spawn_mini_window:
    def wrong_credentials():
        mini_win = Toplevel()
        mini_win.title("Message Window")
        mini_win.geometry("294x100")
        mini_win.config(bg='black')
        Label(mini_win,text="Wrong Username or Password",font=("arial",10,"bold") , fg="red", bg='black').place(x=5,y=30)

    def empty_fields():
        mini_win = Toplevel()
        mini_win.title("Message Window")
        mini_win.geometry("294x100")
        mini_win.config(bg='black')
        Label(mini_win,text="username and password are empty",font=("arial",10,"bold") , fg="orange", bg='black').place(x=5,y=30)

class Loading:
    def __init__(self):
        self.animated_win = tk.Tk()
        self.animated_win.title("Custom Loader")
        self.animated_win.config(bg='black')
        self.animated_win.attributes("-fullscreen", True)

        #loading text
        Label(self.animated_win, text="Loading...", font="Bahnschrift 15", bg='black', fg="#FFBD09").place(x=490, y=320)
        #loading blocks
        for i in range(16):
            Label(self.animated_win, bg="#1F2732", width=2, height=1).place(x=(i+22)*22, y=350)

        #update animation
        self.animated_win.update()
        self.play_animation()
        
        #window in main loop
        # self.animated_win.after(10000, self.animated_win.destroy)
        self.animated_win.mainloop()

    def play_animation(self):
        for i in range(1):
            for j in range(16):
                #makeblock yellow
                Label(self.animated_win, bg="#FFBD09", width=2, height=1).place(x=(j+22)*22, y=350)
                sleep(0.06)
                self.animated_win.update_idletasks()
                #make block dark
                Label(self.animated_win, bg="#1F2732", width=2, height=1).place(x=(j+22)*22, y=350)
        else:
            self.animated_win.destroy()
            MainWindow.play_game()

class  AboutTux:
    def display_info():
        tux_win = Toplevel()
        tux_win.title("Tux Window")
        tux_win.geometry("900x600")
        tux_win.config(bg='grey')
        
        canvass = Canvas(tux_win, width=900, height=70, bg="black")
        canvass.create_text(250, 10, fill="green", font="Arial 24 bold", text="\n\tA Complete History of Tux.")
        canvass.pack(pady=5)

        scrText =  st.ScrolledText(tux_win, width=125, height=30, font=("Arial", 11), bg="black", fg="green")
        scrText.pack(padx=10)
        tux_file = open('tux.txt').readlines()
        tux_text = ""
        for line in tux_file:
            tux_text += line
        scrText.insert('insert',tux_text)
        scrText.config(state=DISABLED)


class MainWindow:
    def play_game():
        def go_to_text():
            AboutTux.display_info()
        
        def go_to_forms():
            run_old()
        
        def go_exit():
            main_win.destroy()

        main_win = Toplevel()
        main_win.title("Main Window")
        # main_win.attributes("-fullscreen", True)
        main_win.geometry("1000x800")
        main_win.config(bg='grey')

        canvass = Canvas(main_win, width=900, height=100, bg="black")
        canvass.create_text(250, 50, fill="green", font="Arial 8 bold", text="\t\tWelcome to my Room\n\nHello there! I am TUX. Please use the arrow keys for controls. Please Help me do the cycle.\neat();\ncode();\nrepeat();\nOh! I forgot sleep();")
        canvass.pack(pady=5)

        exit_pic = PhotoImage(file='static/src/exit.png')
        forms_pic = PhotoImage(file='static/src/forms.png')
        text_pic = PhotoImage(file='static/src/text.png')

        btn_frame = Frame(main_win)
        btn_frame.config(bg="grey",width=900, height=40)

        btn1 = Button(
        btn_frame,
        image=text_pic,
        borderwidth = 0,
        command=go_to_text,
        bg="grey"
        ).place(x=0,y=0)

        btn2 = Button(
        btn_frame,
        image=forms_pic,
        borderwidth = 0,
        command=go_to_forms,
        bg="grey"
        ).place(x=400,y=0)

        btn3 = Button(
        btn_frame,
        image=exit_pic,
        borderwidth = 0,
        command=go_exit,
        bg="grey"
        ).place(x=800,y=0)

        btn_frame.pack()


        w=900
        h=600
        x = w//2
        y = h//2
        
        my_canvas = Canvas(main_win, width=w, height=h, bg="black")
        my_canvas.pack(pady=0)

        #add image
        characters = ['blue_tux.png', 'sleep_tux.png', 'tux.png']
        choosen_tux = random.choice(characters)
        if choosen_tux == 'sleep_tux.png':
            my_canvas.config(bg="pink")
        elif choosen_tux == 'tux.png':
            my_canvas.config(bg="steelblue")

        image = Image.open('static/game/'+choosen_tux)
        image = image.resize((100,80), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        my_character = my_canvas.create_image(x,y, anchor=NW, image=img)

        laptopic = Image.open('static/game/laptop.png')
        laptopic = laptopic.resize((100,80), Image.ANTIALIAS)
        laptop = ImageTk.PhotoImage(laptopic)
        my_laptop = my_canvas.create_image(0,520, anchor=NW, image=laptop)

        bedpic = Image.open('static/game/bed.png')
        bedpic = bedpic.resize((100,80), Image.ANTIALIAS)
        bed = ImageTk.PhotoImage(bedpic)
        my_bed = my_canvas.create_image(800,0, anchor=NW, image=bed)

        food2pic = Image.open('static/game/food2.png')
        food2pic = food2pic.resize((100,80), Image.ANTIALIAS)
        food = ImageTk.PhotoImage(food2pic)
        my_food = my_canvas.create_image(800,520, anchor=NW, image=food)

        def left(event):
            pos=my_canvas.coords(my_character)
            print(pos)
            x = -10
            y = 0
            if pos[0] <= 0:
                pass
            else:
                my_canvas.move(my_character, x, y)
        
        def right(event):
            pos=my_canvas.coords(my_character)
            print(pos)
            x = +10
            y = 0
            if pos[0] >= (w-100):
                pass
            else:
                my_canvas.move(my_character, x, y)
        
        def up(event):
            pos=my_canvas.coords(my_character)
            print(pos)
            x = 0
            y = -10
            if pos[1] <= 0:
                pass
            else:
                my_canvas.move(my_character, x, y)
        
        def down(event):
            pos=my_canvas.coords(my_character)
            print(pos)
            x = 0
            y = +10
            if pos[1] >= (h-80):
                pass
            else:
                my_canvas.move(my_character, x, y)

        #keyboard bindings
        def pressing(event):
            #if Q is press exit
            if event.char == "q" or event.char == "Q":
                main_win.destroy()
                print("exit")

        #limiter
        pos = my_canvas.coords(my_character, x, y)
        print(pos)

        #WASD
        main_win.bind("<Key>", pressing)

        #arrow keys
        main_win.bind("<Left>", left)
        main_win.bind("<Right>", right)
        main_win.bind("<Up>", up)
        main_win.bind("<Down>", down)

        main_win.mainloop()


class FirstPage:
    def login_page(self):
        window = Tk()
        window.title("Welcome!")
        window.geometry("500x500")
        canvass = Canvas(window, width=500, height=100, bg="steelblue")
        canvass.create_text(250, 50, fill="white", font="Arial 35 bold", text="Login")
        canvass.pack()

        def dialog1():
            username=entry1.get()
            password=entry2.get()
            if username == "admin" and password == "admin":
                Loading()
            elif username == "" and password == "":
                Spawn_mini_window.empty_fields()
            elif username != "admin" or password != "admin":
                Spawn_mini_window.wrong_credentials()

        def onClick():
            tkinter.messagebox.showinfo("Credentials",  "Username: admin \nPassword: admin")

        def popup(e):
            try:
                my_menu.tk_popup(e.x_root, e.y_root)

            finally:
                my_menu.grab_release()

        my_menu = Menu(window, tearoff = 0)
        my_menu.add_command(label= "Show credentials", command = onClick)
        my_menu.add_separator()
        my_menu.add_command(label= "Exit", command =window.quit)

        #creation of first page start
        frame = Frame(window)

        Label1 = Label(window,text = 'Username:')
        Label1.pack(padx=15,pady= 5)

        entry1 = Entry(window,bd =5, width=35, font =('Helvetica', 15))
        entry1.pack(padx=15, pady=5)

        Label2 = Label(window,text = 'Password: ')
        Label2.pack(padx = 15,pady=6)

        entry2 = Entry(window, bd=5, width=35, font =('Helvetica', 15), show = "*")
        entry2.pack(padx = 15,pady=7)

        login_btn = PhotoImage(file='static/src/login.png')

        btn = Button(
            frame,
            image=login_btn,
            borderwidth = 0,
            command = dialog1
            )

        btn.pack(side = RIGHT , padx =5)
        frame.pack(padx=100,pady = 19)
        canvass2 = Canvas(window, width=500, height=100, bg="white")
        canvass2.create_text(250,35,fill="orange", font="helvetica 15 bold", text="Right Click here to\n show options")
        canvass2.pack()
        canvass2.bind("<Button-3>", popup)
        window.mainloop()

main_page = FirstPage()
main_page.login_page()