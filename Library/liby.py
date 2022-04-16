import sqlite3
import time

class book():
    def __init__(self,name,author,publisher,kind,press):
        self.name =name
        self.author = author
        self.publisher = publisher
        self.kind = kind
        self.press = press
    def __str__(self):
        return" Book name : {}\nauthor : {}\npublisher : {}\nkind : {}\npress : {}\n".format(self.name,self.author,self.publisher, self.kind,self.press)
class Lib():
    def __init__(self):
        self.creat_connetion()

    def creat_connetion(self):
        self.connection =sqlite3.connect("Library.db")
        self.cursor =self.creat_connetion()
        sorgu ="Creat Table If not exists books(name TEXT,author TEXT,publisher TEXT,kind TEXT,press INT)"
        self.cursor.execute(sorgu)
        self.connection.commit()
    def cls_con(self):
        self.cls_con.close()
    def show_books(self):
        sorgu = "select * From books"
        self.cursor.execute(sorgu)
        books =self.cursor.fetchall()
        if(len(books)==0):
            print("Library has not book!")
        else:
            for i in books:
                book =book(i[0],i[1],i[2],i[3],i[4])
                print(book)
    def book_sorgula(self,name):
        sorgu = "select * from books where name = ?"
        self.cursor.execute(sorgu,(name,))
        books =self.cursor.fetchall()
        if(len(books)==0):
            print("not exist book")
        else:
            books = books(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(books)
    def add_book(self,book):
        sorgu ="insert into books values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(book.name,book.author,book.publisher,book.kind,book.press))
        self.connection.commit()
    def delete_book(self,name):
        sorgu = "Delete From books Where name =?"
        self.cursor.execute(sorgu,(name,))
        self.connection.commit()
    def update_press(self,name):
        sorgu ="Select *From books Where name=?"
        self.cursor.execute(sorgu,(name,))
        books =self.cursor.fetchall()
        if (len(books)==0):
            print("not exist book")
        else:
            press =books[0][4]
            press +=1
            sorgu2="Update books ser press = ? where name =?"
            self.cursor.execute(sorgu2,(press,name))
            self.connection.commit()

