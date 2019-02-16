import os

def count_entries():
	file = open("data.bin",'r')
	data = file.read()
	entries = data.split('!')
	print("[*] Current entries in the database are %d"%(len(entries) - 1))

def encrypt_username():
	pass