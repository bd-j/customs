# process the result of ``grep 'import ' */*py > imports.dat``
# to determine external package dependencies

import sys
from itertools import product

filename = 'bsfh_imports.dat'

imps = {}
for line in open(filename, 'r'):
    if '#' in line:
        continue
    f, i = line.split(':')
    if 'sedpy' in i:
        continue
    i = i.split(' as ')[0]
    words = i.split()
    if True in [w.startswith('.') for w in words]:
        continue
    words = i.split(',')
    if len(words) > 1:
        #root = words[0].split(
        words = ['.'.join(w) for w in product([words[0]], words[1:])]
    
    for w in words:
        w = w.replace('import','.').replace('from','.').replace(' ','').replace('\n', '')
        if w.startswith('.'):
            w = w[1:]
        if w in imps:
            imps[w].extend([f])
        else:
            imps[w] = [f]

#_ = [imps.pop(k) for k in kw]

modnames = []
for k in imps.keys():
    mod = k.split('.')[0]
    if mod not in modnames:
        modnames += [mod]
#        imps.pop(k)
