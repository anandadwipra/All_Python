import subprocess
import re

batcmd="ifconfig"
result = subprocess.check_output([batcmd], stderr=subprocess.STDOUT,text=True,encoding="UTF-8")
x = result.split("\n\n")[:-1]
# print(result)
interface=[]
mo=[]
kumpulan={}
lengkap={}
z=0
for i in x:
	lengkap[i.split(":",1)[0]]=i.split(":",1)[1]
	interface.append(i.split(":")[0])  #interface
	mo.append(re.findall(r'\d+[.]\d+[.]+\d+[.]\d+',i) ) #ip
	kumpulan[str(interface[z])]=mo[z]
	z+=1


