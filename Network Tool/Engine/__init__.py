import netifaces as net 
interfaces=net.interfaces()
ip=lambda x :net.ifaddresses(x)
print(net.ifaddresses("wlp4s0"))
a