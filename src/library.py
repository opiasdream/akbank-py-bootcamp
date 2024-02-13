import os
from typing import IO
import constants as const
from book import Book


class Library:

    def open_file(mode:str = "a+") -> IO:
        return open("books.txt", mode)
        
    def book_list():
        os.system('clear')
        print(const.book_list)
    
        with Library.open_file('r') as file:
            lines = file.read().splitlines()
                  
        file.close()
        
        print(const.book_list_table_header)
        
        for idx, i in enumerate(lines):
            temp:Book = Book.fromString(i)
            
            print(f"│ {idx+1} | {temp.shorten_title()} | {temp.shorten_author()} │")
            
        print(const.book_list_table_footer)
    
    def add_book():
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
    
    def remove_book():
        print("remove book")
    
    def update_book():
        print("update book")
    
    def search_book():
        print("search book")
