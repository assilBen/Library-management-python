
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Define function to register a book
def bookRegister():
    # Get book details from entry fields
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    # SQL query to insert book details into the database
    insertBooks = "insert into "+bookTable+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        # Execute the SQL query
        cur.execute(insertBooks)
        # Commit the changes to the database
        con.commit()
        # Show success message
        messagebox.showinfo('Success', "Book added successfully")
    except:
        # Show error message if insertion fails
        messagebox.showinfo("Error", "Can't add data into Database")
    
    # Print book details (for testing)
    print(bid)
    print(title)
    print(author)
    print(status)
    
    # Close the window after adding book details
    root.destroy()

# Define function to add a book
def addBook(): 
    # Define global variables
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
    
    # Create the root window
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Database connection parameters
    mypass = "cxvfAaasA3423@"
    mydatabase = "db"

    # Connect to MySQL database
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Define table name
    bookTable = "books" # Book Table

    # Create a canvas widget
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)
    
    # Create a frame for the heading
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    # Create a heading label
    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Create a frame for labels and entry fields
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
        
    # Label and Entry field for Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Label and Entry field for Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Label and Entry field for Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Label and Entry field for Book Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
        
    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
    # Enter the Tkinter event loop
    root.mainloop()