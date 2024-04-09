book_time=[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
lst=[]
room=[]
for i in book_time:
    sh,sm=(i[0].split(":"))
    eh,em=(i[1].split(":"))
    lst.append([(int(sh)*60+int(sm)),(int(eh)*60+int(em)+10)])
    lst.sort()
print(lst)

def solution(n, computers):
    
    parents = [i for i in range(n)]
    
    def FindRoot(node): # 부모노드를 찾는다
        parentNode = parents[node]
        
        if parentNode != node:
            return FindRoot(parentNode)
        return parentNode
    
    def UnionSet(node1, node2):
        rootNode1 = FindRoot(node1)
        rootNode2 = FindRoot(node2)
        if rootNode1 == rootNode2:
            return
        else:
            parents[rootNode1] = rootNode2
            return
        
    def CountRoot(parents):
        roots = set()
        for i in range(n):
            roots.add(FindRoot(i))
        return len(set(roots))
    
    for node1 in range(n):
        for node2 in range(node1, n):
            if computers[node1][node2]:
                UnionSet(node1, node2)
    return CountRoot(parents)



parents = [i for i in range(n)]
def find_root(Node):
    parentNode = parents[Node]
    
    if parents[Node] != parentNode:
        return find_root(parentNode)
    return parentNode

def UnionSet(node1, node2):
    rootNode1 = find_root(node1)
    rootNode2 = find_root(node2)
    
    if rootNode1 == rootNode2:
        return 
    else:
        parents[rootNode1] = rootNode2
        return
    
def CountRoot(parents):
    roots = set()
    
    for i in range(n):
        roots.add(find_root(i))
    return len(set(roots))

for node1 in range(n):
    for node2 in range(node1, n):
        if computer[node1][node2]:
            UnionSet(node1, node2)
    
return CountRoot(parents)