def isPerfectNum(num):
   if(type(num) == int): 
    currentSum = 0
    for i in range(num)[1:]:
     if num % i == 0:
         currentSum = currentSum + i

    return num == currentSum

print('yup', isPerfectNum(27))


def perfectNumsTo1000():
    perfectNumsArr = []
    for i in range(1000+1):
        if (isPerfectNum(i)):
            perfectNumsArr.append(i)

    return perfectNumsArr;
        
        
    
print('arr', perfectNumsTo1000())
