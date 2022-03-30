# ageClassifier.py
# Author: Cody Vantienen
# Date: 10/7/20
# Purpose:Write a program that prompts the user to enter their age displays a message indicating whether the person is an infant, child, teenager, or an adult.
# Notes: 
# infant <= 1
# child > 1 < 13
# teenager > 13 < 20
# adult > 20

# input
ageInput = int(input("Please enter your age in years: "))
print()
# Working variable 
classification ="none"

# Algorithm/Conditional Processing
if ageInput <= 1:
    #print("Based on the age you entered, you are classified as a/an: infant)
    classification = "infant"
else: 
    if ageInput <= 12: 
        #print("Based on the age you entered, you are classified as a/an: child)
        classification =  "child"
    else: 
        if ageInput <= 20:
            #print("Based on the age you entered, you are classified as a/an: teenager)
            classification =  "teenager"
        else:
            #print("Based on the age you entered, you are classified as a/an: adult)
            classification =  "adult"
               
# output Section
print("Based on the age you entered, you are classified as a/an: ", classification) 

        



