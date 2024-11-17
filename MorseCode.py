#Translating words into morse

morseCodeDict = {
    'a': '*-',    'b': '-***', 'c': '-*-*', 'd': '-**',  'e': '*',    
    'f': '**-*',  'g': '--*',  'h': '****', 'i': '**',   'j': '*---',
    'k': '-*-',   'l': '*-**', 'm': '--',   'n': '-*',   'o': '---',
    'p': '*--*',  'q': '--*-', 'r': '*-*',  's': '***',  't': '-',
    'u': '**-',   'v': '***-', 'w': '*--',  'x': '-**-', 'y': '-*--',
    'z': '--**'
}


def morseOrText(text):
    morseText = ''
    if(type(text) == str):
     for char in text:
        newChar = char if  char not in list(morseCodeDict) else morseCodeDict[char]
        morseText = morseText + newChar + ' '

     return morseText

morseText = input()
print(morseOrText(morseText))    
