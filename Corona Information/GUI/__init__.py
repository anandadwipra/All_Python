import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen
# from PIL import Image, ImageTk
import json,re,webbrowser


class mainWindow(tk.Tk):
	
	def __init__(self):
		tk.Tk.__init__(self)
		self.config(bg="blue")
		self.title("Covid-19 Update")
		self.resizable(width=False, height=False)
		try:
			self.iconbitmap("img/icon.ico")
		except:
				self.iconphoto(False, tk.PhotoImage(file='img/virus.png'))
		photo=tk.PhotoImage(file="img/main.png")
		self.frame=tk.Frame(self,width=820,height=600)
		self.frame.pack(fill="both",expand=False)
		img = tk.Label(self.frame, image=photo)
		img.place(x=0, y=0)
		self.menu()
		# load=Image.open("img/main.jpg")
		# render = ImageTk.PhotoImage(load)
		# img = tk.Label(self.frame, image=render)
		# img.image = render
		self.data()
		self.button1=tk.Button(self.frame,text="View",command=self.view,font=("Helvetica",15),width=6);self.button1.place(x=350,y=350)
		self.mainloop()

	
	def view(self,xx="Global",x="z",y="z",z="z"):
		if x=="z":
			x=self.confirmed
			y=self.recovered
			z=self.deaths
		# self.button1.destroy()
		self.frame2=tk.Frame(self.frame,width=420,highlightbackground="#f7d557", bg="#43d8e6",highlightcolor="green", highlightthickness=3,height=300,bd=10)
		self.abc=tk.StringVar()
		self.entry=tk.Entry(self.frame2,textvariable=self.abc)
		self.entry.place(x=100,y=20)
		tk.Button(self.frame2,text="search",command=self.search).place(x=230,y=20)
		tk.Label(self.frame2,text=xx,font=("Helvetica",20),bg="#43d8e6").place(x=20,y=50)
		tk.Label(self.frame2,text=f"Confirmed  : {x}",font=("Helvetica",15),bg="#43d8e6").place(x=20,y=90)
		tk.Label(self.frame2,text=f"Active\t  : ",font=("Helvetica",15),bg="#43d8e6").place(x=20,y=120)
		tk.Label(self.frame2,text=f"Death\t  : {y}",font=("Helvetica",15),bg="#43d8e6").place(x=20,y=150)
		tk.Label(self.frame2,text=f"Recovered : {z}",font=("Helvetica",15),bg="#43d8e6").place(x=20,y=180)
		self.frame2.place(x=200,y=160)

	
	def search(self):
		text=["","","",""]
		value=self.abc.get()
		with urlopen("https://covid19.mathdro.id/api/confirmed") as response:
			source=response.read()
			data=json.loads(source)  
		if value.lower()=="global":
			self.data()
			return
		elif value.lower()=="china":
			messagebox.showwarning(title="Warning",message="China Dan Beberapa Negar Tidak Akurat")
		for i in data:
			if (str(i["countryRegion"])).lower()==value.lower():
				text[0]=str(i["countryRegion"])
				text[1]=i["confirmed"]
				text[2]=i["recovered"]
				text[3]=i["deaths"]
				break
		else:
			messagebox.showwarning(title="Eror",message="Invalid Country")
		self.frame2.destroy()
		self.view(text[0],text[1],text[2],text[3]) 

	
	def data(self,value=" "):
		try:
			with urlopen("https://covid19.mathdro.id/api") as response:
				source=response.read()
				data=json.loads(source)
				self.confirmed=data["confirmed"]["value"]
				self.recovered=data["recovered"]["value"]
				self.deaths=data["deaths"]["value"]
		except:
			messagebox.showwarning(title="Please",message="Tolong Cek koneksi internet anda")



	def menu(self):
		def close():
			self.menubar.destroy()
			messagebox.showinfo(title="Information",message="Press 'Shift+M' to Show Menu 'Shift+H' to Hide Menu")
		def aboutFUNC():
			messagebox.showinfo(title="About",message="Covid-19 Information".center(30)+"\n"+"Version 1".center(30)+"\nBuild By Ananda Dwi Prayoga")
		self.menubar=tk.Menu(self)
		self.bind("<M>",lambda a:self.menu())
		self.bind("<H>",lambda a:self.menubar.destroy())
		self.config(menu=self.menubar)
		# help
		helpmenu=tk.Menu(self.menubar,tearoff=0)
		helpmenu.add_command(label="About",command=aboutFUNC)
		helpmenu.add_command(label="Source Code",command=lambda :webbrowser.open("https://github.com/anandadwipra/All_Python/tree/master/Corona%20Information"))
		helpmenu.add_command(label="Api",command=lambda:webbrowser.open("https://covid19.mathdro.id/api/"))
		helpmenu.add_command(label="Help",command=lambda :webbrowser.open("https://www.instagram.com/ananda.dwi.p/"))
		self.menubar.add_cascade(label="help",menu=helpmenu)
		#view
		viewmenu=tk.Menu(self.menubar,tearoff=0)
		viewmenu.add_command(label="Hide Menu",command=close)
		self.menubar.add_cascade(label="view",menu=viewmenu)
