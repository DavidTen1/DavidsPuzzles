def canNumsdivideValue(value,numsArray):
    hasArrayNumsOnly = len(set(type(x) for x in numsArray)) == 1 and len(numsArray) > 0 and type(numsArray[0] == int) # check if the array is non-empty & has integers only
    if(type(numsArray) == list and type(value) == int and hasArrayNumsOnly): #is the target value an int and did you indeed use an array
     for targetValue in numsArray: # find out if all the array's numbers can divide the target number, if so, return true, else, false
      if(value % targetValue != 0):
          return False
     return True  



def leastCommonMultiple(array):
    if(type(array) == list and len(array) > 0 ):# is it a non-empty array
     print('array ', array)
     i = 0    # i is an iteration number which is also a target
     while(i >= 0): # while 
        i = i +1 #increment target number
        if canNumsdivideValue(i,array): # if number is found that can be divided by all the array's numbers, print it
            print('LCM found: ', i)
            break
       
        
        
leastCommonMultiple([1, 2, 3, 4, 5, 6, 7, 8, 9])
