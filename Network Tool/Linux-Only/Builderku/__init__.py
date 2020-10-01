import sys
sys.path.append("/home/zeth/Documents/Dokumen/Python/Kivy/Kivy Basic/Project 1")
from engine import interface
with open("../1.kv",'w') as file:
	file.write("<CustomDropDown>:")
	for i in interface:
		file.write("""
	Button:
		text: '{}'
		size_hint_y: None
		height: 44
		on_release: root.select('{}')""".format(i,i))

# <CustomDropDown>:
#     Button:
#         text: 'My first Item'
#         size_hint_y: None
#         height: 44
#         on_release: root.select('item1')
#     # Label:
#     #     text: 'Unselectable item'
#     #     size_hint_y: None 
#     #     height: 44
#     Button:
#         text: 'My second Item'
#         size_hint_y: None
#         height: 44
#         on_release: root.select('item2')