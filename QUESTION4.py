import numpy as np 
import random 
import math 
import matplotlib.pyplot as plt


#4a
#it is an infintie loop and the same value is assigned at first 
#>= in if statement can be changed to 

#root should be assigned 0 first

#4b
def foo2(value, tolerance):
    x = value
    root = value #assum sqrt of x is x
    while abs(root - x) >= tolerance:
        x = ( root+ (value/ root))*0.5 
        root =x
    return root

foo2(2, 10 ** -5)==math.sqrt(2) #should there by 3 arguments?

foo2(51,  10 ** -5) ==math.sqrt(51)
foo2(1029, 10 ** -5) ==math.sqrt(1029)

#Qc
def foo3(value, tolerance):
    x = value
    root = 0
    iterats = 0
    while abs(root - x) >= tolerance:
        root =(x + (value / x))**0.5
        x = root
        iterats+=1 #each iteration add 1
    return root
#x-aaxis
x_axis = np.arange(10e-12, 1, 10e-1)

#y_axis
y = [] #random integers 

for i in range(100):
    y.append(random.randrange(2, 10**6))
    
#make meshgrid 


#T,X = np.meshgrid(x_axis,y)
#z_axis = foo3(int(T),int(X)) 