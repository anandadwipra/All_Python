import kivy
kivy.require('2.0.0rc')

from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

class Login(Screen):
	user=ObjectProperty(None)
	pw=ObjectProperty(None)
	def login(self) :
		SM.current="Main"
class Create(Screen):
	pass 
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
if __name__=="__main__":
	MyApp().run()