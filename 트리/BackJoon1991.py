'''
    트리는 비선형 구조이다. 비선형 구조는 데이터가 계층적으로 구성되어있다
    이진트리: 이진 트리가 되려면, 루트 노드를 중심으로 둘로 나뉘는 두 개의 서브트리와 그 서브트리의 모든 서브티리가 이진트리여야 합니다
    포화 이진 트리: 모든 레벨이 꽉찬 이진 트리
    완전 이진 트리: 모든 레벨이 꽉 찬 상태는 아니지만 빈틈 없이 노드가 채원진 이진 트리
    left, right를 잘 고려해서 구현해야 하며, 전위 중위 후위 순회가 있습니다.
'''

import sys

n = int(sys.stdin.readline())
tree = dict() #tree를 dictionary 타입으로 정의

for i in range(n):
    root, left, right = map(int,input().split()) #루트 노드, 왼쪽, 오른쪽 입력 받기
    tree[root] = left, right #2진 트리를 생성
    
def preorder(v):
    if v != ".": #자식 노드가 있으면
        print(v, end="") #루트 노드 출력
        preorder(tree[v][0]) #재귀적으로 왼쪽 노드 탐색
        preorder(tree[v][1]) #재귀적으로 오른쪽 노드 탐색
        
def inorder(v):
    if v != ".": #자식 노드가 있다면
        inorder(tree[v][0])
        print(v,end="")