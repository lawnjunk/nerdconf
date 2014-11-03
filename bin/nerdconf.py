#!/opt/local/bin/python3.3

import sys

args = sys.argv
num_args = len(sys.argv)
helpfile = open('nerdconf.help', 'r')



if num_args == 1 or num_args > 3:
	print(helpfile.read())	
if num_args == 2:
	if args[1] == '-u':    
		print("nerdconf update")
	if args[1] == '-l':
		print("nerdconf list")
	if args[1] in ["-h", "-help", "--help"]:
		print(helpfile.read())
	if args[1] not in ["-l", "-u", "-h", "-help", "--help"]:
		print("invalid imput\n")
		print(helpfile.read())
if num_args == 3:
	if args[1] == '-a':
		print("nerd conf add file")
	if args[1] == '-r':
		print("nerdconf rm file")
	if args[1] not in ['-a', '-r']:
		print(helpfile.read())



print()
print("printing arg list")
for arg in args:
	print(arg)


