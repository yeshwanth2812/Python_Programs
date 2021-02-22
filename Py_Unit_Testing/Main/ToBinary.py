# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: ToBinary

def binary(num): 
    if num > 1: 
        binary(num // 2)  #floor division 
    print(num % 2, end = '') #getting the reminder
    return num
  
if __name__ == '__main__': 
      
    decimal_number = int(input("Enter A Number:"))    
     
    binary(decimal_number) # Calling function
    print(" : Is The Binary Number")