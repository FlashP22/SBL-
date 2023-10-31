import tkinter as tk

# Function to be executed when the Start button is clicked
def start_application():
    login = login_entry.get()
    password = password_entry.get()
    # You can add your authentication logic here
    print(f"Login: {login}, Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Login Application")

# Create and place the login label and entry field
login_label = tk.Label(root, text="Login:")
login_label.pack()
login_entry = tk.Entry(root)
login_entry.pack()

# Create and place the password label and entry field
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Mask the password with asterisks
password_entry.pack()

# Create and place the Start button
start_button = tk.Button(root, text="Start", command=start_application)
start_button.pack()

# Start the GUI main loop
root.mainloop()
