#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import pyperclip, re

#date regex
dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

#split the groups into days, months, years
days = []
months = []
years = []
fullDates = []

text = str(pyperclip.paste())
for groups in dateRegex.findall(text):
    date = '/'.join([groups[0],groups[1],groups[2]])
    fullDates.append(date)
    days.append(groups[0])
    months.append(groups[1])
    years.append(groups[2])
    




#check if date is valid

validDates = []
fullRejects = []

#checks for given year range
for i in range(len(days)):
    if int(years[i]) > 2999 or int(years[i]) < 1000: 
        fullRejects.append(fullDates[i])
    #checks for valid months
    elif (int(months[i]) == 1 or int(months[i]) ==3 or int(months[i]) == 5 or int(months[i]) == 7 or int(months[i]) == 8  or int(months[i]) == 10 or int(months[i]) == 12) and (int(days[i]) <= 31):
        validDates.append(fullDates[i])
    elif (int(months[i]) == 4 or int(months[i]) == 6 or int(months[i]) == 9 or int(months[i]) == 11) and (int(days[i]) <=30):
        validDates.append(fullDates[i])
    
    #checks February specifically because of leap years  
    elif months[i] == '02':
        if int(years[i]) % 4 == 0 and int(days[i]) <= 29:
            if (int(years[i]) % 100 == 0 and int(years[i]) % 400 != 0):
                fullRejects.append(fullDates[i])
            else:
                validDates.append(fullDates[i])
        elif int(days[i]) <= 28:
            validDates.append(fullDates[i])

   
        




for i in validDates:
    print(' This is a valid date: ' + i)




