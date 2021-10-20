#sorting in python
from itertools import accumulate
location = 'unitedkingdom'
 #print(tuple(accumulate(sorted(location)))[-1])

my_list = ['Science', 'constitute', 'Business', 'flux', 'Jim', 'Zloppy']
my_list.sort()
#print(my_list)

#sorted function 
def sort_string(phrase):
    splitted_phrase = phrase.split(" ")
    sort_phrase = sorted(splitted_phrase, key=lambda v:v.upper())
    return sort_phrase



if __name__=="__main__":
    print(sort_string("banana ORANGE apple"))
