# bmi.py
# The program calculates the BMI of the user:
# Author: Ciaran Moran

# Asks the user for their height (cm) and weight (Kg)
height = float(input("What is your height in centimetres?:"))
weight = float(input("What is your weight kilograms?:"))

#Converts height from cm to m²
metresSquared = (height/100)**2

# Computes BMI
bmi = round(weight / metresSquared,2)

#Prints BMI Output
print("BMI is " + str(bmi) + ' kg/m²')


# References: 
# Stored on read me file