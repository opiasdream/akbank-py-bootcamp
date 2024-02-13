import os
import constants as const
from library import Library

# Main function to start the program.
def main():
    """
    Display a menu and handle user selections.
    """
    
    os.system('clear')  # Clear the console screen
    print(const.menu)  # Display the menu options
    
    while True:
        selection = input("Enter your selection (1-4): ")  # Prompt user for input
        
        if selection == "1":
            Library.book_list()  # Display the list of books
        elif selection == "2":
            Library.add_book()  # Add a new book
        elif selection == "3":
            Library.remove_book()  # Remove a book
        elif selection == "4":
            Library.update_book()  # Update book information
        elif selection in ["Q", "q"]:
            print("Goodbye!")  # Display goodbye message
            quit()  # Exit the program
        else:
            print("\033[91mInvalid selection!\x1B[0m")  # Display error message

        main() # recursive call

main()

