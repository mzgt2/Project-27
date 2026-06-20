from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





    password_list = [choice(letters) for a in range(randint(8, 10))] + [choice(symbols) for b in range(randint(2, 4))] + [choice(numbers) for c in range(randint(2, 4))]

    shuffle(password_list)

    passcode = "".join(password_list)
    pyperclip.copy(passcode)

    password_input.delete(0, END)
    password_input.insert(0,f"{passcode}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open ("/Users/Mz/PycharmProjects/password-manager-start/data.txt", "a") as file:
        web = web_input.get()
        username = username_input.get()
        passwords = password_input.get()
        # need to display message for input validation without using while loop to have user continue input
        if len(web) <= 0 or len(username) <= 0 or len(passwords) <= 0:
            messagebox.showwarning(title="Invalid Input", message="Please correct empty fields.")
            return
        is_ok = messagebox.askokcancel(title=web, message=f"The information entered: \nEmail: {username} "
                                                   f"\nPassword: {passwords} \nIs it ok to save?")
        if is_ok:
            web_input.delete(0,END)
            username_input.delete(0, END)
            password_input.delete(0, END)
            file.write(f"\n{web} | {username} | {passwords}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "email@example.com")

password = StringVar()
password_input = Entry(width=21, textvariable=password, show="*")
password_input.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=pass_gen)
generate_pass.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
