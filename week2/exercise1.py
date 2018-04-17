"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']
#l think it find words in the six words above 
for word in some_words:
    print(word) #and print the word

for x in some_words:#also find words above
    print(x)#print the words out

print(some_words)#print the ['what', 'does', 'this', 'line', 'do', '?']

if len(some_words) > 3:#check the woeds > 3
    print('some_words contains more than 3 words')#if words >3 print 'some_words contains more than 3 words' out

def usefulFunction(): #define usefulfunction 
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())#print platform.uname

usefulFunction()
