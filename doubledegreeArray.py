f = open("rosalind_ddeg.txt",'r')
num=[]
num = f.readline()

srtd =num.strip()
srtd = map(int, srtd.split(' '))	
v = srtd[0]
print v
e = srtd[1]
print e

graph = {}
for i in range (1,e+1):
	num=[]
	num = f.readline()

	srtd =num.strip()
	srtd = map(int, srtd.split(' '))
	
	k = srtd[0]
	vv = srtd[1]
	if not graph:
		graph[k] = [vv]
		graph[vv] = [k]
	else:
	  if k in graph:
		  graph[k].append(vv)
	  else:
		  graph[k] = [vv]
	  if vv in graph:
		  graph[vv].append(k)
	  else:
		  graph[vv] = [k]
f.close()
for i in range(1,v+1):
	if i not in graph:
		graph[i]=[]
  
A=[]
for key in sorted(graph):
	sum = 0
	arr=graph[key]
	for i in range(0,len(arr)):
	    degree = len(graph[arr[i]])
	    sum = sum + degree
	idx = int(key)
	A.append(sum)
ff = open("output5.txt",'w')
for i in range (0,len(A)):
  ff.write(str(A[i])+" ")
ff.close()
