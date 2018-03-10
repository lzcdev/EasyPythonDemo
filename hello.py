#! usr/bin/python

# print 'hello world'
# print 'This\'s is the second sentence.\
# This is 2'
# i = 5
# print i
# i = i + 1
# print i
# s = '''This is a multi-line string.
# This is the second line.'''
# print s

# length = 5
# breadth = 2
# area = length * breadth
# print 'Area is', area
# print 'Perimeter is', 2 * (length + breadth)

# number = 23
# running = True

# while running:
# 	guess = int(raw_input('Enter an integer: '))

# if guess == number:
# 	print 'Congratulations, you guessed it.' # New block starts here
# 	print '(but you do not win any prizes!)' # New block ends here
# 	running = False
# elif guess < number:
# 	print 'No, it is a little higher than that' # Another block
# # You can do whatever you want in a block ...
# else:
# 	print 'No it is a little lower than that'
# # you must have guess > number to reach here

# print 'Done'
# # This last statement is always executed, after the if statement is executed
# 	

# for i in range(1, 5):
# 	print i
# else: print 'The for loop is over'

# while True:
# 	s = raw_input('Enter something:')
# 	if s == 'quit':
# 		print 'Length of the string is', len(s)
# 		print 'Done'
# 		break

# while True:
# 	s = raw_input('Enter something:')
# 	if s == 'quit':
# 		break
# 		if len(s) < 3:
# 			continue
# print 'Input is of sufficient length'

# def sayHello():
# 	print 'Hello world'

# sayHello()	

# def printMax(a, b):
# 	if a > b:
# 		print a, 'is maximum'
# 	else:
# 		print b, 'is maximum'
# printMax(3, 4)	

# def func(x):
# 	print 'x is', x
# 	x = 2
# 	print 'Changed local x to', x

# x = 50
# func(x)
# print 'x is still', x	

# def func():
# 	global x
# 	print 'x is', x
# 	x = 2
# 	print 'Changed locol x to', x

# x = 50
# func()
# print 'Value of x is', x

# def say(message, times = 1):
# 	print message * times
# say('Hello')
# say('world', 5)	

# print 'ab' * 3

# import sys

# print 'The command line arguments are:'
# for i in sys.argv:
# 	print i
# print '\n\nThe PYTHONPATH is', sys.path, '\n'

# if __name__ == '__main__':
# 	print 'This program is being run itself'
# else:
# 	print 'I am being imported from another module'	

import mymudule

mymudule.sayhi()
print 'Version', mymudule.version	
		
