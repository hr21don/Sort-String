
#sorting in python
from itertools import accumulate
location = 'unitedkingdom'
 #print(tuple(accumulate(sorted(location)))[-1])

my_list = ['Science', 'constitute', 'Business', 'flux', 'Jim', 'Zloppy']
my_list.sort()
#print(my_list)

#sorted function 
def sort_string(input):
    string = input.split()
    string = [s.lower() + s for s in string]
    string.sort()
    string = [s[len(s)//2:] for s in string]
    return ''.join(words)
