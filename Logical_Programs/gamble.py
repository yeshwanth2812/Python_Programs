#header
#author name : Yeshwanth
#date : 9/2/2021

print ("")
import time
cash = 5000
print("you brought",'$',cash,'today')
while cash>0:
    from random import randint
    die = randint(1,1)
    while True:
        try:
    print
        choice1 = int(raw_input('First guess: '))
        print
        choice2 = int(raw_input('Second guess: '))
        print
        break
            except ValueError:
        print 'Please, enter a number.'
        print 'rolling die..'
        time.sleep(3)
        if choice1+choice2==die:
            #PROBLEM: The operation below does not change the value of cash, why not?. 
                cash=cash+1000
                print cash
                print 'you rolled',die
                print 'win! you won $1000, you\'re new balance is:',cash
                #PROBLEM: The new val of cash should be printed here ^ but it remains as 5000
        else:
            cash-1000
            print 'you rolled',die
            print 'lose! you lost $1000, you\'re new balance is:',cash
        if cash<0:
            print 'Bankrupt.'
            time.sleep(3)
            quit()
        if cash==1000000:
            print 'Millionaire!'
            break