'''
Implement a student library System using OOPs
where students can borrow a book from the list 
of books

Create a separate Library amnd student class
your program must be menu driven

You are free to choose methods and attributes
of your choice to implement this functionality.

'''


class Library:
    def __init__(self, book):
        self.listofBooks = []
        self.listofBooks = book

    def borrow(self, bookname):
        flag = 0
        self.bookname = bookname
        for item in self.listofBooks:
            if item == self.bookname:
                flag = 1
            else:
                break
            
        if flag == 1:
            print(f"You have successfully borrowed {self.bookname}")
            self.listofBooks.remove
            print(f"available books are: {self.listofBooks}")
        else:
            print(f"This book '{self.bookname}' is unavailable at the current moment. Look for this book after some days")


class Student:
    pass

print("----------------------Welcome to Library------------------------------")
n = input("please enter your name is lower case:")

books = ["Gitanjali", "Chander Pahar", "Tenida"]
Lib = Library(books)


while True:
    n = int(input("1. Borrow book by name\n2.Borrow book by number\n3.Return previously borrowed book\n4.Exit\n\nChoose an option:"))
    
    if n == 1:
        name = input("Enter the name of Book you want: ")
        c1 = Library()
        c1.borrow(name)
    elif n==2:
        pass
    elif n==3:
        pass
    elif n==4:
        print("----------------Thanks for visiting our Library--------------")
        exit()