

class Book: 
    def __init__(self, title:str, author:str, publish_year:str, pages:str):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        

    def toString(self) -> str:
        return f"{self.title},{self.author},{self.publish_year},{self.pages}"
    
    def fromString(string:str) -> object:
        
        values = string.split(",")
        
        return Book(title=values[0], author=values[1], publish_year=values[2], pages=values[3])
        
    def shorten_title(self) -> str:
        if(len( self.title) > 37):
            return self.title[:37] + "..."
        elif(len( self.title) <= 37):
            return self.title.__add__(" " * (40 - len( self.title)))
        else:
            return self.title
    
    def shorten_author(self) -> str:
        if(len( self.author) > 27):
            return self.author[:27] + "..."
        elif(len( self.author) <= 27):
            return self.author.__add__(" " * (30 - len( self.author)))
        else:
            return self.author