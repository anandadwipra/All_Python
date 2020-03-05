import tkinter as tk
import sqlite3
from tkinter import messagebox
# this program use sqlite
class form_login(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.databases_conn()
		self.title("Form Login Sederhana")
		self.geometry("500x600+120+120")
		self.config(bg="grey")
		#membuat frame
		self.window1=tk.Frame(self,bg="grey",width=500, height=600)
		self.window1.pack(fill="both", expand=True)
		self.membuatentry()
		self.button()
	def databases_conn(self):
		try: 
			self.conn = sqlite3.connect('testing.db')
			self.c=self.conn.cursor()
			print("Opened database successfully");
			self.c.execute('''CREATE TABLE User
         	(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         	Username           TEXT    NOT NULL,
         	Password            TEXT     NOT NULL
         	);''')
			print ("Table created successfully");  
		except Exception as e:
			print(e)


	def membuatentry(self):
		self.labelutama=tk.Label(self.window1,text="Silakan Login ",bg="grey",font=("helvetica",30)).place(x=130,y=10)
		self.username=tk.Entry(self.window1,width=27,font=("Helvetica",15))
		self.labelusername=tk.Label(self.window1,width=10,text="Username : ",bg="grey",font=("BatangChe",15))
		self.labelusername.grid(row=0,column=0,padx=(30,0),pady=(90,10))
		self.username.grid(row=0,column=1,padx=10,pady=(90,10))
		
		self.password=tk.Entry(self.window1,width=27,font=("Helvetica",15),show="*")
		self.labelpassword=tk.Label(self.window1,width=10,text="Password : ",bg="grey",font=("BatangChe",15))
		self.labelpassword.grid(row=1,column=0,padx=(30,0),pady=0)
		self.password.grid(row=1,column=1,padx=10,pady=0)
		self.password.bind("<Return>",self.login)

		self.username.focus_set()

	def button(self):
		self.login=tk.Button(self.window1,text="Login",width=27,command=self.login)
		self.login.grid(row=3,column=1,pady=(30,0),padx=(105,0))

	def login(self,sementara=False):
		abc0=self.username.get()
		abc=self.password.get()
		self.username.delete(0,tk.END)
		self.password.delete(0,tk.END)
		self.username.focus_set()
		try:
			warning=self.c.execute(f"SELECT Username FROM User WHERE Username='{abc0}'").fetchall()
			if not warning:
				messagebox.showwarning("Failed","{} Tidak ada harap daftar terlebih dahulu".format(warning[0][0]))
				return
		except Exception as e:
			print(e)
		try:
			login=self.c.execute(f"SELECT * FROM User WHERE Username='{abc0}'").fetchall()[0]
			if login[1]==abc0 and login[2]==abc:
				messagebox.showinfo("Berhasil","Selamat anda berhasil Login ")
				self.window1.destroy()
				tk.Label(self,text="Selamat Anda Berhasil Login !!!",font=("helvetica",20),bg="grey").place(x=65,y=230)
			else:
				messagebox.showerror("Gagal","Username atau Password tidak valid")
		except Exception as e:
			print(f"Failed{e}")

abc=form_login()
abc.mainloop()
abc.conn.close()