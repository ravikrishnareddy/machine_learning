import numpy as np

var_dict = {2012:{11:'AA',12:'BB',13:'CC'}}

dict_2011 = {1:'A',2:'B',3:'C'}

print(var_dict)
var_dict.get(2012)

var_dict[2011] = dict_2011
print(var_dict)

var_dict.update({2012:dict([(1, 'A'), (2, 'B')])})
print(var_dict)

fruits = ['apple', 'banana', 'grapes', 'apple', 'watermelon', 'grapes', 'apple', 'mango', 'apple', 'banana', 'cherry', 'mango']
var_dict = {}
for i in set(fruits):
    if fruits.count(i) in var_dict.keys():
        var_dict[fruits.count(i)].append(i)
    else:
        var_dict[fruits.count(i)] = [i]
print(var_dict[sorted(var_dict, reverse = True)[0]])

from collections import Counter, most_common
print(Counter(fruits))
print(Counter(fruits).most_common(1)[0][0])

from collections import defaultdict
var_dict = defaultdict(list)
for i in set(fruits):
    var_dict[fruits.count(i)].append(i)
print(dict(var_dict))
