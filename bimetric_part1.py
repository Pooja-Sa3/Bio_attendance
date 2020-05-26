import os
import cv2
import numpy as np
import pandas as pd
import face_recognition as fc
import xlsxwriter as xl
import xlrd
import openpyxl
import csv
data=pd.read_csv(r'C:\Users\lenovo\Desktop\asd.csv')
f=pd.DataFrame(data)
user=input('Create Username: ')
password=input('Create password: ')
mobile=input('Mobile No.: ')
email=input('Email: ')
v=cv2.VideoCapture(0)
ret,i=v.read()
fl=fc.face_locations(i)
fe=fc.face_encodings(i,fl)
details=[user,password,mobile,email,fe]
df=pd.DataFrame()
df['Username']=details[0::5]
df['Password']=details[1::5]
df['Mobile']=details[2::5]
df['Email']=details[3::5]
df['Pic_Encoding']=details[4::5]
data=data.append(df,ignore_index=True,sort=False)
#data.to_excel('Data.xlsx',index=False)
data.to_csv(r'C:\Users\lenovo\Desktop\asd.csv')

