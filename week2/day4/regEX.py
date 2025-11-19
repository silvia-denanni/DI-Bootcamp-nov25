import re

# metacharacters used in RegEx, along with their functionality:

#SPECIAL SEQUENCES "\"
#followed by any one of the following characters, based on their particular functionality.

#RE FUNCTIONS:
#)1----------------------------------------- re.findall()

#returns a list of strings containing all matches of the specified pattern
#The function takes as input the following:

'''a CHARACTER pattern
the STRING from which to search'''

string = "at what time?"
match = re.findall('at',string)    #we are looking for all instances of "at" inside the string
print (match)       #['at', 'at']

#2)----------------------------------------re.search()

#returns a match object in case a match is found

''' In case of more than one match, the first occurrence is returned. * If no occurrence is found, None.'''

import re

string = "at what time?"
match = re.search('at',string)       #we are looking for instances of "at" inside the string
if (match):
    print("String found at: " ,match.start())           #match.start = returns the starting index point (0 in this case)
else:
    print("String not found!")          #>>> String found at:  0


#3)----------------------------------------re.split()
# splits the string at every occurrence of the sub-string and RETURNS a LIST OF STRINGS which have been SPLIT

import re

string = "at what time?"
match = re.split('a',string)    #we wish to split a string wherever there is an occurrence of "a"

print (match)  #>>> ['', 't wh', 't time?']

'''if there is NO occurrence, we get the string but in LIST format'''


#3)----------------------------------------re.sub()
# to replace occurrences of a particular sub-string with another sub-string

import re

string = "at what time?"
match = re.sub("\s","!!!",string)    #we are REPLACING " " btw words with "!!!"
print (match)                    #>>> at!!!what!!!time?
