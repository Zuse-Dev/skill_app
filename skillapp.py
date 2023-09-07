# import area
import sqlite3
from random import *

# setup
datebasename = r"skillapp.db"
db = sqlite3.connect(datebasename)
dbcr = db.cursor()
db.execute("create table if not exists users (user_id integer ,name string ,password string)")
db.execute("create table if not exists userskills (user_id integer, skill string, progress integer)")
print(dbcr.fetchmany())

def adduser(): # get with "1"
    username = input("your name : ").strip()
    password = input("write your password : ").strip()
    addskill = input("your skill (write one only) : ")
    addprogressmsg = f"please write you progress in '{addskill}' (number less than 100) : "
    try :
        addprogress = int(input(addprogressmsg).strip())
    except :
        addprogress = "asd"
    # print(addprogress)

    while type(addprogress) != int:
        try :
            addprogress = int(input(addprogressmsg).strip())
        except :
            pass
    
    if addprogress > 100 :
        while addprogress > 100 :
            try :
                addprogress = int(input(addprogressmsg).strip())
            except :
                pass
    userid = (len(username) + len(password)) * randint(456,27465)
    paramsadd1 = (userid,username,password)
    paramsadd2 = (userid,addskill,addprogress)
    dbcr.execute(f"insert into users (user_id ,name ,password ) values(? , ? , ?)", paramsadd1)
    dbcr.execute(f"insert into userskills (user_id ,skill ,progress) values(?, ?, ?)", paramsadd2)
    db.commit()
    print("-_" * 49)
    print(f"Done, your name : '{username}' and your password : '{password}'\nwith skill in\n{addskill} -> {addprogress}%")
    print("-_" * 49)

def addskills(): # get with "2"
    askname = input("username : ").strip()
    askpassword = input("password : ").strip()
    dbcr.execute("select name,password from users")
    allusersdate = dbcr.fetchall() # name,password
    dbcr.execute("select user_id from users")
    userid = dbcr.fetchall() # user_id
    dbcr.execute("select user_id,name,password from users")
    allusersdatewithid = dbcr.fetchall() # user_id,name,password
    # print(allusersdate)
    allask = (askname,askpassword)
    if allask in allusersdate :
        for i in userid :
            allask2 = (i[0],askname,askpassword)
            # print(allask)
            # print(allask2)
            # print(allusersdate)
            # print(allusersdatewithid)
            # print(userid)
            if allask2 in allusersdatewithid :
                askuserid = i[0]
                # print(askuserid)
                addskill = input("your skill (write one only) : ").strip()
                addprogressmsg = f"please write you progress in '{addskill}' (number less than 100) : "
                # try :
                #     addprogress = int(input(addprogressmsg))
                # except :
                #     addprogress = "asd"
                # print(addprogress)
                addprogress = ""
                while type(addprogress) != int:
                    try :
                        addprogress = int(input(addprogressmsg).strip())
                    except :
                        pass

                if addprogress > 100 :
                    while addprogress > 100 :
                        try :
                            addprogress = int(input(addprogressmsg).strip())
                        except :
                            pass
                # print(type(addprogress))
                # print(addprogress)
                if type(addprogress) == int and addprogress < 101:
                    paramaddskill = (askuserid,addskill,addprogress)
                    db.execute("insert into userskills (user_id,skill,progress) values (?,?,?)", paramaddskill)
                    db.commit()
                    print("Done")


    elif not allask in allusersdate :
        print("name or password is wrong")

def changeuserdate(): # get with "3"
    askname = input("username : ").strip()
    askpassword = input("password : ").strip()
    dbcr.execute("select name,password from users")
    allusersdate = dbcr.fetchall() # name , password
    dbcr.execute("select user_id from users")
    userid = dbcr.fetchall() # user_id
    # print(allusersdate)
    dbcr.execute("select user_id,name,password from users")
    allusersdatewithid = dbcr.fetchall() # user_id,name,password
    allask = (askname,askpassword)
    if allask in allusersdate :
        askskill =""
        for i in userid :
            allask2 = (i[0],askname,askpassword)
            if allask2 in allusersdatewithid :
                newask = ""
                while type(newask) != int:
                    try :
                        newask = int(input("what do you want to change? [1,2,3]\n1- 'name'\n2- 'password'\n3- 'delete skill' . ").strip())
                    except :
                        pass
                while newask > 3:
                    try :
                        newask = int(input("what do you want to change? [1,2,3]\n1- 'name'\n2- 'password'\n3- 'delete skill' . ").strip())
                    except :
                        pass
                if newask == 1:
                    newusername = input("new name : ").strip()
                    print(f"your new name is '{newusername}'")
                    paramsnewname = (newusername,askpassword)
                    dbcr.execute(f"update users set name = ? where password = ?", paramsnewname)
                    db.commit()
                elif newask == 2:
                    newpassword = input("new password : ").strip()
                    print(f"your new password is '{newpassword}'")
                    paramsnewpassword = (askname,newpassword)
                    dbcr.execute(f"update users set password = ? where name = ?", paramsnewpassword)
                    db.commit()
                elif newask == 3:
                    dbcr.execute("select skill from userskills")
                    selectskill = dbcr.fetchall() # skill
                    dbcr.execute("select user_id,skill from userskills")
                    selectskilldatewithid = dbcr.fetchall() # id , skills
                    # print(selectskilldatewithid)
                    # print(i[0])
                    print("what did you want to delete ?")
                    num = 0
                    userskilllist = []
                    for f in selectskilldatewithid :
                        if i[0] in f :
                            num += 1
                            userskilllist.append(f[1])
                            print(f"{num}- {f[1]}")
                    # print(selectskilldatewithid)
                    # print(userskilllist)
                    askskill = input("write the skill that you want to delete . ").strip()
                    # print(askskill)
                    if askskill in userskilllist :
                        user_id = i[0]
                        paramsdeleteskill = (user_id,askskill)
                        # print(paramsdeleteskill)
                        dbcr.execute("delete from userskills where user_id = ? and skill = ? ", paramsdeleteskill)
                        print(f"'{askskill}' had been deleted !")
                        db.commit()
                    else :
                        print("you write wrong skill, try again .")

    else : 
        print("name or password is wrong .")
        # print(f"your name is '{username}'\nand you have skills in\n'{userskill}' -> '{progress}%'")
    print("-_" * 49)

def showskill(): # get with "4"
    askname = input("username : ").strip()
    askpassword = input("password : ").strip()
    dbcr.execute("select name,password from users")
    allusersdate = dbcr.fetchall() # name , password
    dbcr.execute("select user_id from users")
    userid = dbcr.fetchall() # user_id
    # print(allusersdate)
    dbcr.execute("select user_id,name,password from users")
    allusersdatewithid = dbcr.fetchall() # user_id,name,password
    allask = (askname,askpassword)
    if allask in allusersdate :
        for i in userid : # i is the user_id
            allask2 = (i[0],askname,askpassword)
            if allask2 in allusersdatewithid :
                    dbcr.execute("select user_id,skill from userskills")
                    showskill = dbcr.fetchall() # skill , progress
                    dbcr.execute("select user_id,progress from userskills")
                    showprogresswithid = dbcr.fetchall() # id , skills
                    # print(i[0])
                    num = 0
                    userskilllist = []
                    userprogresslist = []
                    for priskill in showskill:
                        if i[0] in priskill:
                            userskilllist.append(priskill[1])
                    for priprogress in showprogresswithid:
                        if i[0] in priprogress:
                            userprogresslist.append(priprogress[1])
                    # print(userprogresslist)
                    # print(userskilllist)
                    for lol in range(1,len(userskilllist) + 1) :
                        print(f"{lol}- '{userskilllist[num]}' -> {userprogresslist[num]}%")
                        num += 1
                    # print(showskill)
                    # print(userskilllist)

    else : 
        print("name or password is wrong .")
        # print(f"your name is '{username}'\nand you have skills in\n'{userskill}' -> '{progress}%'")
    print("-_" * 49)


def exit(): # get with "5"
    print("The terminal has been close .")
    db.close()


while True :
    sqlite3.connect(datebasename)
    answer = input("choose want you want\n1- 'add user'\n2- 'add skills'\n3- 'change your date'\n4- 'show skills'\n5- 'Esc' (write numbers) . ").strip()
    print("-_" * 49)
    if answer == "1":
        adduser()
    elif answer == "2":
        addskills()
    elif answer == "3":
        changeuserdate()
    elif answer == "4":
        showskill()
    elif answer == "5":
        exit()
        break
    else :
        print("please write numbers [1,2,3,4,5] !")
