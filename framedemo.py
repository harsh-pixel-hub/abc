from tkinter import *
from tkinter import  messagebox
import  mysql.connector as m1
con=m1.connect(host='localhost',user='root', database='personaldetails',password='')
root = Tk()
root.geometry('600x400+50+50')
root.title('frame demo')
root.configure(bg = 'red')

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    x.set(0)
    y.set(0)
    z.set(0)

def submit():

    a=e1.get()
    b=e2.get()
    c=int(e3.get())
    d=e5.get()
    e = int(e6.get())
    if x.get()==1:
        m = 'male'
    if y.get()==1:
        m='female'
    if z.get()==1:
        m='other'
    cursor=con.cursor()
    qry= 'insert into studentdeatils values( "{}", "{}" ,{}, "{}" ,{},"{}")'.format(a,b,c,d,e,m)
    cursor.execute(qry)
    con.commit()
    messagebox.showinfo(message='Data saved successfully')


x=IntVar()
y=IntVar()
z=IntVar()


f2 = LabelFrame(root,text = 'Personal details',width = 600,height = 200,bg = 'white')
f2.pack()

l1  = Label(f2,text = 'Enter Name')
l1.place(x=50,y=50)

e1 = Entry(f2)
e1.place(x = 150,y =50)

l2=Label(f2, text='Course')
l2.place(x = 300,y=50)

e2=Entry(f2)
e2.place(x=370,y=50)

l3=Label(f2, text='Age')
l3.place(x=50,y=100)

e3=Entry(f2)
e3.place(x=150,y=100)

l4=Label(f2,text='Gender')
l4.place(x=300,y=100)

ch1=Checkbutton(f2,text='Male',onvalue=1,offvalue=0,variable=x)
ch1.place(x=370,y=100)

ch2=Checkbutton(f2,text='Female',onvalue=1,offvalue=0,variable=y)
ch2.place(x=445,y=100)

ch3=Checkbutton(f2,text='Other',onvalue=1,offvalue=0,variable=z)
ch3.place(x=525,y=100)

f1 = Frame(root,width = 600,height = 200,bg = 'cyan')
f1.pack()

l5=Label(f1,text='Qualification')
l5.place(x=150,y=30)

e5=Entry(f1)
e5.place(x=270,y=30)

l6=Label(f1,text='CGPA')
l6.place(x=150,y=65)

e6=Entry(f1)
e6.place(x=270,y=65)

b1=Button(f1,text='SUBMIT',font=('Algerian','10'),fg='white',bg='black',command=submit)
b1.place(x=150,y=150)

b2=Button(f1,text='Exit',font=('Algerian','10'),fg='white',bg='black',command=f1.destroy)
b2.place(x=300,y=150)

b3=Button(f1,text='Clear',font=('Algerian','10'),fg='white',bg='black',command=clear)
b3.place(x=450,y=150)


root.mainloop()
