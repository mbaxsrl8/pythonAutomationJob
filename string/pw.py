#! python3
# ! pw.py - An insecure password locker program
import sys
import pyperclip

PASSWORDS = {
    'email': 'Xmgcsysm@2014',
    'payment': '086204',
    'newPW': 'L1Rui1995'
}

if len(sys.argv) < 2:
    print('Usage: py py.pw [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
