import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = [[], []]
    
    nodes = []
    # 노드 번호를 추가하고 y좌표를 기준으로 정렬하는 코드
    for i in range(len(nodeinfo)):
        node = [i+1] # 노드 번호를 추가합니다.
        node += nodeinfo[i] # nodeinfo의 i번째 요소를 추가합니다.
        nodes.append(node)
        
    def sort_key(node):
        return node[2] # y 좌표를 return
    
    nodes = sorted(nodes, key=sort_key, reverse=True)
    
    class Node:
        def __init__(self,num,x,y):
            self.num = num
            self.x = x
            self.y = y
            self.left = None
            self.right = None
            
    root = Node(nodes[0][0], nodes[0][1], nodes[0][2])
    
    for node in nodes[1:]:
        num, x, y = node
        current = root
        while True:
            if x < current.x:
                if current.left is None:
                    current.left = Node(num,x,y)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(num,x,y)
                    break
                else:
                    current = current.right        
    
    def preorder(node):
        if node is not None:
            answer[0].append(node.num)
            preorder(node.left)
            preorder(node.right)
            
    preorder(root)
    
    def postorder(node):
        if node is not None:
            postorder(node.left)
            postorder(node.right)
            answer[1].append(node.num)
            
    postorder(root)       
    
    return answer