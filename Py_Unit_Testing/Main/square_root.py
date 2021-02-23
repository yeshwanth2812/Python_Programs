# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: Square_root

def square_root(number):
    
    root=number 
    epsilon = 1e-15
    while abs(root - number/root) > epsilon*root: #finding square root of a number 
        root = round((number/root + root)/2,2)
        print(root)
    return root

if __name__ == "__main__":
    number = int(input("Enter A number You Want The Square Root Of: "))
    root=number 
    square_root(number)