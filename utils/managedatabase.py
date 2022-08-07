import sqlite3
import platform

if platform.system() == "Linux":
    sqlpath = "./firechat"
else:
    sqlpath = "./../database/firechat"

def updateRoomList(room_name,firebase_url):
    con = sqlite3.connect(sqlpath)
    cur = con.cursor()
    update_query = "update config set firebase_url = '{0}' where room_name = '{1}'".format(firebase_url,room_name)
    cur.execute(update_query)
    con.commit()
    con.close()

def deleteRoom(room_name):
    con = sqlite3.connect(sqlpath)
    cur = con.cursor()
    update_query = "delete from config where room_name = '{0}'".format(room_name)
    cur.execute(update_query)
    con.commit()
    con.close()

def getRoomNameList():
    con = sqlite3.connect(sqlpath)
    cur = con.cursor()
    cur.execute("select distinct(room_name) from config")
    sl = cur.fetchall()
    dl = []
    for i in sl:
        dl.append(list(i))
    if len(dl) != 0:
        return len(dl), len(dl[0]), dl
    else:
        return len(dl), 0, dl

def getFirebaseUrl(room_name):
    con = sqlite3.connect(sqlpath)
    cur = con.cursor()
    cur.execute("select firebase_url from config where room_name = '{0}'".format(room_name))
    sl = cur.fetchall()
    dl = []
    for i in sl:
        dl.append(list(i))
    if len(dl) != 0:
        return len(dl), len(dl[0]), dl
    else:
        return len(dl), 0, dl


def checkIfRoomExists(room_name):
    a = getRoomNameList()[2]
    namelist = []
    if len(a) != 0:
        for i in a:
            namelist.append(i[0])
    if room_name not in namelist:
        return 0
    else:
        return 1

def insertRoomItem(room_name, firebase_url):
    # check if the room name already exist
    if checkIfRoomExists(room_name) == 0:
        con = sqlite3.connect(sqlpath)
        cur = con.cursor()
        insert_query = "insert into config(room_name,firebase_url) " \
                       "values('{0}','{1}')".format(room_name, firebase_url)
        cur.execute(insert_query)
        con.commit()
        con.close()
        return 0
    else:
        return 1