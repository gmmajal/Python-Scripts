f = open("rosalind_2sum.txt",'r')
num=[]
num = f.readline()

srtd =num.strip()
srtd = map(int, srtd.split(' '))	
line = srtd[0]
#print line
size = srtd[1]
#print size

out=[]
for i in range(1,line+1):
	k = 0
	count = 0
	num = f.readline()
	A = num.strip()
	A = map(int, A.split(' '))	
	while k<size:
		for j in range(k, size):
			if A[k]==-A[j] and k<j:
				#print "A[k]",A[k]
				#print "-A[j]",-A[j]
				count = 1
				  #if k<j:
				out.append(k+1)
				out.append(j+1)
				break
				  #else:
					  #out.append(j)
					  #out.append(k)
					  #break
		if(count):
			break
		k+=1
		if(not(count) and k==size):
			out.append(-1)
f.close()
ff = open("output8.txt",'w')
i = 0
while i< len(out):
	if(out[i]==-1):
		ff.write(str(out[i])+"\n")
		i+=1
	else:
		ff.write(str(out[i])+" "+str(out[i+1])+"\n")
		i+=2
ff.close()