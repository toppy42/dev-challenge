# Exercises for chapter 3:

# Name: Ethan Puzarne


def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

repeat_lyrics()
# 3.1:  # "NameError: name 'repeat_lyrics' is not defined. "


# 3.2
# the program executes correctly because the call to print_lyrics 
# is not actually executed until the call to repeat_lyrics which post both definitions



# 3.3

def right_justify (s):
	align_column = 70
	given_length = len(s)
	space_require = align_column - given_length
	print " " * space_require + s

right_justify("Hello")
right_justify("t")
right_justify("This is a test sentence")




# 3.4-1
#def do_twice(f):
#	f()
#	f()

#def print_spam():
#	print 'spam'

#do_twice(print_spam)

# 3.4-2  
def do_twice(f, val):
	f(val)
	f(val)

# 3.4-3
def print_twice(s):
	print s
	print s

# 3.4-4
do_twice(print_twice, "spam")

# 3.4-5
def do_four(f, val):
	do_twice(f, val)
	do_twice(f, val)

do_four(print_twice, "spam")



