def dfs(graph):
	global visited
	visited = [False]
	for key in sorted(graph):
		visited.append(False)
	count = 0
	for key in sorted(graph):
		if not visited[key]:
			explore(graph,key)
			count+=1
	return count
def explore(graph,v):
	visited[v] = True
	arr = graph[v]
	for i in range(0,len(arr)):
		if not visited[arr[i]]:
			explore(graph,arr[i])	

f = open("rosalind_cc.txt",'r')
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


component = dfs(graph) 
print component
ff = open("output10.txt",'w')
ff.write(str(component))
ff.close()