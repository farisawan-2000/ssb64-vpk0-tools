import sys,os

def btoi(a):
	return int.from_bytes(a,'big')

iFile = open(sys.argv[1],'rb')
bFile = iFile.read()

outPath = os.getcwd()+'/files/'
if not os.path.isdir(outPath):
	os.mkdir('files')

fileSpaceStart = 0x1B2C6C
compressedExt = '.vpk0'
uncompressedExt = '.bin'


with open('ssb64filetable.txt') as reference:
	for line in reference:
		iC, offset, x, cSize, y, dSize = line.split()
		cSize = int(cSize,16)
		if iC == '80':
			oFile = open(outPath+'0x'+offset+'.'+dSize+compressedExt,'wb+')
			toStart = fileSpaceStart + int(offset,16)
			oFile.write(bFile[ toStart : toStart + (cSize * 4 )])
			oFile.close()
		else:
			oFile = open(outPath+'0x'+offset+'.'+dSize+uncompressedExt,'wb+')
			toStart = fileSpaceStart + int(offset,16)
			oFile.write(bFile[ toStart : toStart + (cSize * 4 )])
			oFile.close()

iFile.close()