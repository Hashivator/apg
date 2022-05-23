from os import system
from random import choice
try:
	from argparse import ArgumentParser
except:
	system("python -m pip install argparse")
from argparse import ArgumentParser

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


args = parser.parse_args()



class Color: 
    if args.color:
        GRAY = '\033[1;30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
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
        GRAY = ''

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
    print(Color.RED + Color.BOLD + 'Error: ' + Color.END + Color.GRAY + 'You cannot have both capital and lowercase letters' + Color.END)
    exit()
elif args.punctuation == True and args.nop == True:
    print(Color.RED + Color.BOLD + 'Error: ' + Color.END + Color.GRAY + 'You cannot have both punctuation and no punctuation' + Color.END)
    exit()
elif args.digits == True and args.nod == True:
    print(Color.RED + Color.BOLD + 'Error: ' + Color.END + Color.GRAY + 'You cannot have both digits and no digits' + Color.END)
    exit()
elif args.lowercase == True and args.nol == True:
    print(Color.RED + Color.BOLD + 'Error: ' + Color.END + Color.GRAY + 'You cannot have both lowercase and no lowercase' + Color.END)
    exit()
elif args.capital == True and args.nol == True:
    print(Color.RED + Color.BOLD + 'Error: ' + Color.END + Color.GRAY + 'You cannot have both capital and no capital' + Color.END)
    exit()



# if no punctuation is selected, remove punctuation from all
if args.nop == True:
    all = all.replace(pu, '')
elif args.nod == True:
    all = all.replace(di, '')
elif args.nol == True:
    all = all.replace(low + up, '')



for i in range(args.number):
    
    if args.capital:
        passwd = choice(all) + ''.join(choice(all) for i in range(args.length))
        passwd = passwd.upper()
    
    elif args.digits:
        passwd = ''.join(choice(di) for i in range(args.length))
    
    elif args.punctuation:
        passwd = ''.join(choice(pu) for i in range(args.length))
    
    elif args.lowercase:
        passwd = choice(all) + ''.join(choice(all) for i in range(args.length))
        passwd = passwd.lower()
    
    elif args.capital == False and args.digits == False:
        passwd = ''.join(choice(all) for i in range(args.length))
    
    
    # terminal output
    print(Color.CYAN + Style.forflashss + Color.END + Color.YELLOW + passwd + Color.END + Color.CYAN + Style.backflashss + Color.END + nl)

    if args.output:
        with open(args.output, 'a') as f:
            f.write(passwd + '\\n')
    elif args.output == '':
        pass
