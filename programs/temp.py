import re 

TEXT = input()

phoneNum = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNum.search(TEXT)
print('Phone number found: ' + mo.group())
print(mo.groups())