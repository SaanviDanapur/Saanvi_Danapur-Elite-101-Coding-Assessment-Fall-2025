from datetime import datetime, timedelta

library_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    },
    {
        "id": "B3",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": True,
        "due_date": None,
        "checkouts": 3
    },
    {
        "id": "B4",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True,
        "due_date": None,
        "checkouts": 4
    },
    {
        "id": "B5",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "available": True,
        "due_date": None,
        "checkouts": 6
    },
    {
        "id": "B6",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "available": False,
        "due_date": "2025-11-10",
        "checkouts": 8
    },
    {
        "id": "B7",
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "available": True,
        "due_date": None,
        "checkouts": 1
    },
    {
        "id": "B8",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-Age",
        "available": False,
        "due_date": "2025-11-12",
        "checkouts": 3
    }
]


def view_overdue_books():
    current_date = datetime.now().date() #used ai to get datetime syntax
    print(type(current_date))
    print("The following book titles are overdue: ")
    for i in library_books:
        if i['due_date'] != None:
            if i['due_date'] < str(current_date):
                print(i['due_date'])
    

class Book:
    def __init__(self, library_books, user_input):
        self.book_info = library_books
        self.user_input = user_input
    
    def view_books(self):
        for i in library_books:
            if i['available'] == True:
                book_id = i['id']
                print(f'Id: {book_id}')
                book_title = i['title']
                print(f'Title: {book_title}')
                book_author = i['author']
                print(f'Author: {book_author}')
                print("-"*40)

    def checkout(self, id):
        
        for i in self.book_info:
            if (i['id'] == id) and (i['available'] == True):
                i['available'] == False
                print(f'The book with the id {i['id']} has been checked out of the system')
                return i['available']
        print(f'The book with the id {id} is not availible in the system')
            
    def return_book(self, identify):
        for i in self.book_info:
            if (i['id'] == identify) and (i['available'] == False):
                i['available'] == True
                print(f'The book with the id {identify} has been returned back to the system')
                return i['available']

        print(f'The book with the id {identify} is already availible in the system')
    
    def search_books(self, user_search):
        for i in self.book_info:
            if user_search.lower() == i['author'].lower() or user_search.lower() == i['title'].lower():
                print(i['title'])
                return user_search
        print(f"Sorry the book/author {user_search} is not available at this time.")
    
    def view_top_three_books(self):
        check_out_list = []
        top_books = ""
        for i in self.book_info:
            check_out_list.append(i['checkouts'])
        check_out_list.sort()
        
        for i in self.book_info:
            if i['checkouts'] in check_out_list[-3:]:
                top_books += i['title'] + "\n"
        print(top_books)

    def view_overdue_books(self):
        current_date = datetime.now().date() #used ai to get current date with datetime syntax        print("The following book titles are overdue: ")
        
        for i in self.book_info:
            if i['due_date'] != None:
                if i['due_date'] < str(current_date):
                    print(i['due_date'])
                
        


def menuFunction():
    library = Book(library_books, "")
    print("--Welcome to the Library application menu--\n1. View books\n2. View top three books\n3. View overdue books\n4. Checkout books\n5. Return books\n6. Exit")
    user_selection = input(("--Please select from the following choices(1-6):"))
    while user_selection !="6":
        if user_selection == "1":
            library.view_books()
        elif user_selection == "2":
            library.view_top_three_books()
        elif user_selection == "3":
            library.view_overdue_books()
        elif user_selection == "4":
            bookid_checkout = input("Enter the id of the book you want to checkout: ")
            library.checkout(bookid_checkout)
        elif user_selection == "5":
            bookid_return = input("Enter the id of the book you want to checkout: ")
            library.return_book(bookid_return) 
        user_selection = input(("--Welcome back to the menu--\n1. View books\n2. View top three books\n3. View overdue books\n4. Checkout books\n5. Return books\n6. Exit\nPlease select from the following choices(1-6):"))
    print("Thank you for using the Library system, have a great rest of your day.")


menuFunction()