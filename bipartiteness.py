def checkBipartitness(graph,node):
	colorArr=[]
	for key in graph:
		colorArr.append(-1)
	colorArr.append(-1)
	colorArr[node] = 1 
	q=[]
	q.append(node)
	#print "Queue :",q
	while len(q)!=0: 
		#print "Queue contains: ",q
		u =q.pop(0)
		arr=graph[u]
		#print "u is :",u,"with color:",colorArr[u]
		for i in range(0,len(arr)):
			v=arr[i]
			if colorArr[v]==-1:
				colorArr[v] = 1 - colorArr[u]
				q.append(v)
			elif colorArr[v]==colorArr[u]:
				return 0
			#print "v is ",v," with color ",colorArr[v]
		#print "Color Array is ",colorArr
	return 1

	

f = open("rosalind_bip.txt",'r')

num = int(f.readline())
print num
emptyline=f.readline()


lst=[]
for ii in range(0,num):
	edgelist = f.readline()
	edgelist =edgelist.strip()
	edgelist = map(int, edgelist.split(' '))	
	v = edgelist[0]
	#print "No of vertices",v
	e = edgelist[1]
	#print "No of edges",e
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
	if checkBipartitness(graph,1):
	      lst.append(1)
	else:
	      lst.append(-1)
	emptyline = f.readline()
f.close()
ff = open("output15.txt",'w')

for i in range(len(lst)):
	ff.write(str(lst[i])+" ")
ff.close()