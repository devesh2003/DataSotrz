import os
from hashlib import md5

def add_active_user(username):
	if(os.isfile("sessions.bin") == null):
		file = open("sessions.bin",'w')
	else:
		file = open("sessions.bin",'a')
	info = username + ":Active;"
	file.write(info)
	file.close()

def login(user_name,passwd):
	passwd_hash = md5(passwd.encode("utf-8")).hexdigest()
	file = open("data.bin",'r')
	entries = file.read().split('!')
	for index in range(0,len(entries)-1):
		data = entries[index].split(";")
		_user_name = data[1]
		passwd = data[2]
		if(_user_name == user_name):
			if(passwd == passwd_hash):
				print("[*] Login successful")
				add_active_user(user_name)
				#Validation stuff
				file.close()
				return
	print("[*] Login failed")
	return

def logout(user_name):
	file = open("sessions.bin",'ra')
	entries = file.read().split(';')
	for entry in entries:
		data = entry.split(":")
		if(data[0] == user_name):
			info = user_name + ":Dead"
			file.write(info)
	file.close()
