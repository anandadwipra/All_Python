import kivy 
kivy.require("2.0.0")

from kivy.app import App 	
from kivy.uix.widget import Widget 
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from kivy.properties import ObjectProperty
from kivy.lang import Builder
Builder.load_file('1.kv')

from engine import kumpulan,lengkap

class CustomDropDown(DropDown):
    pass



class Window(Widget):
	btn=ObjectProperty(None)
	text=ObjectProperty(None)
	def __init__(self,**kwargs):
		super(Window,self).__init__(**kwargs)
		dropdown = CustomDropDown()
		self.btn.bind(on_release=dropdown.open)
		# dropdown.bind(on_select=lambda instance, x: setattr(self.btn, 'text', x))
		dropdown.bind(on_select=lambda instance,x:self.allinone(instance,x))
	def allinone(self,instance ,x):
		self.text.text=lengkap[x]
		setattr(self.btn, 'text', x)

	

class MyApp(App):
	def build(self):
		return Window()

if __name__ =="__main__":
	MyApp().run()










