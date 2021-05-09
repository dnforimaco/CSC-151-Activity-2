from tkinter import *
import sqlite3

class Student (object):

    def __init__(self, firstName,middleInit, lastName, idNum, Course):
        self.fname=firstName
        self.mi=middleInit
        self.lname=lastName
        self.idnum=idNum
        self.course=Course


def run_old():
	def open_db():
		def go_to_update():
			def update_dis():
				def update_thing():
					def updated_f():
						ch_f = str(chain.get())
						conn.execute("UPDATE studentRecord set FirstName = ? WHERE ID = ?", (ch_f,find))
						conn.commit()
						display()
					def updated_l():
						ch_f = str(chain.get())
						conn.execute("UPDATE studentRecord set LastName = ? WHERE ID = ?", (ch_f,find))
						conn.commit()
						display()
					def updated_m():
						ch_f = str(chain.get())
						conn.execute("UPDATE studentRecord set MiddleInitial = ? WHERE ID = ?", (ch_f,find))
						conn.commit()
						display()
					def updated_c():
						ch_f = str(chain.get())
						conn.execute("UPDATE studentRecord set Course = ? WHERE ID = ?", (ch_f,find))
						conn.commit()
						display()


					d_choice = str(choice.get())
					choices = Label(upd_win,text="you are currently updating "+d_choice,font=("arial",10,"bold") , fg="steelblue").place(x=5,y=70)
					if d_choice == 'First Name':
						chain = StringVar(None)
						changes_f = Entry(upd_win,textvariable = chain, width = 34,bg="pink")
						changes_f.place(x=5,y=145)
						ch_but = Button(upd_win,text="CHANGE",width=10, height=1,command= updated_f).place(x=215,y=142)
					elif d_choice == 'Last Name':
						chain = StringVar(None)
						changes_f = Entry(upd_win,textvariable = chain, width = 34,bg="pink")
						changes_f.place(x=5,y=145)
						ch_but = Button(upd_win,text="CHANGE",width=10, height=1,command= updated_l).place(x=215,y=142)
					elif d_choice == 'Middle Initial':
						chain = StringVar(None)
						changes_f = Entry(upd_win,textvariable = chain, width = 34,bg="pink")
						changes_f.place(x=5,y=145)
						ch_but = Button(upd_win,text="CHANGE",width=10, height=1,command= updated_m).place(x=215,y=142)
					elif d_choice == 'Course':
						chain = StringVar(None)
						changes_f = Entry(upd_win,textvariable = chain, width = 34,bg="pink")
						changes_f.place(x=5,y=145)
						ch_but = Button(upd_win,text="CHANGE",width=10, height=1,command= updated_c).place(x=215,y=142)


				find = str(sID_num.get())
				quer.execute("SELECT * FROM studentRecord WHERE ID = ?", (find,))
				for row in quer.fetchall():
					Disp = Label(upd_win,text = row, font="arial 9 bold").place(x=5,y=30)
				choice_lab = Label(upd_win,text = "what do you want to update?").place(x=5,y=50)

				
				options = [
					'First Name',
					'Last Name',
					'Middle Initial',
					'Course'
				]
				choice = StringVar(None)
				choice.set( "First Name" )
				drop = OptionMenu( upd_win , choice , *options ).place(x=5,y=97)
				upd_choice = Button(upd_win,text = "Enter",width=10, height=1,command= update_thing).place(x=215,y=97)

			upd_win = Toplevel()
			upd_win.title("Update Window")
			upd_win.geometry("299x180")
			ID_label = Label(upd_win,text="Search ID: ").place(x=3,y=5)
			sID_num = StringVar(None)
			sID_box= Entry(upd_win,textvariable=sID_num,width=25,bg="pink")
			sID_box.place(x=60,y=5)
			upd_but = Button(upd_win,text="Search",width=10, height=1,command= update_dis).place(x=215,y=3)




		db_name = str(entry_box.get())+'.db'
		conn = sqlite3.connect(db_name)
		quer = conn.cursor()
		quer.execute('''
		CREATE TABLE IF NOT EXISTS studentRecord(
			FirstName CHAR(20) NOT NULL,
			MiddleInitial CHAR(20) NOT NULL,
			LastName CHAR(20) NOT NULL,
			ID CHAR(20) NOT NULL UNIQUE,
			Course CHAR(20) NOT NULL
		)''')
		conn.commit()
		print(db_name + " successfily created")

		def go_to_add():

			def adding():
				def goto_error_window(error):
					error_window=Toplevel()
					error_window.title("Adding Window")
					error_window.geometry("330x50")
					Label(error_window,text=error,font=("arial",10,"bold") , fg="red").place(x=5,y=25)

				st_ID = str(ID_num.get())
				st_lname = str(lname.get())
				st_mi = str(mi.get())
				st_fname = str(fname.get())
				st_course = str(Crs.get())
				
				quer.execute('SELECT * FROM studentRecord WHERE ID="'+st_ID+'"')
				exist = quer.fetchone()
				if exist:
					error_message = exist[0]+" "+exist[2]+" already exists."
					goto_error_window(error_message)

				elif st_ID == '' or st_lname == '' or st_mi == '' or st_fname == '' or st_course == '':
					error_message = "Info fields should not be empty"
					goto_error_window(error_message)

				else:
					try:
						stud = Student(st_fname,st_mi,st_lname,st_ID,st_course)
						quer.execute("INSERT INTO studentRecord (FirstName, MiddleInitial, LastName, ID, Course) VALUES (?,?,?,?,?)",
						(stud.fname,stud.mi, stud.lname,stud.idnum,stud.course))
						conn.commit()


						ID_box.delete(0, END)
						fname_box.delete(0, END)
						mi_box.delete(0, END)
						lname_box.delete(0, END)
						course_box.delete(0, END)
						display()
					except:
						error_message = "Error: Failed to Insert Record"
						goto_error_window(error_message)



			new_win=Toplevel()
			new_win.title("Adding Window")
			new_win.geometry("330x105")

			ID_label= Label(new_win,text="ID num: ").place(x=3,y=5)
			fname_label= Label(new_win,text="First Name: ").place(x=3,y=25)
			mi_label= Label(new_win,text="Middle Initial: ").place(x=3,y=45)
			lname_label= Label(new_win,text="Last Name: ").place(x=3,y=65)
			course_label= Label(new_win,text="Course: ").place(x=3,y=85)

			ID_num = StringVar(None)
			ID_box= Entry(new_win,textvariable=ID_num,width=25,bg="pink")
			ID_box.place(x=90,y=5)
			fname = StringVar(None)
			fname_box= Entry(new_win,textvariable=fname,width=25,bg="pink")
			fname_box.place(x=90,y=25)
			mi= StringVar(None)
			mi_box= Entry(new_win,textvariable=mi,width=25,bg="pink")
			mi_box.place(x=90,y=45)
			lname = StringVar(None)
			lname_box= Entry(new_win,textvariable=lname,width=25,bg="pink")
			lname_box.place(x=90,y=65)
			Crs = StringVar(None)
			course_box= Entry(new_win,textvariable=Crs,width=25,bg="pink")
			course_box.place(x=90,y=85)

			add_but = Button(new_win,text="Add",width=10, height=1,command=adding).place(x=245,y=80)



		def display():
			db_name = str(entry_box.get()) + '.db'
			op_db = open(db_name,'r')
			box_all = Listbox(root,width=57, height=15,bg="lightblue")
			quer.execute('SELECT * FROM studentRecord')
			for row in quer.fetchall():

				sep0 = "   "
				# print (sep0)
				box_all.insert(END, row[3]+sep0+row[2] + sep0 +row[0]+sep0+row[1]+sep0+row[4])
				# print (row)

			box_all.place(x=9,y=200)
			op_db.close()
		display()

		def go_to_delete():
			def deletion():
				def erase():
					find = str(ID_num.get())
					quer.execute("DELETE FROM studentRecord WHERE ID = ? ", (find,))
					conn.commit()
					display()
				def exit():
					del_win.destroy()

				quer.execute('SELECT * FROM studentRecord WHERE ID="'+str(ID_num.get())+'"')
				exist = quer.fetchone()
				to_delete = "No record match to this ID."
				if exist != None:
					to_delete = exist[0]+" "+exist[2]
				Label(del_win,text=to_delete,font=("arial",10,"bold") , fg="red").place(x=5,y=30)
				Label(del_win,text="are you sure?",font=("arial",10,"bold") , fg="steelblue").place(x=5,y=50)
				yes = Button(del_win,text="Yes",width=10, height=1,command= erase).place(x=5,y=70)
				no = Button(del_win,text="No",width=10, height=1,command= exit).place(x=207,y=70)

			del_win = Toplevel()
			del_win.title("Delete Window")
			del_win.geometry("294x100")
			ID_label = Label(del_win,text="ID num: ").place(x=3,y=5)
			ID_num = StringVar(None)
			ID_box= Entry(del_win,textvariable=ID_num,width=25,bg="pink")
			ID_box.place(x=50,y=5)
			del_but = Button(del_win,text="Delete",width=10, height=1,command= deletion).place(x=207,y=3)

		def go_to_sort():
			quer.execute("SELECT * FROM studentRecord ORDER BY ID ASC")
			conn.commit()


		add = Button(root,text="Add",width=15, height=2,command=go_to_add).place(x=5,y=155)
		delete = Button(root,text="Delete",width=15, height=2,command=go_to_delete).place(x= 125,y=155)
		update = Button(root,text="Update",width=15, height=2,command=go_to_update).place(x=245,y=155)
		#sort = Button(root,text="Sort",width=15, height=2,command=go_to_sort).place(x=125,y=445)


	root = Tk()
	root.title("Second GUI")
	root.geometry("365x450+0+0")
	heading = Label(root, text="Mini Record",bg="pink",font=("arial",35,"bold") , fg="steelblue").pack(fill=X)
	file_naming= Label(root,text="Database Name: ").place(x=10,y=110)

	entry_box = Entry(root,width=25, bg="lightblue")
	entry_box.pack(padx = 15,pady=50)
	print(entry_box.get())
	work = Button(root,text="Enter",width=10, height=1,command=open_db).place(x=270, y=105)

	root.mainloop()
