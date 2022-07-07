'''
Seats
1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.a = seats
        self.seatsNo =[]
        i = 1
        while i <= self.seats:
            self.seatsNo.append(i)
            i = i+ 1

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seast available in the train are {self.seats}")
    

    def fareInfo(self):
        print(f"The price of the ticket is Rs.{self.fare}")

    def bookTicket(self):
        if self.seats>0:
            print(f"Your ticket has been booked! \n Your Seat number is {self.seats}")
            self.seatsNo.remove(self.seats)
            print("List of available seats", self.seatsNo)
            self.stat = self.seats
            self.seats = self.seats - 1
            
        else:
            print("Sorry. This train is full! Kindly try in tatkal")

    def cancelTicket(self):
        print(f"Your Ticket no- {self.stat} is canceled")
        if self.seats < self.a:
            self.seats = self.seats + 1
            self.seatsNo.append(self.stat)
            self.stat = self.stat + 1 
            print("List of available seats", self.seatsNo)
        else:
            print("No seats to cancel")
        
        

intercity = Train('Intercity Express: 14015', 90, 10)   


while True:
    a = int(input("1.Book Ticket 2.Cancel Ticket 3.Get fare info 4.Status 5.Exit \n Your Choice: "))
    if a == 1:
        intercity.bookTicket()
    elif a == 2:
        intercity.cancelTicket()    
    elif a == 3:
        intercity.fareInfo()
    elif a == 4:
        intercity.getStatus()
    else:
        exit()

