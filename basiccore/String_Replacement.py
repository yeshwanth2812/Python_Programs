# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title: String Replacement 
 
from string import Template 

# List Student stores the name and marks of three students 
Student = ['Yesh','akash'] 

# We are creating a basic structure to print the name and 
# marks of the students. 
t = Template('Hi $Student, How are you') 

for i in Student: 
	print (t.substitute(Student = i )) 