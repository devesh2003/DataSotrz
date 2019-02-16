import struct
import time
import os
from hashlib import md5

def check_user(username):
	try:
		file = open("data.bin",'r')
		entries = file.read().split('!')
		for index in range(0,len(entries)):
			data = entries[index].split(';')
			user_name = data[1]
			if(user_name == username):
				return True
		return False
	except:
		return False


def add_user(email,user_id,passwd):
	if(os.path.isfile("data.bin") != True):
		file = open("data.bin",'w')
	else:
		file = open("data.bin",'a')
	if(check_user(user_id) != True):
		file.write(email + ";")
		file.write(user_id + ";")
		passwd_hash = md5(passwd.encode("utf-8")).hexdigest()
		file.write(passwd_hash + '!')
		file.close()
		print("[*] User added!")
	else:
		print("[*] User name aldready in use")
	return
