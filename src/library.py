import string
from typing import IO
import constants as const
from book import Book
from helper import clear_terminal


class Library:
    """
    This class represents a library. It provides methods for managing a collection of books.
    """
    def __init__(self):None
    pass

    def open_file(self, mode:str = "a+") -> IO:
        """
        Opens a file in read or append mode.

        Args:
            mode (str): The mode in which the file should be opened. Default is "a+".

        Returns:
            IO: A file object.
        """
        
        return open("books.txt", mode)
    
    def go_back(self):
        """
        Waits for user input to return to the main menu.
        """
        
        input("Press a key to return to the main menu\n")
        
    def unknown_error(self):
        """
        Prints a message for an unknown error.
        """
        
        print("\033[91mAn unknown error occurred!\x1B[0m")

    def print_book_list(self) -> list:
        """
        Prints a list of books from a file and returns the list of books.

        Returns:
            list: A list of books.
        """
        
        try:
            try:
                with self.open_file('r') as file:
                    lines = file.read().splitlines()
            except:
                with self.open_file('a+') as file:
                    lines = file.read().splitlines()
                    
            file.close()
        
            print(const.book_list_table_header)
            
            for idx, i in enumerate(lines):
                    temp:Book = Book.fromString(i)
                    print(f"│ {idx+1} | {temp.shorten_title()} | {temp.shorten_author()} │")
                    
            print(const.book_list_table_footer)
            
            return lines
        except:
            self.unknown_error()
            return []
        
        
    def book_list(self):
        """
        Clears the screen, prints a book list, and then prints the book list.
        """
        try:
            clear_terminal()
            print(const.book_list)

            self.print_book_list()        
        except:
            self.unknown_error()
        
        finally:
            self.go_back()
        
    def add_book(self):
        """
        Clears the screen, prompts the user to enter book details, writes the book details to a file, and prints a success message.
        """
        
        try:
            clear_terminal()
            print(const.add_book)
        
            book = Book(
                title = input("Enter book title: "),
                author = input("Enter book author: "),
                publish_year = input("Enter book publish year: "),
                pages = input("Enter number of book pages: ")
            )
        
            with self.open_file() as file:
                file.write(book.toString() + "\n"),
            file.close()
            
            print("\033[92mBook added successfully!\x1B[0m")
        except:
            self.unknown_error()
        finally:
            self.go_back()
    
    def remove_book(self):
        """
        Clears the screen, prompts the user to enter book details, writes the book details to a file, and prints a success message.
        """
        
        try:
            clear_terminal()
            print(const.remove_book)
            
            lines = self.print_book_list()

            if(len(lines) <= 0):
                print("\033[91mNo books found!\x1B[0m")
                return
            
            print("Press 'Q' to return to the main menu.") 
            while(1):
                selection = input("Enter book number to remove (1-" + str(len(lines)) + "): ")
                if selection in ["q","Q"]: return
                selection = "0" + selection
                selection = int(selection.strip(string.ascii_letters))

                
                if(selection <= len(lines) and selection > 0):
                    with self.open_file('w') as file:
                        for idx, i in enumerate(lines):
                            if(idx+1 != int(selection)):
                                file.write(i + "\n")
                        file.close()
                    print("\033[92mBook removed successfully!\x1B[0m")

                    break
                else:
                    print("\033[91mInvalid selection!\x1B[0m")  
                    
        except Exception as e:
            self.unknown_error()

        self.go_back()
    
    def update_book(self):
        """
        Clears the screen, prints an update book message, prints the book list, prompts the user for a book number to update, and then updates the selected book.
        """
        
        try:
            clear_terminal()
            print(const.update_book)
            
            lines = self.print_book_list()
            
            if(len(lines) <= 0):
                print("\033[91mNo books found!\x1B[0m")
                return
            
            print("Press 'Q' to return to the main menu.")
            while(1):
                selection = input("Enter book number to update (1-" + str(len(lines)) + "): ")
                if selection in ["q","Q"]: return
                selection = "0" + selection
                selection = int(selection.strip(string.ascii_letters))

                
                if(selection <= len(lines) and selection > 0):
                    with self.open_file('w') as file:
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
            self.unknown_error()
        finally:
            self.go_back()
