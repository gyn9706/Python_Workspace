class Book(object):
    def __init__(self,title,isbn):
        self._title=title
        self._isbn=isbn

    def __repr__(self): #Object(최고 조상 클래스) 
        return "ISBN:"+self._isbn+"; TITLE:"+self._title
    
book=Book("The Python Tutorial","0123456")
print(book.__repr__())