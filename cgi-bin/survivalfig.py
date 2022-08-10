#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb

import cgitb; cgitb.enable()

import os

import random

# Create instance of FieldStorage
form = cgi.FieldStorage()

procid = os.getpid()

Gender = form.getvalue('Gender')
Age = form.getvalue('Age')
EOR = form.getvalue('EOR')
Ki67 = form.getvalue('Ki67')
Grade = form.getvalue('Grade')
Location = form.getvalue('Location')
TumorSide = form.getvalue('TumorSide')
Diameter = form.getvalue('Diameter')
Chemotherapy = form.getvalue('Chemotherapy')
Radiotherapy = form.getvalue('Radiotherapy')
PolysomyStatus = form.getvalue('PolysomyStatus')

print()

with open('header.html') as f:
    lines = f.readlines()
    for i in lines:
        print(i, end='')
    f.close()

if Gender=="": 
    print(f'Gender missing')
elif Age=="": 
    print(f'Age missing')
elif EOR=="": 
    print(f'EOR missing')
elif Ki67=="": 
    print(f'Ki67 missing')
elif Grade=="": 
    print(f'Grade missing')
elif Location=="": 
    print(f'Location missing')
elif TumorSide=="":  
    print(f'TumorSide missing')
elif Diameter=="": 
    print(f'Diameter missing')
elif Chemotherapy=="": 
    print(f'Chemotherapy missing')
elif Radiotherapy=="": 
    print(f'Radiotherapy missing')
elif PolysomyStatus=="": 
    print(f'PolysomyStatus missing')
else:
    print (f'<h3>Oligodendroglioma recurrence and survival prediction</h3>')
#  os.system(f"Rscript survplot.r {Gender} {Age} {EOR} {Ki67} {Grade} {Location} {TumorSide} {Diameter} {Chemotherapy} {Radiotherapy} {PolysomyStatus} {procid}")
    
    os.system(f"R < survplot.r --vanilla --slave --args {Gender} {Age} {EOR} {Ki67} {Grade} {Location} {TumorSide} {Diameter} {Chemotherapy} {Radiotherapy} {PolysomyStatus} {procid}")
    print (f'<img src=\"outfig.py?name={procid}_relapse.jpg\"  alt=\"{procid}2.jpg\">')
    print (f'<img src=\"outfig.py?name={procid}_surv.jpg\"  alt=\"{procid}.jpg\">')


with open('footer.html') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
