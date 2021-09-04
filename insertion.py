def insertsort(arr,n):
	count = 0
	for i in range(1,n):
		k = i
		while k > 0 and arr[k]<arr[k-1]:
			tmp = arr[k-1]
			arr[k-1] = arr[k]
			arr[k] = tmp
			count = count + 1
			k = k - 1
	return count
f = open("rosalind_ins.txt",'r')
num = int(f.readline())
A = []
arr = f.readline()
A = arr.strip()
A = map(int,arr.split(' '))
count = insertsort(A,num)
f.close()
ff = open("output4.txt","w")
ff.write(str(count))
ff.close()
