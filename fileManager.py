import os
from hashlib import md5

def store_files(username,user_file):
	f = open(user_file,'rb')
	data = user_file.read()
	f.close()
	try:
		os.mkdir("User Files")
		os.chdir("User Files")
	except:
		os.chdir("C:/Users/pathik/Desktop/Data Storage/")
		os.mkdir("User Files")
		os.chdir("User Files")

	file_name = md5(username.encode("utf-8")).hexdigest()
	out_file = open(str(file_name),'wb')
	out_file.write(data)
	out_file.close()
	print("File Uploaded")
