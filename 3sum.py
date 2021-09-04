def threeSum(S,dic,key):
	mydict={}
	for i in range(0,len(S)):
		if not S[i] in mydict:
			mydict[S[i]]=i
	#print mydict
	S.sort()
	n=len(S)
	for i in range(0,n-2):
		a = S[i];
		start = i+1;
		end = n-1;
		while (start < end):
			b = S[start]
			c = S[end]
			if (a+b+c == 0 and (a<b) and(b<c)):
					#print "A=",a,"B=",b,"C=",c
					temp = [mydict[a]+1,mydict[b]+1,mydict[c]+1]
					temp.sort()
					dic[key].append(temp[0])
					dic[key].append(temp[1])
					dic[key].append(temp[2])
					start = start + 1
					end = end - 1
					break
			elif (a+b+c > 0):
			      end = end - 1
			else:
			      start = start + 1
		if dic[key]:
			break
	if dic[key]==[]:
		dic[key].append(-1)      


f = open("rosalind_3sum.txt",'r')
num=[]
num = f.readline()

srtd =num.strip()
srtd = map(int, srtd.split(' '))	
line = srtd[0]
#print line
size = srtd[1]

dic={}
for i in range(1,line+1):
	dic[i]=[]

for i in range(1,line+1):
	num = f.readline()
	A = num.strip()
	A = map(int, A.split(' '))
	threeSum(A,dic,i)
f.close()

ff = open("output14.txt",'w')
for i in range(1,line+1):
	  arr=dic[i]
	  for j in range(0,len(arr)):
		ff.write(str(arr[j])+" ")
	  ff.write("\n")
ff.close()