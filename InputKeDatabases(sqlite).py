import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
# this program use sqlite
class Input_database(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.databases_conn()
		self.title("Input User Ke Database")
		self.geometry("500x600")
		self.config(bg='grey')
		self.membuatentry()
		self.button()
	def databases_conn(self):
		try:
			self.conn = sqlite3.connect('bismilah.db',timeout=1)
			self.c=self.conn.cursor()
			print("Opened database successfully");
			self.c.execute('''CREATE TABLE User
         	(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         	Username           TEXT    NOT NULL,
         	Password            TEXT     NOT NULL
         	);''')
			print ("Table created successfully");
		except:
			print("Your conection is failed")


	def membuatentry(self):
		self.username=tk.Entry(self,width=27,font=("Helvetica",15))
		self.labelusername=tk.Label(self,width=10,text="Username : ",bg="grey",font=("BatangChe",15))
		self.labelusername.grid(row=0,column=0,padx=(30,0),pady=(50,10))
		self.username.grid(row=0,column=1,padx=10,pady=(50,10))
		
		self.password=tk.Entry(self,width=27,font=("Helvetica",15),show="*")
		self.labelpassword=tk.Label(self,width=10,text="Password : ",bg="grey",font=("BatangChe",15))
		self.labelpassword.grid(row=1,column=0,padx=(30,0),pady=0)
		self.password.grid(row=1,column=1,padx=10,pady=0)
		self.password.bind('<Return>',self.login)

		self.username.focus_set()

	def button(self):
		self.login=tk.Button(text="Login",width=27,command=self.login)
		self.login.grid(row=3,column=1,pady=(30,0),padx=(105,0))

	def login(self,sementara="abc"):
		abc0=self.username.get()
		abc=hashlib.md5(self.password.get().encode()).hexdigest()
		self.username.delete(0,tk.END)
		self.password.delete(0,tk.END)
		self.username.focus_set()
		try:
			warning=self.c.execute(f"SELECT username FROM User WHERE username='{abc0}'").fetchall()
			if warning:
				messagebox.showwarning("Failed","{} Already".format(warning[0][0]))
				return
		except Exception as er:
			print(er)
		try:
			comand="INSERT INTO User (ID,Username,Password) VALUES ( null,'{}','{}')".format(abc0,abc)
			print(comand)
			self.c.execute(comand);
			self.conn.commit()
			messagebox.showinfo('Succes','Data Berhasil Ditambahkan')
		except Exception as err:
			print(err)

abc=Input_database()
abc.mainloop()
abc.conn.close()