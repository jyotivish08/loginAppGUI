from tkinter import *
from PIL import ImageTk, Image  #imported from pillow to add image on screen
from tkinter import messagebox # to show message box like login sucessful

def handle_login():
    print('click')
    email = email_input.get()
    password = password_input.get()

    if email== 'jyoti@gmail.com' and password == '1234':
        messagebox.showinfo('yayy', 'Login successful')
    else:
        messagebox.showerror('Error', 'Login Failed')


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
text_label.config(font=('verdana', 24))

#MAKING TABLE 

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana', 12))
email_input = Entry(root, width=50)
email_input.pack(ipady = 5, pady=(1,10))


password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana', 12))
password_input = Entry(root, width=50)
password_input.pack(ipady = 5, pady=(1,10))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, command = handle_login )
login_btn.pack(pady=(14,20))
text_label.config(font=('verdana', 12))





root.mainloop() 