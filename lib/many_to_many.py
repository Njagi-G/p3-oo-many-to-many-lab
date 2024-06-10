class Author:
    pass

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    pass

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    pass

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("author must be an instance of Author class")
       
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if type(book) == Book:
            self._book = book
        else:
            raise Exception("book must be of type Book")

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")

        self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) == int:
            self._royalties = royalties
        else:
            raise Exception("Royalties must be integers")

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
        


book_1 = Book("Bible")    
print(book_1.title)

author_1 = Author("Moses")
print(author_1.name)

date_1 = "18/05/2024"
royalties_1 = 40000
contract_1 = Contract(author_1, book_1, date_1, royalties_1)
print(contract_1.author.name)
print(contract_1.book.title)
print(contract_1.date)
print(contract_1.royalties)

print(author_1.contracts()[0].date)
print(author_1.contracts()[0].royalties)
print(author_1.contracts()[0].book.title)

print(book_1.contracts()[0].date)
print(book_1.contracts()[0].royalties)
print(book_1.contracts()[0].author.name)

publisher = Author("Mike")
textbook = Book("Kung Fu")
paper_contract = publisher.sign_contract(textbook, "20/01/2023", 60000)
print(paper_contract.author.name)
print(paper_contract.book.title)
print(paper_contract.date)
print(paper_contract.royalties)

author = Author("Name")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")

Contract(author, book1, "01/01/2001", 10)
Contract(author, book2, "01/01/2001", 20)
Contract(author, book3, "01/01/2001", 30)
print(author.total_royalties())

writer_1 = Author("Jack")
novel_1 = Book("Adventure 1")
novel_2 = Book("Adventure 2")
novel_3 = Book("Adventure 3")
writer_2 = Author("Jane")
novel_4 = Book("Adventure 4")
agreement_1 = Contract(writer_1, novel_1, "02/01/2001", 10)
agreement_2 = Contract(writer_1, novel_2, "01/01/2001", 20)
agreement_3 = Contract(writer_1, novel_3, "03/01/2001", 30)
agreement_4 = Contract(writer_2, novel_4, "01/01/2001", 40)

Contract.contracts_by_date('01/01/2001')
for contract in Contract.all:
    print("Author:", contract.author.name)
    print("Book:", contract.book.title)
    print("Date:", contract.date)
    print("Royalties:", contract.royalties)
    print()



