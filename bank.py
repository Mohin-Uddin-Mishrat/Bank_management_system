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
        user.id =serial 
        self.user[user.id]=user

    def deposit(self,user,amount):
        user.balance+=amount
        self.balance+=amount
        user.transferHistory.append(f"# deposit:{amount} taka  Current balance :{user.balance} ")
        print(f"# deposite:{amount} taka \n Current balance :{user.balance}")


        
    def WithDeaw(self,user,amount):
        if user.balance >=amount:
            if self.balance >= amount:
                user.balance -= amount
                self.balance -=amount
                user.transferHistory.append(f"# withdraw:{amount} taka Current balance :{user.balance} ")
                print(f"withdraw:{amount} taka \n Current balance :{user.balance}")
            else :
                print(f"Bank is bankrupt")
        else :
            print(f"Withdrawal amount exceeded")
        
    def loan(self, user, amount) :
        if user.loan <=1 :
            if amount <= self.balance :
                if self.loanOn ==1:
                   user.due +=amount
                   self.balance -=amount
                   user.loan +=1
                   self.loanGiven +=amount
                   user.transferHistory.append(f"loan::{user.due}")
                else :
                    print("Loan is off for this time")
            else :
                print(f"Sorry bank has not sufficiat amount to give u loan")
        else :
            print(f"Sorry you already teken loan 2 times")
    

    def transMoneyToAnother(self ,sender, reciever,amount ) :
        if reciever.id in self.user :
           sender.balance -=amount
           reciever.balance +=amount
           sender.transferHistory.append(f"send money to {reciever.id} {amount} taka  :current Balance ::{sender.balance}")
           reciever.transferHistory.append(f"received money from {sender.id} {amount} taka :current Balance ::{reciever.balance}")
           print(f"successfully send money done")

        else :
            print(f"Account does not exist")
            
    def createAdmin(self , admin):
        self.admin[admin.name]  =admin
    
    def deleteAccount(self, user,admin):
        if admin.name in self.admin:
            self.user.pop(user.id)
        
    def seeAllUser(self, admin):
        if admin.name in self.admin:
            print( self.user)  
        else :
            print("Only admin can access")
       
    def checkBalance(self, admin):
        if admin.name in self.admin:
            print( self.balance)  
        else :
            print("Only admin can access")
       
    def checkLoanBalance(self, admin):
        if admin.name in self.admin:
            print( self.loanGiven)  
        else :
            print("Only admin can access")
       

    def LoanOnORoff(self, admin,onOff):
        if admin.name in self.admin:
            self.loanOn=onOff
        else :
            print("Only admin can access")
       

    def __repr__(self) -> str:
        return f"name :{self.name} address : {self.email}"
#USER
mishrat = User("mishrat","@gmail.com","noakhali")
m1 = User("mishrat","@gmail.com","noakhali")
m2 = User("mishrat","@gmail.com","noakhali")
sonaliBank = Bank("sonali","kankirhat")
sonaliBank.openUserAccount(mishrat)
sonaliBank.openUserAccount(m1)
sonaliBank.openUserAccount(m2)
sonaliBank.deposit(mishrat,50000)
sonaliBank.deposit(m1,50000)
sonaliBank.WithDeaw(mishrat,5000)
mishrat.availableBalance()
mishrat.transanctionHiatory()
sonaliBank.loan(m2,7000)
print(m2.due)
sonaliBank.transMoneyToAnother(mishrat,m2,1000)


#ADMIN
admohin = Admin("mohin")
sonaliBank.createAdmin(admohin)
sonaliBank.deleteAccount(m1,admohin)
sonaliBank.deleteAccount(m2,admohin)
sonaliBank.seeAllUser(admohin)
sonaliBank.checkBalance(admohin)
sonaliBank.checkLoanBalance(admohin)
sonaliBank.LoanOnORoff(admohin,0)
sonaliBank.loan(m2,7000)


