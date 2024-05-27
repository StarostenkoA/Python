from datetime import date

class BookCard ():
    __author = ''
    __title = '' 
    __year = 2024
    
    def __init__(self, author,title,year) -> None:
        self.author = author
        self.title = title
        self.year = year
    
    def __eq__(self, other_BookCard ) -> bool:
        return self.year == other_BookCard.year

    def __ne__(self, other_BookCard ) -> bool:
        return self.year != other_BookCard.year

    def __lt__(self, other_BookCard ) -> bool:
        return self.year < other_BookCard.year

    def __gt__(self, other_BookCard ) -> bool:
        return self.year > other_BookCard.year

    def __le__(self, other_BookCard ) -> bool:
        return self.year <= other_BookCard.year

    def __ge__(self, other_BookCard ) -> bool:
        return self.year >= other_BookCard.year

    @property #getter  
    def autor(self):
        return self.__author
    
    @autor.setter
    def autor(self, val):
        if isinstance(val, str):
            self.__author = val
        else:
            raise ValueError ("autor is not str")
        
    @property #getter  
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, val):
        if isinstance(val, str):
            self.__title = val
        else:
            raise ValueError ("title is not str")
        
    @property #getter  
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, val):
        if not isinstance(val, int):
            raise ValueError ("year is not int")
        elif val < 0 or val > date.today().year:
            print(date.today().year)
            raise ValueError ("year is not range 0-2024")
        else:
            self.__year = val
            
book = BookCard("King","Strah",1997)
