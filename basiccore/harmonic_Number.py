# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 13:00:53
# @Title: Python program to find the sum of harmonic series 
  
def sum(n): 
    i = 1
    s = 0.0
    for i in range(1, n+1): 
        s = s + 1/i; 
    return s; 
  
# Driver Code  
n = 5
print("Sum is", round(sum(n), 6)) 
