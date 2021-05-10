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

xspeed = 5
yspeed = 5
xspeed2 = -5
yspeed2 = -5

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

class Boundary:
    def check_boundary(position, movement):
        current_x = position[0]
        current_y = position[1]
        if movement == "left":
            if current_x <= 0:
                can_move = False
            else:
                can_move = True
        if movement == "right":
            if current_x >= 800:
                can_move = False
            else:
                can_move = True
        if movement == "up":
            if current_y <= 0:
                can_move = False
            else:
                can_move = True
        if movement == "down":
            if current_y >= 520:
                can_move = False
            else:
                can_move = True
        return can_move

class Images:
    def choose_character():
        characters = ['blue_tux.png', 'sleep_tux.png', 'tux.png']
        choosen_tux = random.choice(characters)
        characters.remove(choosen_tux)
        r_tux = random.choice(characters)
        characters.remove(r_tux)
        l_tux = random.choice(characters)
        print(choosen_tux)
        print(l_tux)
        print(r_tux)
        print("---------------------------------")
        choosen = Image.open('static/game/'+choosen_tux)
        image1 = choosen.resize((100,80), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(image1)

        right_tux = Image.open('static/game/'+r_tux)
        image2 = right_tux.resize((100,80), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(image2)

        left_tux = Image.open('static/game/'+l_tux)
        image3 = left_tux.resize((100,80), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(image3)

        if choosen_tux == 'sleep_tux.png':
            background_canvas = 'pink'
        elif choosen_tux == 'tux.png':
            background_canvas = 'steelblue'
        else:
            background_canvas = 'green'

        return img1, img2, img3, background_canvas

    def laptop():
        laptopic = Image.open('static/game/laptop.png')
        laptopic = laptopic.resize((100,80), Image.ANTIALIAS)
        laptop = ImageTk.PhotoImage(laptopic)
        return laptop
    
    def bed():
        bedpic = Image.open('static/game/bed.png')
        bedpic = bedpic.resize((100,80), Image.ANTIALIAS)
        bed = ImageTk.PhotoImage(bedpic)
        return bed
    
    def food():
        food2pic = Image.open('static/game/food2.png')
        food2pic = food2pic.resize((100,80), Image.ANTIALIAS)
        food = ImageTk.PhotoImage(food2pic)
        return food

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
        choosen_tux, l_tux, r_tux, background_canvass = Images.choose_character()
        
        my_canvas.config(bg=background_canvass)
        my_character = my_canvas.create_image(x,y, anchor=NW, image=choosen_tux)
        righthand_tux = my_canvas.create_image(x,y, anchor=NW, image=r_tux)
        lefthand_tux = my_canvas.create_image(x,y, anchor=NW, image=l_tux)

        #display laptop image
        laptop = Images.laptop()
        my_laptop = my_canvas.create_image(0,520, anchor=NW, image=laptop)
        #displaying bed image
        bed = Images.bed()
        my_bed = my_canvas.create_image(800,0, anchor=NW, image=bed)
        #displaying food image
        food = Images.food()
        print(food)
        my_food = my_canvas.create_image(800,520, anchor=NW, image=food)

        #on-press movements on keybindings
        def left(event):
            pos=my_canvas.coords(my_character)
            x = -10
            y = 0
            can_move = Boundary.check_boundary(pos, 'left')
            print(can_move)
            if can_move:
                my_canvas.move(my_character, x, y)
        
        def right(event):
            pos=my_canvas.coords(my_character)
            x = +10
            y = 0
            can_move = Boundary.check_boundary(pos, 'right')
            print(can_move)
            if can_move:
                my_canvas.move(my_character, x, y)
        
        def up(event):
            pos=my_canvas.coords(my_character)
            x = 0
            y = -10
            can_move = Boundary.check_boundary(pos, 'up')
            print(can_move)
            if can_move:
                my_canvas.move(my_character, x, y)
        
        def down(event):
            pos=my_canvas.coords(my_character)
            x = 0
            y = +10
            can_move = Boundary.check_boundary(pos, 'down')
            print(can_move)
            if can_move:
                my_canvas.move(my_character, x, y)


        def auto_move_right_tux():
            global xspeed, yspeed
            my_canvas.move(righthand_tux, xspeed, yspeed)
            current_x, current_y = my_canvas.coords(righthand_tux)
            if current_x <= 0 or current_x >= (w-100):
                xspeed = -xspeed
            if current_y <= 0 or current_y >= (h-80):
                yspeed = -yspeed
            my_canvas.after(30, auto_move_right_tux)

        my_canvas.after(30, auto_move_right_tux)

        def auto_move_left_tux():
            global xspeed2, yspeed2
            my_canvas.move(lefthand_tux, xspeed2, yspeed2)
            current_x, current_y = my_canvas.coords(lefthand_tux)
            if current_x <= 0 or current_x >= (w-100):
                xspeed2 = -xspeed2
            if current_y <= 0 or current_y >= (h-80):
                yspeed2 = -yspeed2
            my_canvas.after(30, auto_move_left_tux)

        my_canvas.after(30, auto_move_left_tux)

        #keyboard bindings
        def pressing(event):
            #if Q is press exit
            if event.char == "q" or event.char == "Q":
                main_win.destroy()
                print("exit")
        main_win.bind("<Key>", pressing)

        #arrow key bindings
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