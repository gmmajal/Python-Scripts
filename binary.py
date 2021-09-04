def bin(array, key, imin,imax ):
	if imax < imin:
		return -1
	if not array:
		return -1
	if imin==imax:
		if array[imin]==key:
			return imin
		else:
			return -1
	imid = (imin+imax)/2
	if array[imid]>key:
		return bin(array,key, imin, imid-1)
	elif array[imid]<key:
		return bin(array,key, imid+1,imax)
	else:
		return imid
f = open('rosalind_bins.txt','r')
arr=[]
arr = f.readlines()
n = int(arr[0])
print n
m = int(arr[1])
print m
srtd =arr[2].strip()
srtd = map(int, srtd.split(' '))	
unsrtd =arr[3].strip()
unsrtd = map(int, unsrtd.split(' '))
f.close()
idx = []

for i in range (m):
	index= bin(srtd,unsrtd[i],0,n-1)
	if index !=-1:
	  if srtd[index]!=unsrtd[i]:
		    print 'Match not met '
	  index+=1
	
	idx.append(index)
ff = open('output2.txt','w')
output=""
for i in idx:
  ff.write(str(i)+" ")
ff.close()
