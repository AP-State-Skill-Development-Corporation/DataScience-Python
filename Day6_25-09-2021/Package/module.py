def Leap_Yr(year):
    if (year%4 == 0) | (year%400==0 & year%100 != 0) :
        return True
    else :
        return False
    
def Check_Number():
    n = int(input("Enter any number"))
    if n<0 :
        print("Negative Number")
    else:
        print("Positive Number")