from generator import *

def passgen():
	'''This is the version 0.4 of password generator tool.
	the code has been updated so every function is in a different file
	and classes are used'''

	pswrdgen=True
	while pswrdgen:
		servicename=input("What service is this password for: ")
		sitename=input("Please fill the domain name for this service: ")
		username=input("What is your username: ")

		running=True
		while running:
		    #ask about the length of the password
		    try:
		        passlen=int(input("Please enter the number of characters the password should have: "))
		    except:
		        print("Sorry, only words with number of characters grater or equal to 8 allowed")
		        continue
		    if passlen<8:
		        print("Password should have at least 8 characters")
		        continue
		    else:
		        break

		#creating an instance of the class generator and the argument is the length of the password
		new_passwprd=Generator(passlen)
		created_password=new_passwprd.pswrd()
		new_passwprd.filewrite(servicename,sitename,username,created_password)

		print(f"Your login for {servicename} we created has USERNAME: {username} and PASSWORD: {created_password}")


		##ask for another password y/n, if yes redo, no close.

		newpassask=[]

		while newpassask not in ["y","n"]:

			newpassask=input("Would you like another password? (y/n): ")

		if newpassask=="n":
			break
		continue
if __name__=="__main__":
	passgen()
