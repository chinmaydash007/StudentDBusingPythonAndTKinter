from tkinter import *
import tkinter.messagebox
import stdDatabase

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x2000+0+0")
        self.root.config(bg='#67E6DC')

        StdID=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Dob=StringVar()
        Age=StringVar()
        Gender=StringVar()
        Address=StringVar()
        Mobile=StringVar()

        #------------------------------------fUNCTION-------------
        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit or not")
            if(iExit>0):
                root.destroy()
                return
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtdob.delete(0,END)
            self.txtage.delete(0,END)
            self.txtgender.delete(0,END)
            self.txtaddr.delete(0,END)
            self.txtmob.delete(0,END)

        def addData():
            if(len(StdID.get())!=0):
                stdDatabase.addStudentRecord(StdID.get(),Firstname.get(),Surname.get(),Dob.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                studentList.delete(0,END)
                studentList.insert(END,(StdID.get(),Firstname.get(),Surname.get(),Dob.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))

        def displayData():
            studentList.delete(0, END)
            for row in stdDatabase.viewData():
                studentList.insert(END,row,str(""))
        def StudentRec(event):
            global sd
            searchStd=studentList.curselection()[0]
            sd=studentList.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END,sd[2])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END,sd[3])
            self.txtdob.delete(0, END)
            self.txtdob.insert(END,sd[4])
            self.txtage.delete(0, END)
            self.txtage.insert(END,sd[5])
            self.txtgender.delete(0, END)
            self.txtgender.insert(END,sd[6])
            self.txtaddr.delete(0, END)
            self.txtaddr.insert(END,sd[7])
            self.txtmob.delete(0, END)
            self.txtmob.insert(END,sd[8])
        def DeleteData():
            if (len(StdID.get()) != 0):
                stdDatabase.deleteRec(sd[0])
                clearData()
                displayData()
        def searchData():
            studentList.delete(0, END)
            for row in stdDatabase.searchData(StdID.get(),Firstname.get(),Surname.get(),Dob.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()):
                studentList.insert(END,row,str(""))
        def updateData():
            if (len(StdID.get()) != 0):
                stdDatabase.deleteRec(sd[0])
            if (len(StdID.get()) != 0):
                stdDatabase.addStudentRecord(StdID.get(),Firstname.get(),Surname.get(),Dob.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                studentList.delete(0,END)
                studentList.insert(END,(StdID.get(),Firstname.get(),Surname.get(),Dob.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))




        #--------------------------------------Frames-------------------
        MainFrame=Frame(self.root,bg="#3C40C6")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bg="#25CCF7", bd=2, padx=54, pady=8, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lableTitle=Label(TitleFrame,font=('arial',47,'bold'),text="Student Database Management System",bg='white')
        self.lableTitle.grid()

        ButtomFrame = Frame(MainFrame,width=1350,height=70, bg="#1BCA9B", bd=2, padx=18, pady=10, relief=RIDGE)
        ButtomFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,width=1300,height=400, bg="#019031", bd=2, padx=20, pady=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT= LabelFrame(DataFrame,width=1000,height=600, bg="#F4C724", bd=2, padx=20, pady=20, relief=RIDGE,font=('arial',20,'bold'),text="Student Information \n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame,width=450,height=300 ,bg="#25CCF7", bd=2, padx=31, pady=3, relief=RIDGE,font=('arial',20,'bold'),text="Student Details \n")
        DataFrameRight.pack(side=RIGHT)


        #----------------------------------------Label and Entry Widgets--------------------
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="Student ID:",padx=2, pady=2,bg='white')
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white',textvariable=StdID,width=40)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="First Name:", padx=2, pady=2, bg='white')
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white', textvariable=Firstname, width=40)
        self.txtfna.grid(row=1, column=1)

        self.lblsna = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="Sir Name:", padx=2, pady=2, bg='white')
        self.lblsna.grid(row=2, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white', textvariable=Surname, width=40)
        self.txtsna.grid(row=2, column=1)

        self.lbldob = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="DOB:", padx=2, pady=2, bg='white')
        self.lbldob.grid(row=3, column=0, sticky=W)
        self.txtdob = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white', textvariable=Dob, width=40)
        self.txtdob.grid(row=3, column=1)

        self.lblage = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="Age:", padx=2, pady=2, bg='white')
        self.lblage.grid(row=4, column=0, sticky=W)
        self.txtage = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white', textvariable=Age, width=40)
        self.txtage.grid(row=4, column=1)

        self.lblgender = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="Gender:", padx=2, pady=2, bg='white')
        self.lblgender.grid(row=5, column=0, sticky=W)
        self.txtgender = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white', textvariable=Gender, width=40)
        self.txtgender.grid(row=5, column=1)

        self.lbladdr = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="Address:", padx=2, pady=2, bg='white')
        self.lbladdr.grid(row=6, column=0, sticky=W)
        self.txtaddr = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white', textvariable=Address, width=40)
        self.txtaddr.grid(row=6, column=1)

        self.lblmob = Label(DataFrameLEFT, font=('arial', 10, 'bold'), text="Mobile:", padx=2, pady=2, bg='white')
        self.lblmob.grid(row=7, column=0, sticky=W)
        self.txtmob = Entry(DataFrameLEFT, font=('arial', 10, 'bold'), bg='white', textvariable=Mobile, width=40)
        self.txtmob.grid(row=7, column=1)

        # ----------------------------------------ListBox and ScrollBar--------------------
        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentList=Listbox(DataFrameRight,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        studentList.bind("<<ListboxSelect>>",StudentRec)
        studentList.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentList.yview)

        # ----------------------------------------Button Widgets--------------------
        self.btnAddData=Button(ButtomFrame,text="Add New",font=('arial',12,'bold'),width=10,height=1,bd=4,command=addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtomFrame, text="Display", font=('arial', 12, 'bold'), width=10, height=1, bd=4,command=displayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtomFrame, text="Clear", font=('arial', 12, 'bold'), width=10, height=1, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtomFrame, text="Delete", font=('arial', 12, 'bold'), width=10, height=1, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtomFrame, text="Search", font=('arial', 12, 'bold'), width=10, height=1, bd=4,command=searchData)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtomFrame, text="Update", font=('arial', 12, 'bold'), width=10, height=1, bd=4,command=updateData)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtomFrame, text="Exit", font=('arial', 12, 'bold'), width=10, height=1, bd=4,command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__=='__main__':
     root=Tk()
     application=Student(root)
     root.mainloop()

