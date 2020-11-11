# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:32:10 2020

@author: limbs
"""

def inputIsValid(strIn):
    if type(strIn) != type(""):
        return False
    if strIn == "":
        return False
    else:
        return True

def getInput():
    plantName = []
    wateringFrequency = []
    while not inputIsValid(plantName):
        plantName = input("Enter the name of your plant: \n")
        if not inputIsValid(plantName):
            print("Sorry, I don't understand that plant name")
    
    while not inputIsValid(wateringFrequency):
        wateringFrequency = input("How often does your plant need watering?: \n")
        if not inputIsValid(wateringFrequency):
            print("Sorry, I don't understand that")