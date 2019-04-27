# Class definition for Book entity

class Book:
    bookId = 1
    def __init__(self, title, publisher, author, edition, publishedOn):
        self.__title = title
        self.__publisher = publisher
        self.__author = author
        self.__edition = edition
        self.__publishedOn = publishedOn
        self.__bookId = Book.bookId
        Book.bookId += 1
    
    def __repr__(self):
        return "\nBook Id: {0}\nTitle: {1}\nAuthor: {2}\nEdition: {3}".format(str(self.__bookId), str(self.__title), str(self.__author), str(self.__edition))

    def getBookTitle(self):
        return self.__title

    def getBookAuthor(self):
        return self.__author
    
def UnitTestBook():
    b1 = Book("Deception Point", "Rekha Publications", "Dan Brown", "2", "21/11/2018")
    print(b1)

def main():
    UnitTestBook()

if __name__ == "__main__":
    main()