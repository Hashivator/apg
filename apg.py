#!/usr/bin/python3
from argparse import ArgumentParser
from random import choice

low = 'abcdefghijklmnopqrstuvwxyz'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
di = '0123456789'
pu = '!@#$%^&*()_+-=[]\{\}|;\':",./<>?\\'
all = low + up + di + pu



parser = ArgumentParser()
parser.add_argument('-l', '--length', type=int, default=8, help='length of password')
parser.add_argument('-o', '--output', type=str, default='', help='output file')
parser.add_argument('-n', '--number', type=int, default=1, help='number of passwords')
parser.add_argument('-C', '--capital', action='store_true', help='capital letters')
parser.add_argument('-L', '--lowercase', action='store_true', help='lowercase letters')
parser.add_argument('-d', '--digits', action='store_true', help='digits only')
parser.add_argument('-p', '--punctuation', action='store_true', help='punctuation only')
parser.add_argument('--nop', action='store_true', help='no punctuation')
parser.add_argument('--nod', action='store_true', help='no digits')
parser.add_argument('--nol', action='store_true', help='no letters')
parser.add_argument('-c', '--color', action='store_true', help='colorize output')
parser.add_argument('-s', '--style', action='store_true', help='style of output')
parser.add_argument('-N', '--newline', action='store_true', help='newline at the end')
parser.add_argument('-a', '--add', type=str, default='', help='additional characters')
# your string of characters
parser.add_argument('-y', '--your', type=str, default='', help='your string of characters')
# remove characters you don't want
parser.add_argument('-r', '--remove', type=str, default='', help='remove characters')
parser.add_argument('-v', '--version', action='version', version='APG v1.1')


args = parser.parse_args()



class Color:
    DARKGREY2 = '\033[1;90m'
    RED2 = '\033[31m'
    BOLD2 = '\033[1m'
    END2 = '\033[0m'
    UNDERLINE2 = '\033[4m'
        
    if args.color:
        DARKGREY = '\033[90m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        END = '\033[0m'
        BOLD = '\033[1m'
    else:
        RED = ''
        GREEN = ''
        YELLOW = ''
        BLUE = ''
        MAGENTA = ''
        CYAN = ''
        WHITE = ''
        END = ''
        DARKGREY = ''
        BOLD = ''

        

class Style:
    if args.style:
        forflash = '-->'
        backflash = '<--'
        forflashs = '--> '
        backflashs = ' <--'
        forflashss = '-->  '
        backflashss = '  <--'
    else:
        forflash = ''
        backflash = ''
        forflashs = ''
        backflashs = ''
        forflashss = ''
        backflashss = ''
        corner = ''
    

if args.newline:
    nl = '\n'
else:
    nl = ''

# give error if both are true
if args.capital == True and args.lowercase == True:
    exit(Color.RED2 + Color.BOLD2 + 'Error: ' + Color.END2 + Color.DARKGREY2 + 'You cannot have both capital and lowercase letters' + Color.END2)
elif args.punctuation == True and args.nop == True:
    exit(Color.RED2 + Color.BOLD2 + 'Error: ' + Color.END2 + Color.DARKGREY2 + 'You cannot have both punctuation and no punctuation' + Color.END2)
elif args.digits == True and args.nod == True:
    exit(Color.RED2 + Color.BOLD2 + 'Error: ' + Color.END2 + Color.DARKGREY2 + 'You cannot have both digits and no digits' + Color.END2)
elif args.lowercase == True and args.nol == True:
    exit(Color.RED2 + Color.BOLD2 + 'Error: ' + Color.END2 + Color.DARKGREY2 + 'You cannot have both lowercase and no lowercase' + Color.END2)
elif args.capital == True and args.nol == True:
    exit(Color.RED2 + Color.BOLD2 + 'Error: ' + Color.END2 + Color.DARKGREY2 + 'You cannot have both capital and no capital' + Color.END2)
elif args.nop == True and args.nod == True and args.nol == True:
    exit(Color.RED2 + Color.BOLD2 + 'Error: ' + Color.END2 + Color.DARKGREY2 + 'You cannot have all of no ' + Color.UNDERLINE2 + 'punctuations'+ Color.END2 + Color.DARKGREY2 +', ' + Color.UNDERLINE2 + 'no digits'+ Color.END2 + Color.DARKGREY2 + ', and no ' + Color.UNDERLINE2 + 'letters' + Color.END + Color.END2)


if args.your == '':
    if args.nop == True:
        all = all.replace(pu, '')
    if args.nod == True:
        all = all.replace(di, '')
    if args.nol == True:
        all = all.replace(low + up, '')


    # remove characters you don't want
    if args.remove != '':
        for i in args.remove:
            all = all.replace(i, '')


    if args.capital:
        all = all.replace(low, '')
    if args.lowercase:
        all = all.replace(up, '')
    if args.digits:
        all = all.replace(low+up+pu, '')
    if args.punctuation:
        all = all.replace(low+up+di, '')
else:
    # remove duplicates
    args.your = args.your.replace(' ', '')
    args.your = ''.join(set(args.your))
    all = args.your


if all == '':
    exit(Color.RED2 + Color.BOLD2 + 'Error: ' + Color.END2 + Color.DARKGREY2 + 'No characters to use' + Color.END2)

for i in range(args.number):
    
    # generate password
    passwd = ''.join(choice(all) for i in range(args.length))
    
    # terminal output
    print(Color.CYAN + Style.forflashss + Color.END + Color.YELLOW + passwd + Color.END + Color.CYAN + Style.backflashss + Color.END + nl)


    # file output
    if args.output:
        with open(args.output, 'a') as f:
            f.write(passwd + '\n')
    elif args.output == '':
        pass
