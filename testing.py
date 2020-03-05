# import re 
# import tkinter as tk 
 
# class App(tk.Tk): 
#     def __init__(self): 
#         super().__init__() 
#         self.pattern = re.compile("^\w{0,10}$") 
#         print(self.pattern)
#         self.label = tk.Label(self, text="Enter your username") 
#         vcmd = (self.register(self.validate_username), "%i", "%P") 

#         self.entry = tk.Entry(self, validate="key", 
#                               validatecommand=vcmd, 
#                               invalidcommand=self.print_error) 
#         self.label.pack() 
#         self.entry.pack(anchor=tk.W, padx=10, pady=10) 
 
#     def validate_username(self, index, username): 
#         print("Modification at index " + index) 
#         return self.pattern.match(username) is not None 
 
#     def print_error(self): 
#         print("Invalid username character") 
 
# if __name__ == "__main__": 
#     app = App() 
#     app.mainloop() 

# import os
# os.system("--version")
def is_phone_number(text):
    if len(text) != 11:
        return False
    for i in range(0, 3):
    	if not text[i].isdecimal():
        	return False
    	if text[3] != ' ':
        	return False
    for i in range(4, 11):
        if not text[i].isdecimal():
            return False
    return True
    print('021 8229311 adalah nomor telepon:')
pesan = 'Panggil saya di nomor 061 7981011 besok. Kalau sore bisa hubungi kantor saya di 061 7939999.'
for i in range(len(pesan)):
    text = pesan[i:i+11]
    if is_phone_number(text): 
        print("Nomor telepon ditemukan:", text)
    # print("selesai")