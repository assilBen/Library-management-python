from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
mypass = "cxvfAaasA3423@" #use your own password
mydatabase="db" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.25

# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.LANCZOS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)
