class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The user's email has been updated")

    def __repr__(self):
        print("User " + self.name + ", email: " + self.email + ", books read: " + len(self.books))
              
    def __eq__(self, other_user):
        if (self.email == other_user.email):
            if (self.name == other_user.name):
                return true

    def read_book(book, rating):
        self.books[book] = rating 
        

    def get_average_rating():
        temp = 0
        for spot in self.books ():
            temp = temp + spot

        average = temp / len(self.books)
        return average
        

class book (object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self_ratings = []

    def get_title ():
        return title

    def get_isbn ():
        return isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The book's isbn has been updated")

    def add_rating(rating):
        if (0 <= rating <= 4):
            self.ratings = self.ratings + rating
        else:
            return print("Invalid rating")

    def __eq__ (self, other_self):
        if (self.title == other_self.title):
            if (self.isbn == other_self.isbn):
                self = other_self

    def get_average_rating ():
        temp = 0
        for spot in self.ratings ():
            temp = temp + spot
        average_rating = temp / len(self.ratings)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))
                
    class Fiction(object):
        
        def __init__ (self, title, author, isbn):
            book.__init__(self, title, isbn)
            self.author = author
            
        def get_author(author):
            return author

        def __repr__ ():
            return print(title + " by " + author)

    class Non_Fiction(object):
        
        def __init__ (self, title, subject, level, isbn):
            book.__init__(self, title, isbn)
            self.subject = subject
            self.level = level
            
        def get_subject(subject):
            return subject

        def get_level(level):
            return level
        
        def __repr__ ():
            return print(title + ", a " + level + " manual on " + subject)


class TomeRater ():
    
    def __init__ (self):
        self.users = {}
        self.books = {}

    def create_book(self,title, isbn):
        self.books(title, isbn)
        return book
        
    def create_novel(title, author, isbn):
        self.Fiction(title, author,isbn)
        return Fiction

    def create_non_function(title, subject, level, isbn):
        self.Non_Fiction(title, subject, level, isbn)
        return Non_Fiction

    def add_book_to_user(book, email, rating):
        self.users[email]
        if (self.users[email]):
            user.read_book(book, rating)
            book.add_rating(rating)
            for book1 in self.books:
                if (book1 == book):
                    self.books[book] =+ 1
                    
                else:
                    self.books[book] = 1
            
        else:
            print("No user with the email " + email + "!")
            

    def add_user(name, email, user_books):
        self.users(name, email)
        

    def print_catelog():
        print(self.books())

    def print_users():
        print(self.users)

    def most_read_book():
        print(self.book)

    def highest_rated_book():
        print(self.rating)

    def most_positive_user():
        print(self.users)
        
        
    
