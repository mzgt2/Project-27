# Project-27
Password Manager
# Password Manager 🔐

A Tkinter-based GUI application for generating strong passwords and securely storing them with associated websites and usernames. Passwords are automatically copied to clipboard and saved to a file.

## Requirements

```bash
pip install pillow pyperclip
```

## Project Structure
password-manager/

├── main.py

├── logo.png          # Lock icon for UI

└── data.txt          # Stored passwords (created automatically)

## How to Run

```bash
python main.py
```

## How to Use

1. Enter the website/service name in the "Website" field
2. Enter your email/username in the "Email/Username" field
3. Click "Generate Password" to create a strong random password (automatically copied to clipboard)
4. Or manually enter a password in the "Password" field
5. Click "Add" to save the entry
6. Confirm the save dialog
7. All entries are saved to `data.txt`

## Features

✅ **Password Generator** - Creates random strong passwords (8-10 letters, 2-4 symbols, 2-4 numbers)  
✅ **Auto-Copy** - Generated password automatically copied to clipboard  
✅ **Input Validation** - Prevents saving with empty fields  
✅ **Confirmation Dialog** - Shows details before saving  
✅ **File Storage** - Saves to data.txt in format: Website | Username | Password  
✅ **Password Masking** - Password field displays asterisks  
✅ **Clean UI** - Professional-looking Tkinter interface  

## Password Generator Specs

- **Minimum letters**: 8-10 random letters (a-z, A-Z)
- **Symbols**: 2-4 random symbols (!,#,$,%,&,(,),*,+)
- **Numbers**: 2-4 random digits (0-9)
- **Total**: 12-18 character passwords
- **Security**: Shuffled for random order

## Example Session
Website: Gmail

Email/Username: myemail@gmail.com

[Click Generate Password]

Password field: Bx8@m#L9qR2k (auto-filled and copied)

[Click Add]

Confirmation: "Is it ok to save?"

[Click OK]

Result saved to data.txt as:

Gmail | myemail@gmail.com | Bx8@m#L9qR2k

## Data Storage Format

The `data.txt` file stores entries as pipe-separated values:
Website | Email/Username | Password

Gmail | myemail@gmail.com | Bx8@m#L9qR2k

Facebook | user@email.com | P4$sWd9#Kx2

Netflix | netflix@email.com | M7&nP2@Wq5L

## Input Validation

- **Empty fields** - Shows warning dialog if any field is empty
- **Confirmation prompt** - Displays entered data before saving
- **Field clearing** - Fields clear after successful save

## Customization

### Change Password File Location
```python
with open("path/to/your/passwords.txt", "a") as file:
```

### Adjust Password Length
```python
[choice(letters) for a in range(randint(12, 16))]  # 12-16 letters instead of 8-10
```

### Add More Symbols
```python
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '@', '^']
```

### Change Password Masking Character
```python
password_input = Entry(width=21, textvariable=password, show="•")  # Bullet instead of asterisk
```

### Set Default Username
```python
username_input.insert(0, "your-email@gmail.com")  # Change default email
```

## What I Learned

- **Tkinter GUI** - Building complete desktop applications with widgets
- **List comprehension** - Generating lists of random characters efficiently
- **Random module** - Using `choice()` and `randint()` for randomization
- **String methods** - `shuffle()`, `join()`, `delete()`, `insert()`
- **File I/O** - Reading/writing to files with context managers
- **Message boxes** - Using `messagebox.askokcancel()` and `showwarning()`
- **Clipboard integration** - Using `pyperclip` to copy text automatically
- **Input validation** - Checking field values before processing
- **Widget configuration** - Using `StringVar()` for password masking
- **Event handling** - Button commands with `command=`

## Security Notes

⚠️ **Warning**: This is a basic password manager for learning purposes. For production use, consider:
- Encrypting stored passwords with libraries like `cryptography`
- Using a secure database instead of plain text files
- Implementing master password protection
- Using environment variables for sensitive data

## Tips for Strong Passwords

- Use the generator feature for maximum randomness
- Never reuse passwords across websites
- Consider using a professional password manager (1Password, Bitwarden, LastPass)
- Regularly update passwords for important accounts
- Store this file in a secure location

Perfect for organizing and generating passwords! 🔑
