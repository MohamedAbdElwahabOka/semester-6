from math import *


error = 100
xr_old = 0

Xl = float(input("Enter XL: "))
Xu = float(input("Enter Xu: "))
function_of_Xl = pow((pow(Xl, 2) + 1), 2) - 25
function_of_Xu = pow((pow(Xu, 2) + 1), 2) - 25
r3 = function_of_Xl * function_of_Xu

    
while (error > 0.001):
        xr = (Xl + Xu) / 2
        function_of_Xl = pow((pow(Xl, 2) + 1), 2) - 25
        function_of_xr = pow((pow(xr, 2) + 1), 2) - 25
        r3 = function_of_Xl * function_of_xr
        if r3 ==0:
            break
        elif r3 > 0:
            Xl = xr
        else:
            Xu = xr
        error = abs((xr - xr_old) / xr)*100
        xr_old = xr
print("The root is", xr)
print("The error is", error)
