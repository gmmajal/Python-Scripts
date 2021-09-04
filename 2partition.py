#import random

def partition(arr):
	i = 1
	j = len(arr)-1
	while True:
		while arr[i]<=arr[0]:
			i+=1
			if i==len(arr)-1:
				break
			#print "i has been incremented to index value: ",i	
		while (arr[j]>=arr[0]):
			j-=1
			if j==0:
				break
			#print "j has been decremented to index value: ",j
		if i>=j:
			break
		tmp = arr[i]
		#print "tmp value is:",tmp
		arr[i] = arr[j]
		#print "New Arr[i] value is:",arr[i]
		arr[j] = tmp
		#print "New Arr[j] value is: ",arr[j]
		#print "Array looks like:",arr
	#print "Final swap taking place:----------"
	
	tmp = arr[0]
	#print "tmp value is: ",tmp
	arr[0] = arr[j]
	#print "Arr[0] value is: ",arr[0]
	arr[j] = tmp
	#print "Arr[j] value is: ",arr[j]
	return arr


f = open('rosalind_par.txt','r')
arr=[]

arr = f.readline()
n = int(arr[0])
#print n

arr = f.readline()
A = arr.strip()
A = map(int, A.split(' '))
#print A
f.close()

#A = random.sample(range(1, 51),50)
#print A
newarray = partition(A)
#print newarray
ff = open('output13.txt','w')
for i in range(0,len(newarray)):
	  ff.write(str(newarray[i])+" ")
ff.close()
