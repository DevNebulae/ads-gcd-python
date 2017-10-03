#!/usr/bin/env python
import glob
import timeit
from functools import reduce
import operator
import mincemeat

def file_contents(filename):
    with open(filename, "rb") as f:
        return f.read()

def mapfn(key, value):
    from stopwords import allStopWords
    import re

    words = re.findall(r"[\w']+", value)
    for word in words:
        word = word.lower()

        if (word in allStopWords):
            continue
        elif len(word) == 1:
            continue
        else:
            yield word, 1

def reducefn(key, values):
    result = 0

    for value in values:
        result += value

    return result

start = timeit.default_timer()
files = glob.glob('large/*.*')
data = dict((file_contents(f).decode('latin1'), f) for f in files)

s = mincemeat.Server()

# The data source can be any dictionary-like object
s.datasource = dict(enumerate(data))
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
results = results[:10]

stop = timeit.default_timer()

print(stop - start)
with open('results.txt', 'w') as f:
    f.write(str(results))
