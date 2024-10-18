from typing import List, Optional

class Book:
    def __init__(self, title: str, author: str, publication_year: int, genre: str, pages: int) -> None:
        """
        Initialize a new instance of the Book class.

        Parameters:
        title (str): The title of the book. It should be a non-empty string.
        author (str): The author of the book. It should be a non-empty string.
        publication_year (int): The publication year of the book. It should be a positive integer.
        genre (str): The genre of the book. It should be a non-empty string.
        pages (int): The number of pages in the book. It should be a positive integer.

        Returns:
        None: This method does not return any value. It initializes a new instance of the Book class.
        """
        if not title:
            raise ValueError("Title cannot be empty.")
        if not author:
            raise ValueError("Author name cannot be empty.")
        if publication_year <= 0:
            raise ValueError("Publication year must be a positive number.")
        if pages <= 0:
            raise ValueError("Number of pages must be a positive number.")
        
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__genre = genre
        self.__pages = pages

    def __repr__(self) -> str:
        """
        Return a string representation of the Book object.

        The string representation includes the title, author, and publication year of the book.

        Parameters:
        None

        Returns:
        str: A string representation of the Book object in the format:
            "Book(title='{self.title}', author='{self.author}', year={self.publication_year})"
        """
        return(
            f"""Book(title='{self.title}', 
            author='{self.author}', 
            year={self.publication_year})"""
        )


    @property
    def title(self) -> str:
        """
        Get the title of the book.

        Returns:
        str: The title of the book.

        Note:
        This method returns the title of the book. The title is stored as a private attribute and can be accessed through this method.
        """
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        """
        Set the title of the book.

        Parameters:
        value (str): The title of the book. It should be a non-empty string.
            This parameter is used to set the new title of the book.

        Returns:
        None: This method does not return any value. It modifies the internal state of the book object.
            The new title is stored in the private attribute `__title`.

        Raises:
        ValueError: If the provided value is an empty string, a ValueError is raised.
        """
        if not value:
            raise ValueError("Title cannot be empty.")
        self.__title = value

    @property
    def author(self) -> str:
        """
        Get the author of the book.

        Returns:
        str: The author of the book.

        Note:
        This method returns the author of the book. The author is stored as a private attribute and can be accessed through this method.
        """
        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        """
        Set the author of the book.

        Parameters:
        value (str): The author of the book. It should be a non-empty string.
            This parameter is used to set the new author of the book.

        Returns:
        None: This method does not return any value. It modifies the internal state of the book object.
            The new title is stored in the private attribute `__author`.

        Raises:
        ValueError: If the provided value is an empty string, a ValueError is raised.
        """
        if not value:
            raise ValueError("Author name cannot be empty.")
        self.__author = value

    @property
    def publication_year(self) -> int:
        """
        Get the publication year of the book.

        Returns:
        int: The publication year of the book.
        """
        return self.__publication_year

    @publication_year.setter
    def publication_year(self,value: int) -> None:
        """
        Set the publication year of the book.

        Parameters:
        value (int): The publication year of the book. It should be a positive integer.

        Returns:
        None: This method does not return any value. It modifies the internal state of the book object.
        """
        if value <= 0:
            raise ValueError("Publication year must be a positive number.")
        self.__publication_year = value


class Library:
    def __init__(self):
        """
        Initialize a new instance of the Library class.

        Parameters:
        None

        Returns:
        None: This method does not return any value. It initializes a new instance of the Library class.
        """
        self.__books: List[Book] = []

    def __repr__(self):
        return f"Library({self.__books})"

    def add_book(self, book: Book) -> None:
        """
        Add a book to the library.

        Parameters:
        book (Book): The book to be added to the library.

        Returns:
        None: This method does not return any value. It modifies the internal state of the library object.
        """
        self.__books.append(book)

    def remove_book(self, book: Book) -> None:
        """
        Remove a book from the library.

        Parameters:
        book (Book): The book to be removed from the library.

        Returns:
        None: This method does not return any value. It modifies the internal state of the library object.
        """
        if book in self.__books:
            self.__books.remove(book)

    def search_by_title(self, title: str) -> Optional[Book]:
        """
        Search for a book by its title.

        Parameters:
        title (str): The title of the book to be searched.

        Returns:
        Optional[Book]: The book with the matching title if found, otherwise None.
        """
        for book in self.__books:
            if book.title == title:
                return book.title
        return None

    def get_books_by_author(self, author: str) -> List[Book]:
        """
        Get all books by a specific author.

        Parameters:
        author (str): The author whose books are to be retrieved.

        Returns:
        List[Book]: A list of books written by the specified author.
        """
        return [book for book in self.__books if book.author == author]

    def get_books_sorted_by_year(self) -> None:
        """
        Get all books sorted by their publication year.

        Parameters:
        None

        Returns:
        None: This method does not return any value. It returns a sorted list of books.
        """
        return sorted(self.__books, key=lambda book: book.publication_year)


def main():
    # Пример использования
    library = Library()
    book1 = Book("Название1", "Автор1", 2001, "Жанр1", 300)
    book2 = Book("Название2", "Автор2", 1999, "Жанр2", 150)
    library.add_book(book1)
    library.add_book(book2)
    print(library.search_by_title("Название1"))
    print(library.get_books_by_author("Автор1"))
    print(library.get_books_sorted_by_year())

if __name__ == '__main__':
    main()
    