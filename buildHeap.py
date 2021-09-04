def heapify (A, i, n):
	left  = 2*i + 1
	#print "Left value is: ",left
	right = 2*i + 2
	#print "Right value is: ",right
	largest = i
	#print "Largest value is :",largest
	
	if left < n and A[left] > A[largest]:
		largest = left
	if right < n and A[right] > A[largest]:
		largest = right
	#print "Largest value now is: ",largest
	if largest != i:
		tmp = A[largest]
		A[largest] = A[i]
		A[i] = tmp
		heapify(A,largest,n)
	#print "Current status of the array: ",A
def buildMaxHeap(A):
	n=len(A)
	for i in range(n/2,-1,-1):
		heapify(A,i,n)


f = open("rosalind_hea.txt",'r')

num=[]
num = f.readline()

size =num.strip()
size = map(int, size.split(' '))
size = size[0]
#print size
arr=[]
arr.append(0)
arr=f.readline()
arr =arr.strip()
arr = map(int, arr.split(' '))
#print arr
f.close()
buildMaxHeap(arr)
print arr
ff = open("output11.txt",'w')
for i in range (0,size):
	ff.write(str(arr[i])+" ")
ff.close()		
