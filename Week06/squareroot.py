# squareroot.py
# The program asks the user for a positive floatint-point number and outputs an approx. square root. 
# based on if the input number is odd or even. The progam ends if 1 is entered.
# Author: Ciaran Moran

number = input("Enter an positive number: ") 

def userValidation(number):
    while True:     
        try:
            numberFloat = float(number)                                                          # try convert number variable to float
            if numberFloat < 0:
                number = input("Number is negative, enter an positive number: ")                                           
                continue                                                                             # jump back to start of while loop            
            else:
                sqrt(numberFloat)                                                                    # pass numberFloat into sqrt function
                break                                                                                # exit loop 
                               
        except ValueError:                                                                       # if error raised between try and except statement:  
            number = input("Cant convert to float, enter an positive number: ")  
            continue                                                                             # jump back to start of while loop


def sqrt(numberFloat,tolerance = 0.000001):                                          # set tolerance limit to low value (will cause more loop iterations)  
    estimate = numberFloat                                                       
    diff = 9999999999                                                                    # large diff variable ensures 1st iteration of  while loop will run 

    while diff > tolerance:
        newEstimate = estimate - ((estimate**2 - numberFloat) / (2*estimate))                # Newton's Method                    
        diff = newEstimate - estimate                                                        # difference between two guesses
        diff = abs(diff)                                                                     # return absolute difference
        estimate = newEstimate 

    print("The square root of {} is approx. {}".format(numberFloat,round(newEstimate,2)))   

userValidation(number) 

# References: 
# Stored on read me file