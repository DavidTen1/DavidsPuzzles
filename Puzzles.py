
#for  i in range(100+1):
#    currentValue =  "Fizz" if (i%3 == 0 and i%5 != 0 ) else  ("Buzz" if ( i%3 != 0and i%5 == 0) else ("FizzBuzz" if(i%3 == 0 and i%5 == 0) else i) )
#    print(currentValue)

'''
inp = input()

inputParts= str(inp).split(' ')

longestWord = ''

print(inputParts)

for word in  inputParts:
    longestWord = word if len(word) > len(longestWord)  else longestWord
print('lw', longestWord)    



#move capital letters to the fronts

inp = input()

newInput = ""

inpArray = list(inp)
print('new input', inpArray)

tmp = None

for i in range(len(inpArray)):
    print('i',inp[i])
    for j in range(len(inpArray)):
     print('j',inp[j])
     if inpArray[i].islower() and inpArray[j].isupper() :
         tmp = inpArray[i]
         inpArray[i]= inpArray[j]
         inpArray[j] = tmp
         break


newInput = ''.join(inpArray)
print('new input', newInput)

def multiply(x,y):
    result = 0
    while(y > 0):
        result = result + x
        y = y - 1
    return result    


print(multiply(2,3))



def digit_sum(number):
    digitSum = 0
    if(type(number) == int):
     strNum = str(number)
     for char in strNum:
         digitSum = digitSum + int(char)

     return digitSum    
        


print(digit_sum(625))
'''
