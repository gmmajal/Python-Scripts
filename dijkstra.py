def dijkstra(graph,s):
	inf = 1000
	dist = [inf]
	Q={}
	for v in sorted(graph):
		if v==s:
			dist.append(0)
		else:
			dist.append(inf)
			#prev.append(-1)
		Q[v]=dist[v]
	#dist.append(inf)
	while len(Q)!=0:
		#print "Heap is: ",Q
		u=min(Q, key=Q.get)
		del Q[u]
		#print"Heap pop U:",u,"\n"
		arr= graph[u]
		for i in range(0,len(arr)):
			#print "Array is: ",arr[i]
			v = (arr[i])[0]
			#print"Vertex is : ",v,"\n"
			l = (arr[i])[1]
			#print"Weight is : ",l,"\n"
			#print"Dist[v]: ",dist[v]," for node: ",v,"\n"
			if v in Q:
				#"If conditional was entered \n"
				if dist[v]>dist[u]+l:
					dist[v] = dist[u]+l
					Q[v]=dist[v]
					#print"Dist[v] was modified to: ",dist[v]," for node: ",v,"\n"
	for u in range(0,len(dist)):
		if dist[u]== inf:
			dist[u]=-1
	dist.pop(0)
	return dist


#{1: [[2, 4], [3, 2]], 2: [[3, 3], [4, 2], [5, 3]], 3: [[4, 4], [5, 5], [2, 1]], 4: [], 5: [[4, 1]], 6: [[3, 2]]} rosalind_dij

f = open("rosalind_dij.txt",'r')
num=[]
num = f.readline()

srtd =num.strip()
srtd = map(int, srtd.split(' '))	
v = srtd[0]
print v
e = srtd[1]
print e

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
	w = srtd[2] 
	if not graph:
		weight[k] = w
		graph[k] = [vv,w]
	else:
	  if k in graph:
		  graph[k].append([vv,w])
	  else:
		  graph[k] = [vv,w]
f.close()

lst = dijkstra(graph,1)
#print lst

ff = open("output17.txt",'w')
for i in lst:
	ff.write(str(i)+" ")
ff.close()