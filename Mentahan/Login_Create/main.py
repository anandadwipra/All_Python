import kivy
kivy.require('2.0.0rc')

from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from database import add_user,close,login
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label

class Login(Screen):
	user=ObjectProperty(None)
	pw=ObjectProperty(None)
	def login(self) :
		i=login([self.user.text,self.pw.text])
		if len(i) > 1 :
			muncul(i)
		SM.current=i[0]

class Create(Screen):
	user=ObjectProperty(None)
	pw=ObjectProperty(None)
	email=ObjectProperty(None)
	def create(self,x):
		z=add_user([self.user.text,self.email.text,self.pw.text])
		muncul(z)

class Main(Screen):
	pass

SM=ScreenManager()
kv=Builder.load_file("my.kv")
screen=[Login(name="Login"),Create(name="Create"),Main(name="Main")]
for i in screen :
	SM.add_widget(i)


SM.current="Login"

class MyApp(App):
	def build(self):
		return SM 

def muncul(x):
	print("ini x ",x)
	isipopupku=FloatLayout()
	button=Button(text="Ok",size_hint=(.7,.2),pos_hint={'x': 0.15,'y':0.1})
	popupku=Popup(title=x[0],content=isipopupku,size_hint=(None,None),size=(300,300),auto_dismiss=False)
	isipopupku.add_widget(Label(text=x[1],size_hint=(.7,.2),pos_hint={'x':.15,'y':0.7}))	
	isipopupku.add_widget(button)
	if "berhasil didaftarkan" in x[1]:
		button.bind(on_press=lambda a:(popupku.dismiss(),pindahlayar("Login")))
	else:
		button.bind(on_press=lambda a:popupku.dismiss())
	popupku.open()
def pindahlayar(x):
	SM.current=x

if __name__=="__main__":
	MyApp().run()
	close()
