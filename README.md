### Usage:
To run this program click watcher.exe in dist directory. For this program working correct you also should type your email to login.txt (without spaces). Also you can change a password in "password.txt". Be careful, password must consist of numbers only. This program also requires some process you should create on your own.
#### To create this process follow next steps:
1. Press Win+R
2. Type "taskschd.msc"
3. In following window click on "Create task" in the right panel
4. In popped out window check on "Run with highest privilegy" box
5. In "Name" section type "Term"
6. In "Configure for" list choose your OS
7. In "Actions" tab click on "New" button
8. In following window click "Browse"
9. Find and click on "term.exe"
10. Click on "OK"
11. In "Conditions" tab make sure that first box in "Power" section is unchecked
12. In "Settings" tab make sure that "Allow task to be run on demand" is checked
13. Make sure that "Do not start a new instance" is choosen in list below
14. Click on OK
15. Make sure that process is working properly.
	1. Click on "Task sheduler library" in the left panel
	2. Run Task manager
	3. Find and click on Term process by right mouse button
	4. Click on Run.
	5. If Task manager has been closed you did it right.
To quit the program you should enter a password that you have set. By default it's 83742.
#### Note:
If you don't want to create a process you can change the value in "settings.txt" to 1. But be careful. If you change this value and somebody launch task manager as this program is running computer will shutdown. So make sure you have saved all important files.

P.S. I did it just to learn some pyqt
