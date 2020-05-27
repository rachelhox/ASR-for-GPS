"""List phones used in the pronunciation dictionary.

$ python list_phones.py [pron-dict] > monophones
"""

import sys

if __name__ == '__main__':
	f = open(sys.argv[1])
	lines = f.readlines()
	f.close()
	phl = []
	for line in lines:
		ll = line.strip('\n').split('\t')
		if len(ll) == 3:
			pl = ll[2].split()
			for p in pl:
				if not p in phl: phl.append(p)
	print '\n'.join(phl)



