# LeapYear.py
# By Alex Graalum

def leapyear(x):
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False
        
if __name__ == '__main__':
    x = int(raw_input("Enter a desired year: "))
    if(leapyear(x)):
        print(str(x) + " is a leap year")
    else:
        print(str(x) + " is not a leap year")

