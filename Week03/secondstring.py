# secondstring.py
# This program takes in a string the user and outputs every second letter in reverse order.
# The first and last characters of the string are indexed by default and a negative stride of 2 is used.
# Author: Ciaran Moran

sentence = input("Please enter a sentence: ")
reverseString = sentence[::-2]
print(reverseString)

# References: 
# Stored on read me file