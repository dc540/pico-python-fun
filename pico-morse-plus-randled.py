import time
import random
from machine import Pin
led=Pin(25,Pin.OUT)
led1=Pin(1,Pin.OUT)
led2=Pin(2,Pin.OUT)
led3=Pin(3,Pin.OUT)
led4=Pin(14,Pin.OUT)
led5=Pin(15,Pin.OUT)
led6=Pin(28,Pin.OUT)
led7=Pin(27,Pin.OUT)
led8=Pin(26,Pin.OUT)
led9=Pin(22,Pin.OUT)
led10=Pin(21,Pin.OUT)

BRate=0.1

def rand_led(maxled):
    if maxled == 1:
        led1.toggle()
    if maxled == 2:
        led2.toggle()
    if maxled == 3:
        led3.toggle()
    if maxled == 4:
        led4.toggle()
    if maxled == 5:
        led5.toggle()
    if maxled == 6:
        led6.toggle()
    if maxled == 7:
        led7.toggle()
    if maxled == 8:
        led8.toggle()
    if maxled == 9:
        led9.toggle()
    if maxled == 10:
        led10.toggle()

def morse_dash():
    led.toggle()
    rand_led(random.randint(1,10))
    time.sleep(4*BRate)
    led.toggle()
    rand_led(random.randint(1,10))
    time.sleep(BRate)

def morse_dot():
    led.toggle()
    rand_led(random.randint(1,10))
    time.sleep(BRate)
    led.toggle()
    rand_led(random.randint(1,10))
    time.sleep(BRate)
    
def morse_pause():
    time.sleep(4*BRate)

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