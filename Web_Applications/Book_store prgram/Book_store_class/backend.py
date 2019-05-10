import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        #conn.close()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book values(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        #self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        #self.conn.close()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        #self.conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        #self.conn.close()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
        #self.conn.close()

    def __del__(self):
        self.conn.close()



#insert("The Sun", "John Machel", 1566, 91323315)
#delete(2)
#update(4,"The Moon", "John Smooth",1917,4564646)
#print(view())
#print(search(author="John Smith"))
