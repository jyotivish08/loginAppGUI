from tkinter import *
from PIL import ImageTk, Image  #imported from pillow to add image on screen

root = Tk()

root.title('Login Form')
#root.iconbitmap('favicon.ico')

#root.minsize(400,100)
#root.maxsize(400,400)
root.geometry('350x500')

root.configure(background='#0096DC')

# ADDING iMAGE AND TEXT (FLIPKART)

#img = ImageTk.PhotoImage(Image.open('flipkart-logo.png'))
img = Image.open('flipkart-logo.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

# u use label to print text but u can also use it to print image, jo ki root/main page par baithega, aur uski value img daal di, jo upar image open ki thi hamne
img_label = Label(root, image=img)

#jab bhi aap label create karte ho, aapko usko explicitely bol kar k gui par bithana padta hai aur iske liye geometry mangaer ki jarurat hoti hai, jo ye decide karta hai ki koi bhi ui element screen par kaha jaa kar baithega, 2 type ke hote hai pack and grid, pad y for giving space upar neeche se
img_label.pack(pady=(10,10))

text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 22))

#MAKING TABLE 





root.mainloop() 