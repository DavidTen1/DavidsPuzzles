def isDisarium(num):
    if(type(num) == int):
     disariumResult = 0
     i = 0
     numString = str(num)
     for digit in numString:
        i = i + 1
        disariumResult = disariumResult +  int(digit)**(i)

     return [disariumResult,num == disariumResult ]   
         

print('disarium', isDisarium(518))

#A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
