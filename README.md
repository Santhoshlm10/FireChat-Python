# FireChat 🔥

Send instantaneous messages using google's firebase!.

![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/images/MainApp1.png)

![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/images/MainApp2.png)


### Tech Stack
- PyQT5 (A drag and drop like GUI designer)
   Library - https://pypi.org/project/PyQt5/
   Tool - https://www.qt.io/
- Python 3

### Project setup
- Make sure you have python/python3 installed in your machine
- Install PyQT5 GUI designer from the link provided in tech stack (Optional)
- Make sure you have a google account inorder to use googles firebase service
- To create a firebase real time database go to https://firebase.google.com/ 
- Go to the console
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/images/Firebase1.png)

- Add a new project 
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/images/Firebase2.png)

- At the left choose real time database feature and create database
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/images/Firebase3.png)


-  **IMPORTANT** !!!  under security rules choose "Start in Test Mode"
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/images/Firebase4.png)


- Install the required libraries by using: 
	**for python2**
	pip install -r requirements.txt
	**for python3** 
	pip3 install -r requirements.txt
- And then run python MainApplication .py 

### Important!
- Make sure there is always a child class called "FireChat" in firebase's real time database

### Getting the build
- If you like to get the build without any command simply download the auto-py-to-exe python library else you can follow the steps given below
- To get the program into executable form depending on your operating system you can use pyinstaller 
- Install pyinstaller using "pip3 install pyinstaller"
- To get the build use "pyinstaller MainApplication.py"
- Even as better option use auto-py-to-exe (https://pypi.org/project/auto-py-to-exe/)

