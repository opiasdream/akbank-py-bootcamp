import constants as const
from library import Library

print(const.menu)

while(1):
    ### user input
    selection = input("Enter your selection (1-5): ")
    
    if(selection == "1"):
        Library.book_list()
    elif(selection == "2"):
        Library.add_book()
    elif(selection == "3"):
        Library.remove_book()
    elif(selection == "4"):
        Library.update_book()
    elif(selection == "5"):
        Library.search_book()
    elif(selection == "Q" or selection == "q"):
        print("Goodbye!")
        quit()
    else:
        print("\033[91mInvalid selection!\x1B[0m")
    

