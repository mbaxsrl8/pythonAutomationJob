#! python3
# Finds phone numbers and email address on the clipboard

import pyperclip
import re

phoneRegex = re.compile(r'''
(\d{3}|\(\d{3}\))?                               # are code
(\s|-|\.)?                                       # separator
(\d{3})                                          # first 3 digits
(\s|-|\.)                                        # separator
(\d{4})                                          # last 4 digits
(\s*(ext|x|ext\.)\s*(\d{2,5}))?                 # extensions
''', re.VERBOSE)

# Creat Email regex
emailRegex = re.compile(r'''
[a-zA-Z0-9,_+-]+                              # user name
@                                             # @ symbol
[a-zA-Z0-9.-]+                                # domain name
\.[A-Za-z]{2,4}                               # dot-something
''', re.VERBOSE)

# Find matches in clipboard
text = str(pyperclip.paste())
matches = []
groups = phoneRegex.findall(text)
for group in groups:
    phoneNum = '-'.join([group[0], group[2], group[4]])
    if group[7] != '':
        phoneNum += ' X' + group[8]
    matches.append(phoneNum)

emails = emailRegex.findall(text)
for email in emails:
    matches.append(email)

# Copy result to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found')
