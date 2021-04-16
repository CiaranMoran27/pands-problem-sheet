# es.py
# This program reads in a text file from an arguement on the command line. 
# It outputs the number of "e" characters in the file.
# Author: Ciaran Moran

# Notes:
# As per feedback below I updated filename to read the 2nd arguemnt from the command line
# (this was not the case in "Programming Repository")

# Feedback:
# I asked you to read in the file name as an argument (apart from that this is very comprehensive)



#import os
import sys

filename = sys.argv[1]                             # accept the 2nd arguement from the command line

def readFile(filename):
    with open(filename,'r') as f:                     # open file in read only mode, use of alias means no need to close file
        data = f.read()                                  # call the read function on the alias
        return data
        


def eCharacterCount(data):
    eLowerCount = data.count("e")                       # use of .count method to count occurances of a character in a file               
    eUpperCount = data.count("E")
    eTotalCount = eCount + ECount

    print("There are {} lowercase 'e' characters in this text file".format(eLowerCount))
    print("There are {} uppercase 'E' characters in this text file".format(eUpperCount))    
    print("There are {} total 'e' characters in this text file (case independant)".format(eTotalCount))
 
data = readFile(filename)
eCharacterCount(data)

# References: 
# Stored on read me file