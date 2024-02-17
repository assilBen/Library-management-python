from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from tkinter import *
from PIL import Image, ImageTk

mypass = "cxvfAaasA3423@" #use your own password
mydatabase="db" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor
# Import the necessary modules

# Create a Tkinter root window
root = Tk()

# Set the title of the window
root.title("Library")

# Set the minimum size of the window
root.minsize(width=400, height=400)

# Set the geometry of the window
root.geometry("600x500")

# Initialize variables
same = True
n = 0.25

# Adding a background image
background_image = Image.open("lib.jpg")

# Get the size of the background image
[imageSizeWidth, imageSizeHeight] = background_image.size

# Calculate the new size of the background image
newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

# Resize the background image
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.LANCZOS)

# Convert the background image to a PhotoImage object
img = ImageTk.PhotoImage(background_image)

# Create a canvas widget
Canvas1 = Canvas(root)

# Create an image on the canvas
Canvas1.create_image(300, 340, image=img)

# Configure the canvas properties
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)

# Pack the canvas widget into the root window
Canvas1.pack(expand=True, fill=BOTH)

# Create a frame widget with background color '#FFBB00' and border width 5
headingFrame1 = Frame(root, bg="#2C3E50", bd=5)

# Place the headingFrame1 widget relative to its parent widget (root)
# The position is defined as 20% from the left and 10% from the top of the parent widget
# The width and height of the widget are defined as 60% of the width and 16% of the height of the parent widget, respectively
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

# Create a label widget within the headingFrame1 widget
# The label text is set to "Welcome to \n Your Library"
# Background color is set to '#2C3E50' (a dark blue), foreground color is set to 'white'
# Font is set to Arial with size 20, bold
headingLabel = Label(headingFrame1, text="Welcome to \n Your Library", bg='#2C3E50', fg='white', font=('Arial', 20, 'bold'))

# Place the headingLabel widget relative to its parent widget (headingFrame1)
# The label is placed at (0,0) relative to the top-left corner of the parent widget
# The width and height of the label widget are set to match the parent widget
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Adding the Buttons


# Create a button widget for adding book details
btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)

# Place the btn1 widget relative to its parent widget (root)
# The position is defined as 28% from the left and 40% from the top of the parent widget
# The width and height of the widget are defined as 45% of the width and 10% of the height of the parent widget, respectively
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

# Create a button widget for deleting books
btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)

# Place the btn2 widget relative to its parent widget (root)
# The position is defined as 28% from the left and 50% from the top of the parent widget
# The width and height of the widget are defined as 45% of the width and 10% of the height of the parent widget, respectively
btn2.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

# Create a button widget for viewing the book list
btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)

# Place the btn3 widget relative to its parent widget (root)
# The position is defined as 28% from the left and 60% from the top of the parent widget
# The width and height of the widget are defined as 45% of the width and 10% of the height of the parent widget, respectively
btn3.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

# Create a button widget for issuing books to students
btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)

# Place the btn4 widget relative to its parent widget (root)
# The position is defined as 28% from the left and 70% from the top of the parent widget
# The width and height of the widget are defined as 45% of the width and 10% of the height of the parent widget, respectively
btn4.place(relx=0.28, rely=0.85, relwidth=0.45, relheight=0.1)

# Create a button widget for returning books
btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)

# Place the btn5 widget relative to its parent widget (root)
# The position is defined as 28% from the left and 80% from the top of the parent widget
# The width and height of the widget are defined as 45% of the width and 10% of the height of the parent widget, respectively
btn5.place(relx=0.28, rely=1, relwidth=0.45, relheight=0.1)

# Enter the Tkinter event loop
root.mainloop()

