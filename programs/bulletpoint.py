import pyperclip

text = pyperclip.paste()
pyperclip.cop
#seperate lines and add bullet points 
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)

print(text)