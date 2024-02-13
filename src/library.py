import os
from typing import IO
import constants as const
from book import Book
import string


class Library:
    """
    This class represents a library. It provides methods for managing a collection of books.
    """

    def open_file(mode:str = "a+") -> IO:
        """
        Opens a file in read or append mode.

        Args:
            mode (str): The mode in which the file should be opened. Default is "a+".

        Returns:
            IO: A file object.
        """
        
        return open("src/books.txt", mode)
    
    def go_back():
        """
        Waits for user input to return to the main menu.
        """
        
        input("Press a key to return to the main menu\n")
        
    def unknown_error():
        """
        Prints a message for an unknown error.
        """
        
        print("\033[91mAn unknown error occurred!\x1B[0m")

    def print_book_list() -> list:
        """
        Prints a list of books from a file and returns the list of books.

        Returns:
            list: A list of books.
        """
        
        try:
            try:
                with Library.open_file('r') as file:
                    lines = file.read().splitlines()
            except:
                with Library.open_file('a+') as file:
                    lines = file.read().splitlines()
                    
            file.close()
        
            print(const.book_list_table_header)
            
            for idx, i in enumerate(lines):
                    temp:Book = Book.fromString(i)
                    print(f"│ {idx+1} | {temp.shorten_title()} | {temp.shorten_author()} │")
                    
            print(const.book_list_table_footer)
            
            return lines
        except:
            Library.unknown_error()
            return []
        
        
    def book_list():
        """
        Clears the screen, prints a book list, and then prints the book list.
        """
        try:
            os.system('clear')
            print(const.book_list)

            Library.print_book_list()        
        except:
            Library.unknown_error()
        
        finally:
            Library.go_back()
        
    def add_book():
        """
        Clears the screen, prompts the user to enter book details, writes the book details to a file, and prints a success message.
        """
        
        try:
            os.system('clear')
            print(const.add_book)
            
            book = Book(
                title = input("Enter book title: "),
                author = input("Enter book author: "),
                publish_year = input("Enter book publish year: "),
                pages = input("Enter number of book pages: ")
            )
        
            with Library.open_file() as file:
                file.write(book.toString() + "\n"),
            file.close()
            
            print("\033[92mBook added successfully!\x1B[0m")
        except:
            Library.unknown_error()
        finally:
            Library.go_back()
    
    def remove_book():
        """
        Clears the screen, prompts the user to enter book details, writes the book details to a file, and prints a success message.
        """
        
        try:
            os.system('clear')
            print(const.remove_book)
            
            lines = Library.print_book_list()

            if(len(lines) <= 0):
                print("\033[91mNo books found!\x1B[0m")
                return
            
            while(1):
                selection = input("Enter book number to remove (1-" + str(len(lines)) + "): ")
                selection = "0" + selection
                selection = int(selection.strip(string.ascii_letters))

                
                if(selection <= len(lines) and selection > 0):
                    with Library.open_file('w') as file:
                        for idx, i in enumerate(lines):
                            if(idx+1 != int(selection)):
                                file.write(i + "\n")
                        file.close()
                    print("\033[92mBook removed successfully!\x1B[0m")
                    break
                else:
                    print("\033[91mInvalid selection!\x1B[0m")  
                    
        except Exception as e:
            Library.unknown_error()
        finally:
            Library.go_back()
    
    def update_book():
        """
        Clears the screen, prints an update book message, prints the book list, prompts the user for a book number to update, and then updates the selected book.
        """
        
        try:
            os.system('clear')
            print(const.update_book)
            
            lines = Library.print_book_list()
            
            if(len(lines) <= 0):
                print("\033[91mNo books found!\x1B[0m")
                return
            
            while(1):
                selection = input("Enter book number to update (1-" + str(len(lines)) + "): ")
                selection = "0" + selection
                selection = int(selection.strip(string.ascii_letters))

                
                if(selection <= len(lines) and selection > 0):
                    with Library.open_file('w') as file:
                        for idx, i in enumerate(lines):
                            if(idx+1 == int(selection)):
                                book = Book(
                                    title = input("Enter new book title: "),
                                    author = input("Enter new book author: "),
                                    publish_year = input("Enter new book publish year: "),
                                    pages = input("Enter new number of book pages: ")
                                )
                                file.write(book.toString() + "\n")
                            else:
                                file.write(i + "\n")
                        file.close()
                    print("\033[92mBook updated successfully!\x1B[0m")
                    break
                else:
                    print("\033[91mInvalid selection!\x1B[0m")
        except:
            Library.unknown_error()
        finally:
            Library.go_back()
