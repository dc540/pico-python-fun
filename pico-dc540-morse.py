import time
from machine import Pin
led=Pin(25,Pin.OUT)
led1=Pin(1,Pin,OUT)

BRate=0.1

def morse_dash():
    led.toggle()
    led1.toggle()
print('dash')
    time.sleep(4*BRate)
    led.toggle()
    led1.toggle()
    time.sleep(BRate)

def morse_dot():
    led.toggle()
    led1.toggle()
    print('dot')
    time.sleep(BRate)
    led.toggle()
    led1.toggle()
    time.sleep(BRate)
    
def morse_pause():
    time.sleep(4*BRate)
    print('pause')

CODE = {' ': '_', 
"'": '.----.', 
'(': '-.--.-', 
')': '-.--.-', 
',': '--..--', 
'-': '-....-', 
'.': '.-.-.-', 
'/': '-..-.', 
'0': '-----', 
'1': '.----', 
'2': '..---', 
'3': '...--', 
'4': '....-', 
'5': '.....', 
'6': '-....', 
'7': '--...', 
'8': '---..', 
'9': '----.', 
':': '---...', 
';': '-.-.-.', 
'?': '..--..', 
'A': '.-', 
'B': '-...', 
'C': '-.-.', 
'D': '-..', 
'E': '.', 
'F': '..-.', 
'G': '--.', 
'H': '....', 
'I': '..', 
'J': '.---', 
'K': '-.-', 
'L': '.-..', 
'M': '--', 
'N': '-.', 
'O': '---', 
'P': '.--.', 
'Q': '--.-', 
'R': '.-.', 
'S': '...', 
'T': '-', 
'U': '..-', 
'V': '...-', 
'W': '.--', 
'X': '-..-', 
'Y': '-.--', 
'Z': '--..', 
'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        print('Char' , character , '\n')
        encodedSentence += CODE[character] + " " 
    return encodedSentence

while True:
    sentence = "DC540  "
    encodedSentence = convertToMorseCode(sentence)
    print(encodedSentence)
    for i in encodedSentence:
        if i == ".": 
            morse_dot()
        elif i == "-":
            morse_dash()
        else:
            morse_pause()