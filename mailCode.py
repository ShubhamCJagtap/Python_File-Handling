import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w{5,10}[.]\w{2,3}$'  

def login(mail,password):
    global success
    success = False
    file = open("mail_data.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==mail and b==password):
            success = True
            break
    file.close()
    if success == True:
        print("Login Successful!")
        print("Have a great Day!!!!")
        print("*******************    :)")
    else:
        print("Oh Snap! Wrong username or Password!")
        ans = input("Forgot password?   Or   Not Registered! Want to Register?    (Forgot/Register): ")
        if(ans.lower()=='register'):
            option = 'register'
            access(option)
        elif(ans.lower()=='forgot'):
            givepassword()
        else:
            print("Oh No! Please try again")

def givepassword():
    mail = input("Enter Your mail: ")
    print('Please Wait')
    sol1 = check(mail)
    if sol1 == "N":
        print("Oh No! Invalid Email Syntax!")
        givepassword()
    file = open("mail_data.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==mail):
            print('Your registered Password is : ')
            print(b)
            file.close()
            break
    else:
        print("No Hit! Let's Register")
        file.close()
        option = 'register'
        access(option)

    

def register(mail,password):
    file = open("mail_data.txt","a")
    file.write("\n"+mail+","+password)
    file.close()
    print('Done! You are registered!')
    

def access(option):
    global mail
    sol1 = ''
    sol2 = ''
    if (option.lower()=="login"):
        print("Proceed for login :")
        mail = input("Enter Your mail: ")
        print('Please Wait')
        password = input("Enter your Password: ")
        print('Please Wait')
        login(mail,password)
        
    else:
        print("Enter Your Name and Password To register ")
        mail = input("Enter Your mail: ")
        print('Please Wait')
        sol1 = check(mail)
        if sol1 == "N":
            print("Oh No! Invalid Email!")
            access(option)

        password = input("Enter your Password: ")
        print('Please Wait')
        sol2 = checkpass(password)
        if sol2 == "N":
            print("Oh No! Invalid Password!")
            access(option)
        if (sol1 == "Y" and sol2 == "Y"):
            register(mail,password)
            
        

def begin():
    global option
    print('Welcome to login system')
    option = input('Login or Register : ')
    
    if (option.lower() == 'login' or option.lower()=='register'):
        print('Done')
    else:
        print('Oh! Wrong Option!')
        begin()

def check(email):   
  
    if(re.search(regex,email)):   
        return "Y"   
    else:   
        return "N"  

def checkpass(password):
    p= password
    x = True
    while x:
        if (len(p)<5 or len(p)>16):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif re.search("\s",p):
            break
        else:
            x=False
            return "Y"
        break

    if x:
        return "N"

begin()
access(option)