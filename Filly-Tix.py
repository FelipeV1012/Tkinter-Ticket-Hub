from tkinter import *
import tkinter as tk
import re
import os
from tkinter import messagebox
from datetime import datetime
import time as tm
import time
from tkinter import ttk

##################################################################################################
#password validation
def register_user():
    username_info = username.get()
    password_info = password.get()

    #file opening and closing to write
    #2 files for 1 password and 1 username for easier access
    lower, upper, digit = 0,0,0
    flag = 0
    index = 0
    userfile=open("username_info.txt", "r")
    for line in userfile:
        index +=1
        if username_info in line:
            flag = 1
            break
    if flag == 1:
        messagebox.showinfo("Error", "Username is already taken")
    else:
        if(len(password_info) >=9):
            for i in password_info:
                if(i.islower()):
                    lower+=1
                if(i.isupper()):
                    upper+=1
                if(i.isdigit()):
                    digit+=1
            if (lower >= 1 and upper >= 1 and digit >= 1):
                messagebox.showinfo("Success", "Account Creation Successful")
                userfile=open("username_info.txt", "a") 
                userfile.write(username_info+"\n")
                userfile.close()
                passfile=open("password_info.txt", "a")
                passfile.write(password_info+"\n")
                passfile.close()
                desScreen2()
            else:
                messagebox.showinfo("Error", "Password Requirements Not Met")
        else:
                messagebox.showinfo("Error", "Password Requirements Not Met")

    Label(screen1, text = "registration was successful", fg = "green", font = ("calibri", 11))
    #if register has password is correct and seeing if it is a new user and pass is valid
    

def register():
    global screen1

    screen1 = tk.Tk()
    screen1.title("register")
    screen1.geometry("500x250")
    screen1.config(bg = ('black'))
    screen1.eval('tk::PlaceWindow . center')


    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Enter your credentials",bg = "Black", fg= "Gold").pack()
    Label(screen1, text = "Password Must be 9 characters",bg = "Black", fg= "Gold").pack()
    Label(screen1, text = "Password Must have 1 uppercase and lower case",bg = "Black", fg= "Gold").pack()
    Label(screen1, text = "Password Must be 1 digit",bg = "Black", fg= "Gold").pack()
    
    Label(screen1, text = "Username ",bg = "Black", fg= "Gold").pack()
    username_entry = Entry(screen1, textvariable = username).pack()
    username_entry
    Label(screen1, text = "Password ",bg = "Black", fg= "Gold").pack()
    password_entry = Entry(screen1, textvariable = password).pack()
    password_entry
    Label(screen1,text = "",bg = "Black", fg= "Black").pack()
    Button(screen1, text = "Register", width = 10, height = 1,bg = "Black", fg= "Gold", command = register_user).pack()
    
##################################################################################################
#check to see if login has account
#check to see if password is 

#login verification
   
def login():
    global screen2
    screen.destroy()
    screen2 = tk.Tk()
    screen2.title("login")
    screen2.geometry("300x200")
    screen2.config(bg = ('black'))
    Label(screen2, text = "Please enter details below to login",bg = "Black", fg= "Gold").place(x=60,y=2)
    screen2.eval('tk::PlaceWindow . center')

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username",bg = "Black", fg= "Gold").place(x=60,y=40)
    username_entry1 = Entry(screen2, textvariable = username_verify).place(x=120,y=40)
    username_entry1

    Label(screen2, text = "Password",bg = "Black", fg= "Gold").place(x=60,y=70)
    password_entry1 = Entry(screen2, textvariable = password_verify).place(x=120,y=70)
    password_entry1
    Button(screen2, text = "Login" ,bg = "Black", fg= "Gold", width = 10, height = 1, command = login_verify,).place(x=120,y=100)


def  login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if (username1 == "Theman1012" and password1 == "Man123"):
        managerLogin()
        screen2.destroy()
        screen6.destroy()
    else:
        pass
        
    success = False
    try:
        with open("username_info.txt") as usernames, open("password_info.txt") as passwords:
            while True:
                name = next(usernames).rstrip()
                pw = next(passwords).rstrip()
                if name == username1 and pw == password1:
                    success = True
                    break
    except StopIteration:
        pass
    if success:
        messagebox.showinfo("title", "Login Success")
        screen2.destroy()
        Ticket_Select()
    else:
        messagebox.showwarning("title", "User not found")


    
##################################################################################################
#milestone 2 page after login
#selecting times
def Ticket_Select():
    global screen6
    screen6= tk.Tk()
    screen6.title("Ticket Selection")
    screen6.geometry("250x175")
    screen6.config(bg = ('black'))
    screen6.eval('tk::PlaceWindow . center')
    Label(screen6, text = 'Please Select Show Time',font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Button(screen6, text=' Evening ', width=20,font=("helvetica",17,"bold"),bg = "Black", fg= "Gold",command = Evening_Time).pack()
    Button(screen6, text=' Matinee ', width=20,font=("helvetica",17,"bold"),bg = "Black", fg= "Gold", command = Matinee_Time).pack()
#buttons for each of the times
def Matinee_Time():
    screen6.destroy()
    global screen7
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    if (current_time <= '12:30'):
        screen7= tk.Tk()
        screen7.title("Ticket Selection")
        screen7.geometry("750x550")
        screen7.config(bg = ('black'))
        Label(screen7, text = 'Please Select Your Seat',font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
        screen7.resizable(False,False)
        screen7.config(bg = ('black'))

        S_Price_Mat()
    
        photo = tk.PhotoImage(file="Theater.gif")
        T_pic= tk.Label(image= photo)
        T_pic.image = photo
        T_pic.place(x=50,y=50)
        var1= StringVar()
        var1.set("Front Row")
        frontrow = ("101","102","103","104","105")

        var2= StringVar()
        var2.set("Mid Row")
        midrow = ("106","107","108","109","110","111","112")
    
        var3= StringVar()
        var3.set("Balcony")
        balcony = ("201","202","203","204","205","206","207","208","209","210","211")
        
        frontrow_menu = tk.OptionMenu(screen7,var1,*frontrow)   
        frontrow_menu.config(bg="Black",fg="Gold")
        frontrow_menu.config(width=10)
        frontrow_menu.config(height=2)
        frontrow_menu["menu"].config(bg="Black",fg="Gold")
        frontrow_menu.place(x=550,y=125)


        midrow_menu = tk.OptionMenu(screen7,var2,*midrow)
        midrow_menu.config(bg="Black",fg="Gold")
        midrow_menu.config(width=10)
        midrow_menu.config(height=2)
        midrow_menu["menu"].config(bg="Black",fg="Gold")
        midrow_menu.place(x=550,y=225)
    

        balcony_menu = tk.OptionMenu(screen7,var3,*balcony)
        balcony_menu.config(bg="Black",fg="Gold")
        balcony_menu.config(width=10)
        balcony_menu.config(height=2)
        balcony_menu["menu"].config(bg="Black",fg="Gold")
        balcony_menu.place(x=550,y=325)

        midrow_menu.config(width=10)
        midrow_menu.config(height=2)
        midrow_menu["menu"].config(bg="Black",fg="Gold")
        midrow_menu.place(x=550,y=225)
    

        balcony_menu = tk.OptionMenu(screen7,var3,*balcony)
        balcony_menu.config(bg="Black",fg="Gold")
        balcony_menu.config(width=10)
        balcony_menu.config(height=2)
        balcony_menu["menu"].config(bg="Black",fg="Gold")
        balcony_menu.place(x=550,y=325)

        Label(screen7,font='ariel 12',bg="Black",fg="Gold",text="Current Time -").place(x=500,y=30)
        Label(screen7,font='ariel 12',bg="Black",fg="Gold",text=current_time).place(x=605,y=30)
        Label(screen7,font='ariel 12',bg="Black",fg="Gold",text="Show Time - 12:30").place(x=500,y=70)

        buy_button = Button(text=' BUY ', width=10, font=("helvetica",12,"bold"),bg="Black",fg="Gold", command=buyticketmat).place(x=550,y=425)
        
    elif (current_time >= '12:30'):
        Ticket_Select()
        messagebox.showinfo("Error", "Please Select Another Show time, To Late To This Show")
    

def Evening_Time():
    screen6.destroy()
    global screen8
    global var1
    global var2
    global var3
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    if (current_time <= '20:30'):
        screen8= tk.Tk()
        screen8.title("Ticket Selection")
        screen8.geometry("750x550")
        screen8.config(bg = ('black'))
        Label(screen8, text = 'Please Select Ticket',font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
        screen8.resizable(False,False)
        screen8.config(bg = ('black'))

        S_Price_eve()
    
        photo = tk.PhotoImage(file="Theater.gif")
        T_pic= tk.Label(image= photo)
        T_pic.image = photo
        T_pic.place(x=50,y=50)
        var1= StringVar()
        var1.set("Front Row")
        frontrow = ("Front Row","101","102","103","104","105")

        var2= StringVar()
        var2.set("Mid Row")
        midrow = ("Mid Row","106","107","108","109","110","111","112")
    
        var3= StringVar()
        var3.set("Balcony")
        balcony = ("Balcony","201","202","203","204","205","206","207","208","209","210","211")
        
        frontrow_menu = tk.OptionMenu(screen8,var1,*frontrow)   
        frontrow_menu.config(bg="Black",fg="Gold")
        frontrow_menu.config(width=10)
        frontrow_menu.config(height=2)
        frontrow_menu["menu"].config(bg="Black",fg="Gold")
        frontrow_menu.place(x=550,y=125)


        midrow_menu = tk.OptionMenu(screen8,var2,*midrow)
        midrow_menu.config(bg="Black",fg="Gold")
        midrow_menu.config(width=10)
        midrow_menu.config(height=2)
        midrow_menu["menu"].config(bg="Black",fg="Gold")
        midrow_menu.place(x=550,y=225)
    

        balcony_menu = tk.OptionMenu(screen8,var3,*balcony)
        balcony_menu.config(bg="Black",fg="Gold")
        balcony_menu.config(width=10)
        balcony_menu.config(height=2)
        balcony_menu["menu"].config(bg="Black",fg="Gold")
        balcony_menu.place(x=550,y=325)

    
        midrow_menu.config(width=10)
        midrow_menu.config(height=2)
        midrow_menu["menu"].config(bg="Black",fg="Gold")
        midrow_menu.place(x=550,y=225)
    

        balcony_menu = tk.OptionMenu(screen8,var3,*balcony)
        balcony_menu.config(bg="Black",fg="Gold")
        balcony_menu.config(width=10)
        balcony_menu.config(height=2)
        balcony_menu["menu"].config(bg="Black",fg="Gold")
        balcony_menu.place(x=550,y=325)

        Label(screen8,font='ariel 12',bg="Black",fg="Gold",text="Current Time -").place(x=500,y=30)
        Label(screen8,font='ariel 12',bg="Black",fg="Gold",text=current_time).place(x=605,y=30)
        Label(screen8,font='ariel 12',bg="Black",fg="Gold",text="Show Time - 20:30").place(x=500,y=70)

        buy_button = tk.Button(text=' BUY ', width=10, font=("helvetica",12,"bold"),bg="Black",fg="Gold", command=buyticketevening).place(x=550,y=425)

    elif (current_time >= '20:30'):
        Ticket_Select()
        messagebox.showinfo("Error", "Sorry For The Inconvience We Are Currently Closed, Check Back Another Time")
       
################################
#def statments to show pricing for the seats
def S_Price_eve():
    global screen9
    screen9= tk.Tk()
    screen9.title("Pricing")
    screen9.geometry("250x250")
    screen9.config(bg = ('black'))
    Label(screen9, text = 'Seat Pricing For Evening',font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    screen9.resizable(False,False)
    screen9.config(bg = ('black'))

    Label(screen9, text = "101-105 -$80",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen9, text = "108-110 -$60",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen9, text = "106,107,111 & 112 -$50",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen9, text = "205,206,207 -$40",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen9, text = "203,204,208,209 -$30",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen9, text = "201,202,210,211 -$20",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()

def S_Price_Mat():
    global screen10
    screen10= tk.Tk()
    screen10.title("Pricing")
    screen10.geometry("250x250")
    screen10.config(bg = ('black'))
    Label(screen10, text = 'Seat Pricing For Matinee',font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    screen10.resizable(False,False)
    screen10.config(bg = ('black'))
    screen10.eval('tk::PlaceWindow . center')

    Label(screen10, text = "101-105 -$50",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen10, text = "108-110 -$40",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen10, text = "106,107,111 & 112 -$30",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen10, text = "205,206,207 -$20",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen10, text = "203,204,208,209 -$15",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen10, text = "201,202,210,211 -$10",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
#####################################  

def buyticketevening():
    
    fileEV=open("seat_inv_user_ev.txt","a")
    try:
        with open("TicketEv.txt","r") as fileseat:
            invseat101 = IntVar()
            invseat101 = next(fileseat).rstrip()
            invseat102 = next(fileseat).rstrip()
            invseat103 = next(fileseat).rstrip()
            invseat104 = next(fileseat).rstrip()
            invseat105 = next(fileseat).rstrip()
            invseat106 = next(fileseat).rstrip()
            invseat107 = next(fileseat).rstrip()
            invseat108 = next(fileseat).rstrip()
            invseat109 = next(fileseat).rstrip()
            invseat110 = next(fileseat).rstrip()
            invseat111 = next(fileseat).rstrip()
            invseat112 = next(fileseat).rstrip()
            invseat201 = next(fileseat).rstrip()
            invseat202 = next(fileseat).rstrip()
            invseat203 = next(fileseat).rstrip()
            invseat204 = next(fileseat).rstrip()
            invseat205 = next(fileseat).rstrip()
            invseat206 = next(fileseat).rstrip()
            invseat207 = next(fileseat).rstrip()
            invseat208 = next(fileseat).rstrip()
            invseat209 = next(fileseat).rstrip()
            invseat210 = next(fileseat).rstrip()
            invseat211 = next(fileseat).rstrip()
    except StopIteration:
        pass
######Front Row
#the program will grab from the var list such as var1
#selects var 1 and sees what is inside of it
#if the seat is 0 then display error messages
#else is if not set to 0 then take the value and subtract it by 1
    if(var1.get()!= "frontrow"):
        seat = var1.get()
        if(seat == "101"):
            if(invseat101 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat101 = int(invseat101)
                invseat101-=1
                invseat101 = str(invseat101)
                cost = 80.00
                cost = str(cost)
            
        elif(seat == "102"):
            if(invseat102 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat102 = int(invseat102)
                invseat102-=1
                invseat102 = str(invseat102)
                cost = 80.00
                cost = str(cost)
            
        elif(seat == "103"):
            if(invseat103 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat103 = int(invseat103)
                invseat103-=1
                invseat103 = str(invseat103)
                cost = 80.00
                cost = str(cost)
            
        elif(seat == "104"):
            if(invseat104 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat104 = int(invseat104)
                invseat104-=1
                invseat104 = str(invseat104)
                cost = 80.00
                cost = str(cost)
            
        elif(seat == "105"):
            if(invseat105 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat105 = int(invseat105)
                invseat105-=1
                invseat105 = str(invseat105)
                cost = 80.00
                cost = str(cost)
            
#######MID ROW
            
    if(var2.get() != "Mid Row"):
        seat = var2.get()
        if(seat == "106"):
            if(invseat106 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat106 = int(invseat106)
                invseat106-=1
                invseat106 = str(invseat106)
                cost = 50.00
                cost = str(cost)
            
        elif(seat == "107"):
            if(invseat107 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat107 = int(invseat107)
                invseat107-=1
                invseat107 = str(invseat107)
                cost = 50.00
                cost = str(cost)

        elif(seat == "108"):
            if(invseat108 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat108 = int(invseat108)
                invseat108-=1
                invseat108 = str(invseat108)
                cost = 60.00
                cost = str(cost)
            
        elif(seat == "109"):
            if(invseat109 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat109 = int(invseat109)
                invseat109-=1
                invseat109 = str(invseat109)
                cost = 60.00
                cost = str(cost)
            
        elif(seat == "110"):
            if(invseat110 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat110 = int(invseat110)
                invseat110-=1
                invseat110 = str(invseat110)
                cost = 60.00
                cost = str(cost)
            
        elif(seat == "111"):
            if(invseat111 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat111 = int(invseat111)
                invseat111-=1
                invseat111 = str(invseat111)
                cost = 50.00
                cost = str(cost)

        elif(seat == "112"):
            if(invseat112 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat112 = int(invseat112)
                invseat112-=1
                invseat112 = str(invseat112)
                cost = 50.00
                cost = str(cost)
            
#######Balcony
    if(var3.get() != "Balcony"):
        seat = var3.get()
        if(seat == "201"):
            if(invseat201 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat201 = int(invseat201)
                invseat201-=1
                invseat201 = str(invseat201)
                cost = 20.00
                cost = str(cost)
            
        elif(seat == "202"):
            if(invseat202 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat202 = int(invseat202)
                invseat202-=1
                invseat202 = str(invseat202)
                cost = 20.00
                cost = str(cost)

        elif(seat == "203"):
            if(invseat203 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat203 = int(invseat203)
                invseat203-=1
                invseat203 = str(invseat203)
                cost = 30.00
                cost = str(cost)
            
        elif(seat == "204"):
            if(invseat204 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat204 = int(invseat204)
                invseat204-=1
                invseat204 = str(invseat204)
                cost = 30.00
                cost = str(cost)
            
        elif(seat == "205"):
            if(invseat205 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat205 = int(invseat205)
                invseat205-=1
                invseat205 = str(invseat205)
                cost = 40.00
                cost = str(cost)
            
        elif(seat == "206"):
            if(invseat206 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat206 = int(invseat206)
                invseat206-=1
                invseat206 = str(invseat206)
                cost = 40.00
                cost = str(cost)

        elif(seat == "207"):
            if(invseat207 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat207 = int(invseat207)
                invseat207-=1
                invseat207 = str(invseat207)
                cost = 40.00
                cost = str(cost)
            
        elif(seat == "208"):
            if(invseat208 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat208 = int(invseat208)
                invseat208-=1
                invseat208 = str(invseat208)
                cost = 30.00
                cost = str(cost)
            
        elif(seat == "209"):
            if(invseat209 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat209 = int(invseat209)
                invseat209-=1
                invseat209 = str(invseat209)
                cost = 30.00
                cost = str(cost)

        elif(seat == "210"):
            if(invseat210 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat210 = int(invseat210)
                invseat210-=1
                invseat210 = str(invseat210)
                cost = 20.00
                cost = str(cost)
            
        elif(seat == "211"):
            if(invseat211 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat211 = int(invseat211)
                invseat211-=1
                invseat211 = str(invseat211)
                cost = 20.00
                cost = str(cost)
            

    open("TicketEv.txt","w").close()
    file=open("TicketEv.txt","a")
    file.write(invseat101+"\n")
    file.write(invseat102+"\n")
    file.write(invseat103+"\n")
    file.write(invseat104+"\n")
    file.write(invseat105+"\n")
    file.write(invseat106+"\n")
    file.write(invseat107+"\n")
    file.write(invseat108+"\n")
    file.write(invseat109+"\n")
    file.write(invseat110+"\n")
    file.write(invseat111+"\n")
    file.write(invseat112+"\n")
    file.write(invseat201+"\n")
    file.write(invseat202+"\n")
    file.write(invseat203+"\n")
    file.write(invseat204+"\n")
    file.write(invseat205+"\n")
    file.write(invseat206+"\n")
    file.write(invseat207+"\n")
    file.write(invseat208+"\n")
    file.write(invseat209+"\n")
    file.write(invseat210+"\n")
    file.write(invseat211+"\n")
    file.close()

    global screen11
    screen11= tk.Tk()
    screen11.title("Ticket")
    screen11.geometry("600x350")
    screen11.config(bg = ('black'))
    Label(screen11, text = "Ticket Stub",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen11, text = "Username-"+username_verify.get(),font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen11, text = "Seat Number-"+seat,font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen11, text = "Seat Price-"+cost,font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen11, text = "Seating is genreal admission for all sections",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen11, text = "No Refunds",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen11, text = "Show Ticket at Door",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    

################################################################    
        
def buyticketmat():
    
    fileEV=open("seat_inv_user_n.txt","a")
    try:
        with open("TicketNight.txt","r") as fileseat:
            invseat101 = IntVar()
            invseat101 = next(fileseat).rstrip()
            invseat102 = next(fileseat).rstrip()
            invseat103 = next(fileseat).rstrip()
            invseat104 = next(fileseat).rstrip()
            invseat105 = next(fileseat).rstrip()
            invseat106 = next(fileseat).rstrip()
            invseat107 = next(fileseat).rstrip()
            invseat108 = next(fileseat).rstrip()
            invseat109 = next(fileseat).rstrip()
            invseat110 = next(fileseat).rstrip()
            invseat111 = next(fileseat).rstrip()
            invseat112 = next(fileseat).rstrip()
            invseat201 = next(fileseat).rstrip()
            invseat202 = next(fileseat).rstrip()
            invseat203 = next(fileseat).rstrip()
            invseat204 = next(fileseat).rstrip()
            invseat205 = next(fileseat).rstrip()
            invseat206 = next(fileseat).rstrip()
            invseat207 = next(fileseat).rstrip()
            invseat208 = next(fileseat).rstrip()
            invseat209 = next(fileseat).rstrip()
            invseat210 = next(fileseat).rstrip()
            invseat211 = next(fileseat).rstrip()
    except StopIteration:
        pass
######Front Row
    
    if(var1.get()!= "frontrow"):
        seat = var1.get()
        if(seat == "101"):
            if(seat101 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat101 = int(invseat101)
                invseat101-=1
                invseat101 = str(invseat101)
                cost = 50.00
                cost = str(cost)
                
        elif(seat == "102"):
            if(invseat102 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat102 = int(invseat102)
                invseat102-=1
                invseat102 = str(invseat102)
                cost = 50.00
                cost = str(cost)
                
        elif(seat == "103"):
            if(invseat103 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat103 = int(invseat103)
                invseat103-=1
                invseat103 = str(invseat103)
                cost = 50.00
                cost = str(cost)
            
        elif(seat == "104"):
            if(invseat104 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat104 = int(invseat104)
                invseat104-=1
                invseat104 = str(invseat104)
                cost = 50.00
                cost = str(cost)
            
        elif(seat == "105"):
            if(invseat105 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat105 = int(invseat105)
                invseat105-=1
                invseat105 = str(invseat105)
                cost = 50.00
                cost = str(cost)
            
#######MID ROW
            
    if(var2.get() != "Mid Row"):
        seat = var2.get()
        if(seat == "106"):
            if(invseat106 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat106 = int(invseat106)
                invseat106-=1
                invseat106 = str(invseat106)
                cost = 30.00
                cost = str(cost)
            
        elif(seat == "107"):
            if(invseat107 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat107 = int(invseat107)
                invseat107-=1
                invseat107 = str(invseat107)
                cost = 30.00
                cost = str(cost)

        elif(seat == "108"):
            if(invseat102 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat108 = int(invseat108)
                invseat108-=1
                invseat108 = str(invseat108)
                cost = 40.00
                cost = str(cost)
            
        elif(seat == "109"):
            if(invseat109 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat109 = int(invseat109)
                invseat109-=1
                invseat109 = str(invseat109)
                cost = 40.00
                cost = str(cost)
            
        elif(seat == "110"):
            if(invseat110 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat110 = int(invseat110)
                invseat110-=1
                invseat110 = str(invseat110)
                cost = 40.00
                cost = str(cost)
            
        elif(seat == "111"):
            if(invseat111 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat111 = int(invseat111)
                invseat111-=1
                invseat111 = str(invseat111)
                cost = 30.00
                cost = str(cost)

        elif(seat == "112"):
            if(invseat112 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat112 = int(invseat112)
                invseat112-=1
                invseat112 = str(invseat112)
                cost = 30.00
                cost = str(cost)
            
#######Balcony
    if(var3.get() != "Balcony"):
        seat = var3.get()
        if(seat == "201"):
            if(seat201 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat201 = int(invseat201)
                invseat201-=1
                invseat201 = str(invseat201)
                cost = 10.00
                cost = str(cost)
            
        elif(seat == "202"):
            if(invseat202 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat202 = int(invseat202)
                invseat202-=1
                invseat202 = str(invseat202)
                cost = 10.00
                cost = str(cost)

        elif(seat == "203"):
            if(invseat203 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat203 = int(invseat203)
                invseat203-=1
                invseat203 = str(invseat203)
                cost = 15.00
                cost = str(cost)
            
        elif(seat == "204"):
            if(invseat204 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat204 = int(invseat204)
                invseat204-=1
                invseat204 = str(invseat204)
                cost = 15.00
                cost = str(cost)
            
        elif(seat == "205"):
            if(invseat205 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat205 = int(invseat205)
                invseat205-=1
                invseat205 = str(invseat205)
                cost = 20.00
                cost = str(cost)
            
        elif(seat == "206"):
            if(invseat206 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat206 = int(invseat206)
                invseat206-=1
                invseat206 = str(invseat206)
                cost = 20.00
                cost = str(cost)

        elif(seat == "207"):
            if(invseat207 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat207 = int(invseat207)
                invseat207-=1
                invseat207 = str(invseat207)
                cost = 20.00
                cost = str(cost)
            
        elif(seat == "208"):
            if(invseat208 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat208 = int(invseat208)
                invseat208-=1
                invseat208 = str(invseat208)
                cost = 15.00
                cost = str(cost)
            
        elif(seat == "209"):
            if(invseat209 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat209 = int(invseat209)
                invseat209-=1
                invseat209 = str(invseat209)
                cost = 15.00
                cost = str(cost)

        elif(seat == "210"):
            if(invseat210 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat210 = int(invseat210)
                invseat210-=1
                invseat210 = str(invseat210)
                cost = 10.00
                cost = str(cost)
            
        elif(seat == "211"):
            if(invseat211 == "0"):
                messagebox.showerror("Error","SOLD OUT")
            else:
                invseat211 = int(invseat211)
                invseat211-=1
                invseat211 = str(invseat211)
                cost = 10.00
                cost = str(cost)
            

    open("TicketNight.txt","w").close()
    file=open("TicketNight.txt","a")
    file.write(invseat101+"\n")
    file.write(invseat102+"\n")
    file.write(invseat103+"\n")
    file.write(invseat104+"\n")
    file.write(invseat105+"\n")
    file.write(invseat106+"\n")
    file.write(invseat107+"\n")
    file.write(invseat108+"\n")
    file.write(invseat109+"\n")
    file.write(invseat110+"\n")
    file.write(invseat111+"\n")
    file.write(invseat112+"\n")
    file.write(invseat201+"\n")
    file.write(invseat202+"\n")
    file.write(invseat203+"\n")
    file.write(invseat204+"\n")
    file.write(invseat205+"\n")
    file.write(invseat206+"\n")
    file.write(invseat207+"\n")
    file.write(invseat208+"\n")
    file.write(invseat209+"\n")
    file.write(invseat210+"\n")
    file.write(invseat211+"\n")
    file.close()

    global screen12
    screen12= tk.Tk()
    screen12.title("Ticket")
    screen12.geometry("600x350")
    screen12.config(bg = ('black'))
    Label(screen12, text = "Ticket Stub",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen12, text = "Username-"+username_verify.get(),font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen12, text = "Seat Number-"+seat,font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen12, text = "Seat Price-"+cost,font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen12, text = "Seating is genreal admission for all sections",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen12, text = "No Refunds",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()
    Label(screen12, text = "Show Ticket at Door",font=("Helvetica",14,"bold"),bg = "Black", fg= "Gold").pack()


def managerLogin():
    #login()
   
    root = tk.Tk()
    root.geometry('300x300')
    root.title('TICKETS')
    root.config(bg = ('black'))

    t1 = open("TicketNight.txt","r")
    seatinv1 = t1.readlines()

    t2 = open("TicketEv.txt","r")
    seatinv2 = t2.readlines()

    
    # progressbar
    manLabel1= tk.Label(root,text='Matinee', font=("Helvetica",26,"bold"), fg="Gold", bg ="Black")
    manLabel1.pack()
    pb = ttk.Progressbar(root,orient='horizontal',mode='determinate',length=280)
    
    # place the progressbar
    pb.pack()
    
    i=0
    total=0
    while (i < 22):
        seatinv1[i] = int(seatinv1[i])
        total=total+seatinv1[i]
        i+=1
    fill = total
    total = str(total)
    tk.Label(root,text=total+"/750",font=("Helvetica",26,"bold"), fg="Gold", bg ="Black").pack()
    total = int(total)


    while (fill > 0 ):
        pb ["value"] += 0.134
        fill-=1
    

    #####
    manLabel2= tk.Label(root,text='Evening', font=("Helvetica",26,"bold"), fg="Gold", bg ="Black")
    manLabel2.pack()
    pb2 = ttk.Progressbar(root,orient='horizontal',mode='determinate',length=280)
    
    # place the progressbar
    pb2.pack()
    
    i=0
    total=0
    while (i < 22):
        seatinv2[i] = int(seatinv2[i])
        total=total+seatinv2[i]
        i+=1
    fill = total
    total = str(total)
    tk.Label(root,text=total+"/750",font=("Helvetica",26,"bold"), fg="Gold", bg ="Black").pack()
    total = int(total)
    
    while (total > 0 ):
        pb2 ["value"] += 0.134
        total-=1
        
      
    #23

      
##################################################################################################
def cancel():
    screen.destroy()
##################################################################################################
def main_screen():
    global screen
#Top    
    screen= tk.Tk()
    screen.title("TicketPlace")
    screen.minsize(width=550,height=200)
    screen.resizable(False,False)
    screen.config(bg = ('black'))       
#colum configurations
    screen.columnconfigure(0, minsize = 150)
    screen.columnconfigure(1, minsize = 175)
    screen.columnconfigure(2, minsize = 150)
    screen.rowconfigure(0, minsize = 50)
    screen.rowconfigure(1, minsize = 75)
    screen.rowconfigure(2, minsize = 100)
#Logo/header
    screen.heading_label = tk.Label(text='Filly-Tix Concert', font=("Helvetica",26,"bold"), fg="Gold", bg ="Black")
    screen.heading_label.grid(row=0,column=1)
#Picture For theater import
    photo = tk.PhotoImage(file="logo.gif")
    theater_pic= tk.Label(image= photo)
    theater_pic.image = photo
    theater_pic.grid(row=1, column=0, columnspan=3)
#Register Button
    register_button = Button(screen, text=' New Account ', width=16,font=("helvetica",15,"bold"),bg = "Black", fg= "Gold", command=register)
    register_button.grid(row=2,column=2,padx=5,pady=5)
#Login Button
    login_button = Button(text=' Login ', width=16,font=("helvetica",15,"bold"),bg = "Black", fg= "Gold",command=login)                                    
    login_button.grid(row=2,column=1,padx=15,pady=5)
#Close Button
    cancel_button = Button(screen, text=' Exit ', width=16,font=("helvetica",15,"bold"),bg = "Black", fg= "Gold",command=cancel)
    cancel_button.grid(row=2,column=0,padx=5,pady=5)    
main_screen()
