#Register
# - username, or email and password
# - generate user account 
# - create user account 

#Login
# - username,or email and password 

#Banking options
# - withdrawal,deposit,transfer, airtime,logout


# Initializing the system
import random

database = {} #dictionary

def init():
    print("****welcome to sky bank****")

    account = int(input("do you have an account: 1 (YES), 2 (NO) \n"))

    if(account == 1):
        login()

    elif(account == 2):
        register()

    else:
        print("you selected invalid option")
        init()
    
def login():
    print("login")
   
    accountNumberFromUser = int(input("enter your account number: \n"))

    password = input("what is your password? \n")
    
   
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankoperation(userDetails)
    
    login()

 


        

def register():
    print("register")

 
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]



    print("account created")            
    print("Your account number is: %d" % accountNumber)
    login()           
                   


def bankoperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedoption = int(input("what would you like to do: 1 (withdrwal), 2 (deposit) 3 (transfer) 4 (airtime) 5 (logout) \n"))

    if(selectedoption == 1):
        withdrawal()

    elif(selectedoption == 2):
         deposit()

    elif(selectedoption == 3):
         transfer()

    elif(selectedoption == 4):
         airtimepurchase()    

    else:
        print("invalid option selected")
        login()
            

def withdrawal():
    print("withdrawal")

    withdrawal=int(input("how much would you like to withdraw: 1 (1000), 2 (5000), 3 (10000), 4 others \n"))
   
    if withdrawal==1:
       accounttype()
    elif withdrawal==2:
       accounttype()
    elif withdrawal==3:
       accounttype()
    elif withdrawal==4:
       int(input("amount: \n"))
       accounttype()
    else:
        print("you selected an invalid option")
        login()

def deposit():

    print("deposit")
    deposit=int(input("how much would you like to deposit: \n"))
    accounttype()

def transfer():
    print("transfer")
    transfer=int(input("how much would you like to transfer: \n"))

    selectbank=int(input("select bank: 1 (oceanic bank), 2 (intercontinental bank), 3 (eastern bank) \n"))
    if selectbank==1:
       accounttype()
    elif selectbank==2:
         accounttype()
    elif selectbank==3:
         accounttype()
    else:
        print("invalid option selected")
        login()

def airtimepurchase():
    print("airtime")

    airtime=int(input("how much airtime do you want to purchase: \n"))
    phonenumber=int(input("phone number: \n"))
    airtime=int(input("select service provider: 1 (mtn), 2 (glo), 3 (airtel) \n"))
    if airtime==1:
       accounttype()
    elif airtime==2:
         accounttype()
    elif airtime==3:
         accounttype()
    else:
        print("invalid option selected")
        login()
        
def accounttype():
    print("accounttype")
    accounttype=int(input("choose account: 1 (savings), 2 (current), 3 (fixed deposit) \n"))
    if accounttype==1:
       receipt()
    elif accounttype==2:
       receipt()
    elif accounttype==3:
       receipt()
    else:
        print("invalid option selected")
        login()


def receipt():
    receipt=int(input("do you want a receipt for these transaction: 1 (YES), 2 (NO) \n"))
    if(receipt==1):
       transaction()
    elif(receipt==2):
       transaction()
    else:
        print("invalid option selected")
        login()

def transaction():
    transaction=int(input("do you want to perform another transaction: 1 (YES), 2 (NO) \n"))
    if(transaction==1):
       login()

    elif(transaction==2):

       print("take your card")
       logout()


def generationAccountNumber():
    print("account number generation")
    return random.randrange(1111111111,9999999999)

def logout():
    login
init()
####ACTUAL BANKING SYSTEM #### 
