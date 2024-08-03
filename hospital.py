from tkinter import*
from tkinter import ttk
from tkinter import Tk, Label
from PIL import Image, ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import re
from tkinter import Tk, Button, Toplevel
from tkcalendar import DateEntry


def main():
    win=Tk()
    app=login(win)
    win.mainloop()



class login:
    def __init__(self,root):
        self.root=root 
        self.root.title("Login Form")
        self.root.geometry("1600x900+0+0")
        
        self.new_window = None
        
        
        # Load the background image
        bg_image = Image.open(r"E:\HMS\loginwallpaper.jpg")
        # Resize the image to fit the window size
        bg_image = bg_image.resize((1600, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        
        lbl_bg = Label(self.root, image=self.bg)
        # Place the image to cover the entire window
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame=Frame(self.root,bg="black")
        #frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        frame.place(x=610,y=170,width=340,height=450)
        
        # self.Center(direction=wx.VERTICAL)
        
        img1=Image.open(r"E:\HMS\user-avatar-red-icon-vector-8825308.jpg")
        img1=img1.resize((100,100),Image.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="HOSPITAL ADMIN",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=55,y=110)
        
        #LABLE
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.password=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.password.place(x=40,y=250,width=270)
        
        #ICON IMAGES
        img2=Image.open(r"E:\HMS\9187604.png")
        img2=img2.resize((25,25),Image.BILINEAR)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"E:\HMS\lock1.jpg")
        img3=img3.resize((25,25),Image.BILINEAR)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        
        #LOGINBUTTON
        loginbtn=Button(frame,command=self.loginbtn,text="Login",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="cyan",activeforeground="white",activebackground="cyan")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #REGISTRATIONBUTTON
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #PASSWORDBUTTON
        forgetpasswordbtn=Button(frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpasswordbtn.place(x=10,y=370,width=160)
        
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def loginbtn(self):
        self.new_window=Toplevel(self.root)
        if self.txtuser.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All field Required")
        elif self.txtuser.get()=="Saurabh" and self.password.get()=="1234":
            messagebox.showinfo("Success", "Login Sucessfully")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.password.get()
                
                                                        ))
            
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Usename and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=hospital(self.new_window)
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()
    #RESET
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Plase enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            query=("SELECT * FROM register WHERE email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Plaese enter correct Answer",parent=self.root2)
            else:
                query=("UPDATE register SET password=%s WHERE email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                mycursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,plaese login new password",parent=self.root2)
                self.root2.destroy()
            
        
    
    
    
    
    
    
    #FORGET PASSWORD
            
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Email to Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("Error","Please Enter Valid UserName")
            else:
                conn.close()
                self.root2=Tk()
                #self.root2=Toplevel()
                self.root.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="azure2")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_securiy_Q = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_securiy_Q["values"] = ("Select", "Your Birth Place", "Your Mother Name", "Your Pet Name")
                self.combo_securiy_Q.place(x=50, y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_security.place(x=50, y=180, width=250)
                
                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_newpass.place(x=50, y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                
                
                        
                
                
            
            
            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #VARIABLES
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        
        self.bg=ImageTk.PhotoImage(file=r"E:\HMS\morng.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left
        # self.bg1=ImageTk.PhotoImage(file=r"D:\Hotel\regs1.jpg")
        # left_lbl=Label(self.root,image=self.bg1)
        # left_lbl.place(x=50,y=100,width=509,height=399)
        
        #MAINFRAME
        frame=Frame(self.root,bg="azure2")
        frame.place(x=370,y=290,width=775,height=500)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="azure1")
        register_lbl.place(x=35,y=20)
        
        #LABEL AND ENTRY
        
        #ROW1
        fname=Label(frame,text="First Name",font=("times new roman",16,"bold"),bg="azure1")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",16,"bold"),bg="azure1")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #ROW2
        
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="azure1",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="azure1",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #ROW3
        #ROW3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="azure1", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_securiy_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_Q["values"] = ("Select", "Your Birth Place", "Your Mother Name", "Your Pet Name")
        self.combo_securiy_Q.place(x=50, y=270, width=250)
        self.combo_securiy_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="azure1", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        
        #ROW4
        
        pswd=Label(frame,text="Password ",font=("times new roman",15,"bold"),bg="azure1",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15),show="*")
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="azure1",fg="black")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15),show="*")
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        #CHECKBUTTON
        chechbtn=Checkbutton(frame,variable=self.var_check,text="I Agree with the terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        chechbtn.place(x=40,y=380)
        
        #BUTTONS
        img=Image.open(r"E:\HMS\registerbtn.jpg")
        img=img.resize((200,55),Image.BILINEAR)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=22,y=427,width=200)
        
        
        img1=Image.open(r"E:\HMS\loginnow1.jpg")
        img1=img1.resize((200,117),Image.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=338,y=410,width=200)
        
    #FUNCTION
    
    def register_data(self):
        # Validate first name
        if not self.var_fname.get().isalpha():
            messagebox.showerror("Error", "First name must contain only alphabets")
            return
        
        # Validate last name
        if not self.var_lname.get().isalpha():
            messagebox.showerror("Error", "Last name must contain only alphabets")
            return
        
        # Validate contact number
        if not re.match(r"^\d{10}$", self.var_contact.get()):
            messagebox.showerror("Error", "Contact number must be a 10-digit number")
            return
        
        # Validate email
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.var_email.get()):
            messagebox.showerror("Error", "Invalid email address")
            return
        
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror( "Error", "All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists")
            else:
                mycursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(), 
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_securityQ.get(),
                                                                                     self.var_securityA.get(),
                                                                                     self.var_pass.get()
                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration successful")
            
    def return_login(self):
        self.root.destroy()
class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Managemnet System")
        self.root.geometry("1550x850+0+0")
        
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Managemnet System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
        
        #DATA FRAME
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)
        
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=500,height=350)
        
        
        #BUTTON FRAME
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        #DETAILS FRAME
        
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1530,height=190)
        
        
        #DATAFRAME LEFT
        
        lblNameTablet=Label(DataFrameLeft,text="Name of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=37,state="readonly")
        comNametablet["values"]=("Nice","Corona","Vacacine","Aceraminophen","Adderall","Amlodipin","Ativan")
        comNametablet.grid(row=0,column=1)
        
        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        
        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)
        
        lblNoOftablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Tablets::",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=N)
        txtNoOftablets=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        
        
        lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)
        
        
        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)
        
        
        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect=Label (DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        
        lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)
        
        
        lblMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)
        
        
        lblPatientId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)
        
        
        lblNhsNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number" ,padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        
        lblPatientname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name" ,padx=2, pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)
        
        lblDateofBirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Birth",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataFrameLeft,font=("arial",12, "bold"),textvariable=self.DateOfBirth,width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        # Calendar widget for Issue Date
        self.cal_issuedate = DateEntry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate, width=35, background="blue", foreground="white")
        self.cal_issuedate.grid(row=5, column=1)

        # Calendar widget for Exp Date
        self.cal_expdate = DateEntry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.ExpDate, width=35, background="blue", foreground="white")
        self.cal_expdate.grid(row=6,column=1)
        
        
        #DATAFRAME RIGHT
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        #BUTTONS
        
        btnPrescription=Button(Buttonframe,command=self.iPrectioption,text="Show Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=24)
        btnPrescription.grid(row=0, column=1)
        
        btnPrescriptiondata=Button(Buttonframe,command=self.iPrescriptionData,text="Add Presciption",bg="green",fg="white",font=("arial",12,"bold"),width=24)
        btnPrescriptiondata.grid(row=0,column=0)
        
        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=24)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=24)
        btnDelete.grid(row=0,column=3)
        
        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=24)
        btnClear.grid(row=0,column=4)
        
        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=24)
        btnExit.grid(row=0,column=5)
        
        
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailsFrame,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate",
                                                              "expdate","dailydose","storage","nhsnumber","patientname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=BOTTOM, fill=Y)


        
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        
        self.hospital_table.heading("nameoftablet", text="Name Of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("patientname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        
        self.hospital_table["show"]="headings"
        
        
        self.hospital_table.column("nameoftablet", width=100)  
        self.hospital_table.column("ref", width=100)  
        self.hospital_table.column("dose", width=100) 
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=190)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)  
        self.hospital_table.column("storage", width=100)  
        self.hospital_table.column("nhsnumber", width=100)   
        self.hospital_table.column("patientname", width=100)
        self.hospital_table.column("dob", width=100) 
        self.hospital_table.column("address", width=100)

        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def validate_fields(self):
        errors = []
        
        if not self.ref.get().isalnum():
            errors.append("Reference No must be alphanumeric.")
        if not self.Dose.get().isdigit():
            errors.append("Dose must be an integer.")
        if not self.NumberofTablets.get().isdigit():
            errors.append("Number of Tablets must be an integer.")
        if not self.Lot.get().isdigit():
            errors.append("Lot must be an integer.")
        if not self.DailyDose.get().isdigit():
            errors.append("Daily Dose must be an integer.")
        if not self.sideEffect.get().isalpha():
            errors.append("Side Effect must be alphabetic.")
        if not self.FurtherInformation.get().isalpha():
            errors.append("Further Information must be alphabetic.")
        if not self.DrivingUsingMachine.get().isdigit():
            errors.append("Blood Pressure must be an integer.")
        if not self.StorageAdvice.get().isalpha():
            errors.append("Storage Advice must be alphabetic.")
        if not self.HowToUseMedication.get().isalpha():
            errors.append("Medication must be alphabetic.")
        if not self.PatientId.get().isdigit():
            errors.append("Patient ID must be an integer.")
        if not self.PatientName.get().replace(' ', '').isalpha():
            errors.append("Patient Name must be alphabetic.")
        if not self.nhsNumber.get().isdigit():
            errors.append("NHS Number must be an integer.")
        
        return errors
        
        
    def iPrescriptionData(self):
        errors = self.validate_fields()
        if errors:
            messagebox.showerror("Error", "\n".join(errors))
            return
        
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydata")
        my_cursor = conn.cursor()
        
        # Check if Patient ID is unique
        my_cursor.execute("SELECT * FROM hospital WHERE PatientId = %s", (self.PatientId.get(),))
        result = my_cursor.fetchone()
        if result:
            messagebox.showerror("Error", "Patient has been already inserted")
            conn.close()
            return

        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "INSERT INTO hospital (nameoftablet, ref, dose, nooftablets, lot, issuedate, expdate, dailydose, sideEffect, furtherinfo, storage, drivingUsingMachine, howtousemedication, PatientId, nhsnumber, patientname, dob, patientaddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.sideEffect.get(),
                self.FurtherInformation.get(),
                self.StorageAdvice.get(),
                self.DrivingUsingMachine.get(),  
                self.HowToUseMedication.get(),  
                self.PatientId.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
            )
        )
        conn.commit()
        self.fetch_data()    
        conn.close()
        messagebox.showinfo("Success", "Record has been inserted")

    def update(self):
        errors = self.validate_fields()
        if errors:
            messagebox.showerror("Error", "\n".join(errors))
            return
        
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE hospital SET nameoftablet=%s, dose=%s, nooftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, sideEffect=%s, furtherinfo=%s, storage=%s, drivingUsingMachine=%s, howtousemedication=%s, PatientId=%s ,nhsnumber=%s, patientname=%s, dob=%s, patientaddress=%s WHERE ref=%s", (
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.sideEffect.get(),
            self.FurtherInformation.get(),
            self.StorageAdvice.get(),
            self.DrivingUsingMachine.get(),
            self.HowToUseMedication.get(),
            self.PatientId.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated")
        self.fetch_data()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.sideEffect.set(row[8])
        self.FurtherInformation.set(row[9])
        self.StorageAdvice.set(row[10])
        self.DrivingUsingMachine.set(row[11])
        self.HowToUseMedication.set(row[12])
        self.PatientId.set(row[13])
        self.nhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DateOfBirth.set(row[16])
        self.PatientAddress.set(row[17])

    def iPrectioption(self):
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "StorageAdvice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END, "PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "NHSNumber:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "PatientName:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydata")
        my_cursor = conn.cursor()
        query = "DELETE FROM hospital WHERE ref=%s"
        values = (self.ref.get(),)
        my_cursor.execute(query, values)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iExit > 0:
            self.root.destroy()
            return
        
           
        

        
        
    

        


            
        
        
       





      



if __name__=="__main__":
    main()
        
