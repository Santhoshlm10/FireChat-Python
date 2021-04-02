# FireChat 🔥

Send instantaneous messages using nothing but google's firebase.

![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/FireChat/images/MainApp1.png)

![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/FireChat/images/MainApp2.png)






### How does it work?
Usually many messaging apps use client server interaction in order to exchange the information, but here many number of clients are linked with a unique firebase io URL or simply the database.

![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/FireChat/images/Structure.png)

Firechat uses simple replication process in order to get the messages.



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
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/FireChat/images/Firebase1.png)

- Add a new project 
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/FireChat/images/Firebase2.png)

- At the left choose real time database feature and create database
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/FireChat/images/Firebase3.png)


-  **IMPORTANT** !!!  under security rules choose "Start in Test Mode"
![github-small](https://github.com/Santhoshlm10/FireChat-Python/blob/main/FireChat/images/Firebase4.png)


- Install the required libraries by using: 
	**for python2**
	pip install -r requirements.txt
	**for python3** 
	pip3 install -r requirements.txt
- And then run python MainApplication .py 

### Caution
- Make sure there is always a child class called "FireChat" in firebase's real time database
- The application might feel a bit laggy due to high refresh rate of incoming messages

### Getting the build
- To get the program into executable form depending on your operating system you can use pyinstaller 
- Install pyinstaller using "pip3 install pyinstaller"
- To get the build use "pyinstaller MainApplication.py"
