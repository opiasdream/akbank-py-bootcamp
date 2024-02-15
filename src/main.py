import os
import constants as const
from library import Library
from helper import clear_terminal

# Main function to start the program.
def main():
    clear_terminal()
    print(const.menu)  # Display the menu options
    
    while True:
        selection = input("Enter your selection (1-4): ")  # Prompt user for input

        library = Library()
        
        if selection == "1":
            library.book_list()  # Display the list of books
        elif selection == "2":
            library.add_book()  # Add a new book
        elif selection == "3":
            library.remove_book()  # Remove a book
        elif selection == "4":
            library.update_book()  # Update book information
        elif selection in ["Q", "q"]:
            print("Goodbye!")  # Display goodbye message
            quit()  # Exit the program
        else:
            print("\033[91mInvalid selection!\x1B[0m")  # Display error message

        main() # recursive call

main()

