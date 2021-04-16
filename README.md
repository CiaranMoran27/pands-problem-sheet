
<H1 align="center"> Weekly Tasks 2021 </H1>
<H1 align="center"> Programming and Scripting </H1>
<br/>

## Introduction
This README file gives a more in-depth explanation of the code used to complete the weekly tasks for the 2021<br/>Programming and Scripting GMIT module as part of the Higher Diploma in Science in Computing.  
<br/>


## Task 1: (Bmi.py):
*Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres<br/>and weight in kilograms. The output is their weight divided by their height in metres squared.* 
<br/>

### Code:
``` Python
height = float(input("What is your height in centimetres?:"))
weight = float(input("What is your weight kilograms?:"))
metres_sq = (height/100)**2
bmi = round(weight / metres_sq,2)
print("BMI is " + str(bmi) + ' kg/m²')
```

### Code breakdown:
- User is asked for their height(cm) and weight(Kg).
- Height is convered from cm to m² and stored in *metres_sq* variable.
- Weight(Kg) is divided by height(m²), rounded to two decimal places and passed to *bmi* variable.
- The bmi result is passed into a {} placeholder via string formatting and printed.

<br/>

### References:
1.	Active, 2021, What is BMI and How to Calculate It, viewed 31 Jan 2021,<br/>*<https://www.active.com/fitness/articles/what-is-bmi-and-how-to-calculate-it>*.
2.	GeeksforGeeks, 2021, round () function in Python, viewed 31 Jan 2021,<br/>*<https://www.geeksforgeeks.org/round-function-\python>*.
3.	Real Python, 2021, A guide to the newer Python string format techniques, viewed 31 Jan 2021,<br/>*<https://realpython.com/python-formatted-output>*.
4.	Sweigart, A, 2015, Automate the boring stuff with Python, No Starch press, San Francisco, pp 15.
<br/>
<br/>

## Task 2: (secondstring.py):

*Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*
<br/>

### Code:
``` Python
sentence = input("Please enter a sentence: ")
reverse_string = sentence[::-2]
print(reverse_string)
```

### Code breakdown:
- User is asked to input a sentence.
- The full string is sliced by default as no index number is placed in the first two placeholders of [::-2].
- A negative stride of 2 is used and the the resulting string stored in the reverse_string variable.
- The reversed string is printed.
<br/>

### References:
1. Real Python, 2021, String slicing, viewed 31 Jan 2021,<br/>*<https://realpython.com/python-strings/#specifying-a-stride-in-a-string-slice>*.

<br/>
<br/>

## Task 3: (collatz.py):

*Write a program that asks the user to input any positive integer and outputs the successive values of the following:*<br/>
 *At each step calculate the next value by taking the current value and:*
    - *Divide by 2 if even.*
    - *Multily by 3 and add 1 if odd.*
    - *End the progam if current value is 1.*

<br/>

### Code:
``` Python
numberList = []

number = input("Enter a number: ")
                                       

while True:
    try:
        numberInt = int(number)                                            
        numberList.append(int(number))                                      
        if numberInt < 0:                                                   
            numberInt = int(input("Enter a Enter a positive number: "))
            continue                                                           
        else:
            break                                                             

    except ValueError:                                                  
        number = input("Enter an integer: ")    
        continue                                                            


while numberInt!=1:                                                 
    if numberInt % 2 == 0:                                              
        numberInt = numberInt // 2                                          
    else:
        numberInt = (numberInt * 3) + 1                                    
    numberList.append(numberInt)       
print(numberList)
```

### Code breakdown:
- User is asked for a positive integer.
- **First While loop** is designed to validate the user input in the block of code between  *try* and *except* where:
    - Tries to convert the input string to an integer, if this fails a *ValueError* is raised and the program asks the<br/> user to *"Enter an integer: "* and jumps back to the start of the while loop.
    - Assuming that point 1 above has executed sucessfully (i.e the user input can be cast as an integer) the program<br/>checks if the integer is negative, in which case the program asks user to "Enter a positive number:" and jumps<br/>back to the start of the while loop.
 - **Second While loop** performs sucessive calculations on user input and resulting values until the resulting value=1. 
     - Checks if the remainder of the user input divided by 2 = 0 (i.e is it even), in which case the program re-defines<br/>the *numberInt* variable as itself divide by 2 and appends it to *numberList*.
     - Checks if the remainder of the user input divided by 2 != 0 (i.e is it odd), in which case the program re-defines<br/>the *numberInt* variable as (itself divided by 3) + 1 and appends it to *numberList*.
         - The while loop runs re-uses the newly defined *numberInt* variable until the value = 1, then the list is <br/>printed.
<br/>
<br/>

### References:
1. Cunningham, P, 2014, Check if input is positive integer, viewed 19 Feb 2021, <br/>*<https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer>*.
2. Real Python, 2021, The try and except Block: Handling Exceptions, viewed 19 Feb 2021,*<https://realpython.com/python-exceptions/>*.
3. Programiz, 2021, What is the use of break and continue in Python?, viewed 19 Feb 2021,<br/>*<https://www.programiz.com/python-programming/break-continue>*.  

<br/>
<br/>

## Task 4: (weekday.py):

*Write a program that outputs whether or not today is a weekday.*
<br/>

### Code:
``` Python
weekIndex = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wednesday",
    3 : "Thursday",
    4 : "Friday",
    5 : "Saturday",
    6 : "Sunday"
}

todaysDate = datetime.date.today()   
dayIndex = todaysDate.weekday()       


weekendMsg = "It is the weekend, yay! (Day: {})".format(weekIndex[dayIndex])
weekdayMsg = "Yes, unfortunately today is a weekday (Day: {}).".format(weekIndex[dayIndex])

if dayIndex > 4:
    print(weekendMsg)
else:
    print(weekdayMsg)
```

### Code breakdown:
- The datetime module is imported
- Dictionary named weekIndex is declared:
    - Keys are set to 0-6 which represent the index of the days of the week (i.e index 0 = Monday, index 6 = Sunday).
    - Values distunguish between the days of the week.
    - The *todaysDate* variable uses the *.date.today* methods of  datetime library to obtain todays date.
    - The *dayIndex* variable uses the *.weekday* method of  datetime library to convert todays date to an index <br/>number(0 - 6).
    <br/>
- The dayIndex is checked in a if statement, 
    - if the value is greater than 4 the weekend message is printed and the dictionary is used to print the day of the week using the dayIndex as a reference. 
    - The else result is the same as the if, except the weekend message is replaced with the weekday message.
<br/>

### References:
1. Sweigart, A, 2015, Automate the boring stuff with Python, Dictionaries and structuring data, No Starch press,<br/> San Francisco, pp 120.
2. Docs.python.org, 2021, Datetime — Basic date and time types — Python 3.9.2 Documentation, viewed 20 Feb 2021,<br/>*<https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday>*.

<br/>

## Task 5: (squareroot.py):

*Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*
<br/>

### Code:
``` Python
number = input("Enter an positive number: ") 

def userValidation(number):
    while True:     
        try:
            numberFloat = float(number)                                                          
            if numberFloat < 0:
                number = input("Number is negative, enter an positive number: ")                                           
                continue                                                                                       
            else:
                sqrt(numberFloat)                                                                    
                break                                                                                
                               
        except ValueError:                                                                       
            number = input("Cant convert to float, enter an positive number: ")  
            continue                                                                             



def sqrt(numberFloat,tolerance = 0.000001):                                          
    estimate = numberFloat                                                       
    diff = 9999999999                                                                    

    while diff > tolerance:
        newEstimate = estimate - ((estimate**2 - numberFloat) / (2*estimate))                                
        diff = newEstimate - estimate                                                        
        diff = abs(diff)                                                                     
        estimate = newEstimate 

    print("The square root of {} is approx. {}".format(numberFloat,round(newEstimate,2)))   

userValidation(number)  
```

### Code breakdown:
- User is asked for a positive integer.
    <br/>

- **User Validation function** is designed to validate the user input in the block of code between  *try* and *except* where the function:
    - Tries to convert the input string to a float, if this fails a *ValueError* is raised and the program asks the<br/> user to enter a positive number and jumps back to the start of the while loop.
    - Assuming that point 1 above has executed sucessfully (i.e the user input can be cast as a float) the program<br/>checks if the float is negative, in which case the program asks user to enter a positive number and jumps back to the<br/>start of the while loop.
    -  Condintinal that the user input meets the preceeding criteria, the input is passed into the *sqrt* function.
   <br/>

 - **Square Root Function** uses Newton's method for approximating square root which works by producing successively better approximations:
     - The function recieves the user input *numberFloat* which is re-defined as *estimate*.
     - The function parameter *tolerance* is set to a low number. Assigning a low number is important as it will play<br/>a part in determining when the proceeding while loop will break.
     - A variable called *diff* is set to a large number to ensure the first iteration of the while loop will run<br/>(i.e *while diff > tolerance*).
     - The *newEstimate* variable contains the result of applying Newtons equation to the userinput. The variable then gets redefining to *estimate* (for further use on next while loop iteration).
     - If the difference between the *newEstimate* and *estimate* (i.e user input on first iteration) is greater than<br/>the tolerance limit set then the while loop restarts, however when its less the output is printed.

### References:
1. Real Python, 2021, Defining Your Own Python Function,Argument Passing, viewed 27 Feb 2021,<br/>*<https://realpython.com/defining-your-own-python-function/#argument-passing>*.
2. Sıddık Açıl, 2018, Newton Square Root Method in Python, viewed 27 Feb 2021,<br/>*<https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d>*.
3. Approximating Square Roots w/ Newton's Method,2018, added by Nerdfirst, viewed 27 Feb 2021<br/>*<https://www.youtube.com/watch?v=tUFzOLDuvaE&t=1042s>*.

<br/>
<br/>


## Task 6: (es.py):

*This program reads in a text file that is requested by user and outputs the number of "e" characters in the file.*
<br/>

### Code:
``` Python
import sys

filename = sys.argv[1] 

def readFile(filename):
    with open(filename,'r') as f:                 
        data = f.read()                               
        return data
        

def eCharacterCount(data):
    eCount = data.count("e")                                   
    ECount = data.count("E")
    eTotal = eCount + ECount

    print("There are {} lowercase 'e' characters in this text file".format(eCount))
    print("There are {} uppercase 'E' characters in this text file".format(ECount))    
    print("There are {} total 'e' characters in this text file (case independant)".format(eTotal))
 
data = readFile(filename)
eCharacterCount(data)
```

### Code breakdown:

- **.argv[]**  #This method of the system library accepts arguements from the command line and stores them<br/>in a list. The list contains the filename as the first argument (index 0) and any further arguments are stored in the proceeding index values. In this script sys.argv[1] is stored in the filename variable.
   <br/>

- **readFile Function:**
    - Filename variable is passed into this function (i.e second argument from command line). 
    - Function attempts a read file operation using the filename variable and returns the file if successful.
    - If a file is returned its stored in a variable called data.
   <br/>

- **eCharacterCount Function:**
    - This function recieves the data variable which contains the file that was read in previously.
    - Note: String count() method iterators over a string to return a count of a specified substring.
    - Three eCount variables are declared, these store the number of upper/lowercase and total e characters<br/>(obtained using the count() method). the contents of these variables are printed with descriptors.
   <br/>


### References:
1. Docs.python.org, 2021, 7.2. Reading and Writing Files — Python 3.9.2 Documentation, viewed 05 March 2021,<br/> 
*<https://docs.python.org/3/tutorial/inputoutput.html>*.
2. GeeksforGeeks, 2019, With statement in Python, viewed 05 March 2021,<br/>
*<https://www.geeksforgeeks.orgwith-statement-in-python>*.
3. Gutenberg.org, 2000, Moby Dick, viewed 05 March 2021,<br/>*<https://www.gutenberg.org/files/2701/old/moby10b.txt>*.


<br/>
<br/>


## Task 7: (plottask.py):

*This program displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.*
<br/>

### Code:
``` Python
import matplotlib.pyplot as plt
import numpy as np
import os

x = np.arange(0,5,1)                              
                                                                                                
y1  =  x                                          
y2  =  x**2                                       
y3  =  x**3                                       

xy1_label = 'f(x)=x'
xy2_label = 'g(x)=x^2'
xy3_label = 'h(x)=x^3'    

xy1_Colour = 'red'
xy2_Colour = 'green'
xy3_Colour = 'blue'

xAxisLabel = 'x - axis'
yAxisLabel = 'y - axis'
AxisFontSize = 12 

xy_linetype =  'dashed'
plotAreaColour = "lightgrey"


def customPlot(): 
    plt.plot(x, y1, color = xy1_Colour, linestyle = xy_linetype, label = xy1_label)
    plt.plot(x, y2, color = xy2_Colour, linestyle = xy_linetype, label = xy2_label)
    plt.plot(x, y3, color = xy3_Colour, linestyle = xy_linetype, label = xy3_label)

    plt.xlabel(xAxisLabel, fontsize = AxisFontSize)
    plt.ylabel(yAxisLabel, fontsize = AxisFontSize)

    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",mode="expand", borderaxespad=0, ncol=3, fontsize = 14)
    plt.grid(True,which="both", linestyle='--')

    ax = plt.axes()
    ax.set_facecolor(plotAreaColour)
    return plt


def writePlot(myPlot):
    os.chdir(os.path.dirname(__file__))
    plt.savefig('plottask.png')
    plt.show()


myPlot = customPlot()
writePlot(myPlot)
```

### Code breakdown:

- **Declaring  Variables** 
    - An array of 0 to 4 in steps of 1 are stored in the x variable, achieved using the numpy library.
    - x, x squared and x cubed arrays are stored in y, y1 and y2 variables respectively.
    - Plot descriptors such as axis labels, legend labels, linetype, series colours and plot colour are stored in<br/>multiple variables 

- **customPlot function** 
    - Passes the pre-declared plot variables into the of the plot function of the Matplotlib library.
    - Adds custom x and y Axis labels and legend then returns the plot.
    - Plot is stored in myPlot variable.

- **writePlot Function:**
    - This function recieves the myPlot variable (i.e customPlot return statement).
    - The directory is changed to that of the this file using *os.chdir(os.path.dirname(__file__)).*
    - plot stored in myPlot variable is saved as extension .png.



### References:
1. Eric, 2015, Save matplotlib file to a directory, viewed 11 March 2021,<br/>
*<https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory>*.
2. Nick T, 2014, How to change plot background color?, viewed 11 March 2021,<br/>
*<https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color>*.
3. Matplotlib.org, 2021, Controlling the legend entries, Matplotlib version 3.3.3, viewed 11 March 2021,<br/>
*<https://matplotlib.org/3.3.3/tutorials/intermediate/legend_guide.html>*.
4. Matplotlib.org, 2021, Plotting multiple sets of data, Matplotlib version 3.3.4, viewed 11 March 2021,<br/>
*<https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html>*.
5. Moonbooks.org, 2019, How to add a grid on a figure in matplotlib?, viewed 11 March 2021,<br/>
*<https://moonbooks.org/Articles/How-to-add-a-grid-on-a-figure-in-matplotlib-/>*.
6. Real Python, 2021, NumPy arange(): How to Use np.arange(), viewed 11 March 2021,<br/>
*<https://realpython.com/how-to-use-numpy-arange/>*.

<br/>
<br/>


































