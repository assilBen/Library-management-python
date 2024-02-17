from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "cxvfAaasA3423@"
mydatabase="db"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" 

# Define a function to display all books in the library
def View(): 
    
    # Create the root window
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Create a canvas widget
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)

    # Create a frame for the heading
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    # Create a label for the heading
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    # Create a frame for displaying book details
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    # Create labels for column headings
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable

    try:
        # Execute the SQL query to fetch all books
        cur.execute(getBooks)
        con.commit()

        # Iterate over the fetched books and display them
        for i in cur:
            Label(labelFrame,text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        # Show error message if fetching fails
        messagebox.showinfo("Failed to fetch files from database")
    
    # Create a button to quit the window
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Enter the Tkinter event loop
    root.mainloop()
