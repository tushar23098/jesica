#I tried to make this assistant more intreactive as i can, it will greet you as you run it, you can ask her name,you can ask her how she's feeling and in reply she will ask you. and many more things.
import pyttsx3
import os
print("*Things You should know before using jesica:-")
print("1) Always use work jesica Before\After giving a command. \n2) Use command jesica ['what all things you can do']to know the things jesica can do for you.\n")
pyttsx3. speak("Welcome Master. this is jesicaa. your personal assistant at your service")
pyttsx3. speak("orders master")
while True:
	p=input("What can i do for you master:")

	if("what" in p) and ("name" in p) and ("your" in p):
		pyttsx3.speak("my name is jesicaa master")

	if("jesica" in p) and ("all things" in p) and ("do" in p):
		pyttsx3.speak("i can do following things for you master")
		print("I can launch- Notepad, Whatsapp, Google, Recycle Bin, Microsoftedge, alarm, Youtube, Camera, Time, System info, \nInstagram, Facebook, paint, This PC folder, Media Player, Vlc Player, Firefox, \nVirtual Machine, Calculator, Control Panel, Jupyter, Wikipedia,open mails, You can wish her hi,\n Can ask her how is she and she will respond you back if your mood is not good she even will gonna tell you a joke\n Can play music for you,  \n You can create or Delete a file and folder, \nCan search for you the best teacher for python, \nand search the best course for python")
	
	if("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("clock" in p) or ("alarm" in p) or ("alarm clock" in p)):
		pyttsx3.speak("opening alarm clock")
		os.system("explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App")

	elif(("hi" in p) or ("hey" in p) or ("hello" in p)) and ("jesica" in p):
		pyttsx3.speak("hello master")

	elif("how" in p) and ("you" in p) and ("jesica" in p):
		pyttsx3.speak("i am superb master. what about you")
		I=input("you:")
		if("i" in I) and (("good" in I) or ("great" in I) or ("superb" in I)) and ("jesica" in I):
			pyttsx3.speak("good to hear master")
		elif(("not fine" in I) or ("bad" in I)) and ("jesica" in I):
			pyttsx3.speak("Do you want me to tell a joke for you")
			j=input("yes/no:-")
			if ("yes" in j):
				pyttsx3.speak("Maths Teacher : What Is A Line. Santa : A Line Is A Dot That’s Going For A Walk. Teacher : Then What Is A Parallel Line. Santa : A Dot Is Going For A Walk With His Girl Friend.")
				pyttsx3.speak("i hope now you are feeling some better now")
			else:
				
				pyttsx3.speak("ok master. everything will be fine")

	elif("you" in p) and ("are" in p) and (("great" in p) or ("awesome" in p)):
		pyttsx3.speak("thank you master. that means so much")

#the "Don't open" command you were talking about in session sir. i tried to create it:

	elif("jesica" in p) and (("dont" in p) or ("do not" in p)) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)):
		pyttsx3. speak("Ok Master, i won't open it. hahaha")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and  (("notepad" in p)or("editor" in p)or ("notebook" in p)):
		pyttsx3.speak("Running Notepad")
		os. system("notepad")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("ms edge" in p):
		pyttsx3.speak("Running microsoftedge ")
		os. system("microsoftedge")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("paint" in p):
		pyttsx3.speak("Running paint")
		os. system("mspaint")


	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("media player" in p):
		pyttsx3.speak("Running media player")
		os. system("wmplayer")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("chrome" in p):
		pyttsx3.speak("Running chrome")
		os. system("chrome")
	
	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("calci" in p) or ("calculator" in p)):
		pyttsx3.speak("Running calculator")
		os.system("calc")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("camera" in p):
		pyttsx3.speak("opening Camera. embrace your beauty")
		os.system("start microsoft.windows.camera:")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("firefox" in p):
		pyttsx3.speak("Running firefox")
		os.system("firefox")
	
	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("virtual machine" in p) or ("vm" in p)):
		pyttsx3.speak("which virtual machine you want to open master")
		u=input("which virtual machine, Name:")
		if("virtual" in u) and ("box" in u):
			pyttsx3.speak("Running virtual box")
			os.system("VirtualBoxVM")	
		else:
			pyttsx3.speak("V M ware")
			os.system("vmware")

	elif("jesica" in p) and (("run" in p) or ("execute" in p)or ("open" in p)) and (("my pc" in p) or ("mypc" in p) or ("this pc" in p)or ("my Computer")):
		pyttsx3.speak("opening My Computer")
		os.system("start explorer shell:mycomputerfolder")
	
	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("system info" in p) or ("system information" in p):
		pyttsx3.speak("Running system information")
		os.system("systeminfo")

	elif("jesica" in p) and (("create" in p) or ("make" in p)) and  ("folder" in p):
		pyttsx3.speak("Where you want to create the folder")
		print("Where you want to create the folder?")
		jonny=input("Here:")
		pyttsx3.speak("give a name to the folder")
		tonny=input("Here:")
		path=("C:\\Users\\admin\\"+jonny+"\\")
		pyttsx3.speak("ok master creating the folder called"+tonny+ "in" +jonny)
		os.mkdir(path+tonny)

	elif("jesica" in p) and (("create" in p) or ("make" in p)) and  ("file" in p):
		pyttsx3.speak("Where you want to create the file")
		print("Where you want to create the file?")
		jon=input("Here:")
		pyttsx3.speak("name the file with the type(txt, mp3, etc etc")
		print("in (txt, mp3, etc etc) format")
		ton=input("Here:")
		path1=("C:\\Users\\admin\\"+jon+"\\")
		pyttsx3.speak("ok master creating the file called"+ton+ "in" +jon)
		os.system("type nul >"+path1+ton)

	elif("jesica" in p) and (("delete" in p) or ("remove" in p)) and ("file" in p):
		pyttsx3.speak("location of the file you want to delete")
		print("Location of the file:")
		re=input("Here:")
		pyttsx3.speak("name the file with the type(txt, mp3, etc etc")
		print("in (txt, mp3, etc etc) format")
		tus=input("Here:")
		path2=("C:\\Users\\admin\\"+re+"\\")
		pyttsx3.speak("ok master deleting the file called"+tus+"from"+re)
		os.system("del "+path2+tus)

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("recycle bin" in p):
		pyttsx3.speak("opening recycle bin")
		os.system("start shell:RecycleBinFolder")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("whatsapp" in p):
		pyttsx3.speak("opening Whatsapp")
		os.system("chrome https://web.whatsapp.com/")
	
	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p) or ("what is" in p) or ("whats" in p)) and ("date" in p):
		pyttsx3.speak("Todays date is")
		os.system("date")
	
	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p) or ("what is" in p) or ("whats" in p)) and ("time" in p):
		pyttsx3.speak("the time is")
		os.system("time")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("control panel" in p) or ("c panel" in p) or ("cpanel" in p)):
		pyttsx3.speak("running control panel")
		os.system("control panel")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("vlc player" in p):
		pyttsx3.speak("opening v l c media player")
		os.system("vlc")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("jupyter" in p) or ("jupyter notebook" in p)):
		pyttsx3.speak("opening jupyter notebook")
		os.system("jupyter notebook")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("facebook" in p) or ("fb" in p)):
		pyttsx3.speak("opening facebook")
		os.system("chrome https://www.facebook.com/")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("google" in p):
		pyttsx3.speak("opening google")
		os.system("chrome https://www.google.co.in/")
	
	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("wiki" in p) or ("wikipedia" in p)):
		pyttsx3.speak("opening Wikipedia")
		os.system("chrome https://www.wikipedia.org/")
	
	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("youtube" in p):
		pyttsx3.speak("opening youtube")
		os.system("chrome https://www.youtube.com/")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("mails" in p)or ("mail" in p)):
		pyttsx3.speak("opening your mails")
		os.system("chrome https://mail.google.com/mail/u/0/#inbox/FMfcgxwJXVJDFRQXmPPvDNVZNtkChMhL")

	elif("jesica" in p) and ("who" in p) and ("best" in p) and ("teacher" in p) and ("python" in p):
		pyttsx3.speak("searching the best teacher of python")
		os.system("chrome https://in.linkedin.com/in/vimaldaga")
	
	elif("jesica" in p) and ("learn" in p) and ("python" in p):
		pyttsx3.speak("searching the best course for python")
		os.system("chrome https://www.youtube.com/playlist?list=PLAi9X1uG6jZ1s-_ffUVn-e-b0LiUDfQJT")
	
	elif("jesica" in p) and ("play" in p) and ("music" in p):
		pyttsx3.speak("playing music. enjoy master")
		os.system("chrome https://youtu.be/EiiyYkae33k")

	elif("jesica" in p) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("insta" in p) or ("instagram")):
		pyttsx3.speak("opening your insta account")
		os.system("chrome https://www.instagram.com/?hl=en")
		

	elif("jesica" in p) and (("bye" in p) or ("tata" in p) or("seeya" in p)):
		pyttsx3. speak("bye have a great day master. please come quick")
		break

	else:
		pyttsx3.speak("wrong input master")
		print("Wrong Input")