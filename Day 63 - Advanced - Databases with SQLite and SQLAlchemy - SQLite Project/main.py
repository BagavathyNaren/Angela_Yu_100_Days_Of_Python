import sqlite3


"""
Now create a connection to a new database (if the database does not exist then it will be created).
"""


"""
Next we need to create a cursor which will control our database.

So a cursor is also known as the mouse or pointer.

If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data 
or edit/delete data, we also need a cursor to modify our SQLite database

"""












try:

    with sqlite3.connect("books-collection.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
        cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
        
        # Verify the insertion
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        print("Records in database:", rows)
  
except sqlite3.Error as e:
    print(f"Database error: {e}")




"""

SQLite Databases
First, let's create a database. The most used database in the world is SQLite. It's so popular that it's included by default in all Python installations, so if you're creating a Python project, you've already got it installed. We're going to create an SQLite database to store our book data.



Let's briefly play with SQLite in a separate project before we turn our attention back to Library website.



1. Create a new project and inside the main.py file import the sqlite3 module.

import sqlite3
2. Now create a connection to a new database (if the database does not exist then it will be created).

db = sqlite3.connect("books-collection.db")
3. Run main.py and you should see a new file appear in PyCharm called books-collection.db


NOTE: Don't try to open the .db file in PyCharm, it won't work, I'll show you how to download the software to open these files a little later.

4. Next we need to create a cursor which will control our database.

cursor = db.cursor()
So a cursor is also known as the mouse or pointer. If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data, we also need a cursor to modify our SQLite database.


Creating Tables in our Database
Coming back to the Excel analogy, a single Excel file can contain many tables (sheets), each tab is a different table.


Similarly, our database can contain many tables.

5. Let's create one. Add this code below all the previous lines.

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

Let's break this down.

cursor - We created this in step 4 and this is the mouse pointer in our database that is going to do all the work.

.execute() - This method will tell the cursor to execute an action. All actions in SQLite databases are expressed as SQL (Structured Query Language) commands. These are almost like English sentences with keywords written in ALL-CAPS. There are quite a few SQL commands. But don't worry, you don't have to memorise them.

CREATE TABLE -  This will create a new table in the database. The name of the table comes after this keyword.

Docs: https://www.w3schools.com/sql/sql_ref_create_table.asp

books -  This is the name that we've given the new table we're creating.

() -  The parts that come inside the parenthesis after CREATE TABLE books are going to be the fields in this table. Or you can imagine it as the Column headings in an Excel sheet.


id INTEGER PRIMARY KEY -  This is the first field. It's a field called "id" which is of data type INTEGER and it will be the PRIMARY KEY for this table. The primary key is the one piece of data that will uniquely identify this record in the table. e.g. The primary key of humans might be their passport number because no two people in the same country have the same passport number.

title varchar(250) NOT NULL UNIQUE -  This is the second field. It's called "title" and it accepts a variable-length string composed of characters. The 250 in brackets is the maximum length of the text. NOT NULL means it must have a value and cannot be left empty. UNIQUE means no two records in this table can have the same title.

author varchar(250) NOT NULL -  A field that accepts variable-length Strings up to 250 characters called author that cannot be left empty.

rating FLOAT NOT NULL -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called rating.



6. Run the code from step 5 and there will be no noticeable changes. In order to view our database we need to download some specialised software.

Head over to the link below and download DB Browser for your operating system. (If you are on Windows go for the Standard Installer).

https://sqlitebrowser.org/dl/

7. Once you've downloaded and installed DB Browser, open it and click on "Open Database".


8. Navigate to your project location (it should in a folder called PyCharm Projects) and open the books-collection.db


Now you should see a table called books that contains 4 fields:


This is our database.

9. To add data to our table we can head back to main.py and write the following code:

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
This will create a new entry in our books table for the Harry Potter book and commit the changes to our database.

10. Now comment out the previous line of code where you are created the table called books. Otherwise, you'll get sqlite3.OperationalError: table books already exists.

11. Then close down the database in DB Browser by clicking Close Database. Otherwise, you'll get a warning about database locked when you work with the database in PyCharm.


12. Now run the code in main.py and re-open the database in DB Browser to see the updated books table. it should look like this:


SQL queries are very sensitive to typos. If instead of writing:

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
You wrote:

cursor.execute("INSERT INTO books VALUE(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
Then it won't work at all (can you even spot the difference in the code?)

Luckily, there are much better ways of working with SQLite in Python projects, we can use a tool called SQLAlchemy to write Python code instead of all these error-prone SQL commands. That's what we'll do in the next lesson!



Code Snippet from this lesson.

# SQLite code snippet

import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")

db.commit()

"""