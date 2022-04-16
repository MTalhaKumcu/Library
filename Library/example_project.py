from liby import *
import time

print("""
       Welcome Library Program
   transactions
   1- Showing Books
   2- Find a Book
   3- Add Book
   4- Delete Book
   5- Press Update
   exit for press q
""")
library = library()
while True:
    transactions = input("choose the transaction : ")
    if (transactions == "q"):
        print("have a good day bye!")
        break
    elif(transactions == "1"):
        library.show_books()
    elif (transactions == "2"):
        name =input("Enter book name: ")
        print("finding.....")
        time.sleep(2)

        library.book_sorgula(name)

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
                book = book (i[0],i[1],i[2],i[3],i[4])
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

