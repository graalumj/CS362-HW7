# FizzBuzz.py
# By Alex Graalum

def fizzbuzz(x):
    if x % 15 == 0:
        return("FizzBuzz")
    elif x % 5 == 0:
        return("Buzz")
    elif x % 3 == 0:
        return("Fizz")
    else:
        return(str(x))
        
if __name__ == '__main__':
    for x in range(100):
        print(fizzbuzz(x+1))