import pyperclip, re

TEXT = pyperclip.paste()
data = []

findPhoneNum = re.compile(r'''(  #number finder based on US numbering system
    
    (\d{3}|\(\d{3}\))? #optional area code that can be three digits or three digits in parenthesis
    (\s|-|\.)? #can be a space, hyphen or a period, although this is optional
    (\d{3})
    (\s|-|\.)?
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
                      
                    )''' , re.DOTALL | re.VERBOSE)

phoneNum = findPhoneNum.findall(TEXT)

findEmailAddress = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #email username
    @ +
    [a-zA-Z0-9.-]+ #domain name
    (\.[a-zA-Z]{2,4}) #dot-something, must be between 2 and 4 characters                   
                              
                              )''' ,re.I | re.DOTALL | re.VERBOSE)

emailAddress = findEmailAddress.findall(TEXT)

for groups in findPhoneNum.findall(TEXT):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    data.append(phoneNum)
for groups in findEmailAddress.findall(TEXT):
    data.append(groups[0])

if len(data) > 0:
    pyperclip.copy('\n'.join(data))
    print('Copied to Clipboard')
    print('\n'.join(data))
else: 
    print('No phone numbers or emails found')
