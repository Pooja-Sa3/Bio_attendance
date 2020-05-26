import cv2
import face_recognition as fc
import pandas as pd
import numpy as np
import smtplib as sm
import random as r
import time
f=pd.read_csv(r'C:\Users\lenovo\Downloads\student.csv')
fd=cv2.CascadeClassifier(r'C:\Users\lenovo\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
user=input('enter name')
user in f.items()
if(True):
    password=input('enter the password')
    password in f.items()
    if(True):
        v=cv2.VideoCapture(0)
        ret,i=v.read()
        j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        face=fd.detectMultiScale(j)
        print(face)
        f=fc.face_locations(i)
        f_enc=fc.face_encodings(i,f)
        f_enc in f
        if(True):
            while(True):
                c=''
                c=c+str(r.randint(1000,9999))
                m=c
                sender='palak33sahu@gmail.com'
                p=f[user][password]
               
                sender=f[p]
                msg=m
                s=sm.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login(sender,'@AIR2016in')
                s.sendmail(sender,recievers,msg)
                s.close()
                OTP=input('enter your OTP')
                if(OTP==c):
                    f['attendence']=att
                    att=att+1
                    print('your attendence is marked')
                t=time.localtime()
                time_enter=time.strftime("%H:%M:%S",t)
                today9am = t.replace(hour=9, minute=0, second=0, microsecond=0)
                if(today9am> time_enter):
                    sender='palak33sahu@gmail.com'
                    recievers=f['user']['email']
                    msg="""you are late and warned to not to do so again
                    if you did this more than 5 time you will probably face a probation
                    Have A nice day"""
                    s=sm.SMTP('smtp.gmail.com',587)
                    s.starttls()
                    s.login(sender,'@AIR2016in')
                    s.sendmail(sender,recievers,msg)
                    s.close()
                        
                            
        else:
            print('your attendence cannot be marked')
    else:
        print('you have entered wrong credential')
        sender='palak33sahu@gmail.com'
        recievers=f['user']['email']
        pass__=f['user','password']
        msg=pass__
        s=sm.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(sender,'@AIR2016in')
        s.sendmail(sender,recievers,msg)
        s.close()
print('this user dosent exist')
u=input('your name')
pa=input('enter the password')
v1=cv2.VideoCapture(0)
ret,k=v1.read()
f_k=fc.face_locations(k)
fe_k=fc.face_encodings(k,f_k)
e=input('enter email address')
f({'store_user':u,'store_pass':pa,'f_enco':fe_k,'email':e},ignore_index=True)











