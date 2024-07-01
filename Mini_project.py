from tkinter import * 
import tkinter.messagebox as MessageBox
import mysql.connector as project

def sign_up_window():
    sign_up_window = Tk()
    sign_up_window.title("Sign Up Window")
    sign_up_window.geometry("500x500")
    
    def Sign_up():
        User_id = entry_sign_up0.get()
        Username=entry_sign_up1.get()
        Password=entry_sign_up2.get()
 
        if( User_id == "" or Username=="" or Password == ""):
            MessageBox.showinfo("ALERT", "Please enter all fields")
           
        else:
            con = project.connect(host="localhost", user="root", password="Pawan@2811", database="project")
            cursor=con.cursor()
            cursor.execute("insert into users values( '"+User_id+"','"+Username+"' ,'"+Password+"')")
            cursor.execute("commit")
            MessageBox.showinfo("Status", " Sign Up Successfull.")
            con.close()

    sign_up1 = Label(sign_up_window, text='Sign Up form', font='times 20')
    sign_up1.place(x=150, y=20)
    User_id = Label(sign_up_window, text='User ID :')
    User_id.place(x=120, y=100)
    entry_sign_up0 = Entry(sign_up_window )
    entry_sign_up0.place(x=220, y=100)
    Username = Label(sign_up_window, text='Username :')
    Username.place(x=120, y=150)
    entry_sign_up1 = Entry(sign_up_window )
    entry_sign_up1.place(x=220, y=150)
    Password = Label(sign_up_window, text='Password :')
    Password.place(x=120, y=200)
    entry_sign_up2 = Entry(sign_up_window )
    entry_sign_up2.place(x=220, y=200)
    button_sign_up = Button(sign_up_window, text='Sign up', command=Sign_up)
    button_sign_up.place(x=200, y=280)

def show_window(result):
            show_window = Tk()
            show_window.title("Show_window")
            show_window.geometry("500x500")
            show_window.configure(bg="white")
            
            label0=Label(show_window, text='Item_id')
            label0.grid(row=0, column=0)
            label1=Label(show_window, text='Item_name')
            label1.grid(row=0, column=1)
            label2=Label(show_window, text='Quantity')
            label2.grid(row=0, column=2)
            label3=Label(show_window, text='MRP')
            label3.grid(row=0, column=3)
            for i in result :
                label1=Label(show_window, text=i[0], bg="white") 
                label1.grid(row=i[0], column=0)
                label2=Label(show_window, text=i[1], bg="white")
                label2.grid(row=i[0], column=1)
                label3=Label(show_window, text=i[2], bg="white")
                label3.grid(row=i[0], column=2)
                label4=Label(show_window, text=i[3], bg="white")
                label4.grid(row=i[0], column=3)

def login_window():
    second_window = Tk()
    second_window.geometry("500x500")
    second_window.title("login Window")
    window.destroy()

    def login():
         Username=entry_login1.get()
         Password=entry_login2.get()
 
         if(Username=="" or Password == ""):
             MessageBox.showinfo("ALERT", "Please enter all fields")
           
         else:
             con = project.connect(host="localhost", user="root", password="Pawan@2811", database="project")
             cursor=con.cursor()

             
             query = "select * from users where Username=(%s) and Password=(%s)"
             cursor.execute(query, (Username, Password))
             result = cursor.fetchone()
             
             if result:
                 Item_window()
             else:
                 MessageBox.showinfo("Status", "Invalid Username or Password.")
            
             con.close()
    
    def Item_window():
        item_window = Tk()
        item_window.geometry("500x500")
        item_window.title("item Window")
        second_window.destroy()

        #add method
        def add():
             item_id = item_id_entry.get()
             item = item_entry.get()
             quantity = quantity_entry.get()
             price = price_entry.get()
    
             if(item_id=="" or item == "" or quantity == "" or price == ""):
                 MessageBox.showinfo("ALERT", "Please enter all fields")
             else:
                 con = project.connect(host="localhost", user="root", password="Pawan@2811", database="project")
                 cursor = con.cursor()
                 cursor.execute("insert into added values('"+item_id+"','" + item +"', '"+ quantity +"', '" + price +"')")
                 cursor.execute("commit")
                 MessageBox.showinfo("Status", "Successfully added.")
                 con.close();

        #sell method
        def sell():
            item_id = item_id_entry.get()
            item = item_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()

            if(item == "" or quantity == "" or price == ""):
               MessageBox.showinfo("ALERT", "Please enter all fields")
    
            else:
                con = project.connect(host="localhost", user="root", password="Pawan@2811", database="project")
                cursor = con.cursor()
                cursor.execute("insert into sold values('"+item_id+"','" + item +"', '"+ quantity +"', '" + price +"')")
                cursor.execute("commit")
                MessageBox.showinfo("Status", "Successfully sold.")
                con.close(); 
        
        #update method
        def update():
            item_id = item_id_entry.get()
            item = item_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()
            
            if(item_id=="" or item == "" or quantity == "" or price == ""):
                MessageBox.showinfo("ALERT", "Please enter all fields")
            
            else:
                con = project.connect(host="localhost", user="root", password="Pawan@2811", database="project")
                cursor = con.cursor()
                query = "UPDATE added SET item_name = %s, quantity = %s, MRP = %s WHERE item_id = %s"
                cursor.execute(query, (item, quantity, price, item_id)) 
                cursor.execute("commit")
                MessageBox.showinfo("Status", "Successfully updated.")
                show_all_item()
                con.close();
        
        #show_sold method
        def show_sold():
            con = project.connect(host="localhost", user="root", password="Pawan@2811", database="project")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM sold")
            result = cursor.fetchall()
            show_window(result)
            con.close()
            

        #show_all_item method
        def show_all_item():
           con = project.connect(host="localhost", user="root", password="Pawan@2811", database="project")
           cursor = con.cursor()
           cursor.execute("SELECT * FROM added")
           result = cursor.fetchall()
           show_window(result)
           con.close()
        
        #store name
        store_name= Label(item_window, text='Daily Market', font='times 20')
        store_name.place(x=180,y=20)

        #widgets of item window
        item_id=Label(item_window, text='Item ID :')
        item_id.place(x=120 ,y=100)        
        item_id_entry = Entry(item_window)
        item_id_entry.place(x=220 ,y=100)    
        item=Label(item_window, text='Item name: ')
        item.place(x=120,y=140)
        item_entry = Entry(item_window )
        item_entry.place(x=220, y=140)
        quantity = Label(item_window, text='Quantity : ')
        quantity.place(x=120,y=180)
        quantity_entry = Entry(item_window )
        quantity_entry.place(x=220, y=180)
        price = Label(item_window, text='MRP : ')
        price.place(x=120, y=220)
        price_entry = Entry(item_window)
        price_entry.place(x=220, y=220)
        button_add = Button(item_window, text='ADD', command=add)
        button_add.place(x=150, y=300)
        button_sell = Button(item_window, text='SELL', command=sell)
        button_sell.place(x=250, y=300)
        button_update = Button(item_window, text='UPDATE', command=update)
        button_update.place(x=350, y=300)
        button_show_sold = Button(item_window, text='SHOW SOLD ITEM' , command=show_sold)
        button_show_sold.place(x=100, y=400)
        button_show_available = Button(item_window, text='SHOW ALL ITEM', command=show_all_item )
        button_show_available.place(x=300 , y=400)
         
    sign_up1 = Label(second_window, text='Login form', font='times 20')
    sign_up1.place(x=150, y=20)
    Username = Label(second_window, text='Username : ' )
    Username.place(x=120 ,y=100)
    entry_login1 = Entry(second_window)
    entry_login1.place(x=220 ,y=100)
    Password = Label(second_window, text='Password : ' )
    Password.place(x=120 ,y=160)
    entry_login2 = Entry(second_window)
    entry_login2.place(x=220 ,y=160)
    button_login = Button(second_window, text='login' ,command=login)
    button_login.place(x=200 ,y=220)


window=Tk()
window.title('inventary management')
window.geometry('500x500')

frame = Frame(window, bg='#e7e7e7')
frame.pack(fill = "both", expand = 1)

label1 = Label(frame, text='Inventary Management', bg='white', fg='black' , font='times 20')
label1.place(x=120, y=100)

button_sign_up_window = Button(frame, text='Sign up ', command=sign_up_window )
button_sign_up_window.place(x=180, y=200)

button_login_window = Button(frame, text='Login', command=login_window)
button_login_window.place(x=280, y=200)

window.mainloop()
