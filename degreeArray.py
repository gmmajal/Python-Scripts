f = open("rosalind_deg.txt",'r')
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
freq=[]
for key in sorted(graph):
	occurence = len(graph[key])
	freq.append(occurence)
ff = open("output3.txt",'w')
for i in freq:
	ff.write(str(i)+" ")
ff.close()
