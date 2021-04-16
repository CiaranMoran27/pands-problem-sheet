# weekday.py
# This program that outputs whether or not today is a weekday.
# Author: Ciaran Moran

# Notes: Based on the feedback below I changed the check to use the index value and updated the dictionary to output 
# day name based on the index in the dictionary as an extra. Also the print messages are now stored in variables.

# Feedback:
# I love the fact that you store the information in weekindex.  
# Though it would be quicker to access it by index then using a for loop, 
# also it would be better if the messages were stored in a variable each and put into the list by variable. 
# (that way if you...

import datetime

# dictionary with index 0:6 for Monday:Sunday as keys and days of week as values
weekIndex = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wednesday",
    3 : "Thursday",
    4 : "Friday",
    5 : "Saturday",
    6 : "Sunday"
}

todaysDate = datetime.date.today()    # checks what day it is
dayIndex = todaysDate.weekday()       # converts the day to index 0:6 for Monday:Sunday


weekendMsg = "It is the weekend, yay! (Day: {})".format(weekIndex[dayIndex])
weekdayMsg = "Yes, unfortunately today is a weekday (Day: {}).".format(weekIndex[dayIndex])

if dayIndex > 4:
    print(weekendMsg)
else:
    print(weekdayMsg)


# References: 
# Stored on read me file