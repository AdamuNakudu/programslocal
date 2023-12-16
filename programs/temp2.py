import re

beginswithHello = re.compile(r'AGENT (\w)\w*', re.I)
print(beginswithHello.sub(r'\1**','Agent Nakudu gave the documents to Agent ross for examination'))