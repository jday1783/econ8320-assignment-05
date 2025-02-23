#Class Notes

#Becoming more flexible
#The first thing we want to do is import a library
# There's a reserve word called import, it's how we bring code from another script
import re
## re is a toolbox, we can pull out different functions
# #When we  want to use something from re, we use re.whatever
#we need to create a string to search through
mystring = "I think I'll get a 50"
## Let's find stuff in our string, search takes 2 arguments
# the first argument is a pattern and the second is the string with what we want to search
re.search(r"", mystring)
## r"" is called a raw string, allows us to express a new line character or a tab
# What goes in the raw string? -Whatever pattern we want to match
re.search(r"50", mystring)
## if you find no result, you'll get back none, if you find something it will be a match object
# we can use the bool function to return true or false
bool(re.search(r"50", mystring))
# if we want to find any number, let's put [] in the "", called a character class
re.search(r"[012345]", mystring)
## Using the [], we are expressing any number in [012345] is a valid match
re.search(r"[012345][012345]", mystring)
mystring = "I think I'll get  a 45"
re.search(r"[012345][012345]", mystring)
#nice
# REPEATING CHARACTERS
#let's make a repeating characters class
re.search(r"\d[012345]", mystring)
# \d represents a digit, it represents all digits or [0-9]
# WE want to express the fact that it may repeat using a * or +
# * means we have a digit class repeated 0 or more times  
re.search(r"\d*", mystring)
# this returns a blank string at position 0, not what we want
re.search(r"\d+", mystring)
# the plus operator is shorthand for 1 or more characters, works for everything 0 and up
#REPEATING Characters - more on the slides
# We can use {x,y} to repeat no less than x times and nore more than y times
re.search(r"\d{1,3}", mystring)
# if we wnat a pattern that's only 3 characters long
# We can use the or operator to include anything up to 100, [1-9] doesn't include 0, [0-9] includes all numbers
re.search(r'(100|[1-9][0-9][0-9])', mystring)
#This is still wrong, we need boundaries
#BOUNDARIES
# 3 ways of expressing boundaries
mystring = "I think I'll get a 101"
re.search(r"\b(100|[1-9][\d][\d])\b", mystring)
# search will only find the first match, if you want to find every instance you'll need more 
#If we want to find decimlas, use below
re.search(r"\b(100|[1-9]\d|\d)([.]\d+)?\b", mystring)
# this will still catch 100.5 and still catch decimalas after 100
#Example: let's find US valid phone numbers, 1,3 4 and no 2,5,6 
# every phone number should have 7 digits
mystring = "1-402-889-9609"
#everything in our pattern should go between
re.search(r"^\d{3}-\d{4}$", mystring)
#how do we add an area code?
re.search(r"^(\d{3}-)?\d{}3-\d{4}$", mystring)
#How do we include the country number?
re.search(r"^(1-)?(\d{3}-)?\d{}3-\d{4}$", mystring)
# we need to have a country code only when there's an area code
re.search(r"^(1-)?\d{3}-)?\d{}3-\d{4}$", mystring)
# WORD Boundaries
# Check out additional shorthand in slides
#City state Combination Example - Slides
myaddress = "6708 Pine Street, Omaha, NE 68182"
## brackets [A-Z], we get the state, {2} means two letters
re.search(r"[A-Z]{2}", mystring)
#let's find comma space before NE
re.search(r", [A-Z]{2}", mystring)
# let's find the city name
re.search(r"\w+, [A-Z]{2}", mystring)
#we know we need w+ followed by a comma followed by a space
#we need to denote there might be more words, we need any number of words* followed by a space
re.search(r"(\w+ )*\w+, [A-Z]{2}", mystring)
#Let's add extra parathenses to create non-capturing groups using ?:
re.search(r"((?:)w+ )*\w+)(?:, )([A-Z]{2}", mystring).groups()

# we did not cover positve or negative lookbehinds in class
# Alternative Functionality
