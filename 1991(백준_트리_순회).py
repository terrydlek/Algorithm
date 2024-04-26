import sys
input = sys.stdin.readline

n = int(input())
graph = {}

for _ in range(n):
    a, b, c = map(str, input().strip().split())
    graph[a] = [b, c]

def preorder(cur):
    if cur != '.':
        print(cur, end='')
        preorder(graph[cur][0])
        preorder(graph[cur][1])

preorder('A')
print()
def inorder(cur):
    if cur != '.':
        inorder(graph[cur][0])
        print(cur, end='')
        inorder(graph[cur][1])

inorder('A')
print()
def postorder(cur):
    if cur != '.':
        postorder(graph[cur][0])
        postorder(graph[cur][1])
        print(cur, end='')

postorder('A')
