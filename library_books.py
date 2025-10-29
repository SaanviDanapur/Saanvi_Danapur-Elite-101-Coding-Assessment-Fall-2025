from datetime import date

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

def view_books():
    for i in library_books:
        book_id = i['id']
        print(f'Id: {book_id}')
        book_title = i['title']
        print(f'Title: {book_title}')
        book_author = i['author']
        print(f'Author: {book_author}')
        print("-"*40)

def search_books(user_search):
    for i in library_books:
        if user_search == i['author'] or user_search == i['title']:
            print(i['title'])

def checkout_books(user_checkout_book):
    for i in library_books:
        if i['id'] == user_checkout_book:
            if i['availibility'] == True:
                i['availibility'] == False
            else:
                print(f'The book with the id {user_checkout_book} is not availible at this time')


    # If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# view_books()

def return_book(user_return_book):
    for i in library_books:
        if i['id'] == user_return_book:
            if i['avaiblible'] == False:
                i['available'] == True
            else:
                print(f'The book with the id {user_return_book} is already availible in the system')

def view_overdue_books():
    current_date = date.today

    print("The following book titles are overdue: ")
    for i in library_books:
        if i['due_date'] != None:
            temp_date = i['due_date'].split(" ")
            due_date_touple = temp_date.tuple()
            if current_date > due_date_touple:
                print({i['title']})
        

view_overdue_books()