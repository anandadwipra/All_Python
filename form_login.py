import tkinter as tk
import sqlite3
import hashlib
# this program use sqlite
class form_login(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.databases_conn()
		self.title("Form Login Sederhana")
		self.geometry("500x600")
		self.config(bg='grey')
		self.membuatentry()
		self.button()
	def databases_conn(self):
		try:
			self.conn = sqlite3.connect('testing.db')
			print("Opened database successfully");
			self.conn.execute('''CREATE TABLE User
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

		self.username.focus_set()

	def button(self):
		self.login=tk.Button(text="Login",width=27,command=self.login)
		self.login.grid(row=3,column=1,pady=(30,0),padx=(105,0))

	def login(self):
		abc0=self.username.get()
		abc=hashlib.md5(self.password.get().encode()).hexdigest()
		self.username.delete(0,tk.END)
		self.password.delete(0,tk.END)
		self.username.focus_set()
		try:
			comand="INSERT INTO User (ID,Username,Password) VALUES ( null,'{}','{}')".format(abc0,abc)
			self.conn.execute(comand);
			self.conn.commit()
			print("Succes")
		except:
			print("Failed")

abc=form_login()
abc.mainloop()
abc.conn.close()