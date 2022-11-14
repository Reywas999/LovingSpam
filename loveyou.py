import pyautogui as pt
import time 
import sys

#Set the number of time you want to run the spam
#ex an input of 2 would cycle through the list twice.
repetitions = input("Enter the number of repetitions: ")

#This section creates a timer that counts back from 10. This entire chunk is unnecessary, in its place you can simply write: time.sleep(10)
#This allows you time to move your mouse from the command prompt to the whatsapp "send message" box.
print("Hurry up and click the message bar!")
for remaining in range(10, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

#This is what every message will start with, alter as you see fit.
a = "I love you more than"

#This is what your message will cycle through and end with. Alter as you see fit.
#You can also read in an outside list from a CSV, XLXS, or TXT file with a list of phrases as well. This can be done like so:
#txt = open('Positive-Adjective-List.txt', 'r'). Just make sure the list is in your working directory
txt = [
'apple pie',
'the whole wide world',
'Jesus',
'your own mother',
'eggs and waffles',
'I love my rocks',
'you will ever know',
'I can say',
'yesterday',
'a California Sunset'
]

#b tells our loop that there have been 0 iterations
b = 0 

#This tiny block of code is what works all the magic
while b < int(repetitions): #while b is less than our input number of repetitions, this code will continue to run [int converts the string input to integer]
    for i in txt: #the following section of code will execute for each item (i) in our list of ending phrases (txt).
        pt.write(a + ' ' + i) #It will write out a ("I love you more than") + a blank space (' ') + i (i is equal to each one of the strings in our txt list)
        pt.press('Enter') #After writing out the phrase, 'enter' will be pressed, so you need to make sure you've clicked the send message box!
        time.sleep(3) #This is the lag time between messages. Eliminate this line to instantly send them all
    b += 1 #After running through your entire list, 1 will get added to b, this will continue until b = the number of repetitions you input!