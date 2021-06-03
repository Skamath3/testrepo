# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:14:52 2020

@author: sanch
"""
print("\n This is run by Sancchit")
print
while True:
    print
    celsius_temp = input("What is the temperature in Celsius you want to convert?- Type the value or 'done' to exit: ")
    if celsius_temp == 'done':
        print ('\nThanks for using this tool!\n')
        break
    # checking if the input is numeric. If not it will start the whole loop again
    if celsius_temp.isdigit() == False:
        continue
    #  calculating the conversion
    fahrenheit_temp = float(celsius_temp) * 1.8 + 32
    print ('\n---The Fahrenheit equivalent of', celsius_temp, 'is:', fahrenheit_temp)