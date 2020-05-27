"""
Description
: Creates master macro files (macros+hmmdefs for all monophones) from proto
"""

import sys, re, os

if __name__ == '__main__': 

	monophones = sys.argv[1]
	proto = './hmm0/proto'
	var_floor = './hmm0/vFloors'
	out_path = './hmm0/'

	# 1. List monophones
	f=open(monophones)
	lines=f.readlines()
	f.close()
	mp=[]
	for line in lines: mp.append(line.strip())
	# mp = mp[:-1] # remove the last one for lab question

	# 2. Create a copy of proto and name it hmmdefs
	f=open(proto)
	proto_lines=f.readlines()
	f.close()

	# 3. Create hmmdefs: a copy of proto hmm-definition for each monophone
	out_path_base='/'.join(out_path.rstrip('/').split('/')[:-1])+'/'
	out_path_suffix=out_path.rstrip('/').split('/')[-1]
	if not out_path_suffix in os.listdir(out_path_base): os.mkdir(out_path)
	f=open(out_path+'hmmdefs','w')
	for phone in mp:
		for line in proto_lines:
			line=re.sub('proto',phone,line)
			f.write(line)
	f.close()

	# 4. Create macro file: specification of observation vector and variance floor.
	f=open(var_floor)
	vfloor_lines=f.readlines()
	f.close()
	f=open(out_path+'macros','w')
	f.write('~o\n <VecSize> 39\n <MFCC_0_D_A>\n')
	for line in vfloor_lines: f.write(line)
	f.close()
