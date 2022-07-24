year = int(input("Which year do you want to check? "))
if year % 4 ==0 and year % 400 ==0:
    print("Leap year ")
elif year % 100 ==1:
    print("not Leap year")    
else:
    print("not leap year")       


