# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: Vending machine

def currency_count(change): 
      
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1] 
                 
    note_count = [0, 0, 0, 0, 0, 0, 0, 0,0] 
      
    print ("Change : Note Count ") 

    result = ""
    for number1, number2 in zip(notes, note_count):
        if change >= number1: 
            number2 = change // number1  #floor division
            change = change - number2 * number1
            print (number1 ," : ", number2) 
            result += (str(number1) +" : "+ str(number2) + ",") #converting integer to string take as list
    return result

if __name__ == '__main__':
    change = int(input("Enter The Money: "))
    currency_count(change)