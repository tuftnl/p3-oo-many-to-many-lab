import ipdb

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def __repl__(self):
        return f"<Author= name:{self.name}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else: 
            raise Exception("Name must be a string")
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties = 0):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        royalties_list = [contract.royalties for contract in \
                          Contract.all if contract.author == self]
        return sum(royalties_list)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def __repl__(self):
        return f"<Book= title:{self.title}"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else : 
            raise Exception("Title must be a string")
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book 
        self.date = date 
        self.royalties = royalties
        Contract.all.append(self)

    def __repl__(self):
        return f"<Contract= author:{self.author} book:{self.book} date:{self.date} royalties:{self.royalties}"

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else : 
            raise Exception("Author must be an instance of the Author class")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else : 
            raise Exception("Book must be an instance of the Book class")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else :
            raise Exception("Date must be a string")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else :
            raise Exception("Royalties must be an int")
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]



# author1 = Author("Name 1")
# book1 = Book("Title 1")
# book2 = Book("Title 2")
# book3 = Book("Title 3")
# author2 = Author("Name 2")
# book4 = Book("Title 4")
# contract1 = Contract(author1, book1, "02/01/2001", 10)
# contract2 = Contract(author1, book2, "01/01/2001", 20)
# contract3 = Contract(author1, book3, "03/01/2001", 30)
# contract4 = Contract(author2, book4, "01/01/2001", 40)

# ipdb.set_trace()