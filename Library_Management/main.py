import os.path

class Library:

    def __init__(self, username):
        self.username = username
        self.books = []
        with open("Books.txt", 'r') as f:
            # reading each line    
            for line in f:
            # reading each word        
                for word in line.split():
            # displaying the words           
                    self.books.append(word)
            

    def createRecord(self):
        if os.path.exists(f"{self.username}.txt"):
            with open(f"{self.username}.txt", 'r') as f:
                print(f"You have borrowed:{f.read()}")
        else:
            with open(f"{self.username}.txt", 'w'):
                pass

    def updateRecord(self, bookName, Value):   #To update the userdata according to action
        self.bookname = bookName
        if Value == True:
            with open(f"{self.username}.txt" , 'r') as f:
                userdata = f.readlines()
                n = userdata.index(f"{self.bookname}\n")
                userdata.pop(n)
            with open(f"{self.username}.txt" , 'w') as f:
                f.write("")
            for items in userdata:
                with open(f"{self.username}.txt" , 'a') as f:
                    f.write(items)

        else:   
            with open(f"{self.username}.txt" , 'a') as f:
                f.writelines(f"{bookName}\n")

    def updateBooks(self):
        with open(f"Books.txt" , 'w') as f:
                for item in self.books:
                    f.write(f"{item}\n")

    def displayAvailableBooks(self):
        books = []
        print("Books present in this library are: ")
        for book in self.books:
            books.append(book)
        print(books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. PLease keep it safe and return it within 30 days.\n")
            self.books.remove(bookName)
            self.updateRecord(bookName, False)
            self.updateBooks()

            return True
        else:
            print("Sorry, This book has already been issued to someone else. Please wait until the book is returned\n")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        self.updateRecord(bookName, True)
        self.updateBooks()
        

        print("Thanks for returning this book. Hope you enjoyed reeeding it. Have a great day ahead!!")


class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__=="__main__":

    n = input("Enter your username: ")
    centralLibrary = Library(n)
    centralLibrary.createRecord()
    student = Student()
    
    print("==========Welcome to central Library===========")
    while True:
        
        welcomeMsg = '''
        PLease choose an option:
        1. List all the books 
        2. Request a book
        3. Add/Return a book
        4. Show borrowed books
        5. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()  
        elif a ==2:
            centralLibrary.borrowBook(student.requestBook())   
        elif a ==3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            centralLibrary.createRecord()
        elif a == 5:
            print("Thanks for choosing Central Library! Have a great day")
            exit()
        else:
            print("Invalid Choice")
        
        
