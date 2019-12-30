import sys,os
from datetime import datetime
import time
start = time.time()



nvpk = '~/nvpksrc/nv'

inputFile = '-i ~/mk64-tests/epic.bin'
outputFile = '-o ~/mk64-tests/epic.vpk0'

# iF = outputFile[3:]
# cF = '~/mk64-tests/files/0x000000.6014.vpk0'

lv = '-level'
lzw = '-lzwindow'
lzs = '-lzsize'
m = '-method'

def getFileDifferences():
	i = open('epic.vpk0','rb')
	o = open('files/0x000000.6014.vpk0','rb')
	i = i.read()
	o = o.read()
	output=0
	for idx in range(0,os.path.getsize('files/0x000000.6014.vpk0')):
		try:
			if i[idx] != o[idx]:
				output+=1
		except Exception as e:
			return 99999
	return output



# a = 1
# b = 4096
# c = 128

# ' '.join([nvpk,inputFile,outputFile,lv,str(a),lzw,str(b),lzs,str(c)])

printfile = open('log.txt','w+')

minDifference = 99999
minC = [0]

for a in range(1,3):
	for b in range(100,4096):
		for c in range(11,257):
			for d in range(0,2):
				os.system(' '.join([nvpk,inputFile,outputFile,'-c',lv,str(a),lzw,str(b),lzs,str(c),m,str(d)]))
				s = getFileDifferences()
				if s < minDifference:
					minDifference = s
					minC = [c]
				if s == minDifference:
					minC.append(c)
				print(a,b,c,d,s)
				if s==0:
					printfile.write(' '.join([str(a),str(b),str(c),str(getFileDifferences()),'\n']))


print(minDifference,c)
print("Process time: " + str(time.time() - start))