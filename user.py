


class User:
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email =email
        self.address =address
        self.id=""
        self.balance =0
        self.due = 0
        self.transferHistory =[]
        self.loan=0

    def transanctionHiatory(self):
        print(self.transferHistory)
    def __repr__(self) -> str:
        return f"name :{self.name} address : {self.email}"



class Admin:
    def __init__(self,name) -> None:
        self.name = name



