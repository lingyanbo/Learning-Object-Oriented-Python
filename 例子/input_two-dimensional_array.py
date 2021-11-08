'''
python input a two-dimensional array
First enter an array to divide it with regularity
Secondly, define a one-dimensional array and add a number to a one-dimensional array
Then add the one-dimensional array to the two-dimensional
'''
import re


data2D = []

while True:
    userInput = input('Input:')  # Enter the array, separated by spaces

    info = re.split(r'[\D]',userInput)  # Regular expression split

    data = []  # Define a one-dimensional array

    try:
        for number in info:
            data+=[int(number)]  # One-dimensional array join numbers
        data2D+=[data]  # Add one-dimensional array to two-dimensional
    except:
        break;
data2D
