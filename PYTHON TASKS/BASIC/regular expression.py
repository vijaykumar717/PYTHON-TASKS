'''import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

import re

txt = "That will be 59 dol1lars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

import re

txt = "hellygo planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..y", txt)
print(x)

import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*p", txt)

print(x)


import re
 
# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
 
# \d+ will match a group on [0-9], group
# of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))




import re
 
# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))
 
# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))
 
# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))



from re import split
 
# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))
 
# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
 
# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))




import re
 
# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
 
# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))


Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already',
             flags=re.IGNORECASE))
 
# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already'))
 
# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already',
             count=1, flags=re.IGNORECASE))'''
 
# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
##print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
##             flags=re.IGNORECASE)



'''import re
x="vijay ajay"
print(re.findall("[a-z]",x))     #"/d" digits
fruits=["apple","orange","banana"]    '''






      
import re

name='arun was born in sivakasi #16-06-1996 @now arun age is 26!'

##searching_begin=re.search('\Aa',name) # Finding the word and character at the begin of the given string
##print('1',searching_begin)

      
##searching_any_where=(re.findall(r'\barun', name)) #Finding the word any where from the given string
##print('2',searching_any_where)


##searching_digit=(re.findall('\d', name)) # Finding the digit from the given string
##print('3',searching_digit)


##searching_non_digit=''.join(re.findall('\D', name)) #Finding the Non Digit From the given string 
##print('4',searching_non_digit)


##searching_white_space=(re.findall('\s', name)) # Finding the white space from the given string
##print('5',searching_white_space)


##searching_non_white_space=(re.findall('\S', name)) # Finding the non white space from the given string
##print('6',searching_non_white_space)


##searching_end=re.search('!\Z', name) # Finding the words  and character at the end of the given string
##print('7',searching_end)


##searching_non_special_char =(re.findall('\w, name)) #Finding the Non special character from the given string
##print('8',searching_non_special_char)


##searching_special_char=(re.findall('\W', name)) # Finding the Special character and space from the string
##print('9',searching_special_char)




#notes







# REG expression

# Special Sequence:--> A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

'''
import re

name='arun was born in sivakasi #16-06-1996 @now  arun age is 26'

searching_begin=re.search('\AArunachalam',name) # Finding the word at the begin of the given string \A

searching_any_where=(re.findall(r'\barun',name)) # Finding the word any where from the given string \b (definetly use r)

searching_digit=(re.findall('\d',name)) # Finding the digit from the given string \d

searching_non_digit=''.join(re.findall('\D',name)) # Finding the Non Digit From the given string \D

searching_white_space=re.findall('\s',name) # Finding the white space from the given string \s

searching_non_white_space=re.findall('\S',name) # Finding the non white space from the given string \S

searching_end=re.search('sivakasi\Z',name) # Finding the words at the end of the given string \Z

searching_non_special_char=re.findall('\w',name) # Finding the Non special character from the given string \w

searching_special_char=re.findall('\W',name) # Finding the Special character and space from the given string \W

'''

# Sets

# A set is a set of characters inside a pair of square brackets [] with a special meaning


'''import re

name='arunachalam was born in sivakasi 16 06 1996 at age of 26'

searching_set_character=re.findall('[a]',name) # searching set of character from the given string [abc]
print(searching_set_character)
searching_set_characters=re.findall('[a-z A-z]',name) # searching for range of character from the given string [a-z]
# if mention space in your pattern that space also return in your list
print(searching_set_characters)

removing_set_character=re.findall('[^a]',name) # removing set of charcter from the given string [^a]
print(removing_set_character)
searching_digit=''.join(re.findall('[0-9 ]',name)) # Finding the range digits from the given string [0-z] (note:- space is very important)
print(searching_digit)
number='my mobile number is 9787411068'

searching_number=re.findall('[012345]',number) # Finding set of digits from the given string
print(searching_number)'''


# Metacharacters are characters with a special meaning

import re

name='arunachalam was born in sivakasi at 16-06-1996'

sets_of_character=''.join(re.findall('[0-9-]',name))      #words and digits
print(sets_of_character)

special_digit=re.findall('\d',name)

any_character=re.search('si.....i',name)

start_with=re.search('^arun',name)

end_with=re.search('1996$',name)



