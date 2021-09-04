f=open("rosalind_mer.txt",'r')
arr = []

arr = f.readline()
asize = arr.strip()
asize = map(int,asize.split(' '))
asize =asize[0]
#print "Asize is : ",asize

arr = f.readline()
A = arr.strip()
A = map(int,A.split(' '))
#print "The first list is: ",A

arr = f.readline()
bsize = arr.strip()
bsize = map(int,bsize.split(' '))
bsize = bsize[0]
#print "Bsize is: ",bsize

arr = f.readline()
B = arr.strip()
B = map(int,B.split(' '))
#print "The second list is: ",B

f.close()
merge=[]
#merge = A + B
#merge.sort()
i = 0
j = 0

while (i < asize and j < bsize):
	if (A[i] <= B[j]):
		merge.append( A[i] )
		i = i + 1
        else:
		merge.append( B[j] )
		j = j + 1
while(i < asize):
	merge.append(A[i])
	i = i + 1		
while(j < bsize):
	merge.append(B[j])
	j = j + 1
ff= open("output7.txt",'w')
for i in range (0,len(merge)):
	ff.write(str(merge[i])+" ")
ff.close()			
