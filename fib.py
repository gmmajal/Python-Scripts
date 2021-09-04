def fib(n):
	f=[]
	f.append(0)
	f.append(1)
	for i in range(2, n+1):
		f.append(f[i-1]+f[i-2])
	return f[n]
file1 = open('rosalind_fibo.txt','r')
n=int(file1.readline())
file1.close()
result = fib(n)
ff=open('output1.txt','w')
ff.write(str(result))
