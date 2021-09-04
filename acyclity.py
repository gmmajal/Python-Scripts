
def isAcyclic(graph):	
	global visited
	visited = [0]
	global marked
	marked = [0]
	global acyclic
	acyclic=1
	for key in sorted(graph):
		visited.append(0)
		marked.append(0)
	#print "The graph is : ",graph,"\n"
	for key in sorted(graph):
		if visited[key]==0:
			dfs(key)
			#print "The value of acyclic for key ",key," is: ",acyclic,"\n"
			if acyclic==0:
				break;
	return acyclic

def dfs(v):
	#print "The node sent is : ",v,"\n"
	marked[v]= 1
	visited[v]= 1
	#print "Visited array looks as follows: ",visited,"\n"
	#print "Marked array looks as follows: ",marked,"\n"
	arr = graph[v]
	#print "The array for adjacent nodes is: ", arr,"\n"
	for i in range(0,len(arr)):
		if visited[arr[i]]==0:
			dfs(arr[i])
		else:
			if marked[arr[i]]==1:
				#print "Cycle detected for node ",arr[i],"\n"
				global acyclic
				acyclic=0
				#print "The value for acyclic is ",acyclic,"\n"
	marked[v] = 0
	
	
	
	
f = open("rosalind_dag.txt",'r')
num = int(f.readline())
print num
emptyline=f.readline()


lst=[]
for ii in range(0,num):
	edgelist = f.readline()
	edgelist =edgelist.strip()
	edgelist = map(int, edgelist.split(' '))	
	v = edgelist[0]
	#print "No of vertices ",v,"+++++++++++++++++++ \n"
	e = edgelist[1]
	#print "No of edges",e," +++++++++++++++++++ \n"
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
		else:
			if k in graph:
				graph[k].append(vv)
			else:
				graph[k] = [vv]
	if isAcyclic(graph):
		lst.append(1)
	else:
		lst.append(-1)
	emptyline = f.readline()
f.close()
ff = open("output16.txt",'w')

for i in range(len(lst)):
	ff.write(str(lst[i])+" ")
ff.close()
