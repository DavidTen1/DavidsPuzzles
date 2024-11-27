import sys
#calcs the n-th power of every integer and saves it in the array if the result is in the range [a,b]

def power_ranger(n,a,b):
 if (type(a) != int  or type(b) != int or a >= b):
     sys.exit()
 numbersInRange = []
 for i in range(b+1):
  currentPoweredNum = i**n
  print( "i" ,i," i^n " , currentPoweredNum)
  if(currentPoweredNum >= a and currentPoweredNum <= b):
      numbersInRange.append(currentPoweredNum)

 return numbersInRange



print('final arr ' , power_ranger(2,49,65))
    
