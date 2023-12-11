from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array
import pdb


li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = "Blah blah blah. Thinking about Python"
#print(Counter(li))
#print(Counter(sentence))

#dictionary = defaultdict(lambda: 5, {'a':1, 'b':2})
dictionary = defaultdict(lambda:'does not exist', {'a':1, 'b':2})
#print(dictionary['c'])


#d = OrderedDict()
#d['a'] = 1
#d['b'] = 2
#
#d2 = OrderedDict()
#d2['b'] = 2
#d2['a'] = 1

d = dict()
d['a'] = 1
d['b'] = 2

d2 = dict()
d2['b'] = 2
d2['a'] = 1

#print(d2 == d)


#print(datetime.date.today())


# array - they take less memory, because we have to specify memory usage value
arr = array('i', [1,2,3])
#print(arr[2])

def add( num1, num2 ):
    pdb.set_trace() # python debugger
    t = 4 * 5 
    return num1 + num2

print(add(4, 'sasha'))