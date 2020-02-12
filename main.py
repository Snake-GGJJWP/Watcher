import tkinter as tk
import cv2
import subprocess
import pyHook
import os
import signal
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import shutil


def send_email():
    email_user = "laptopnotification@gmail.com"
    password = "jwoerjwoss"
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "login.txt")
    email_recipient = open(path, "r").read()
    subject = "Message From Python"

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_recipient
    msg["Subject"] = subject
    body = "Warning: invasion attempt.\n"
    msg.attach(MIMEText(body, "plain"))

    file_name = "Test.jpg"
    try:
        attachment = open(file_name, "rb")
    except FileNotFoundError:
        attachment = 0

    if attachment != 0:
        application = MIMEBase("application", "octet-stream")
        application.set_payload(attachment.read())
        encoders.encode_base64(application)
        application.add_header("Content-Disposition", "attachment; filename= " + file_name)
        msg.attach(application)
    else:
        exc = "Can't find a photo"
        msg.attach(MIMEText(exc, "plain"))
    text = msg.as_string()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, password)

    server.sendmail(email_user, email_recipient, text)
    server.quit()

    attachment.close()

    os.remove("Test.jpg")


def take_photo():   # Making a photo
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    cv2.imwrite("Test.jpg", frame)
    cap.release()


def call_insertion(event, x):  # Input the password
    global entry
    entry.insert(tk.END, x)


def get_password(event):  # Getting the password
    global entry, root, label2, r
    file_password_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "password.txt")
    with open(file_password_path, "r") as file_password:
        password = file_password.read()
    if entry.get() == password:  # if password is correct
        print("password is correct")
        entry.delete(0, tk.END)
        with subprocess.Popen("start explorer.exe", shell=True) as process_start:  # Starting explorer.exe
            pass
        with open("pid.txt", "r") as file:
            pid = int(file.read())
            os.kill(pid, signal.SIGTERM)
        file.close()
        os.remove(os.path.join(os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"), "watcher.lnk"))
        try:
            with open("path.txt", "r") as file:
                path_to_history = file.readline()[:-1]
                path_to_cookies = file.readline()[:-1]
                path_to_cache = file.readline()[:-1]
            shutil.move("places.sqlite", path_to_history)
            shutil.move("cookies.sqlite", path_to_cookies)
            shutil.move("cache2", path_to_cache)
        except Exception:
            print("File hasn't been found")
        root.destroy()  # Closing program
    else:
        print("password is incorrect")
        label2["text"] = "Too bad."
        time.sleep(1)
        if r == 0:
            take_photo()
            send_email()
            r = 1


def backspace(event):  # Deleting last symbol
    global entry
    text = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, text)


class Btn(tk.Button):
    def __init__(self, root, x, y, t):
        super().__init__(root, text=t, width=7, height=2)
        self.bind("<Button-1>", lambda event, t=t: call_insertion(event, t))
        self.place(x=x, y=y)


def uMad(event):
    return False


def keylock():
    hm = pyHook.HookManager()
    hm.KeyAll = uMad
    hm.HookKeyboard()


def main():
    global root

    # Starting main window
    root = tk.Tk()
    root.title("Watcher")
    root.geometry("600x400")
    root.resizable(False, False)

    label1 = tk.Label(root, text="Input password:", font="Times 24")
    label1.pack(side=tk.TOP)

    global entry, label2, r

    r = 0

    label2 = tk.Label(root, text="", font="Times 24")
    label2.pack(side=tk.BOTTOM)

    entry = tk.Entry(root)
    entry.place(x=200, y=50, height=30, width=200)

    btn_1 = Btn(root, 205, 100, "1")
    btn_2 = Btn(root, 270, 100, "2")
    btn_3 = Btn(root, 335, 100, "3")
    btn_4 = Btn(root, 205, 150, "4")
    btn_5 = Btn(root, 270, 150, "5")
    btn_6 = Btn(root, 335, 150, "6")
    btn_7 = Btn(root, 205, 200, "7")
    btn_8 = Btn(root, 270, 200, "8")
    btn_9 = Btn(root, 335, 200, "9")

    btn_enter = tk.Button(root, text="Enter", width=16, height=2)
    btn_enter.bind("<Button-1>", get_password)
    btn_enter.place(x=205, y=250)

    btn_backspace = tk.Button(root, text="Back", width=7, height=2)
    btn_backspace.bind("<Button-1>", backspace)
    btn_backspace.place(x=335, y=250)

    root.mainloop()


if __name__ == "__main__":
    keylock()
    main()
