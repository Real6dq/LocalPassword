import tkinter as tk
import hashlib
import ctypes


def shuffle(str1, str2):
    shuffled = ""
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        shuffled += str1[i] + str2[i]
    if len(str1) > len(str2):
        shuffled += str1[min_length:]
    else:
        shuffled += str2[min_length:]
    return shuffled


def generate_password():
    length = int(length_entry.get())
    name = name_entry.get().lower()
    password = password_entry.get().lower()
    birthdate = birthdate_entry.get().lower()
    website = website_entry.get().lower()

    combined = str(length) + name + birthdate + website + str(length)
    sha = hashlib.sha256()
    sha.update(combined.encode())
    secretOne = str(sha.hexdigest())

    combined = str(length)+website+password+birthdate+str(length)
    sha = hashlib.sha256()
    sha.update(combined.encode())
    secretTwo = str(sha.hexdigest())[0:32]
    password = shuffle(secretOne, secretTwo+secretTwo)[0:length]
    password_output.config(text=password)
    copy(password)
    status_label.config(text="Password copied to clipboard!")



# I found this code on github, credits to whoever made it, I forgot to see, sorry.
def copy(str):
    CF_UNICODETEXT = 13
    GMEM_MOVEABLE = 0x0002
    ctypes.windll.user32.OpenClipboard(None)
    ctypes.windll.user32.EmptyClipboard()
    hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_MOVEABLE, len(str)*2+2)
    pchData = ctypes.windll.kernel32.GlobalLock(hCd)
    ctypes.cdll.msvcrt.wcscpy(ctypes.c_wchar_p(pchData), str)
    ctypes.windll.kernel32.GlobalUnlock(hCd)
    ctypes.windll.user32.SetClipboardData(CF_UNICODETEXT, hCd)
    ctypes.windll.user32.CloseClipboard()


root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1)

birthdate_label = tk.Label(root, text="Birthdate (yyyy-mm-dd):")
birthdate_label.grid(row=3, column=0)
birthdate_entry = tk.Entry(root)
birthdate_entry.grid(row=3, column=1)

website_label = tk.Label(root, text="Website:")
website_label.grid(row=4, column=0)
website_entry = tk.Entry(root)
website_entry.grid(row=4, column=1)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

password_output = tk.Label(root, text="")
password_output.grid(row=6, column=0, columnspan=2)

status_label = tk.Label(root, text="")
status_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
