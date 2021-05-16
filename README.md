# pico-python-fun
@baabalicious 2021-05-15

Some random fun for Pico, for the 2021-05-17 DC540 meetup
---------------------------------------------------------

pico-dc540-morse.py -- blink DC540 in morse code using onboard LED
  save on pico with micropython firmware as main.py
  
pico-morse-plus-randled.py -- connect multicolor LEDs on a breadboard
  positive lead to the following pins: 1,2,3,14,15,28,27,26,22,21
  negative leads to common GND-connected bus
  save on pico with micropython firmware as main.py
  the onboard LED will blink "DC540" in morse code, and with every blink on or off a random colored LED will toggle.  
  lather. rinse. repeat.
  
pico-lcd-custom.py -- modified sample code using the Waveshare 1.14" color LCD hat with four onboard tactile button switches
   save on pico with micropython firmware as main.py
   fire it up, a DC540 meetup date shows. A different message appears in text line 4 (60,80) with the press of each button.
   the previous message is cleared before the new message is displayed, by the fill_rect command.
   
 hopefully this collection will grow over time.
