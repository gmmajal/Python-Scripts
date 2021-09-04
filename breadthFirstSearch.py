from collections import deque
def bfs(graph,s):
	inf = 1000
	dist = deque([])
	Q = deque([])
	for u in sorted(graph):
		dist.append(inf)
	dist.append(inf)
	dist[s]=0
	#print "The distance array before the while loop is entered looks like:",dist
	Q.append(s)
	#print "Before entering the while loop the queue looks like: ",Q
	while len(Q)!=0:
		u = Q.popleft()
		#print "The node poped out from the queue is: ",u
		arr=graph[u]
		#print "List of adjacent nodes to the poped out node: ",arr
		#print "Lenght of the list: ",len(arr)
		for i in range(0,len(arr)):
			v=arr[i]
			#print "The adjacent node being accessed is: ",v
			if dist[v]==inf:
				Q.append(v)
				dist[v]=dist[u]+1
	
	for u in range(0,len(dist)):
		if dist[u]== inf:
			dist[u]=-1
	dist.popleft()
	return dist
		

f = open("rosalind_bfs.txt",'r')
num=[]
num = f.readline()

srtd =num.strip()
srtd = map(int, srtd.split(' '))	
v = srtd[0]
#print v
e = srtd[1]
#print e

graph = {}
for i in range(1,v+1):
	graph[i]=[]
for i in range (1,e+1):
	num=[]
	num = f.readline()

	srtd =num.strip()
	srtd = map(int, srtd.split(' '))
	
	k = srtd[0]
	vv = srtd[1]
	if not graph:
		graph[k] = [vv]
		#graph[vv] = [k]
	else:
	  if k in graph:
		  graph[k].append(vv)
	  else:
		  graph[k] = [vv]
	  #if vv in graph:
		  #graph[vv].append(k)
	  #else:
		  #graph[vv] = [k]
f.close()
#for i in range(1,v+1):
	#if i not in graph:
		#graph[i]=[]
#print graph
dst = bfs(graph,1)
#print dst
ff = open("output9.txt",'w')
for i in dst:
	ff.write(str(i)+" ")
ff.close()
