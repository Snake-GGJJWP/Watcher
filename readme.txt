Thank you for purchasing Watcher v3.
This program take care of your computer if you need to leave it alone for a while. To be more precise this program completely blocks your PC until password is right. The small feature there is when password is incorrect the program will send you a photo of offender to your email.

Usage:
	To run this program click watcher.exe in dist directory. For this program working correct you also should type your email to login.txt (without spaces). This program also requires some process you should create on your own.
	To create this process follow next steps:
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
	15.1 Click on "Task sheduler library" in the left panel
	15.2 Run Task manager
	15.3 Find and click on Term process by right mouse button
	15.4 Click on Run.
	15.5 If Task manager has been closed you did it right.
Note:
	If you don't want to create a process you can change the value in "settings.txt" to 1. But be careful. If you change this value and somebody launch task manager as this program is running computer will shutdown. So make sure you have saved all important files.

Warning: the program wasn't tested thoroughly and it may have a bugs. If you find one, please, report it here "vladiksnake@gmail.com"

Hopefully, you'll like it :)