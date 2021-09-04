def merge(A,B):
	merge=[]
	asize = len(A)
	bsize = len(B)
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
	return merge
	
def mergeSort(A,size):
	if size <= 1:
		return A    
	left = []
	right = []
	middle = size/2
	for x in range (0,middle):
		left.append(A[x])
	for x in range (middle,size):
		right.append(A[x])
	left = mergeSort(left,len(left))
	right = mergeSort(right,len(right))
	return merge(left, right)


f = open("rosalind_ms.txt",'r')
num=[]
num = f.readline()

size =num.strip()
size = map(int, size.split(' '))
size = size[0]
#print size

arr=f.readline()
arr =arr.strip()
arr = map(int, arr.split(' '))
#print arr
f.close()
merge=mergeSort(arr,size)

ff = open("output12.txt",'w')
for i in range (0,len(merge)):
	ff.write(str(merge[i])+" ")
ff.close()