#leap year or not program

useryear=int(input("please enter a year : "))  

if (useryear%4==0 and useryear%100!=0) or useryear%400==0:
    print(useryear,"is a leap year")
else:
    print(useryear,"is not a leap year")    