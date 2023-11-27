from user import User, Admin


class Bank:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address =address
        self.balance =0
        self.user = {}
        self.loanGiven =0
        self.admin={}
        self.loanOn=1
    
    def openUserAccount(self,user):
        serial = f"{user.name}{len(self.user)}"
        self.user[serial]=user
        self.user[serial].id =serial
        print(f"account created successfully your account number is {serial}")

    def deposit(self,user,amount):
        if user in self.user:
            self.user[user].balance+=amount
            self.balance+=amount
            self.user[user].transferHistory.append(f"# deposit:{amount} taka  Current balance :{self.user[user].balance} ")
            print(f"# deposite:{amount} taka \n Current balance :{self.user[user].balance}")
        else :
            print("User not found")

    def CheckUserBalance(self,user):
        if user in self.user:
            print(f"your current balance is {self.user[user].balance}")
        else :
            print("User not found")

    def transferHistory(self,user):
        if user in self.user:
             for u in self.user[user].transferHistory:
                 print(u)

        else :
            print("User not found")

        
    def WithDeaw(self,user,amount):
        if user in self.user:
           if self.user[user].balance >=amount:
               if self.balance >= amount:
                  self.user[user].balance -= amount
                  self.balance -=amount
                  self.user[user].transferHistory.append(f"# withdraw:{amount} taka Current balance :{self.user[user].balance} ")
                  print(f"withdraw:{amount} taka \n Current balance :{self.user[user].balance}")
               else :
                    print(f"Bank is bankrupt")
           else :
              print(f"Withdrawal amount exceeded")
        else :
            print("User not found")
    def loan(self, user, amount) :
        if user in self.user :
           if self.user[user].loan <=1 :
               if amount <= self.balance :
                   if self.loanOn ==1:
                       self.user[user].due +=amount
                       self.balance -=amount
                       self.user[user].loan +=1
                       self.loanGiven +=amount
                       self.user[user].transferHistory.append(f"loan::{self.user[user].due}")
                       print(f"successfully loan given {amount} taka to {user} ")
                   else :
                      print("Loan is off for this time")
               else :
                  print(f"Sorry bank has not sufficiat amount to give u loan")
           else : 
              print(f"Sorry you already teken loan 2 times")
    

    def transMoneyToAnother(self ,sender, reciever,amount ) :
        if reciever in self.user and sender in self.user :
           self.user[sender].balance -=amount
           self.user[reciever].balance +=amount
           self.user[sender].transferHistory.append(f"send money to {self.user[reciever].id} {amount} taka  :current Balance ::{self.user[sender].balance}")
           self.user[reciever].transferHistory.append(f"received money from {self.user[sender].id} {amount} taka :current Balance ::{self.user[reciever].balance}")
           print(f"successfully send money {amount} taka done current balance:: {self.user[sender].balance} and receiver balance is {self.user[reciever].balance}")

        else :
            print(f"Account does not exist")
            
    def createAdmin(self , admin):
        self.admin[admin.name]  =admin
        print("admin created successfully ")
    
    def deleteAccount(self, user,admin):
        if admin in self.admin:
            self.user.pop(user)
            print(f"this {user} Deleted succesfully username")
        else :
            print("you are not allowed to access")
        
    def seeAllUser(self, admin):
        if admin in self.admin:
            for u in self.user.values():
                print(f"name:{u.name} email:{u.email}")
        else :
            print("Only admin can access")
       
    def checkBalance(self, admin):
        if admin in self.admin:
            print( self.balance)  
        else :
            print("Only admin can access")
       
    def checkLoanBalance(self, admin):
        if admin in self.admin:
            print( self.loanGiven)  
        else :
            print("Only admin can access")
       

    def LoanOnORoff(self, admin,onOff):
        if admin in self.admin:
            self.loanOn=onOff
            if onOff == "1" :
                 print("Successfully system on")
            else:
                print("successfully loan system off")
        else :
            print("Only admin can access")
       

    def __repr__(self) -> str:
        return f"name :{self.name} address : {self.email}"
#USER
#mishrat = User("mishrat","@gmail.com","noakhali")
#m1 = User("mishrat","@gmail.com","noakhali")
#m2 = User("mishrat","@gmail.com","noakhali")
sonaliBank = Bank("sonali","kankirhat")
#sonaliBank.openUserAccount(mishrat)
#sonaliBank.openUserAccount(m1)
#sonaliBank.openUserAccount(m2)
#sonaliBank.deposit(mishrat,50000)
#sonaliBank.deposit(m1,50000)
#sonaliBank.WithDeaw(mishrat,5000)
#mishrat.availableBalance()
#mishrat.transanctionHiatory()
#sonaliBank.loan(m2,7000)
#print(m2.due)
#sonaliBank.transMoneyToAnother(mishrat,m2,1000)
#
#
##ADMIN
#admohin = Admin("mohin")
#sonaliBank.createAdmin(admohin)
#sonaliBank.deleteAccount(m1,admohin)
#sonaliBank.deleteAccount(m2,admohin)
#sonaliBank.seeAllUser(admohin)
#sonaliBank.checkBalance(admohin)
#sonaliBank.checkLoanBalance(admohin)
#sonaliBank.LoanOnORoff(admohin,0)
#sonaliBank.loan(m2,7000)
#


while True :
     print("1.create an user account")
     print("2.deposit ")
     print("3.withdraw")
     print("4.transfer")
     print("5.check user balance")
     print("6.transaction history")
     print("7.Loan")
     print("8.create an admin account")
     print("9.delete user account")
     print("10.see all user account")
     print("11.check bank balance")
     print("12.loan system off")
     print("13.check bank total amount")
    
     option = input("choose one option: ")
     if option =="1" :
         inputs = input("input your name, email, and address wtih space : ")
         info =inputs.split()
         name = info[0]
         email = info[1]
         address= info[2]
         userInfo =User(name,email,address)
         sonaliBank.openUserAccount(userInfo)
     elif option == "2":
         inputs = input("input userId and amount,  wtih space : ")
         info =inputs.split()
         userId = info[0]
         amount = int(info[1])
         sonaliBank.deposit(userId,amount)

     elif option == "3":
         inputs = input("input userId and amount,  wtih space : ")
         info =inputs.split()
         userId = info[0]
         amount = int(info[1])
         sonaliBank.WithDeaw(userId,amount)

     elif option == "4":
         inputs = input("input sederUserId ,recieverUserId and amount,  wtih space : ")
         info =inputs.split()
         senderUserId = info[0]
         receiverUserId = info[1]
         amount = int(info[2])
         sonaliBank.transMoneyToAnother(senderUserId,receiverUserId,amount)



     elif option == "5":
         userId = input("input your  userId : ")
         sonaliBank.CheckUserBalance(userId)


     elif option == "6":
         userId = input("input your  userId : ")
         sonaliBank.transferHistory(userId)
     
     
     elif option == "7":
         inputs = input("input userId  and amount,  wtih space : ")
         info =inputs.split()
         userId = info[0]
         amount = int(info[1])
         sonaliBank.loan(userId,amount)

     elif option == "8":
         name = input("input adminName   : ")
         admin = Admin(name)
         sonaliBank.createAdmin(admin)


     elif option == "9":
         inputs = input("input userId and admin wtih space : ")
         info =inputs.split()
         userId = info[0]
         admin = info[1]
         sonaliBank.deleteAccount(userId,admin)


     elif option == "10":
         admin = input("input admin : ")
         sonaliBank.seeAllUser(admin)

     elif option == "11":
         admin = input("input admin : ")
         sonaliBank.checkBalance(admin)

     elif option == "12":
         inputs = input("input admin  and 1 or any number,  wtih space : ")
         info =inputs.split()
         admin = info[0]
         on = info[1]
         sonaliBank.LoanOnORoff(admin,on)

     elif option == "12":
         inputs = input("input admin  and press 1 to loan on  or any number to off,  wtih space : ")
         info =inputs.split()
         admin = info[0]
         on = int(info[1])
         sonaliBank.LoanOnORoff(admin,on)


     elif option == "13":
         admin = input("input admin  : ")
         sonaliBank.checkLoanBalance(admin)






         
