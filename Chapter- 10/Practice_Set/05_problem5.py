from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"Ticket is booked in Train No: {self.trainNo} from {fro} to {to} ")

    def getStatus(self):
        print(f" Train No: {self.trainNo} is running on time ")
    
    def getFair(self, fro, to):
        print(f"Ticket is booked in Train No: {self.trainNo} from {fro} to {to} is {randint(222,5555)} ")

t = Train(12339)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFair("Delhi", "Mumbai")