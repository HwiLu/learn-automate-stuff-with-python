import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') 

mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo)

print(mo.group())