
import sqlite3
import smtplib
from datetime import *
print ("WELCOME TO SMART SAVER'S")
print()

def test(ID,Name,Mob,Amount,DateTime):
    c=sqlite3.connect("p.db")
    cmd="SELECT * FROM pihu WHERE ID="+str(ID)
    cur=c.execute(cmd)
    flag=0
    a=(ID,Name,Mob,Amount,DateTime)
    for row in cur:
        flag=1
    if flag==1:
        cmd="UPDATE pihu (ID,Name,Mob,Amount,DateTime) VALUES ('%d','%s','%d','%d','%s')"
    else:
        cmd="INSERT INTO pihu (ID,Name,Mob,Amount,DateTime) VALUES ('%d','%s','%d','%d','%s')"
    c.execute(cmd%a)
    c.commit()
    c.close()

w=input("Name")
x=int(input("ID"))
y=int(input("Mob"))
z=int(input("Amt"))
now= datetime.now()
test(x,w,y,z,now)

def subtract(currency,pay):
    return currency-pay
s=0
r= int(input("Enter amount to pay"))
if(s>r):
    print ("Amount left = ",subtract(s,r))
else:
    print ("Less money in your wallet\nAdd",(r-s),"in your wallet")

def add(currency,pay):
    return currency+pay
r= int(input("Enter amount to add in your wallet"))
print ("Amount added in your wallet = ",add(s,r))

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('lakshyakh08@gmail.com','lk08101998')
mail.sendmail('lakshyakh08@gmail.com','pihuphalod@gmail.com',(str(r)+"Money you  have received from lakshya"))
mail.close()
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('lakshyakh08@gmail.com','lk08101998')
mail.sendmail('lakshyakh08@gmail.com','lakshyakh08@gmail.com',(str(r)+"= Money deducted from your account lakshya\n"+str(s-r)+" Money left in your account"))
mail.close()







