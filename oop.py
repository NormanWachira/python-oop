class Book:
    def __init__(self, title, author):
        # private attributes
        self.__title = title;  
        self.__author = author;

    # Getter for title
    @property
    def title(self):
        return self.__title

    # Setter for title
    @title.setter
    def title(self, value):
        if value.strip():
            self.__title = value
        else:
            raise ValueError("Title cannot be empty")

    # Getter for author
    @property
    def author(self):
        return self.__author
    # Setter for author
    @author.setter
    def author(self, value):
        self.__author = value

    def describe(self):
        print(f"'{self.__title}' by {self.__author}")


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.__genre = genre
    # getter for genre
    @property
    def genre(self):
        return self.__genre
    # setter for genre
    @genre.setter
    def genre(self, value):
        self.__genre = value

    def describe(self):
        print(f"Novel: '{self.title}' by {self.author}, Genre: {self.__genre}")


class Textbook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.__subject = subject
    # getter for subject
    @property
    def subject(self):
        return self.__subject
    # setter for subject
    @subject.setter
    def subject(self, value):
        self.__subject = value

    def describe(self):
        print(f"Textbook: '{self.title}' by {self.author}, Subject: {self.__subject}")


# -------- Testing --------
b1 = Book("Generic Book", "Unknown")
b2 = Novel("1984", "George Orwell", "Dystopian")
b3 = Textbook("Physics 101", "Isaac Newton", "Science")

library = [b1, b2, b3]

for book in library:   # polymorphism
    book.describe()

# Encapsulation in action
print(b2.genre)        # getter
b2.genre = "Political" # setter
b2.describe()
