# bagels calculator
people=input('Enter the number of people attending the event: ')
if people.isnumeric() : # if people is a number (integer) then proceed with calculation
    people=int(people)
    bagels = input('Enter the number of bagels for each person: ')
    if bagels.isnumeric(): # if bagels is a number (integer) then proceed with calculation
        bagels=int(bagels)
        # boxes calculation
        remainder=(people*bagels)%12
        if remainder==0:
          boxes=(people*bagels)//12
          bagels_left = 0
        else:
          boxes=(people*bagels)//12+1
          bagels_left = boxes * 12 - (people * bagels)
        # cost calculation
        if boxes >= 1 and boxes <= 5:
         cost=boxes*15
        else:
             if boxes >= 6 and boxes <= 20 :
               cost = boxes*12.5
             else :
               cost = boxes*9
        # display the results
        print('Minimum boxes of bagels needed: ', boxes)
        print('Bagels left over: ',bagels_left)
        print('Bagels cost: ',format(cost,'.2f'))
    else:
        print(bagels,' is not a valid number')
else:
    print(people,' is not a valid number')