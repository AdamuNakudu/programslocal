#! python3
# A multi-clipboard program

import pyperclip, sys


TEXT = {'agree': """Yes, I agree. That sounds fine to me""",
        'busy': """Sorry, can we do this later""",
        'upsell': """Would you consider making a donation?"""}

#verify if user typed in correct number of args, if not, error message printed and exit
if len(sys.argv) < 2:
    print('Usage: python3 mclip.py [keyphrase]')
    sys.exit()
    
#search for keyphrase in text, if found, copy value of the key to clipboard, if not, print error
if sys.argv[1] in TEXT:
    pyperclip.copy(TEXT[sys.argv[1]])
    print('Text for ' + sys.argv[1] + ' copied to clipboard.')
else:
    print('There is no text for' + sys.argv[1]) 
