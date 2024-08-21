from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
import mysql.connector
from tkinter import PhotoImage
from PIL import ImageTk,Image 

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
)
conn1 = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
)

cursor = conn.cursor()
cursor.execute('create database if not exists unitrade')
cursor.execute('use unitrade')

cursor1 = conn1.cursor()
cursor1.execute('create database if not exists categories')
cursor1.execute('use categories')

root = Tk()
root.title("Home Screen")

x = (root.winfo_screenwidth() - 500 )// 2
y = (root.winfo_screenheight() - 500) // 2
x=-10
y=0
root.geometry(f"1550x840+{x}+{y}")
global flag
flag = 0
def hii():
	buywin.destroy()
def proceeds(e):
	global drop_down2
	cate = drop_down2.get()
	drop_down2.destroy()
	cursor1.execute(f"select * from {cate}")
	t = cursor1.fetchall()
	columns = ("Name", "Price", "Description","email")
	
	style = ttk.Style()
	#style.configure("Treeview", highlightthickness=0, bd=1)
	style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
	#style.map("Treeview", background=[("selected", "#BFBFBF")], fieldbackground=[("selected", "#BFBFBF")])

	tree = ttk.Treeview(buyframe, columns=columns, show="headings")
	for col in columns:
    		tree.heading(col, text=col)
	for i in range(0,2):
    		tree.column(columns[i], width=100)
	tree.column("Description", width=500)
	tree.column("email", width=150)
	for i in t:
		it = i + ("22b01a0570@svecw.edu.in",)
		tree.insert('', 'end', values=it)
	tree.pack()	
	buywin.protocol("WM_DELETE_WINDOW",hii)
def buyy():
	global drop_down2,buyframe,buywin
	root.withdraw()
	buywin = Toplevel(root)
	buywin.title("Sell")
	x = -10
	y = 0
	buywin.geometry(f"1550x840+{x}+{y}")
	img14=Image.open('back.jpg')
	temp14=img14.resize((1600,1000))
	photo14=ImageTk.PhotoImage(temp14)
	Lb14=Label(buywin,image=photo14)
	Lb14.image=photo14
	Lb14.place(x=0,y=0)
	

	buyframe=Frame(buywin,bg='white',width='1300',height='670')
	buyframe.place(x=120,y=80)
	
	img16=Image.open('choose.jpg')
	temp16=img16.resize((600,600))
	photo16=ImageTk.PhotoImage(temp16)
	Lb16=Label(buyframe,image=photo16)
	Lb16.image=photo16
	Lb16.place(x=20,y=0,width=600,height=600)
	
	txt6 = 'Choose category'
	head6=Label(buyframe,text=txt6,font=('yu gothic ui',25,'bold'),bg='white' ,fg='violet')
	head6.place(x=700,y=40,width=500,height=50)
	

	img15 = Image.open('logback.jpg')
	temp15 = img15.resize((600,500))
	photo15=ImageTk.PhotoImage(temp15)
	Lb15=Label(buyframe,image=photo15)
	Lb15.image=photo15
	Lb15.place(x=670,y=105,width=530,height=450)


	cursor1.execute("select * from category")		
	l = cursor1.fetchall()
	categories = [i[0] for i in l]
	drop_down2 = ttk.Combobox(buyframe,values = categories)
	drop_down2.current(0)
	drop_down2.place(x=800,y=200)
	drop_down2.bind("<<ComboboxSelected>>",proceeds)

def selll():
	root.withdraw()
	sellwin = Toplevel(root)
	sellwin.title("Sell")
	x = -10
	y = 0
	sellwin.geometry(f"1550x840+{x}+{y}")
	img11=Image.open('back.jpg')
	temp11=img11.resize((1600,1000))
	photo11=ImageTk.PhotoImage(temp11)
	Lb11=Label(sellwin,image=photo11)
	Lb11.image=photo11
	Lb11.place(x=0,y=0)
	

	sellframe=Frame(sellwin,bg='white',width='1300',height='670')
	sellframe.place(x=120,y=80)
	
	img12=Image.open('choose.jpg')
	temp12=img12.resize((600,600))
	photo12=ImageTk.PhotoImage(temp12)
	Lb12=Label(sellframe,image=photo12)
	Lb12.image=photo12
	Lb12.place(x=20,y=0,width=600,height=600)
	
	txt4 = 'Choose category'
	head4=Label(sellframe,text=txt4,font=('yu gothic ui',25,'bold'),bg='white' ,fg='violet')
	head4.place(x=700,y=40,width=500,height=50)
	

	img13 = Image.open('logback.jpg')
	temp13 = img13.resize((600,500))
	photo13=ImageTk.PhotoImage(temp13)
	Lb13=Label(sellframe,image=photo13)
	Lb13.image=photo13
	Lb13.place(x=670,y=105,width=530,height=450)
	
	def addcategory():
		global label1,entry1,addcat
		drop_down.destroy()
		head4.destroy()
		addbutton.destroy()
		reply1 = messagebox.showinfo("","Category Not found \n No worries Add Yours")
		if(reply1):
			label1 = Label(sellframe,text = "Specify your Category :",font=("Arial",15));
			label1.place(x=730,y=200)
			label1.config(bg="#d8b9e2")
			entry1 = Entry(sellframe,width = 30)
			entry1.place(x=980,y=210)
			entry1.config(fg="black", bg="lavender",bd=2,relief="raised",highlightbackground="purple1")
			addcat = Button(sellframe,text = "ADD",padx = "25",pady ="15",command = additem)
			addcat.place(x=950,y=340)	
			addcat.config(fg="white", bg="purple1",width=15)
	global addbutton	
	addbutton = Button(sellframe,text = "Other",padx = "25",pady = "8",command = addcategory)
	addbutton.place(x=1020,y=450)	
	addbutton.config(fg="white", bg="purple1")

	def additemm():
		x1 = name_entry.get()
		x2 = price_entry.get()
		x3 = des_entry.get()
		cursor1.execute(f"insert into {temp} values ('{x1}','{x2}','{x3}')")
		conn1.commit()
		reply = messagebox.showinfo("Success","item added!!!")
		if(reply):
			sellwin.destroy()
			if(flag == 0):
				logwin.destroy()
			else:
				signwin.destroy()
			decwin.deiconify()
	def selectitem(itemm):
		global name_entry,price_entry,des_entry,temp,name_label,price_label,des_label,addbutton
		temp = itemm
		cursor1.execute(f"create table if not exists {temp} (item_name varchar(50),item_prize int8,item_des varchar(200))")
		conn1.commit()

		txt6 = 'Please fill in'
		head6=Label(sellframe,text=txt6,font=('yu gothic ui',25,'bold'),bg='white' ,fg='violet')
		head6.place(x=700,y=40,width=500,height=50)

		name_label = Label(sellframe,text = "Item name: ",font=("Arial",15));
		name_label.place(x=750,y=175)
		name_label.config(bg="#d8b9e2")
		name_entry = Entry(sellframe,width = 20)
		name_entry.place(x=940,y=175)
		name_entry.config(fg="black", bg="lavender",bd=2,relief="raised",highlightbackground="purple1")
		price_label = Label(sellframe,text = "Item price: ",font=("Arial",15));
		price_label.place(x=750,y=275)
		price_label.config(bg="#d8b9e2")
		price_entry = Entry(sellframe,width = 20)
		price_entry.place(x=940,y=275)
		price_entry.config(fg="black", bg="lavender",bd=2,relief="raised",highlightbackground="purple1")
		des_label = Label(sellframe,text = "Item description: ",font=("Arial",15));
		des_label.place(x=750,y=375)
		des_label.config(bg="#d8b9e2")
		des_entry = Entry(sellframe,width = 20)
		des_entry.place(x=940,y=375)
		des_entry.config(fg="black", bg="lavender",bd=2,relief="raised",highlightbackground="purple1")
		addbutton = Button(sellframe,text = "ADD",padx = "25",pady ="15",command = additemm)
		addbutton.place(x=970,y=460)
		addbutton.config(fg="white", bg="purple1",width=13)
	def proceedd(e):
		tem = drop_down1.get()
		drop_down1.destroy()
		head5.destroy()
		selectitem(tem)
	def additem():
		global drop_down1,head5
		x = entry1.get()
		cursor1.execute(f"insert into category values ('{x}')")
		reply = messagebox.showinfo("Success","category added!!!")
		conn1.commit()
		label1.destroy()
		entry1.destroy()
		addcat.destroy()

		txt5 = 'Choose category'
		head5=Label(sellframe,text=txt5,font=('yu gothic ui',25,'bold'),bg='white' ,fg='violet')
		head5.place(x=700,y=40,width=500,height=50)

		cursor1.execute("select * from category")		
		l = cursor1.fetchall()
		categorie = [i[0] for i in l]
		drop_down1 = ttk.Combobox(sellframe,values = categorie)
		drop_down1.current(0)
		drop_down1.place(x=800,y=200)
		drop_down1.bind("<<ComboboxSelected>>",proceedd)
	
	def proceed(e):
		global label,entry
		cate = drop_down.get()
		drop_down.destroy()
		addbutton.destroy()
		head4.destroy()
		selectitem(cate)
	global dropdown
	cursor1.execute("select * from category")		
	l = cursor1.fetchall()
	categorie = [i[0] for i in l]
	drop_down = ttk.Combobox(sellframe,values = categorie)
	drop_down.current(0)
	drop_down.place(x=800,y=200)
	drop_down.bind("<<ComboboxSelected>>",proceed)
def close_all_windows():
	root.destroy()
def buyorsell():
	global decwin
	decwin = Toplevel(root)
	decwin.title("Login")
	x = -10
	y=0
	decwin.geometry(f"1550x840+{x}+{y}")

	img5=Image.open('back.jpg')
	temp5=img5.resize((1600,1000))
	photo5=ImageTk.PhotoImage(temp5)
	Lb5=Label(decwin,image=photo5)
	Lb5.image=photo5
	Lb5.place(x=0,y=0)

	decframe=Frame(decwin,bg='white',width='1100',height='600')
	decframe.place(x=200,y=130)
	
	#txt2 = 'Are you interested in buying or selling today??'
	txt2 = 'Wanna buy or sell??'
	head2=Label(decframe,text=txt2,font=('yu gothic ui',25,'bold'),bg='blueviolet' ,fg='white')
	head2.place(x=700,y=50,width=300,height=50)

	img6=Image.open('buysell.jpg')
	temp6=img6.resize((600,600))
	photo6=ImageTk.PhotoImage(temp6)
	Lb6=Label(decframe,image=photo6)
	Lb6.image=photo6
	Lb6.place(x=0,y=0,width=600,height=600)

	img7 = Image.open('logback.jpg')
	temp7 = img7.resize((500,500))
	photo7=ImageTk.PhotoImage(temp7)
	Lb7=Label(decframe,image=photo7)
	Lb7.image=photo7
	Lb7.place(x=650,y=120,width=400,height=400)

	buy = Button(Lb7,text = "Buy",width = 22,height = 4,command = buyy)
	sell = Button(Lb7,text = "Sell",width = 22,height = 4,command = selll)
	buy.place(x=110,y=100)
	sell.place(x=110,y=200)
	decwin.protocol("WM_DELETE_WINDOW", close_all_windows)
def signuppage():
	global signwin
	root.withdraw()
	signwin = Toplevel(root)
	signwin.title("Sign Up")
	x = -10
	y = 0
	signwin.geometry(f"1550x840+{x}+{y}")
	def signupfunction():
		global reply
		user = userentry.get()
		pas = passentry.get()
		emai = emailentry.get()

		cursor.execute(f"INSERT INTO users VALUES ('{user}','{pas}','{emai}')")
		conn.commit()
	
		reply = None
		
		reply = messagebox.showinfo("Success","You are in!!!")
		
		if reply :
			flag = 1
			signwin.withdraw()	
			buyorsell()
			
			
	def validate(event = None):
		if(conpassentry.get() and passentry.get() and userentry.get() and emailentry.get()):
			signbutton.config(state= NORMAL)
		else:
			signbutton.config(state = DISABLED)
	
	def check(event = None):
		if (passentry.get() != conpassentry.get()):
			messagebox.showerror("Error","oops!! passwords didn't match")
			conpassentry.delete(0,END)
	img8=Image.open('back.jpg')
	temp8=img8.resize((1600,1000))
	photo8=ImageTk.PhotoImage(temp8)
	Lb8=Label(signwin,image=photo8)
	Lb8.image=photo8
	Lb8.place(x=0,y=0)

	signframe=Frame(signwin,bg='whitesmoke',width='1400',height='700')
	signframe.place(x=75,y=75)
	
	txt3 = 'It\'s time to create your account'
	head3=Label(signframe,text=txt3,font=('yu gothic ui',25,'bold'),bg='blueviolet' ,fg='white')
	head3.place(x=800,y=50,width=500,height=50)

	img9=Image.open('signimg.jpg')
	temp9=img9.resize((600,700))
	photo9=ImageTk.PhotoImage(temp9)
	Lb9=Label(signframe,image=photo9)
	Lb9.image=photo9
	Lb9.place(x=0,y=0,width=600,height=700)
		
	img10 = Image.open('logback.jpg')
	temp10 = img10.resize((650,550))
	photo10=ImageTk.PhotoImage(temp10)
	Lb10=Label(signframe,image=photo10)
	Lb10.image=photo10
	Lb10.place(x=680,y=120,width=650,height=550)
	
	username = Label(Lb10,text = "Username: ",font=("Arial",15))
	username.place(x=100,y=100)
	username.config(bg="purple1")
	userentry = Entry(Lb10,width=25)
	userentry.place(x=350,y=100)
	userentry.bind("<KeyRelease>",validate)
	userentry.config(fg="black",bg="lavender",bd=2)
	password = Label(Lb10,text = "Password: ",font=("Arial",15))	
	password.place(x=100,y=170)
	password.config(bg="purple1")
	passentry = Entry(Lb10,width=25,show="*")
	passentry.config(fg="black",bg="lavender",bd=2)
	passentry.place(x=350,y=170)
	conpassword = Label(Lb10,text = "Confirm Password: ",font=("Arial",15))
	conpassword.place(x=100,y=240)	
	conpassword.config(bg="purple1")
	conpassentry = Entry(Lb10,width=25,show="*")
	conpassentry.place(x=350,y=240)
	conpassentry.bind("<KeyRelease>",validate)
	conpassentry.bind("<FocusOut>",check)
	conpassentry.config(fg="black",bg="lavender",bd=2)
	email = Label(Lb10,text = "email: ",font = ("Arial",16))
	email.place(x=100,y=310)
	email.config(bg="purple1")
	emailentry = Entry(Lb10,width = 25)
	emailentry.place(x=350,y=310)
	emailentry.bind("<KeyRelease>",validate)
	emailentry.config(fg="black",bg="lavender",bd=2)
	signbutton = Button(Lb10,text = "SignUp",padx = "25",pady = "8",state=DISABLED,command = signupfunction)
	signbutton.place(x=370,y=380)	
	signbutton.config(fg="black", bg="purple1",width = 15,height = 1)
def loginpage():
	global logwin
	root.withdraw()
	logwin = Toplevel(root)
	logwin.title("Login")
	x = -10
	y=0
	logwin.geometry(f"1550x840+{x}+{y}")
	def logfunction():
		global logwin,reply
		user = userentry.get()
		pas = passentry.get()
	
		cursor.execute(f"SELECT * FROM users WHERE user_name = '{user}'")
		user1 = cursor.fetchone()
    
		reply = None
		if(user1):
			if(user1[1] == pas):
				reply = messagebox.showinfo("Success","logged in!!!")
			else:
				messagebox.showerror("Oops !!! Invalid password")
		else:
			messagebox.showerror("Oops !!! Invalid username")
		if reply :
			flag = 0
			logwin.withdraw()
			buyorsell()
	def validate(event=None):
		if(userentry.get()):# and (len(passentry.get()) > 7)):
		    logbutton.config(state=NORMAL)
		else:
			logbutton.config(state=DISABLED)
	img4=Image.open('back.jpg')
	temp4=img4.resize((1600,1000))
	photo4=ImageTk.PhotoImage(temp4)
	Lb4=Label(logwin,image=photo4)
	Lb4.image=photo4
	Lb4.place(x=0,y=0)

	loginframe=Frame(logwin,bg='white',width='1100',height='600')
	loginframe.place(x=200,y=130)
	
	txt1 = 'WELCOME AGAIN'
	head1=Label(loginframe,text=txt1,font=('yu gothic ui',25,'bold'),bg='blueviolet' ,fg='white')
	head1.place(x=600,y=50,width=400,height=80)

	img3=Image.open('logimg.jpg')
	temp3=img3.resize((600,600))
	photo3=ImageTk.PhotoImage(temp3)
	Lb3=Label(loginframe,image=photo3)
	Lb3.image=photo3
	Lb3.place(x=0,y=0,width=600,height=600)
	

	username = Label(loginframe,text = "Username: ",font=('yu gothic ui',25,'bold'),bg='white' ,fg='purple2')
	username.place(x=650,y=257)

	entry_font = ("Arial", 12)
	userentry = Entry(loginframe,width=20)
	userentry.place(x=850,y=275)
	userentry.config(fg="black",bg="lavender",font = entry_font,bd=2)
	password = Label(loginframe,text = "Password: ",font=('yu gothic ui',25,'bold'),bg='white' ,fg='purple2')
	password.place(x=650,y=337)	
	passentry = Entry(loginframe,width=20,show="*")
	passentry.place(x=850,y=351)
	passentry.config(fg="black", bg="lavender",font = entry_font,bd=2)
	passentry.bind("<KeyRelease>",validate)

	logbutton = Button(loginframe,text = "Login",width = 15,height = 1,padx = "25",pady = "8",state = DISABLED,command = logfunction)
	logbutton.place(x=850,y=450)	
	logbutton.config(fg="black", bg="purple1",font = entry_font)


img1=Image.open('back.jpg')
temp1=img1.resize((1600,1000))
photo1=ImageTk.PhotoImage(temp1)
Lb1=Label(root,image=photo1)
Lb1.image=photo1
Lb1.place(x=0,y=0)#,width=1000,height=1000)

homeframe=Frame(root,bg='white',width='1400',height='700')
homeframe.place(x=75,y=70)
txt='WELCOME TO CAMPUS MART'

head=Label(homeframe,text=txt,font=('yu gothic ui',25,'bold'),bg='white' ,fg='violet')
head.place(x=100,y=50,width=500,height=30)

img2 = Image.open('logback.jpg')
temp2 = img2.resize((500,500))
photo2=ImageTk.PhotoImage(temp2)
Lb2=Label(homeframe,image=photo2)
Lb2.image=photo2
Lb2.place(x=50,y=120,width=500,height=500)

login = Button(Lb2,text = "Login",width = 22,height = 4,command = loginpage)
signup = Button(Lb2,text = "Sign Up",width = 22,height = 4,command = signuppage)

login.place(x=180, y=150)
signup.place(x=180, y=250)

img=Image.open('right.jpg')
temp=img.resize((700,500))
photo=ImageTk.PhotoImage(temp)
Lb=Label(homeframe,image=photo,bg='white')
Lb.image=photo
Lb.place(x=700,y=80,width=700,height=500)

root.mainloop()
