import sqlite3
def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("Create table if not exists student(id integer primary key,StdID text,Firstname text,Surname text,Dob text,Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()

def addStudentRecord(StdID,Firstname,Surname,Dob,Age,Gender,Address,Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("insert into student values(NULL,?,?,?,?,?,?,?,?)",(StdID,Firstname,Surname,Dob,Age,Gender,Address,Mobile))
    con.commit()
    con.close()
def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("select * from student")
    row=cur.fetchall()

    con.close()
    return row
def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("delete from student where id=?",(id,))
    row = cur.fetchall()
    con.commit()
    con.close()
def searchData(StdID="",Firstname="",Surname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("select * from student where StdID=? or Firstname=? or Surname=? or Dob=? or Age=? or Gender=? or Address=? or Mobile=?",(StdID,Firstname,Surname,Dob,Age,Gender,Address,Mobile))
    row = cur.fetchall()
    con.close()
    return row
def updateData(id,StdID="",Firstname="",Surname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("update   student set StdID=? , Firstname=? ,Surname=?,Dob=?,Age=?,Gender=?,Address=?,Mobile=? where id=?",(StdID,Firstname,Surname,Dob,Age,Gender,Address,Mobile,id))
    con.commit()
    con.close()
studentData()


