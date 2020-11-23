#JIANTANG HUANG (huang.3100)

#login
from tkinter import Tk,messagebox,Toplevel
import tkinter as tk

# variable: success
#keep track of login success or not
success: int = 0

#1.frame
my_window=Tk()
my_window.title("Login system")

#set window size
screen_width,scree_height=my_window.maxsize()
width=300
height=250

#keep window at mid
align_str="%dx%d+%d+%d" % (width,height,(screen_width-width)/2,(scree_height-height)/2)

my_window.geometry(align_str)

my_window.resizable(width=False, height=False)

#add label
user_name_label=tk.Label(my_window,text='Username',font=(12))
user_name_label.place(x=10,y=30)
user_pwd_label=tk.Label(my_window,text="Password",font=(12))
user_pwd_label.place(x=10,y=80)

#enter username
user_name_text=tk.StringVar()

user_name_entry=tk.Entry(my_window,textvariable=user_name_text,font=14,width=15)
user_name_entry.place(x=110,y=30)

#enter password
user_pwd_text=tk.StringVar()

user_pwd_entry=tk.Entry(my_window,textvariable=user_pwd_text,font=14,width=15,show ="*")
user_pwd_entry.place(x=110,y=80)

#read data
def read_data():
    with open("data.txt","r") as f:
        rows=f.readlines()
        user_info_dict={}

        for row in rows:
            dict_list=row.strip().split(":")
            user_info_dict[dict_list[0]]=dict_list[1]
        f.close()
        return user_info_dict

#login event
def user_login():
    global success
    # get username and password
    name=user_name_text.get()
    pwd=user_pwd_text.get()
    user_dict=read_data()
    if name!="" and pwd!="":
        if name in user_dict.keys():
            if pwd==user_dict[name]:
                # print("ok")
                messagebox.showinfo(title="success",message="welcome "+name)
                success = 1
                my_window.destroy()
            else:
                # print("password incorrect")
                messagebox.showerror(title="fail",message="password incorrect")
        else:
            # print("user not exist")
            messagebox.showerror(title="fail",message="user not exist")
    else:
        # print("username and password can't be empty")
        messagebox.showerror(title="fail",message="username and password can't be empty")
    #pwd = len(pwd)*"*"

#pop sign up window
def pop_win():
    top=Toplevel()
    top.title("sign up")
    top.geometry("250x200")
    #button
    #gird
    tk.Label(top,text="username",width=10).grid(row=1,column=0)
    user_name=tk.StringVar()
    tk.Entry(top,textvariable=user_name,width=15).grid(row=1,column=1)

    tk.Label(top,text="password",width=10).grid(row=2,column=0)
    user_pwd=tk.StringVar()
    tk.Entry(top,textvariable=user_pwd,width=15,show = "*").grid(row=2,column=1)

    tk.Label(top,text="password again",width=15).grid(row=3,column=0)
    user_confirm_pwd=tk.StringVar()
    tk.Entry(top,textvariable=user_confirm_pwd,width=15,show = "*").grid(row=3,column=1)

    #sign up event
    def user_register():

        name=user_name.get()
        pwd=user_pwd.get()
        confirm_pwd=user_confirm_pwd.get()
        if pwd==confirm_pwd:
            with open("data.txt","a") as f:
                f.writelines(name+":"+pwd+"\n")
                f.flush()
                f.close()
                messagebox.showinfo(title="success",message="Sign up success!")
                #destory window
                top.destroy()
        else:
            messagebox.showerror(title="fail",message="password different")

    tk.Button(top,text="sign up",width=10,command=user_register).grid(row=4,columnspan=2,pady=15)

#button
#login event
user_login_button=tk.Button(my_window,text="Login",font=("FangSong",14),comman=user_login)
user_login_button.place(x=30,y=130)

#sign event
user_login_button=tk.Button(my_window,text="Sign",font=("FangSong",14),comman=pop_win)
user_login_button.place(x=180,y=130)

my_window.mainloop()
# print(read_data())