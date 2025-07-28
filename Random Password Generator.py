import tkinter as tk
import random
def generate_password():
    length = int(entry.get())
    data = ['q','w','e','r','t','y','u','i','o','p',
            'a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
            'Q','W','E','R','T','Y','U','I','O','P',
            'A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
            '1','2','3','4','5','6','7','8','9','0',
            '!','@','#','$','%','&','*']
    password = ""
    for i in range(length):
        password += random.choice(data)
    result_label.config(text="Your password is: " + password)
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
title_label = tk.Label(root, text="Welcome to the Random Password Generator")
title_label.pack(pady=5)
prompt_label = tk.Label(root, text="How many characters do you want in your password?")
prompt_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.mainloop()
