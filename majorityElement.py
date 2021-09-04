def findCandidate(a,size):
	maj_idx = 0
	count = 1
	#print a
	for i in range (1,size):
		if(a[maj_idx]==a[i]):
			#print " The current majority index: ",a[maj_idx]
			count = count + 1
			#print "The count is: ",count
		else:
			count = count - 1
			#print "Count was reduced: ",count
		if(count == 0):
			maj_idx = i
			#print "Majority index was changed: ",a[maj_idx]
			count = 1
			#print "Count has been reset: ",count
	return a[maj_idx]
def checkMajority(a,size,cand):
	count = 0;
	for i in range (0,size):
		if(a[i] == cand):
			count = count+1
	if(count > size/2):
		return cand
	else:
		return -1
f=open("rosalind_maj.txt",'r')
arr = []
arr = f.readline()
srtd = arr.strip()
srtd = map(int,srtd.split(' '))
no = srtd[0]
size = srtd[1]

a=[]
maj=[]
for i in range(1, no + 1):
	a=f.readline()
	line = a.strip()
	line = map(int,line.split(' '))
	candidate = findCandidate(line,size)
	#print candidate
	common = checkMajority(line,size,candidate)
	maj.append(common)
f.close()
ff= open("output6.txt",'w')
for i in range (0,len(maj)):
	ff.write(str(maj[i])+" ")
ff.close()			
