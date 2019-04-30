import uuid,socket

def get_mac_address(): # 获取mac地址
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def myname():#获取本机电脑名
	myname = socket.getfqdn(socket.gethostname(  ))
	return myname

def myaddr():#获取本机ip
	myaddr = socket.gethostbyname(myname)
	return myaddr

if __name__ == '__main__':
	d = get_mac_address()
	print(d)
