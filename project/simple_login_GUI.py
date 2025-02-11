import tkinter as tk
from tkinter import messagebox
import os

# trying to find directory of this script so can open accounts.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "accounts.txt"
file_path = os.path.join(script_dir, file_name)

def open_register_window():
    # Create a new Toplevel window
    new_window = tk.Toplevel(window)
    new_window.title("registration")
    new_window.geometry("300x300")
    # Add widgets to the new window
    label1 = tk.Label(new_window, text="user registration", font=("Helvetica", 14))
    label1.pack(pady=20)

    # Add an Entry widget for single-line input
    label1 = tk.Label(new_window, text="username:")
    label1.pack()
    name_var = tk.StringVar()
    entry1 = tk.Entry(new_window, textvariable=name_var, width=30)
    entry1.pack(pady=5)

    # Add an Entry widget for single-line input
    label2 = tk.Label(new_window, text="password:")
    label2.pack()
    passwd_var = tk.StringVar()
    entry2 = tk.Entry(new_window, textvariable=passwd_var, width=30)
    entry2.pack(pady=5)

    # Add a button to submit the input
    def get_input():
        # Retrieve the user input from the Entry widget
        uname = entry1.get()
        passwd = entry2.get()

        # loop input until user enters valid password
        if len(passwd) < 10:
            print("please retry, password not long enough!")
            messagebox.showerror("please retry password", "minimum 10 characters required")
        else:
            login = uname + "," + passwd

            with open(file_path, 'a') as file:
                file.write(login + '\n')

            messagebox.showinfo("success!", "user registered!")

        print(f"Username: {uname}")
        print(f"Password: {passwd}")

        # Optionally clear the input field
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)

    submit_button = tk.Button(new_window, text="Submit", command=get_input)
    submit_button.pack(pady=10)

    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

def open_login_window():
    # Create a new Toplevel window
    new_window = tk.Toplevel(window)
    new_window.title("login")
    new_window.geometry("300x300")
    # Add widgets to the new window
    label2 = tk.Label(new_window, text="user login", font=("Helvetica", 14))
    label2.pack(pady=20)

    # Add an Entry widget for single-line input
    label1 = tk.Label(new_window, text="username:")
    label1.pack()
    name_var = tk.StringVar()
    entry1 = tk.Entry(new_window, textvariable=name_var, width=30)
    entry1.pack(pady=5)

    # Add an Entry widget for single-line input
    label2 = tk.Label(new_window, text="password:")
    label2.pack()
    passwd_var = tk.StringVar()
    entry2 = tk.Entry(new_window, textvariable=passwd_var, width=30)
    entry2.pack(pady=5)

    # Add a button to submit the input
    def get_input():
        # Retrieve the user input from the Entry widget
        uname = entry1.get()
        passwd = entry2.get()
        login = uname + "," + passwd

        with open(file_path, 'r') as file:
            # read the entire file and return it as a list of strings
            # where each string represents a line from the file
            list1 = file.readlines()

            # iterate through each line using for loop
            for eachLine in list1:

                # selection using equality operator
                if eachLine.strip() == login:
                    hello_usr = "Hello, "+uname+"!"
                    user_var.set(hello_usr)
                    messagebox.showinfo("login found","you are now logged in!")

        print(f"Username: {uname}")
        print(f"Password: {passwd}")
        # Optionally clear the input field
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
    submit_button = tk.Button(new_window, text="Submit", command=get_input)
    submit_button.pack(pady=10)

    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

def open_view_window():
    # Create a new Toplevel window
    new_window = tk.Toplevel(window)
    new_window.title("view accounts")
    new_window.geometry("300x600")
    # Add widgets to the new window
    label3 = tk.Label(new_window, text="List of registered users", font=("Helvetica", 14))
    label3.pack(pady=20)

    listbox = tk.Listbox(new_window, height=10, width=30)
    listbox.pack(pady=10)

    if user_var.get() != "Hello, World!":
        with open(file_path, 'r') as file:
            # read the entire file and return it as a list of strings
            # where each string represents a line from the file
            list1 = file.readlines()

            # iterate through each line using for loop
            for index, eachLine in enumerate(list1, start=1):
                listbox.insert(tk.END, f"{index}. "+eachLine.split(',', 1)[0])
    else:
        messagebox.showerror("access denied!","you must login first!")

    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

# Create the main window
window = tk.Tk()
window.title("Simple login app")
window.geometry("200x200")

# Add a label
user_var = tk.StringVar()
label = tk.Label(window, textvariable=user_var)
user_var.set("Hello, World!")
label.pack()

# Add a button to register
register_button = tk.Button(window, text="register", command=open_register_window)
register_button.pack(pady=10)

# Add a button to login
login_button = tk.Button(window, text="login", command=open_login_window)
login_button.pack(pady=10)

# Add a button to view accounts
view_button = tk.Button(window, text="view accounts", command=open_view_window)
view_button.pack(pady=10)

# Add a button exit the app
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack()

# Run the application
window.mainloop()

