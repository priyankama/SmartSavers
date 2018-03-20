
import sqlite3
import smtplib
from datetime import *
print ("WELCOME TO SMART SAVER'S")
print()

EWallet1=0
EWallet2=0
EWallet3=0


def test(ID,Mob,Name,EWallet1,EWallet2,EWallet3,Datetime):
    c=sqlite3.connect("test2")
    cmd="SELECT * FROM Wallet WHERE ID="+str(ID)
    cur=c.execute(cmd)
    flag=0
    a=(ID,Mob,Name,EWallet1,EWallet2,EWallet3,Datetime)
    for row in cur:
        flag=1
    if flag==1:
        cmd="UPDATE Wallet (ID,Mob,Name,EWallet1,EWallet2,EWallet3,Datetime) VALUES ('%d','%d','%s','%d','%d','%d','%s')"
    else:
        cmd="INSERT INTO Wallet (ID,Mob,Name,EWallet1,EWallet2,EWallet3,Datetime) VALUES ('%d','%d','%s','%d','%d','%d','%s')"
    c.execute(cmd%a)
    c.commit()
    c.close()

x=int(input("ID"))
y=int(input("Mob"))
z=input("Name")
p=int(input("Amount in wallet1 "))
q=int(input("Amount in wallet2 "))
r=int(input("Amount in wallet3 "))
now= datetime.now()
test(x,y,z,p,q,r,now)

def subtract(currency,pay):
    return currency-pay
s=0
r= int(input("Enter amount to pay"))
if(s>r):
    print ("Amount left = ",subtract(s,r))
else:
    print ("Less money in your wallet\nAdd",(r-s),"in your wallet")

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







