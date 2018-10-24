#!/usr/bin/python
import sys
from collections import Counter
import string
import os

MOST_COMMON = ['e', 't', 'a', 'o', 'i']
text = ''
intab = ''
outtab = ''
done = False


def get_input(l):
	return input('caesar > ' + ' ' * l + '\b' * l)


def decrypt(c='', p=''):
	global text, intab, outtab
	intab += c
	outtab += p
	return text.translate(str.maketrans(intab, outtab))


def analyze(text):
	freqs = dict(Counter(text))
	freqs = reversed(sorted([(j, i) for i, j in freqs.items()]))
	
	i = 0
	last_fr = -1
	for fr, l in freqs:
		if l.isalpha():
			try:
				if fr != last_fr and last_fr != -1:
					i += 1
				last_fr = fr
				print('{} -> {} ? {}'.format(l, MOST_COMMON[i], fr))
			except:
				print('{} - {}'.format(l, fr))
	input('Press any key to continue...')
	os.system('clear')


def clear(l):
	print('\r\b' * l + '\n')


def read_text(f):
	os.system('clear')
	return open(f, 'r').read()


def info():
	for l in string.ascii_uppercase:
		print(l, end='|')
		
	print()
		
	for l in string.ascii_uppercase:
		pos = intab.find(l)
			
		if pos != -1:
			print(outtab[pos], end='|')
			
		else:
			print(' ', end='|')
		
	print()


def delete(c):
	global intab, outtab
	if c.islower():
		pos = outtab.find(c)
	elif c.isupper():
		pos = intab.find(c)
	
	if pos == -1:
		return

	intab = list(intab)
	outtab = list(outtab)
	
	del intab[pos]
	del outtab[pos]
	
	intab = ''.join(intab)
	outtab = ''.join(outtab)


def help():
	print('Genereal usage: <uppercase_letter>, <lowercase_letter>')
	print('Example: A, d - substitute all A\'s to d\'s')
	print('del <letter> - delete the mapping for a certain letter')
	print('analyze - perform a frequency analysis on the text on single characters')
	print('undo - remove the last mapping you added')
	print('file <file_name> - read encrypted text from file')
	print('exit/quit - exit the program')
	input('Press any key to continue...')
	os.system('clear')	


print('Enter the text')
text = get_input(0)

if text.lower().startswith('file '):
	text = read_text(''.join(text.split(' ')[1:]))

#while True:
#	print(text)
#	clear()
#	print(decrypt('C', 'h'))
#	input()	

old_len = 0

while not done:
	clear(len(text))
	print(decrypt('', ''))
	info()
	try:
		user = get_input(old_len)
		old_len = len(user)
	except KeyboardInterrupt: 
		print('\nBye, Bye :)')
		exit()

	if user.lower().startswith('file '):
		try:
			text = read_text(''.join(user.split()[1:]))
		except:
			print('Couldn\'t open file!')
			exit()

	elif user.lower() == 'help':
		help()		

	elif user.lower() == 'analyze':
		analyze(text)

	elif user.lower() == 'quit' or user.lower() == 'exit':
		done = True

	elif ',' in user:
		try:
			c, p = user.split(',')
			c = c.strip(' ')
			p = p.strip(' ')
			decrypt(c, p)
		except Exception as e:
			print('Some error occured: {}'.format(e))
	
	elif user.lower().startswith('del'):
		try:
			delete(user.split()[1])
		except Exception as e:
			print('Some error occured: {}'.format(e))

	elif user.lower() == 'undo':
		intab = intab[:-1]
		outtab = outtab[:-1]
	
