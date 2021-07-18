#!/use/bin/evn python
# https://github.com/ErrorPY404

from zipfile import ZipFile
import sys
import os

argv=False
try:
	if (sys.argv[1]=="-version" or sys.argv[1]=="--version"):
		print("BrokenZip - version 1.0")
		argv=True
	else:
		pass
except:
	pass

def print_help():
	print("""
	
     zip file         :   Specify the zip file.
     password list    :   Specify the password list.
     help             :   Show help.
     quit             :   Exit from the tool.
	""")


try:
	if (sys.argv[1]=="-help" or sys.argv[1]=="--help"):
		print_help()
		argv=True
	else:
		pass
except:
	pass

if (argv==True):
	sys.exit()
else:
	pass

os.system("clear")
print('''
 \033[1;90m BrokenZip - version 1.0 \033[0;0m
''')
print("""\t\033[1;94m
 ______               _                  ______ _        
 | ___ \             | |                |___  /(_)       
 | |_/ / _ __   ___  | | __  ___  _ __     / /  _  _ __  
 | ___ \| '__| / _ \ | |/ / / _ \| '_ \   / /  | || '_ \ 
 | |_/ /| |   | (_) ||   < |  __/| | | |./ /___| || |_) |
 \____/ |_|    \___/ |_|\_\ \___||_| |_|\_____/|_|| .__/ 
                                                  | |    
                                                  |_|    
\033[0;0m""")

print("\t\t\t\033[1;94;40m ErrorPY404 \033[0;0m \n\n\n")

while(True):
	try:
		exit=False
		action=input("\n\t\033[1;90m ENTER YOUR LOCK ZIP FILE PATH :\033[0;0m ")
		if(action=="quit"):
			exit=True
			break
		elif(action=="help"):
			print_help()
		else:
			pass
		try:
			zip=ZipFile(action,"r")
			break
		except:
			if(action=="" or action=="help"):
				pass
			else:
				print("\n\t\033[0;91m[!] Unable To Locate Your Zip File!\033[0;0m")
	except:
		pass


if (exit==True):
	sys.exit()
else:
	pass

list=input("\n\t\033[1;90m Enter Your Password List Path :\033[0;0m ")

try:
	word=open(list,"rb")
	count=open(list,"r")
except:
	print("\n\t\033[0;91m[!] Unable To Locate Your Password List!\033[0;0m")
	sys.exit()

print("\n")
line=count.readline()
condition=0
while(line):
	password=word.readline()
	try:
		zip.extractall(path="Extract",pwd=password.strip())
		print("\n\t\033[1;94m YOUR ZIP FILE PASSWORD : {}\033[0;0m".format(password.decode()))
		condition+=1
		break
	except:
		print(password.decode())
	line=count.readline()
	
if(condition==0):
	print("\n\t\033[1;91m PASSWORD NOT FOUND! .. PLEASE TRY OTHER PASSWORD LIST ..\033[0;0m")
else:
	pass

zip.close()
word.close()
count.close()

