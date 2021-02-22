# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-08 12:45:53
# @Title: to compute the power of 2
# Display the powers of 2 using anonymous function

terms = 4

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))   #map function!

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])