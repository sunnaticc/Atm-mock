import random



database={}
def init():
    print("******WELCOME TO BANK PHB******")
    haveAccount=int(input("do you have an account with us? \n (1) yes \n (2) No \n "))
    if(haveAccount==1):
        login()
    elif(haveAccount==2):
        register()

def login():
    print("******login to your account********")
    
    accountNumberFromUser= int(input("What is your account number? \n"))
    password=input("what is your password \n")
    for accountNumber, Userdetails in database.items():
        if(accountNumber==accountNumberFromUser):
            if(Userdetails[3]==password):
                bankoperation(Userdetails)
                complaintOperations(Userdetails)
    print("Invalid account or password")


    
def register():
    print("******REGISTER******")
    email=input("What is your email \n")
    first_name=input("What is your first name \n")
    last_name=input("What is your last name \n")
    password=input("create a unique password \n")
    print("*******************************************************")
    accountNumber=generationaccountnumber()
    database[accountNumber]=[first_name, last_name, email, password]
    print("*******************************************************")
    print("Your Account Has Been Created")
    print("** **** ******* ******* *****")
    print("your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("** **** ******* ******* *****")
    login()

def bankoperation(User):
    print("Welcome %s %s " % (User[0], User[1]))

    selectedOption = int(input("What would you like  to do? \n (1) deposit \n (2) withdrawal \n (3) complaint \n (4) logout \n (5) exit \n"))
    if(selectedOption ==1):
        
        depositOperations()
        anothertrans()
    elif(selectedOption==2):
        
        withdrawalOperations()
        anothertrans()
    elif(selectedOption==3):
        
        complaintOperations(User)
        anothertrans()
    elif(selectedOption==4):
        
        logout()
    elif(selectedOption==5):
        
        exit()
    else:
        print("Invalid option selected")






def withdrawalOperations():
    print("*******************************************************")
    print("(1) 5000 \n (2) 10000 \n (3) 20000 \n (4) 40000")
    
    withdrawOption=int(input("how much would you like to withdraw? \n "))
    if(withdrawOption==1):
        print("take your cash")
    elif(withdrawOption==2):
        print("take your cash")
    elif(withdrawOption==3):
        print("take your cash")
    elif(withdrawOption==4):
        print("take your cash")
    else:
        print("Invalid Amount")
    
def depositOperations():
    print("*******************************************************")
    depositOption=int(input("how much would you like to deposit? \n"))
    print(" %d have been deposited into your account" % depositOption)
    
def complaintOperations(User):
    print("*******************************************************")
    issues=input("what issue will you like to report? \n ")
    print("*******************************************************")
    print("%s %s, your complaint has been forwarded to the appropriate department" % (User[0], User[1]))
    print("*******************************************************")
    print("Thank you for contacting us.")
    print("*******************************************************")
    
def logout():
    login()

def generationaccountnumber():

    return random.randrange(1111111111,9999999999)

def anothertrans():
    print("*******************************************************")
    anothertrans= int(input("would you like to perform another transaction? \n (1) Yes \n (2) No \n"))
    if(anothertrans==1):
        login()
    elif(anothertrans==2):
        exit()
init()
