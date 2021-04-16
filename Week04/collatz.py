# collatz.py
# The program asks the user for a positive integer and outputs successive values 
# based on if the input number is odd or even. The progam ends when output value = 1.
# Author: Ciaran Moran

numberList = []

number = input("Enter a number: ")
                                       

while True:
    try:
        numberInt = int(number)                                             # try convert number variable to int 
        numberList.append(int(number))                                      # include user input as index[0] in list
        if numberInt < 0:                                                   # checks the number is positive
            numberInt = int(input("Enter a Enter a positive number: "))
            continue                                                            # jump back to start of while loop
        else:
            break                                                               # exit loop 

    except ValueError:                                                  # if error raised between try and except statement:
        number = input("Enter an integer: ")    
        continue                                                            # jump back to start of while loop


while numberInt!=1:                                                 # exits while loop when value is not 1
    if numberInt % 2 == 0:                                              # check if number is even
        numberInt = numberInt // 2                                          # re-defines numberInt variable as itself divide by 2
    else:
        numberInt = (numberInt * 3) + 1                                     # if odd re-defines numberInt variable  as (itself x 3)+1
    numberList.append(numberInt)       
print(numberList)

# References: 
# Stored on read me file