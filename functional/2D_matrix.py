# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 13:00:53
# @Title: program to demonstrate working of method 1 and method 2. 
  
rows, cols = (5, 5) 
  
# method 2a 
arr = [[0]*cols]*rows 
  
# lets change the first element of the  
# first row to 1 and print the array 
arr[0][0] = 1
  
for row in arr: 
    print(row) 
# outputs the following 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
  
# method 2
arr = [[0 for i in range(cols)] for j in range(rows)] 
  
# again in this new array lets change 
# the first element of the first row  
# to 1 and print the array 
arr[0][0] = 1
for row in arr: 
    print(row) 
  
# outputs the following as expected 
#[1, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
